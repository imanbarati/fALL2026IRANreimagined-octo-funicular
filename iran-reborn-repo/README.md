# Iran Reborn: A National Recovery Manual

By the **National Iran Activists Coalition**. A living, append-only book on national rejuvenation and recovery after the war and the damage of the Islamic Republic, with an Atlas of timelines, laws and programs.

**Rules:** always add new chapters; never rewrite existing ones; nothing is omitted.

## Layout
| Path | What it is |
|---|---|
| `manuscript/` | Front matter, chapters 1–23, appendix |
| `atlas/registry/` | The subject registry (events, laws, programs), one CSV per Part A–F |
| `atlas/ENTRY_TEMPLATE.md` | Shape of every Atlas entry |
| `tools/` | Validation, progress and append-only checks |
| `HANDOFF.md` | Full instructions for anyone, human or AI, who continues the work |
| `docs/GITHUB_BEST_PRACTICES.md` | Repository setup checklist |

## Status
Run `python tools/stats.py`. At the time of writing the registry holds 327 queued subjects against a target of about 6,500.

## Build
`make check` · `make stats` · `make epub` (requires pandoc)

## Safety and license
See `SECURITY.md` and `LICENSE.md`.
