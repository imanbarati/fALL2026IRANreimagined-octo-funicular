#!/usr/bin/env python3
"""Progress dashboard: subjects per part vs target, and status counts."""
import csv, glob, collections
TARGET = {"A":1200,"B":900,"C":900,"D":800,"E":1300,"F":1400}  # sums to 6,500
names = {}
counts = collections.defaultdict(collections.Counter)
for p in sorted(glob.glob("atlas/registry/*.csv")):
    for r in csv.DictReader(open(p, encoding="utf-8")):
        counts[r["part"]][r["status"]] += 1
tot = 0
print(f"{'Part':<5}{'Have':>6}{'Target':>8}{'%':>7}   statuses")
for part in "ABCDEF":
    have = sum(counts[part].values()); tot += have
    t = TARGET[part]
    print(f"{part:<5}{have:>6}{t:>8}{100*have/t:>6.1f}%   {dict(counts[part])}")
print(f"TOTAL {tot} of {sum(TARGET.values())} ({100*tot/sum(TARGET.values()):.1f}%)")
