# GitHub best practices for this book

A checklist for the repository owner. Items marked (safety) matter most for this project.

## Before the first push
- Create the repo as **Private**, push, check everything renders, then make it public when ready.
- (safety) Use a pseudonymous account or organization (for example, an org named after the coalition) if contributors could be at risk. Turn on "Keep my email addresses private" in account settings.
- Add a license (see `LICENSE.md`), a README and the files in this repo.
- Commit with your normal identity. Authorship and credit are your decision; the manuscript carries the coalition byline.

## Branches and enforcement of the append-only rule
1. Settings → Branches → add a **branch protection rule** (or ruleset) for `main`:
   - Require a pull request before merging
   - Require status checks to pass: select **append-only** (the job in `.github/workflows/checks.yml`)
   - Require branches to be up to date
   - Do not allow force pushes or deletions
   - Include administrators (so the rule binds you too)
2. Add `.github/CODEOWNERS` handles and enable "Require review from Code Owners".
3. Optional: require signed commits.

## Security
- Enable: secret scanning, push protection, Dependabot alerts, private vulnerability reporting.
- Never commit private testimony, personal data or API keys. Keep sensitive archives encrypted and off GitHub.
- Review third-party text for copyright before pasting; quote under 15 words and cite.

## Organization of the repo
- `manuscript/`: chapters, front matter, appendices, `ERRATA.md` (create when first needed).
- `atlas/registry/`: one CSV per part, sharded to avoid merge conflicts; IDs are permanent.
- `tools/`: validation and progress scripts.
- `docs/`: guides. Add `fa/` (Persian edition) later as new files; never overwrite English.
- `HANDOFF.md` at the root for any human or AI who continues the work.

## Releases and archiving
- Tag editions as `v0.1.0`, `v0.2.0` and so on. Pushing a `v*` tag builds an EPUB and attaches it to a GitHub Release (`.github/workflows/release.yml`).
- Connect the repo to **Zenodo** (GitHub integration) to get a DOI and a permanent archive of each release.
- Keep a second mirror (for example GitLab) and an offline backup. Repositories can be taken down; mirrors protect the "nothing omitted" rule.
- Use GitHub Pages or mdBook later if you want a website.

## Collaboration
- Use **Issues** with the provided templates for proposed subjects and corrections.
- Use **Discussions** for debates (for example unitary vs federal).
- Use small, focused PRs: one chapter or one batch of registry rows per PR.
- Registry batches: add rows only at the end of the CSV; do not reorder.

## Quality
- Run `make check` locally before every PR.
- Keep `[VERIFY]` honest: a subject is only `published` after a source is attached and checked.
- Release notes list new chapters and new subjects by ID.

## Persian edition
Add `fa/` with files named like the English ones (`fa/ch01-ledger-of-damage.md`). Use `dir="rtl"` or an RTL-aware viewer; keep UTF-8 encoding and LF line endings (see `.gitattributes`).
