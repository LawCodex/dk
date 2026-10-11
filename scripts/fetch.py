#!/usr/bin/env python3
"""Fetch Danish legislation in force from Retsinformation (www.retsinformation.dk).

Step 1 (list):  query the public search API used by the website
                (GET /api/documentsearch?dt=<type>&h=false&ps=100&page=N) for every
                document type in scope, restricted to documents in force (h=false).
Step 2 (fetch): for each document, download the document JSON
                (POST /api/document/eli/<...>, the call the website itself makes), which holds
                the metadata and the rendered HTML text. (The ELI XML, GET /eli/<...>/xml, is
                not needed: for documents before ~2000 it carries metadata only, no text.)
Step 3 (pdf):   documents concerning only Greenland / the Faroe Islands have no text on
                retsinformation.dk, only the Lovtidende PDF (GET /eli/<...>/Pdf); fetch those.
Everything is cached under _raw/dk/ so re-runs only fetch what is missing.

Usage: python fetch.py [list|fetch|pdf|all] [--raw DIR] [--workers N]
"""
import argparse
import json
import os
import random
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

BASE = "https://www.retsinformation.dk"
UA = "LawCodex/1.0 (+https://github.com/LawCodex)"
HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_RAW = os.path.normpath(os.path.join(HERE, "..", "..", "_raw", "dk"))

# Retsinformation document type ids (search filter "dt")
DOC_TYPES = {
    10: "LOV",      # Lov (act)
    20: "LOVC",     # Ændringslov (amending act)
    30: "LBK",      # Lovbekendtgørelse (consolidated act)
    60: "BEK",      # Bekendtgørelse (executive order)
    100: "AND",     # Anordning (royal ordinance, e.g. for Greenland / Faroe Islands)
}
# Documents that must always be included regardless of search results
# Grundloven, Tronfølgeloven and its 2009 amendment (Retsinformation flags the last two as
# "historic" because no consolidated version exists, but they are in force)
EXTRA = ["/eli/lta/1953/169", "/eli/lta/1953/170", "/eli/lta/2009/528"]

_session = None


def session():
    global _session
    if _session is None:
        s = requests.Session()
        s.headers["User-Agent"] = UA
        _session = s
    return _session


def req(method, url, **kw):
    for attempt in range(7):
        try:
            r = session().request(method, url, timeout=120, **kw)
            if r.status_code == 200:
                return r
            if r.status_code == 404:
                return None
            err = f"HTTP {r.status_code}"
        except requests.RequestException as e:
            err = str(e)
        wait = min(120, 2 ** attempt + random.random())
        print(f"  retry {attempt + 1} {url}: {err} (sleep {wait:.0f}s)", file=sys.stderr)
        time.sleep(wait)
    raise RuntimeError(f"failed: {url}")


def do_list(raw):
    out = []
    seen = set()
    for dt, code in DOC_TYPES.items():
        page = 0  # the API's page index is 0-based
        while True:
            url = f"{BASE}/api/documentsearch?dt={dt}&h=false&ps=100&page={page}"
            d = req("GET", url).json()
            for doc in d["documents"]:
                link = doc["retsinfoLink"]
                if link in seen:
                    continue
                seen.add(link)
                doc["_dt"] = dt
                out.append(doc)
            print(f"list dt={dt} page {page + 1}/{d['pageCount']} ({d['resultCount']})", file=sys.stderr)
            if page + 1 >= d["pageCount"]:
                break
            page += 1
            time.sleep(0.2)
    for link in EXTRA:
        if link not in seen:
            out.append({"retsinfoLink": link, "_dt": 10, "_extra": True})
    with open(os.path.join(raw, "list.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=0)
    print(f"{len(out)} documents listed", file=sys.stderr)
    return out


def cache_path(raw, link, ext):
    p = link.strip("/").replace("/", "_")
    sub = os.path.join(raw, "docs", p.split("_")[2] if p.count("_") >= 2 else "x")
    os.makedirs(sub, exist_ok=True)
    return os.path.join(sub, p + ext)


def fetch_one(raw, link, xml=False):
    xp = cache_path(raw, link, ".xml")
    jp = cache_path(raw, link, ".json")
    got = 0
    if xml and not os.path.exists(xp):
        r = req("GET", BASE + link + "/xml")
        with open(xp + ".tmp", "wb") as f:
            f.write(r.content if r is not None else b"")
        os.replace(xp + ".tmp", xp)
        got += 1
    if not os.path.exists(jp):
        r = req("POST", BASE + "/api/document" + link, json={"isRawHtml": False})
        with open(jp + ".tmp", "wb") as f:
            f.write(r.content if r is not None else b"")
        os.replace(jp + ".tmp", jp)
        got += 1
    if got:
        time.sleep(0.25)
    return got


def fetch_pdf(raw, link):
    pp = cache_path(raw, link, ".pdf")
    if os.path.exists(pp):
        return 0
    r = req("GET", BASE + link + "/Pdf")
    with open(pp + ".tmp", "wb") as f:
        f.write(r.content if r is not None else b"")
    os.replace(pp + ".tmp", pp)
    time.sleep(0.25)
    return 1


NO_TEXT_MARK = "er derfor ikke tilgængeligt på retsinformation.dk"


def do_pdf(raw, workers):
    with open(os.path.join(raw, "list.json"), encoding="utf-8") as f:
        docs = json.load(f)
    links = []
    for d in docs:
        jp = cache_path(raw, d["retsinfoLink"], ".json")
        if os.path.exists(jp):
            with open(jp, encoding="utf-8") as f:
                if NO_TEXT_MARK in f.read():
                    links.append(d["retsinfoLink"])
    print(f"{len(links)} documents without HTML text; fetching PDFs", file=sys.stderr)
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for fut in as_completed([ex.submit(fetch_pdf, raw, l) for l in links]):
            fut.result()


def do_fetch(raw, workers):
    with open(os.path.join(raw, "list.json"), encoding="utf-8") as f:
        docs = json.load(f)
    links = [d["retsinfoLink"] for d in docs]
    done = 0
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(fetch_one, raw, l): l for l in links}
        for fut in as_completed(futs):
            fut.result()
            done += 1
            if done % 200 == 0:
                print(f"fetched {done}/{len(links)}", file=sys.stderr)
    print(f"fetched {done}/{len(links)}", file=sys.stderr)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("step", nargs="?", default="all", choices=["list", "fetch", "pdf", "all"])
    ap.add_argument("--raw", default=DEFAULT_RAW)
    ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args()
    os.makedirs(a.raw, exist_ok=True)
    if a.step in ("list", "all"):
        do_list(a.raw)
    if a.step in ("fetch", "all"):
        do_fetch(a.raw, a.workers)
    if a.step in ("pdf", "all"):
        do_pdf(a.raw, a.workers)


if __name__ == "__main__":
    main()
