#!/usr/bin/env python3
"""Validate atlas/registry/*.csv. Fails on schema errors, duplicate IDs or ID gaps/rewrites.

Usage: python tools/validate_registry.py [--base origin/main]
With --base, also verifies that no existing row's ID was removed or its ID/title changed
(append-only registry).
"""
import csv, glob, subprocess, sys, re, io

HEAD = ["id","part","type","category","jurisdiction","year","title","status","verify","source","notes"]
PARTS = set("ABCDEF")
TYPES = {"event","law","program","institution","treaty"}
STATUS = {"queued","drafted","sourced","published","withdrawn"}
YEAR = re.compile(r"^-?\d{1,4}(-\d{1,4})?$")

def load(text):
    return list(csv.DictReader(io.StringIO(text)))

def check_file(path, text):
    errs = []
    rows = load(text)
    if rows and list(rows[0].keys()) != HEAD:
        errs.append(f"{path}: header must be {HEAD}")
        return errs, rows
    seen = set()
    for n, r in enumerate(rows, start=2):
        loc = f"{path}:{n}"
        if not re.fullmatch(r"[A-F]-\d{4,}", r["id"]): errs.append(f"{loc} bad id {r['id']!r}")
        if r["id"] in seen: errs.append(f"{loc} duplicate id {r['id']}")
        seen.add(r["id"])
        if r["part"] not in PARTS or not r["id"].startswith(r["part"]): errs.append(f"{loc} part/id mismatch")
        if r["type"] not in TYPES: errs.append(f"{loc} bad type {r['type']!r}")
        if r["status"] not in STATUS: errs.append(f"{loc} bad status {r['status']!r}")
        if not YEAR.match(r["year"]): errs.append(f"{loc} bad year {r['year']!r}")
        if not r["title"].strip(): errs.append(f"{loc} empty title")
        if r["status"] in {"sourced","published"} and not r["source"].strip():
            errs.append(f"{loc} {r['status']} requires a source")
        if r["status"] == "published" and r["verify"] == "VERIFY":
            errs.append(f"{loc} published entries cannot still be marked VERIFY")
    return errs, rows

def main():
    base = None
    if "--base" in sys.argv:
        base = sys.argv[sys.argv.index("--base") + 1]
    errs = []
    for path in sorted(glob.glob("atlas/registry/*.csv")):
        text = open(path, encoding="utf-8").read()
        e, rows = check_file(path, text)
        errs += e
        if base:
            try:
                old = subprocess.run(["git","show",f"{base}:{path}"], capture_output=True, text=True, check=True).stdout
            except subprocess.CalledProcessError:
                continue  # new file
            oldrows = {r["id"]: r for r in load(old)}
            newrows = {r["id"]: r for r in rows}
            for i, o in oldrows.items():
                if i not in newrows:
                    errs.append(f"{path}: ID {i} was removed (use status=withdrawn instead)")
                elif newrows[i]["title"] != o["title"] or newrows[i]["year"] != o["year"]:
                    errs.append(f"{path}: ID {i} title/year changed; add a correction note instead")
    if errs:
        print("\n".join(errs)); sys.exit(1)
    print("registry OK")

if __name__ == "__main__":
    main()
