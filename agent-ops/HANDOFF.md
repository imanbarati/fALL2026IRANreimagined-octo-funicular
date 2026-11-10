# Agent Operations — Persistent Handoff

Last updated: 2026-11-10
Repository: https://github.com/imanbarati/fALL2026IRANreimagined-octo-funicular
Default branch requested by owner: `main`
Owner / final project authority: repository owner (the human user)

## 1. Why this folder exists
This is an additive workstream for coordinating multiple AI and human agents, reducing wasted context, and specifying a lawful APAC-oriented autonomous porter assistance product concept. It does **not** replace the Iran Reborn manuscript or its existing historical research.

The phrase **“Blockade Runner”** is retained only as the owner's working codename/metaphor. It must never be interpreted as permission or a request to evade a blockade, sanctions, customs, export controls, port restrictions, vessel tracking, inspections or law enforcement. The product concept is a compliant logistics/porter assistance and operations-support system.

## 2. Read order for every new agent
1. Root `CLAUDE.md` — shared rules for Claude Code and other agents.
2. Root `HANDOFF.md` — authoritative book status, chapter queue and previous decisions.
3. Root `GITHUB_BEST_PRACTICES.md`.
4. `agent-ops/CHARTER.md` — roles, authority, concurrency and task protocol.
5. `agent-ops/INSTALL-TOOLS.md` — RTK and Caveman.
6. `agent-ops/LEGAL-RESEARCH-PLAN.md` — legal source matrix and gates.
7. `agent-ops/TRADING-AGENT-POLICY.md` — research-only trading boundary.

## 3. Existing project state to preserve
- Root `HANDOFF.md` already exists and contains the book's canonical status, decisions, chapter queue and Atlas instructions. **Do not replace it with this handoff.**
- The manuscript is append-only. At the last inspected root handoff, chapters 00–23 and appendix A were listed as complete; the Atlas registry had 327 queued/VERIFY subjects against an approximately 6,500 target. Re-check the live root handoff and repository tree before relying on these counts.
- An earlier 1984–2026 research workstream was committed under `research/half-life-1984-2026/` with H01–H08 and its own methodology/chronology/source/handoff files. Preserve it and continue only by appending new files.
- The owner previously required preserving concurrent Grok work: do not delete, rename, overwrite or reorganize files another agent may be editing.
- Existing root `README.md`, `GITHUB_BEST_PRACTICES.md`, manuscript files, Atlas CSVs, tools and workflows must remain intact.

## 4. Workstream status
This handoff defines governance and specifications. It does not assert that RTK, Caveman, a trading bot, a porter product, legal approvals, APAC licenses, integrations or production infrastructure have been installed or deployed.

| Workstream | Status | Next action |
|---|---|---|
| Shared agent instructions | Added in root `CLAUDE.md` | Each agent reads it at session start |
| Multi-agent charter | Added in `agent-ops/CHARTER.md` | Use file-scope claims and decision log |
| RTK + Caveman | Setup guide added | Install on each actual workstation; verify commands |
| APAC porter concept | Specification added | Discovery, user journeys, jurisdiction selection, prototype plan |
| Legal research | Matrix and gates added | Counsel-led jurisdiction review before any pilot |
| Trading agents | Safety policy added | Build research/backtest/paper-trading only |

## 5. Product concept: “Blockade Runner” / APAC autonomous porter assistance
Working product label only: **Blockade Runner — APAC Porter Assistance System (APAS)**. “Corpo” is treated as a possible corporate/enterprise operating model, not as a registered company or legal entity.

Proposed lawful scope:
- Assist porters, warehouse teams, dispatchers, freight forwarders and customer-service staff with task intake, queueing, status updates, translation, document completeness checks and exception escalation.
- Provide human-reviewed route and handoff suggestions using authorized, accurate data.
- Support accessibility, multilingual APAC workflows and auditable customer communications.
- Integrate only with licensed/authorized carriers, ports, customs brokers and enterprise systems.
- Maintain human control over safety-critical movement, customs declarations, release of goods, payments, customer commitments and exceptions.

Explicit exclusions:
- No sanctions evasion, blockade running in the literal sense, covert routing, AIS/GPS spoofing, cargo concealment, false manifests, transshipment designed to hide origin/destination, bribery, inspection avoidance or restricted-goods facilitation.
- No autonomous operation of vehicles, cranes, vessels, lifts or machinery in this phase.
- No autonomous customs declarations, legal determinations, payments, contract acceptance or release of cargo.
- No collection of passport/ID, biometrics, location history or sensitive customer data without a documented lawful basis, minimization, retention schedule and security controls.

## 6. Trading-agent scope
Trading agents are separate from logistics agents and from the Iran Reborn manuscript. They may research public market data, explain concepts, build reproducible backtests and simulate paper portfolios. They must not execute real trades or access brokerage accounts, wallets, funds or credentials. See `TRADING-AGENT-POLICY.md`.

## 7. Concurrency protocol
- Every agent announces a task name, intended paths, branch and timestamp in an issue or shared coordination note.
- One writer per file at a time. Parallel work is allowed only on disjoint files.
- Before a commit, fetch latest `main`, inspect status and diff, and preserve intervening commits.
- Prefer focused branches/PRs. If the owner explicitly requests direct-to-main, create only new paths after verifying they do not exist.
- Never use force push, destructive reset, mass formatting, broad find-and-replace or generated rewrites across existing chapters.
- If an agent cannot verify a claim, leave a clearly labeled TODO with the missing source; do not fabricate completion.
- Every handoff update records UTC date/time, commit SHA, files changed, checks run, checks not run, and next owner.

## 8. Immediate next tasks
1. Each agent reads the seven files in the read order above.
2. Coordinator establishes issue-based ownership for each chapter / research batch / software component.
3. Historical agents continue the root HANDOFF chapter queue and 1984–2026 research in their existing separate folders, without editing completed chapters.
4. Legal researcher creates an APAC jurisdiction matrix only after the intended pilot countries and actual activity are identified; no jurisdiction should be assumed.
5. Product architect turns the porter concept into a threat model, workflow diagrams, human-approval gates and a non-production prototype plan.
6. Trading research agent documents data sources, backtest assumptions, costs, slippage and paper-only controls.

## 9. Verification checklist for future updates
- [ ] Existing content preserved; no unintended deletions or modifications.
- [ ] All new facts sourced, date-stamped and jurisdiction-tagged where relevant.
- [ ] No secret, token, private testimony, personal data or credential committed.
- [ ] Legal/safety review status stated honestly.
- [ ] Tests and validation commands run and results recorded.
- [ ] Handoff updated with exact commit SHA.
