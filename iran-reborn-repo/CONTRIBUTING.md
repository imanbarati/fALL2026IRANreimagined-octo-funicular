# Contributing

## The two golden rules
1. **Always add new chapters. Never rewrite existing chapters.** Files in `manuscript/ch*.md` are append-only. Corrections go in `manuscript/ERRATA.md` or in a new chapter or addendum. CI blocks any PR that edits, renames or deletes an existing chapter.
2. **Nothing is omitted.** Subjects are never deleted from the registry. To retire a subject, set `status=withdrawn` and say why in `notes`.

## How to add a chapter
1. Read `HANDOFF.md`.
2. Create `manuscript/chNN-short-slug.md` with the next number.
3. Use the chapter shape: hook, claims, proposals, **Objections and Honest Limits**, **What We Will Do / What You Can Do**.
4. Tag every uncertain fact with `[VERIFY]`. Quote under 15 words; paraphrase everything else.
5. Update the status table in `HANDOFF.md`.

## How to add subjects to the Atlas
`python tools/new_entry.py A event protest Iran 2019 "Title" --source URL`, or open the "Propose a new Atlas subject" issue.

## Before you push
`make check` (requires Python 3). Open a pull request; do not push directly to `main`.

## Tone
Criticize governments, institutions and policies; never peoples, ethnicities or religions. Respect believers and non-believers equally.
