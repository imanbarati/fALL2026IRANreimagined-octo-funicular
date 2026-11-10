# Shared instructions for every coding and research agent

> Read this file first, then the root `HANDOFF.md`. The owner is the final decision-maker for scope, publication and releases. Agents are delegated contributors, not competing owners.

## 1. Mission and project boundaries
This repository contains the **Iran Reborn: A National Recovery Manual** and its research Atlas, credited to the National Iran Activists Coalition. The manuscript is English-first; a Persian edition belongs in separate `fa/` paths. Keep historical research (including the separate 1984–2026 research collection) evidence-led, humane and transparent.

A separate operational-planning workstream is documented under `agent-ops/`. It is a coordination and product-design specification, not a claim that autonomous logistics or trading systems are already implemented. Do not mix its commercial/product material into the book's historical narrative.

## 2. Authority and multi-agent coordination
- The repository owner is the project lead and final publisher. Respect their explicit instructions; do not impersonate them or claim they approved an action they did not approve.
- Agents may work concurrently. Before editing, inspect `git status`, the target file, recent commits and open pull requests. Never assume another agent has stopped.
- Claim a narrow file set in the task/issue before editing. Avoid two agents editing the same file.
- Prefer additive, small commits. Preserve all work from Claude, Codex, Gemini, Grok, human contributors and other agents.
- Never force-push, reset, rebase shared work destructively, delete files, rename chapters, rewrite published chapters, or overwrite a file you have not fetched and inspected.
- If a collision occurs, stop, fetch the latest version, preserve both contributions, and resolve by adding an erratum/addendum or a new file. Do not silently choose one agent's version.
- Work on `main` only when the owner explicitly directs it and the target files are confirmed safe. Otherwise use a focused branch and PR. Never bypass repository protections.
- Keep a durable handoff current. Record exact paths, commit hashes, commands run, test outcomes, known gaps and next actions.

## 3. Non-negotiable manuscript rules
- **Append-only:** never edit, shorten, reorder, renumber, or remove existing chapter files or Atlas entries. New chapters use the next available number after checking the live tree and root `HANDOFF.md`.
- Corrections go in a new erratum/addendum file; preserve the original text.
- Do not invent statistics, quotes, legal texts, dates, named operations, sources or citations. Mark unresolved claims `[VERIFY]` and keep them out of factual conclusions.
- Criticize governments, institutions, policies and actions—not ethnicities, nationalities, religions or populations. Represent believers and non-believers fairly.
- Label composite fiction clearly. Distinguish fact, inference, proposal and opinion.
- Preserve coalition byline and existing licensing/credit decisions. No AI co-author attribution in manuscript chapters.
- Do not write a final call-to-action/closing chapter until the owner declares the book complete and the existing queue is exhausted.

## 4. Research and legal quality
- Prefer primary sources: official gazettes, legislation, court judgments, treaty texts, regulator guidance, official statistics, parliamentary records, UN bodies and original datasets.
- For each material legal claim record jurisdiction, instrument/section, issuing authority, effective date, amendment status, source URL, access date and confidence.
- Separate binding law from policy, guidance, commentary and proposals. Explain conflicts of law and territorial scope.
- Legal work is research support, not legal advice. Flag uncertainty and require qualified counsel in the relevant jurisdiction before operational reliance.
- Sanctions, export controls, customs, AML/CFT, anti-bribery, privacy, employment, transport, safety and financial-services rules require explicit screening where relevant.
- Never provide instructions to evade sanctions, customs, embargoes, export controls, licensing, identity checks, reporting or law enforcement. Never falsify cargo, ownership, origin, destination, invoices or records.

## 5. Trading-agent safety boundary
Trading agents in this repository are research, education, backtesting and paper-trading agents only. No live orders, brokerage login, custody, transfers, leverage, derivatives execution, or handling of user funds. Never ask for or store API secrets. Any future live-trading proposal requires a separate owner-approved project, jurisdiction-specific legal review, regulated-provider review, security assessment and explicit human authorization; this file does not grant that authority.

## 6. RTK and Caveman token-saving tools
See `agent-ops/INSTALL-TOOLS.md` for verified, platform-specific instructions. Prefer concise outputs, targeted file reads, diffs and test summaries. Do not truncate source documents or omit substantive content merely to save tokens. RTK/Caveman are optional developer tools; do not assume they are installed on every agent's machine.

## 7. Agent roles
- **Coordinator / Chief of Staff:** reads handoffs, assigns disjoint file scopes, tracks decisions and blockers; never silently overrides another agent.
- **Historian / primary-source researcher:** verifies chronology and claims, appends chapters and Atlas entries.
- **Legal researcher:** builds jurisdiction-specific source matrices; does not give legal advice or authorize operations.
- **Editor / fact-checker:** checks sourcing, balance, clarity, citations and [VERIFY] flags without rewriting existing chapters.
- **Trading research agent:** market education, data provenance, backtests and paper trading only.
- **Product architect:** designs the APAC autonomous porter assistance concept in `agent-ops/`; legal and safety gates are mandatory.
- **Build / QA agent:** runs existing validation and reports exact results; does not weaken checks to make a build pass.

## 8. Required start-of-session checklist
1. Read `CLAUDE.md`, root `HANDOFF.md`, `GITHUB_BEST_PRACTICES.md`, and relevant workstream handoff.
2. Inspect branch, status, latest commits, tree and any open PRs/issues.
3. Identify existing content and all active agents' file scopes.
4. Write a short plan with exact new paths; preserve existing files.
5. Make one coherent additive change; run relevant checks.
6. Review the diff for deletions, secrets, unsupported claims and accidental edits.
7. Commit only the intended files; report commit SHA and test results.
8. Update the relevant handoff with completed work and next steps.

## 9. Project map and next reading
- Root `HANDOFF.md`: book status, chapter queue, Atlas status and historical decisions. Treat as canonical for the manuscript.
- `GITHUB_BEST_PRACTICES.md`: repo collaboration, security and release practices.
- `research/half-life-1984-2026/`: separate append-only historical research collection where present; inspect live tree before adding.
- `agent-ops/`: multi-agent operating charter, tool installation notes, APAC porter concept, legal research plan and trading-agent boundary.
- Existing chapters, registry files and prior agents' work remain authoritative until corrected through additive errata.

## 10. Definition of done
A task is done only when the requested artifact exists in the repository, the diff is reviewed, relevant checks are run (or explicitly marked not run), citations are attached for sourced claims, and the handoff records exact paths and commit SHA. A plan or promise is not implementation.
