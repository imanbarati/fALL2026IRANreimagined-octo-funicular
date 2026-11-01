#!/usr/bin/env python3
"""Append a new subject to the right registry file with the next free ID.

Usage:
  python tools/new_entry.py PART TYPE CATEGORY JURISDICTION YEAR "Title" [--source URL] [--notes TEXT]
Example:
  python tools/new_entry.py A event protest Iran 2019 "Example event title" --source https://example.org
"""
import csv, glob, sys, argparse, os
ap = argparse.ArgumentParser()
ap.add_argument("part"); ap.add_argument("type"); ap.add_argument("category")
ap.add_argument("jurisdiction"); ap.add_argument("year"); ap.add_argument("title")
ap.add_argument("--source", default=""); ap.add_argument("--notes", default="")
a = ap.parse_args()
files = {os.path.basename(p).split("-")[1]: p for p in glob.glob("atlas/registry/part-*.csv")}
path = files[a.part]
rows = list(csv.DictReader(open(path, encoding="utf-8")))
nxt = max(int(r["id"].split("-")[1]) for r in rows) + 1 if rows else 1
rid = f"{a.part}-{nxt:04d}"
with open(path, "a", newline="", encoding="utf-8") as f:
    csv.writer(f, lineterminator="\n").writerow([rid,a.part,a.type,a.category,a.jurisdiction,a.year,a.title,"queued","VERIFY",a.source,a.notes])
print("added", rid)
