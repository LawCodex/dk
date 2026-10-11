#!/usr/bin/env python3
"""Convert the Retsinformation documents cached by fetch.py into Markdown.

Input:  _raw/dk/list.json and _raw/dk/docs/<year>/<eli>.json|.xml
Output: <repo>/grundloven/, love/<year>/, aendringslove/<year>/,
        bekendtgoerelser/<year>/, anordninger/<year>/

The body text is converted from the HTML rendering that Retsinformation serves for each
document (it exists for every document, whereas the LexDania XML has no body text for older
documents). Metadata comes from the XML <Meta> block and the document JSON.

Usage: python convert.py [--raw DIR] [--out DIR] [--only ELI-SUBSTRING]
"""
import argparse
import datetime
import json
import os
import re
import sys
import unicodedata
from xml.etree import ElementTree as ET

import lxml.html
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_RAW = os.path.normpath(os.path.join(HERE, "..", "..", "_raw", "dk"))
DEFAULT_OUT = os.path.normpath(os.path.join(HERE, ".."))
BASE = "https://www.retsinformation.dk"
RETRIEVED = os.environ.get("RETRIEVED", datetime.date.today().isoformat())

# Constitutional documents placed in grundloven/
CONSTITUTIONAL = {
    "/eli/lta/1953/169": ("grundloven", "constitution"),
    "/eli/lta/1953/170": ("tronfoelgeloven", "constitution"),
    "/eli/lta/2009/528": ("tronfoelgeloven-aendring-2009", "constitution"),
}

# Retsinformation ELI type code -> (directory, front-matter type)
TYPES = {
    "LOVH": ("love", "act"),
    "LBKH": ("love", "consolidated_act"),
    "LOVC": ("aendringslove", "amending_act"),
    "BEKH": ("bekendtgoerelser", "executive_order"),
    "ANDH": ("anordninger", "royal_ordinance"),
}

BLOCK_TAGS = {"p", "div", "section", "header", "footer", "center", "table", "ul", "ol", "dir",
              "menu", "li", "h1", "h2", "h3", "h4", "h5", "h6", "pre", "hr", "blockquote",
              "dl", "dt", "dd", "article", "body", "html", "form", "tbody", "thead", "tr"}
CONTAINER_TAGS = {"div", "section", "header", "footer", "center", "body", "html", "article",
                  "blockquote", "form", "font", "span", "dl", "dd", "dt"}

# heading ranks (lower = higher in hierarchy)
RANK_DEL, RANK_AFSNIT, RANK_KAPITEL, RANK_GRUPPE = 0, 1, 2, 3
PARA_RE = re.compile(r"^§+\s*\d+\s*[a-zæøå]?(\s*[-–]\s*\d+\s*[a-zæøå]?)?\s*\.?$", re.I)
OLD_HEAD_CLASSES = {
    "ktitle0": RANK_DEL, "ktitle1": RANK_KAPITEL, "ktitle2": RANK_GRUPPE, "ktitle3": RANK_GRUPPE,
}


# ---------------------------------------------------------------- helpers

def slugify(s, maxlen=80):
    s = s.lower()
    for a, b in (("æ", "ae"), ("ø", "oe"), ("å", "aa"), ("ä", "ae"), ("ö", "oe"), ("ü", "ue"),
                 ("ß", "ss"), ("§", "")):
        s = s.replace(a, b)
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    if len(s) > maxlen:
        s = s[:maxlen].rsplit("-", 1)[0]
    return s or "dokument"


def clean_title(t):
    t = (t or "").replace("\\n", " ")
    t = re.sub(r"\(\*\s*\d+\)", "", t)  # old-style note markers "(* 1)"
    return re.sub(r"\s+", " ", t).strip()


def classes(el):
    return set((el.get("class") or "").lower().split())


def norm_ws(s):
    return re.sub(r"[ \t\r\n    ]+", " ", s)


def esc_inline(s):
    s = s.replace("\\", "\\\\")
    s = re.sub(r"([*_`])", r"\\\1", s)
    s = re.sub(r"<(?=[A-Za-z/!?])", "&lt;", s)
    s = s.replace("[", "\\[").replace("]", "\\]")
    return s


def esc_line_start(s):
    """Escape constructs that Markdown would interpret at the start of a block."""
    s = s.lstrip()
    m = re.match(r"^(\d+)([.)])(\s|$)", s)
    if m:
        return m.group(1) + "\\" + s[len(m.group(1)):]
    if re.match(r"^([-+]|#{1,6}|>)(\s|$)", s):
        return "\\" + s
    if re.match(r"^(=+|-{3,}|_{3,})\s*$", s):
        return "\\" + s
    return s


# ---------------------------------------------------------------- inline conversion

def inline(el, top=True):
    """Return Markdown for the inline content of el (including its text)."""
    out = []
    if el.text:
        out.append(esc_inline(norm_ws(el.text)))
    for ch in el:
        if isinstance(ch, lxml.html.HtmlComment) or not isinstance(ch.tag, str):
            if ch.tail:
                out.append(esc_inline(norm_ws(ch.tail)))
            continue
        out.append(inline_el(ch))
        if ch.tail:
            out.append(esc_inline(norm_ws(ch.tail)))
    return "".join(out)


def wrap(s, mark):
    m = re.match(r"^(\s*)(.*?)(\s*)$", s, re.S)
    lead, core, trail = m.groups()
    if not core:
        return s
    return f"{lead}{mark}{core}{mark}{trail}"


def inline_el(el):
    tag = el.tag.lower()
    cls = classes(el)
    if tag in ("script", "style"):
        return ""
    if tag == "br":
        return "\n"
    if tag == "img":
        src = el.get("src") or ""
        if src and not src.startswith("data:"):
            if src.startswith("/"):
                src = BASE + src
            elif not src.startswith("http"):
                src = BASE + "/" + src
            return f"![{esc_inline(el.get('alt') or '')}]({src.replace(' ', '%20')})"
        return "[billede]"
    if tag == "table":
        return " " + inline(el) + " "
    s = inline(el)
    if "stknr" in cls:
        return wrap(s, "*")
    if tag in ("b", "strong") or "bold" in cls:
        return wrap(s, "**")
    if tag in ("i", "em") or "italic" in cls:
        return wrap(s, "*")
    if tag == "sup" or "superscript" in cls:
        return f"<sup>{s.strip()}</sup>" if s.strip() else s
    if tag == "sub" or "subscript" in cls:
        return f"<sub>{s.strip()}</sub>" if s.strip() else s
    if tag in BLOCK_TAGS and tag not in ("span", "font"):
        return " " + s + " "
    return s


def tidy(s):
    """Normalise an inline Markdown string: collapse spaces, fix empty emphasis."""
    lines = [re.sub(r" {2,}", " ", l).strip() for l in s.split("\n")]
    lines = [l for l in lines if l]
    s = "\\\n".join(lines)  # hard line breaks
    return s.strip()


# ---------------------------------------------------------------- tables

def cell_text(td):
    parts = []
    blocks = [c for c in td if isinstance(c.tag, str) and c.tag.lower() in BLOCK_TAGS]
    if blocks:
        if td.text and td.text.strip():
            parts.append(esc_inline(norm_ws(td.text)))
        for c in td:
            if not isinstance(c.tag, str):
                continue
            if c.tag.lower() in BLOCK_TAGS:
                if c.tag.lower() == "table":
                    parts.append(table_to_html(c))
                else:
                    t = cell_text(c) if any(isinstance(x.tag, str) and x.tag.lower() in BLOCK_TAGS
                                            for x in c) else tidy(inline(c))
                    if t:
                        parts.append(t)
            else:
                t = tidy(inline_el(c))
                if t:
                    parts.append(t)
            if c.tail and c.tail.strip():
                parts.append(esc_inline(norm_ws(c.tail)))
        return "\n".join(p for p in parts if p.strip())
    return tidy(inline(td))


def unwrap_tables(t):
    """Retsinformation wraps real tables in a single-cell 'Containertable'."""
    while True:
        rows = rows_of(t)
        if len(rows) == 1:
            cells = [c for c in rows[0] if isinstance(c.tag, str) and c.tag.lower() in ("td", "th")]
            if len(cells) == 1:
                inner = [c for c in cells[0].iter("table")]
                txt_outside = norm_ws(cells[0].text_content())
                if inner and norm_ws(inner[0].text_content()).strip() == txt_outside.strip():
                    t = inner[0]
                    continue
        return t


def rows_of(t):
    rows = []
    for ch in t:
        if not isinstance(ch.tag, str):
            continue
        tg = ch.tag.lower()
        if tg == "tr":
            rows.append(ch)
        elif tg in ("tbody", "thead", "tfoot"):
            rows.extend(r for r in ch if isinstance(r.tag, str) and r.tag.lower() == "tr")
    return rows


def md_to_html_inline(s):
    """Markdown produced by inline() -> HTML, for text inside HTML table cells."""
    s = s.replace("\\\n", "<br>").replace("\n", "<br>")
    s = re.sub(r"(?<!\\)\*\*(.+?)(?<!\\)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\\*])\*(?!\*)(.+?)(?<!\\)\*", r"<em>\1</em>", s)
    s = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r'<img src="\2" alt="\1">', s)
    s = re.sub(r"\\([\\*_`\[\]#+\-.)>])", r"\1", s)
    return s


def table_to_html(t):
    rows = rows_of(t)
    out = ["<table>"]
    for r in rows:
        out.append("<tr>")
        for c in r:
            if not isinstance(c.tag, str) or c.tag.lower() not in ("td", "th"):
                continue
            attrs = ""
            for a in ("colspan", "rowspan"):
                v = c.get(a)
                if v and v != "1":
                    attrs += f' {a}="{v}"'
            txt = md_to_html_inline(cell_text(c))
            tg = c.tag.lower()
            out.append(f"<{tg}{attrs}>{txt}</{tg}>")
        out.append("</tr>")
    out.append("</table>")
    return "\n".join(out)


def table_block(t):
    t = unwrap_tables(t)
    rows = rows_of(t)
    if not rows:
        txt = tidy(inline(t))
        return txt
    complex_ = False
    grid = []
    for r in rows:
        cells = [c for c in r if isinstance(c.tag, str) and c.tag.lower() in ("td", "th")]
        for c in cells:
            if (c.get("colspan") not in (None, "", "1")) or (c.get("rowspan") not in (None, "", "1")):
                complex_ = True
            if c.find(".//table") is not None:
                complex_ = True
        grid.append(cells)
    if complex_:
        return table_to_html(t)
    texts = [[cell_text(c).replace("\n", "<br>").replace("\\<br>", "<br>").replace("|", "\\|")
              for c in r] for r in grid]
    texts = [r for r in texts if any(x.strip() for x in r)]
    if not texts:
        return ""
    ncol = max(len(r) for r in texts)
    if ncol == 0:
        return ""
    if ncol == 1 and len(texts) <= 1:
        return texts[0][0] if texts else ""
    texts = [r + [""] * (ncol - len(r)) for r in texts]
    lines = ["| " + " | ".join(texts[0]) + " |", "|" + "---|" * ncol]
    for r in texts[1:]:
        lines.append("| " + " | ".join(r) + " |")
    return "\n".join(lines)


# ---------------------------------------------------------------- block conversion

class Doc:
    def __init__(self):
        self.blocks = []  # (kind, payload): ("h", (rank, text)) | ("p", text) | ("raw", text)
        self.skipped_title = False
        self.pending_kapitel = None


def has_block_children(el):
    for c in el:
        if not isinstance(c.tag, str):
            continue
        t = c.tag.lower()
        if t in BLOCK_TAGS:
            return True
        if t in ("font", "span", "a", "b", "i", "u", "em", "strong", "nobr") and has_block_children(c):
            return True
    return False


HEAD_CLASSES = {
    # class: (rank, is_title_part)  -- is_title_part: the text that follows a number heading
    "bog": (RANK_DEL, False), "del": (RANK_DEL, False),
    "bogoverskrift": (RANK_DEL, True), "deloverskrift": (RANK_DEL, True),
    "afsnit": (RANK_AFSNIT, False), "afsnitsnummer": (RANK_AFSNIT, False),
    "atitle1": (RANK_AFSNIT, False),
    "afsnitoverskrift": (RANK_AFSNIT, True), "afsnitsoverskrift": (RANK_AFSNIT, True),
    "atitle2": (RANK_AFSNIT, True),
    "kapitel": (RANK_KAPITEL, False), "kapitelnummer": (RANK_KAPITEL, False),
    "ktitle1": (RANK_KAPITEL, False),
    "kapiteloverskrift": (RANK_KAPITEL, True), "kapiteloverskrift2": (RANK_KAPITEL, True),
    "ktitle2": (RANK_KAPITEL, True),
    "paragrafgruppeoverskrift": (RANK_GRUPPE, False), "paragrafoverskrift": (RANK_GRUPPE, False),
    "overskriftsnummer1": (RANK_GRUPPE, False), "overskriftstekst1": (RANK_GRUPPE, True),
    "tekstoverskrift": (RANK_GRUPPE, False), "tekstoverskriftb": (RANK_GRUPPE, False),
    "tekstoverskriftvb": (RANK_GRUPPE, False), "tekstoverskriftvenstre": (RANK_GRUPPE, False),
    "tekstoverskriftvenstren": (RANK_GRUPPE, False),
    "overskriftsnummer2": (RANK_GRUPPE + 1, False), "overskriftstekst2": (RANK_GRUPPE + 1, True),
    "overskriftstekst3": (RANK_GRUPPE + 2, False),
}
BILAG_CLASSES = {"bilag", "bilagoverskrift", "bilagsoverskrift", "bilagstitel"}


def heading_info(el):
    """Return (rank, is_title_part) if el is a structural heading, else None."""
    cls = classes(el)
    for c in cls:
        if c in HEAD_CLASSES:
            return HEAD_CLASSES[c]
    tag = el.tag.lower()
    if tag in ("h2", "h3", "h4", "h5", "h6") and not cls & {"title", "undertitel2"}:
        return (RANK_KAPITEL if tag in ("h2", "h3") else RANK_GRUPPE, False)
    return None


def is_heading_wrapper(el):
    total = re.sub(r"\s+", "", el.text_content())
    head = ""
    for d in el.iter():
        if d is el or not isinstance(d.tag, str):
            continue
        if heading_info(d) is not None and not has_block_children(d):
            head += re.sub(r"\s+", "", d.text_content())
    return head == total


def is_title(el):
    cls = classes(el)
    tag = el.tag.lower()
    return (tag == "h1" or "title" in cls or "titel2" in cls or "title-section" in cls
            or "titel" in cls)


def _is_empty(c):
    return (not norm_ws(c.text_content()).strip() and c.tag.lower() not in ("img", "br")
            and not c.xpath(".//img"))


def paragraph_heading(el):
    """If el starts with a '§ n.' label, return (label, rest_markdown)."""
    if el.text and el.text.strip():
        return None
    kids = list(el)
    first = None
    for i, c in enumerate(kids):
        if not isinstance(c.tag, str):
            if c.tail and c.tail.strip():
                return None
            continue
        if _is_empty(c):
            if c.tail and c.tail.strip():
                return None
            continue
        first = i
        break
    if first is None:
        return None
    f = kids[first]
    cls = classes(f)
    tag = f.tag.lower()
    if not ("paragrafnr" in cls or tag in ("b", "strong") or "bold" in cls):
        return None
    label = norm_ws(f.text_content()).strip()
    if not (PARA_RE.match(label) or ("paragrafnr" in cls and label)):
        return None
    rest = []
    if f.tail:
        rest.append(esc_inline(norm_ws(f.tail)))
    for c in kids[first + 1:]:
        if isinstance(c.tag, str):
            rest.append(inline_el(c))
        if c.tail:
            rest.append(esc_inline(norm_ws(c.tail)))
    return esc_inline(label), tidy("".join(rest))


def stk_text(el):
    """Paragraph whose first child is a 'Stk. n.' number span: italicise label."""
    return tidy(inline(el))


def emit_paragraph(doc, el, text=None):
    cls = classes(el)
    if text is None:
        text = tidy(inline(el))
    if not text:
        return
    m = re.match(r"liste(\d)", " ".join(sorted(cls)))
    lst = None
    for c in cls:
        mm = re.match(r"^liste(\d)$", c)
        if mm:
            lst = int(mm.group(1))
    if lst:
        doc.blocks.append(("li", (lst, esc_line_start(text))))
    else:
        doc.blocks.append(("p", esc_line_start(text)))


def walk(doc, el):
    if not isinstance(el.tag, str):
        return
    tag = el.tag.lower()
    cls = classes(el)
    if tag in ("script", "style", "head", "title", "meta", "link"):
        return
    if "bjelke" in cls:
        t = norm_ws(el.text_content()).strip()
        if t and not t.lower().startswith(("oversigt", "den fulde tekst")):
            doc.blocks.append(("h", (-1, esc_inline(t))))
        return
    if "toc" in cls or el.get("id") == "OVERSIGT" or "indholdsfortegnelse" in cls and tag == "table":
        return
    if tag == "a" and not len(el) and not (el.text or "").strip():
        if el.tail and el.tail.strip():
            doc.blocks.append(("p", esc_line_start(tidy(esc_inline(norm_ws(el.tail))))))
        return
    if tag == "hr":
        return
    if tag == "table":
        b = table_block(el)
        if b:
            doc.blocks.append(("raw", b))
        return
    if not doc.skipped_title and is_title(el):
        doc.skipped_title = True
        return
    hi = heading_info(el)
    if hi is not None and has_block_children(el) and not tag.startswith("h"):
        # a heading wrapper (e.g. <div class="Kapitel"><div><h2>..</h2></div></div>) is a
        # heading only if all of its text sits in heading elements
        if not is_heading_wrapper(el):
            hi = None
    if hi is not None:
        rank, is_title_part = hi
        text = tidy(inline(el)).replace("\\\n", " ")
        text = re.sub(r"^\*\*(.*)\*\*$", r"\1", text)
        text = re.sub(r"^\*(.*)\*$", r"\1", text)
        if text:
            doc.blocks.append(("h", (rank, text, is_title_part)))
        return
    if cls & {"centreretparagraf", "aendringcentreretparagraf", "cparagrafnummer"} \
            and not has_block_children(el):
        label = tidy(inline(el)).replace("\\\n", " ")
        if PARA_RE.match(re.sub(r"\\", "", label)):
            doc.blocks.append(("para", (label, "")))
            return
    if cls & BILAG_CLASSES and not has_block_children(el):
        text = tidy(inline(el)).replace("\\\n", " ")
        if text:
            doc.blocks.append(("h", (-1, text)))
        return
    if tag in ("ul", "ol", "dir", "menu"):
        for i, li in enumerate([c for c in el if isinstance(c.tag, str)], 1):
            if li.tag.lower() == "li":
                t = tidy(inline(li)) if not has_block_children(li) else None
                if t is None:
                    sub = Doc()
                    sub.skipped_title = True
                    for c in li:
                        walk(sub, c)
                    t = " ".join(b[1] for b in sub.blocks if b[0] == "p")
                if t:
                    marker = f"{i}. " if tag == "ol" else "- "
                    doc.blocks.append(("li", (1, marker + esc_line_start(t), True)))
            else:
                walk(doc, li)
        return
    if tag in ("p", "li", "pre", "h1", "h2", "h3", "h4", "h5", "h6", "dt", "dd") or \
            (tag in CONTAINER_TAGS and not has_block_children(el)):
        if tag != "p" and has_block_children(el):
            pass
        else:
            ph = paragraph_heading(el)
            if ph:
                doc.blocks.append(("para", (ph[0], ph[1])))
                return
            if tag == "pre":
                txt = el.text_content().strip("\n")
                if txt.strip():
                    doc.blocks.append(("raw", "```\n" + txt + "\n```"))
                return
            plain = norm_ws(el.text_content()).strip()
            if PARA_RE.match(plain):
                doc.blocks.append(("para", (esc_inline(plain), "")))
                return
            emit_paragraph(doc, el)
            return
    # container with block children: walk children, keeping stray text as paragraphs
    if el.text and el.text.strip():
        doc.blocks.append(("p", esc_line_start(tidy(esc_inline(norm_ws(el.text))))))
    inline_buf = []

    def flush():
        if inline_buf:
            t = tidy("".join(inline_buf))
            if t:
                doc.blocks.append(("p", esc_line_start(t)))
            inline_buf.clear()

    for c in el:
        if not isinstance(c.tag, str):
            if c.tail and c.tail.strip():
                inline_buf.append(esc_inline(norm_ws(c.tail)))
            continue
        if c.tag.lower() in BLOCK_TAGS or (c.tag.lower() == "a" and not (c.text or "").strip()):
            flush()
            walk(doc, c)
            if c.tail and c.tail.strip():
                inline_buf.append(esc_inline(norm_ws(c.tail)))
        elif c.tag.lower() in ("span", "font", "a", "b", "i", "u", "em", "strong", "nobr") \
                and has_block_children(c):
            flush()
            walk(doc, c)
            if c.tail and c.tail.strip():
                inline_buf.append(esc_inline(norm_ws(c.tail)))
        else:
            inline_buf.append(inline_el(c))
            if c.tail:
                inline_buf.append(esc_inline(norm_ws(c.tail)))
    flush()


def _quote_pass(blocks):
    """Demote headings that occur inside quoted amendment text (»...«) to bold paragraphs."""
    def btext(b):
        k, pl = b
        if k == "para":
            return pl[0] + " " + pl[1]
        if k == "h":
            return pl[1]
        if k == "li":
            return pl[1]
        return pl if isinstance(pl, str) else ""
    bal = 0
    for b in blocks:
        t = btext(b)
        bal += t.count("»") - t.count("«")
    if bal != 0:
        return blocks
    out = []
    bal = 0
    for b in blocks:
        t = btext(b)
        quoted = bal > 0 or t.lstrip().startswith(("»", "\u00bb"))
        if quoted and b[0] == "para":
            label, rest = b[1]
            b = ("p", f"**{label}**" + (" " + rest if rest else ""))
        elif quoted and b[0] == "h" and b[1][0] >= 0:
            b = ("p", f"**{b[1][1]}**")
        bal = max(0, bal + t.count("»") - t.count("«"))
        out.append(b)
    return out


def render(doc):
    doc.blocks = _quote_pass(doc.blocks)
    # merge "Kapitel 1" + "Overskrift" pairs of the same rank into one heading
    merged = []
    for b in doc.blocks:
        if (b[0] == "h" and merged and merged[-1][0] == "h" and b[1][0] >= 0
                and merged[-1][1][0] == b[1][0] and len(b[1]) > 2 and b[1][2]
                and not (len(merged[-1][1]) > 2 and merged[-1][1][2])
                and len(merged[-1][1][1]) < 40):
            r, t1, _ = merged[-1][1]
            merged[-1] = ("h", (r, f"{t1} — {b[1][1]}", True))
            continue
        merged.append(b)
    ranks = sorted({b[1][0] for b in merged if b[0] == "h" and b[1][0] >= 0})
    level = {r: min(6, i + 2) for i, r in enumerate(ranks)}
    para_level = min(6, len(ranks) + 2)
    lines = []
    kinds = []
    prev = None
    for kind, pl in merged:
        kinds.append(kind)
        if kind == "h":
            r, t = pl[0], pl[1]
            lv = 2 if r < 0 else level[r]
            lines.append("#" * lv + " " + t)
        elif kind == "para":
            label, rest = pl
            lines.append("#" * para_level + " " + label + ("\n\n" + esc_line_start(rest) if rest else ""))
        elif kind == "li":
            depth, t = pl[0], pl[1]
            if len(pl) > 2:  # already has marker
                lines.append("  " * (depth - 1) + t)
            else:
                lines.append("  " * (depth - 1) + "- " + t)
        elif kind == "p":
            lines.append(pl)
        else:
            lines.append(pl)
        prev = kind
    # join with blank lines; consecutive list items form one list
    out = []
    for i, (kind, _) in enumerate(merged):
        pass
    text = ""
    prev_li = False
    for l, k in zip(lines, kinds):
        if not l.strip():
            continue
        if text:
            text += "\n" if (k == "li" and prev_li) else "\n\n"
        text += l
        prev_li = k == "li"
    return text


# ---------------------------------------------------------------- PDF (Greenland / Faroe docs)

NO_TEXT_MARK = "er derfor ikke tilgængeligt på retsinformation.dk"
FOOTER_RE = re.compile(r"^\d{1,2}\. \w+ \d{4}\.?( \d+)? Nr\. \d+\.?$")
PDF_PARA_RE = re.compile(r"^(§+\s*\d+\s*[a-zæøå]?\.)\s*(.*)$")
PDF_STK_RE = re.compile(r"^(Stk\. \d+\.)\s*(.*)$")
PDF_LIST_RE = re.compile(r"^(\d+\)|[a-z]\))\s+(.*)$")
PDF_KAP_RE = re.compile(r"^(Kapitel \d+\s*[a-zæøå]?\.?|KAPITEL [0-9IVXLC]+\.?|Afsnit [0-9IVXLC]+\.?)$")


def pdf_blocks(pdf_path, title=""):
    import pypdf
    reader = pypdf.PdfReader(pdf_path)
    lines = []
    for page in reader.pages:
        for ln in (page.extract_text() or "").split("\n"):
            ln = re.sub(r"\s+", " ", ln).strip()
            if not ln or FOOTER_RE.match(ln) or re.match(r"^[A-Z]{2}\d{6}$", ln) \
                    or re.match(r"^Lovtidende [AB] \d{4}$", ln) or re.match(r"^Udgivet den \d", ln):
                continue
            if lines and lines[-1].endswith("\u00ad"):
                lines[-1] = lines[-1][:-1] + ln
                continue
            lines.append(ln)
    lines = [re.sub(r"\u00ad\s*", "", ln) for ln in lines]
    # drop the title lines at the top
    tnorm = re.sub(r"\W+", "", title.lower())
    acc = ""
    while lines and tnorm:
        nxt = acc + re.sub(r"\W+", "", lines[0].lower())
        if nxt and tnorm.startswith(nxt):
            acc = nxt
            lines.pop(0)
        else:
            break
    doc = Doc()
    cur = None  # [kind, label, text]

    def flush():
        nonlocal cur
        if cur:
            kind, label, text = cur
            text = esc_inline(text.strip())
            if kind == "para":
                doc.blocks.append(("para", (esc_inline(label), text)))
            elif kind == "stk":
                doc.blocks.append(("p", f"*{label}* {text}".strip()))
            elif kind == "li":
                doc.blocks.append(("li", (1, esc_line_start(f"{label} {text}"))))
            elif text:
                doc.blocks.append(("p", esc_line_start(text)))
        cur = None

    def add(text):
        if cur[2].endswith("-") and re.search(r"[a-zæøå]-$", cur[2]) and re.match(r"^[a-zæøå]", text):
            cur[2] = cur[2][:-1] + text
        else:
            cur[2] = (cur[2] + " " + text).strip()

    skip_title = not tnorm
    i = 0
    while i < len(lines):
        ln = lines[i]
        if skip_title:
            skip_title = False
            i += 1
            continue
        m = PDF_KAP_RE.match(ln)
        if m:
            flush()
            title = ln
            if i + 1 < len(lines) and not PDF_PARA_RE.match(lines[i + 1]) and len(lines[i + 1]) < 90:
                title += " — " + lines[i + 1]
                i += 1
            doc.blocks.append(("h", (RANK_KAPITEL, esc_inline(title))))
            i += 1
            continue
        m = PDF_PARA_RE.match(ln)
        if m:
            flush()
            cur = ["para", m.group(1), m.group(2)]
        elif PDF_STK_RE.match(ln):
            m = PDF_STK_RE.match(ln)
            flush()
            cur = ["stk", m.group(1), m.group(2)]
        elif PDF_LIST_RE.match(ln) and cur is not None and cur[0] != "li" or (
                PDF_LIST_RE.match(ln) and cur is not None and cur[0] == "li"):
            m = PDF_LIST_RE.match(ln)
            flush()
            cur = ["li", m.group(1), m.group(2)]
        elif cur is None:
            cur = ["p", "", ln]
        else:
            add(ln)
        i += 1
    flush()
    return doc


# ---------------------------------------------------------------- metadata

def read_meta(xml_path):
    meta = {}
    has_body = False
    try:
        root = ET.parse(xml_path).getroot()
        m = root.find("Meta")
        if m is not None:
            for ch in m:
                if ch.text and ch.text.strip() and ch.tag not in meta:
                    meta[ch.tag] = ch.text.strip()
        has_body = root.find("DokumentIndhold") is not None
    except (ET.ParseError, FileNotFoundError):
        pass
    return meta, has_body


def iso(d):
    if not d:
        return None
    m = re.match(r"^(\d{2})/(\d{2})/(\d{4})$", d)
    if m:
        return f"{m.group(3)}-{m.group(2)}-{m.group(1)}"
    m = re.match(r"^(\d{4}-\d{2}-\d{2})", d)
    return m.group(1) if m else None


class QuotedStr(str):
    pass


def _q(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style='"')


yaml.add_representer(QuotedStr, _q)


def front_matter(fm):
    out = {}
    for k, v in fm.items():
        if v is None or v == "":
            continue
        if k in ("date", "last_amended", "retrieved"):
            out[k] = v  # emitted unquoted below
        elif isinstance(v, str):
            out[k] = QuotedStr(v)
        else:
            out[k] = v
    s = yaml.dump(out, allow_unicode=True, sort_keys=False, width=10000)
    for k in ("date", "last_amended", "retrieved"):
        s = re.sub(rf"^{k}: '(\d{{4}}-\d{{2}}-\d{{2}})'$", rf"{k}: \1", s, flags=re.M)
    return "---\n" + s + "---\n"


# ---------------------------------------------------------------- main

def cache_path(raw, link, ext):
    p = link.strip("/").replace("/", "_")
    return os.path.join(raw, "docs", p.split("_")[2], p + ext)


def convert_one(raw, out, item):
    link = item["retsinfoLink"]
    jp = cache_path(raw, link, ".json")
    xp = cache_path(raw, link, ".xml")
    if not os.path.exists(jp) or os.path.getsize(jp) == 0:
        return None, "missing"
    data = json.load(open(jp, encoding="utf-8"))
    if isinstance(data, list):
        data = data[0]
    meta, _ = read_meta(xp)
    html = data.get("documentHtml") or ""
    title = clean_title(data.get("title") or meta.get("DocumentTitle") or item.get("title"))
    popular = (data.get("popularTitle") or meta.get("PopularTitle") or "").strip()
    short = data.get("shortName") or item.get("shortName") or ""
    code = item.get("documentTypeEliCode")
    _, kind, year, num = link.strip("/").split("/")[:4]
    if link in CONSTITUTIONAL:
        name, typ = CONSTITUTIONAL[link]
        rel = f"grundloven/{name}.md"
    else:
        d, typ = TYPES[code]
        slug = slugify(popular or title)
        rel = f"{d}/{year}/{num}-{slug}.md"

    from_pdf = False
    if NO_TEXT_MARK in html:
        pp = cache_path(raw, link, ".pdf")
        if not os.path.exists(pp) or os.path.getsize(pp) == 0:
            return None, "missing-pdf"
        doc = pdf_blocks(pp, title)
        from_pdf = True
    else:
        doc = Doc()
        tree = lxml.html.fromstring("<div>" + html + "</div>") if html.strip() else None
        if tree is not None:
            walk(doc, tree)
    body = render(doc)

    md = {v["displayName"]: v["displayValue"] for v in data.get("metadata", [])
          if isinstance(v, dict)}
    date = iso(meta.get("DiesSigni")) or iso(md.get("Dato for underskrift"))
    status = "in_force"
    if data.get("isHistorical") and link not in CONSTITUTIONAL:
        status = "repealed"
    fm = {
        "title": title,
        "short_title": popular or None,
        "identifier": short,
        "eli": f"{BASE}{link}",
        "accession_number": data.get("accessionNumber") or meta.get("AccessionNumber"),
        "type": typ,
        "jurisdiction": "dk",
        "language": "da",
        "date": date,
        "last_amended": date if code == "LBKH" else None,
        "status": status,
        "ministry": data.get("ressort") or meta.get("Ministry"),
        "source": f"{BASE}{link}/Pdf" if from_pdf else f"{BASE}{link}",
        "text_source": "Lovtidende PDF (text extracted automatically)" if from_pdf else None,
        "retrieved": RETRIEVED,
    }
    notes = data.get("editorialNotes") or []
    parts = [front_matter(fm), f"# {esc_inline(title)}\n"]
    if short:
        parts.append(f"*{esc_inline(short)}*\n")
    if body:
        parts.append(body + "\n")
    if notes:
        parts.append("## Redaktionelle noter\n")
        for n in notes:
            n = tidy(esc_inline(norm_ws(re.sub(r"<br\s*/?>", "\n", str(n)))))
            if n:
                parts.append(esc_line_start(n) + "\n")
    text = "\n".join(parts)
    text = re.sub(r"\n{3,}", "\n\n", text)
    dest = os.path.join(out, rel)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return rel, ("empty" if not body.strip() else "ok")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default=DEFAULT_RAW)
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--only", default=None)
    a = ap.parse_args()
    items = json.load(open(os.path.join(a.raw, "list.json"), encoding="utf-8"))
    stats = {}
    index = []
    for it in items:
        if a.only and a.only not in it["retsinfoLink"]:
            continue
        try:
            rel, st = convert_one(a.raw, a.out, it)
        except Exception as e:  # keep going, report at the end
            print(f"ERROR {it['retsinfoLink']}: {e!r}", file=sys.stderr)
            st, rel = "error", None
        stats[st] = stats.get(st, 0) + 1
        if st in ("missing", "empty"):
            print(f"{st}: {it['retsinfoLink']}", file=sys.stderr)
        if rel:
            index.append(rel)
    print(json.dumps(stats), file=sys.stderr)


if __name__ == "__main__":
    main()
