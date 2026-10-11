# LawCodex — Denmark (Danmark)

Danish legislation in force — Grundloven, Tronfølgeloven, all acts (*love*), consolidated acts
(*lovbekendtgørelser*), amending acts still listed as in force (*ændringslove*), executive orders
(*bekendtgørelser*) and royal ordinances (*anordninger*) — as Markdown, one file per document,
in Danish, converted from [Retsinformation](https://www.retsinformation.dk), the official legal
information system of the Danish state.

Part of [LawCodex](https://github.com/LawCodex): the legislation of every country, as plain
Markdown in git.

## Coverage

Snapshot of Retsinformation retrieved **2026-10-11**. Only documents that Retsinformation lists
as currently in force (*gældende*, i.e. not *historisk*) are included.

| Directory | Retsinformation type | Content | Files |
|---|---|---|---:|
| `grundloven/` | LOV | Danmarks Riges Grundlov (1953), Tronfølgeloven (1953) and the 2009 act amending it | 3 |
| `love/<year>/` | LOV H, LBK H | Acts (*love*, 824) and consolidated acts (*lovbekendtgørelser*, 689) in force | 1,513 |
| `aendringslove/<year>/` | LOV Æ | Amending acts (*ændringslove*) still listed as in force | 1,296 |
| `bekendtgoerelser/<year>/` | BEK H | Executive orders (*bekendtgørelser*) in force | 8,199 |
| `anordninger/<year>/` | AND H | Royal ordinances (*anordninger*), mostly putting acts into force for Greenland / the Faroe Islands | 123 |
| | | **Total** | **11,134** |

### Consolidated vs. original acts

Denmark consolidates acts by publishing a *lovbekendtgørelse* (LBK), which replaces the earlier
act and LBK as the current text; Retsinformation then flags the superseded documents as
historical. Because only non-historical documents are taken, `love/` contains, for each act,
its current consolidated version (LBK) where one exists, and otherwise the original act (LOV)
as amended only by amending acts that have not yet been consolidated. Those amending acts are
in `aendringslove/`.

Tronfølgeloven (lov nr. 170 af 27/03/1953) and its amendment (lov nr. 528 af 12/06/2009) are
flagged *historisk* by Retsinformation (no consolidated text has been published), but both are
in force; they are included in `grundloven/` with `status: in_force`.

Of these, 666 documents (38 in `love/`, 47 in `aendringslove/`, 575 in `bekendtgoerelser/`,
6 in `anordninger/`) concern only Greenland and/or the Faroe Islands and were converted from
the Lovtidende PDF (see below).

### Not covered

- **272 Greenland/Faroe-only documents published before 1 January 2008** (29 acts/consolidated
  acts, 19 amending acts, 217 executive orders, 7 ordinances): Retsinformation lists them as in
  force but has neither their text nor a PDF ("findes derfor kun i den trykte udgave af
  Lovtidende A"), so no file was generated for them.

- Repealed / historical documents and earlier versions.
- Amending executive orders (*ændringsbekendtgørelser*, BEK Æ), commencement orders
  (*ikrafttrædelsesbekendtgørelser*), circulars (*cirkulærer*), guidelines (*vejledninger*),
  letters (*skrivelser*), decisions (*afgørelser*), international treaties
  (*bekendtgørelser af traktater*, BKI), budget text notes, register regulations — all available
  on Retsinformation but not converted here.
- Parliamentary documents (bills, reports), court decisions.
- Images are not stored in the repository; image links point to retsinformation.dk.
- Hyperlinks between documents are reduced to their link text.

## Source and licence

- Source: [Retsinformation](https://www.retsinformation.dk), operated by Civilstyrelsen for the
  Ministry of Justice. Document lists come from the search API used by the website
  (`GET https://www.retsinformation.dk/api/documentsearch?dt=<type>&h=false`), and each
  document's metadata and rendered text from `POST https://www.retsinformation.dk/api/document/eli/<...>`.
  Every file links to the document's ELI URI (e.g. <https://www.retsinformation.dk/eli/lta/1953/169>).
- Documents that concern only Greenland and/or the Faroe Islands are not available as text on
  retsinformation.dk, only as the Lovtidende PDF. For these the text was extracted from the PDF
  (`text_source:` in the front matter says so); the layout reconstruction is automatic and may
  contain minor errors.
- Licence: Danish laws, executive orders and other official legal texts are not protected by
  copyright (*ophavsretsloven* § 9, "Love, administrative forskrifter, retsafgørelser og lignende
  offentlige aktstykker er ikke genstand for ophavsret"). The Markdown conversion in this
  repository is released into the public domain under the same terms.
- This is **not** an official publication. The authoritative texts are those published in
  Lovtidende and on retsinformation.dk.

## File format

```
grundloven/grundloven.md
love/2024/434-straffeloven.md
bekendtgoerelser/2025/1234-bekendtgoerelse-om-....md
```

File names are `<number>-<slug>.md` inside a directory for the year; `<year>/<number>` is the
document's ELI identifier (`eli/lta/<year>/<number>`; a few older documents use
`eli/retsinfo/<year>/<number>` or `eli/ltb/...`). The slug is derived from the popular title
when there is one, otherwise from the title (æ→ae, ø→oe, å→aa). Each file has YAML front
matter:

```yaml
---
title: "Danmarks Riges Grundlov (Grundloven)"
short_title: "Grundloven"                 # Retsinformation "populærtitel", if any
identifier: "LOV nr 169 af 05/06/1953"    # official short designation
eli: "https://www.retsinformation.dk/eli/lta/1953/169"
accession_number: "A19530016930"
type: "constitution"   # constitution | act | consolidated_act | amending_act | executive_order | royal_ordinance
jurisdiction: "dk"
language: "da"
date: 1953-06-05       # date of signature
last_amended: ...      # for consolidated acts: date of the consolidation
status: "in_force"
ministry: "Statsministeriet"
source: "https://www.retsinformation.dk/eli/lta/1953/169"
retrieved: 2026-10-11
---
```

The body keeps the document's structure: parts/chapters (*afsnit*, *kapitel*) and heading
groups become Markdown headings, each section (*§*) is a heading at the deepest level, *stk.*
(subsections) are paragraphs starting with an italic *Stk. n.*, numbered items are list items.
Inside amending provisions, quoted new text (»...«) is not turned into headings. Simple tables
are Markdown tables; tables with merged cells are kept as HTML. Editorial and official notes
appear at the end of the document.

## Regenerating

```sh
pip install -r scripts/requirements.txt
python scripts/fetch.py list    # list documents in force -> _raw/dk/list.json
python scripts/fetch.py fetch   # download document JSON (cached in _raw/dk/docs/)
python scripts/fetch.py pdf     # download PDFs for Greenland/Faroe-only documents
python scripts/convert.py       # write Markdown into this repository
```

Raw downloads go to `../_raw/dk/` (outside the repository) and can be deleted afterwards.
The fetcher identifies itself as `LawCodex/1.0 (+https://github.com/LawCodex)`, uses at most 4
parallel connections and retries with exponential backoff.
