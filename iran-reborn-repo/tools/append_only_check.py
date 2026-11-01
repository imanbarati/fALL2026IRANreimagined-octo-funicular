#!/usr/bin/env python3
"""Enforce the book's rule: ALWAYS ADD NEW CHAPTERS, NEVER REWRITE EXISTING CHAPTERS.

Usage: python tools/append_only_check.py origin/main
Fails if, relative to the base ref, any file under manuscript/ was modified, deleted or renamed.
Exceptions: manuscript/ERRATA.md and manuscript/appendix-*.md may only gain lines (no deletions).
New files are always allowed.
"""
import subprocess, sys, fnmatch

base = sys.argv[1] if len(sys.argv) > 1 else "origin/main"
out = subprocess.run(["git","diff","--name-status","--find-renames",f"{base}...HEAD","--","manuscript/"],
                     capture_output=True, text=True, check=True).stdout.strip().splitlines()
errors = []
for line in out:
    parts = line.split("\t")
    status, path = parts[0], parts[-1]
    if status.startswith("A"):
        continue
    additive_ok = fnmatch.fnmatch(path, "manuscript/ERRATA.md") or fnmatch.fnmatch(path, "manuscript/appendix-*.md")
    if status == "M" and additive_ok:
        num = subprocess.run(["git","diff","--numstat",f"{base}...HEAD","--",path],
                             capture_output=True, text=True, check=True).stdout.split()
        if num and num[1] != "0":
            errors.append(f"{path}: lines were deleted; append-only files may only gain lines")
        continue
    errors.append(f"{path}: status {status} not allowed (existing manuscript files are append-only)")
if errors:
    print("APPEND-ONLY VIOLATION:\n" + "\n".join(errors))
    sys.exit(1)
print("append-only OK")
