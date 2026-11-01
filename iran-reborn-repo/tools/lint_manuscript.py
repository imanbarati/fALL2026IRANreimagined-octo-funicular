#!/usr/bin/env python3
"""Lint manuscript files: required sections, chapter numbering gaps, and [VERIFY] counts."""
import glob, re, sys
errs, nums = [], []
for p in sorted(glob.glob("manuscript/ch*.md")):
    t = open(p, encoding="utf-8").read()
    m = re.match(r"manuscript/ch(\d{2})-", p)
    nums.append(int(m.group(1)))
    if not t.startswith("# Chapter"): errs.append(f"{p}: must start with '# Chapter N — Title'")
    for sec in ("Objections and Honest Limits", "What We Will Do"):
        if sec not in t: errs.append(f"{p}: missing section '{sec}'")
    if re.search(r"co-?authored by (claude|ai)", t, re.I): errs.append(f"{p}: contains AI co-author line")
gaps = [n for n in range(1, max(nums)+1) if n not in nums]
if gaps: errs.append(f"chapter number gaps: {gaps}")
v = sum(open(p, encoding="utf-8").read().count("[VERIFY") for p in glob.glob("manuscript/*.md"))
print(f"{len(nums)} chapters, {v} [VERIFY] tags outstanding")
if errs: print("\n".join(errs)); sys.exit(1)
print("manuscript OK")
