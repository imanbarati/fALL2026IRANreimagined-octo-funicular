# Multi-Agent Charter and Product Operating Model

## 1. Owner-led governance
The repository owner is the project principal: sets goals, prioritizes work, chooses public releases and has final approval. Agents are empowered to research, draft, test and propose within their assigned scope. “Make me king” is translated into a clear governance rule: **one human owner, delegated agent roles, transparent decisions, no agent self-authorization**.

No agent may claim legal authority, company registration, regulatory approval, customer consent, or owner approval that has not actually been granted.

## 2. Agent topology
| Role | Mandate | Must not |
|---|---|---|
| Chief of Staff / Orchestrator | Maintain handoffs, assign disjoint scopes, track blockers and decisions | Overwrite other agents or make owner-only decisions |
| Historical Researcher | Build chronology, locate primary sources, append chapters | Rewrite completed chapters or turn disputed claims into facts |
| Legal Researcher | Map statutes, regulators, licenses, cases and official guidance | Give definitive legal advice or approve operations |
| Fact-checker / Editor | Verify claims, citations, neutrality, attribution and readability | Delete source nuance or silently rewrite published text |
| Product Architect | Specify porter assistant workflows, APIs, data and safety boundaries | Deploy an autonomous physical system |
| Logistics Operations Analyst | Map authorized porter, warehouse, dispatch and customer workflows | Plan sanctions/customs evasion or concealment |
| Trading Research Agent | Public-data research, reproducible backtests, paper portfolios | Place live orders or handle funds/credentials |
| Software Engineer | Implement isolated components with tests and documented interfaces | Change security controls just to make tests pass |
| QA / Release Agent | Validate builds, accessibility, audit logs and release artifacts | Publish without required approval |

## 3. Task lifecycle
1. **Intake:** write goal, user value, non-goals, risk class and acceptance criteria.
2. **Assign:** give each agent exact files and one accountable owner. Parallelize only disjoint work.
3. **Research:** use primary sources and record access dates. Separate facts from interpretation.
4. **Plan:** identify dependencies, data classes, jurisdictions and human decisions.
5. **Build:** smallest useful increment, no destructive edits.
6. **Review:** independent fact, security, legal and QA review as appropriate.
7. **Approve:** owner approval for public release, live integrations, spending, customer commitments and high-impact actions.
8. **Handoff:** update durable docs, exact commit, tests, limitations and next steps.

## 4. Decision rights
- Agents can create draft documents, code, tests and research branches within assigned scope.
- Owner approval is required before public statements on behalf of the coalition, publishing releases, spending money, contacting third parties, accepting contracts, enabling live integrations, handling funds or making irreversible changes.
- Legal counsel approval is required before relying on legal conclusions for a real APAC deployment.
- A safety-critical action always remains under a qualified human operator in this concept phase.

## 5. “Blockade Runner” APAC Porter Assistance System (APAS)
This is a working product concept for a corporate/enterprise porter-assistance service across APAC. The name is a codename, not an operational objective to run blockades.

### Intended users
- Porters and warehouse floor staff
- Dispatch and shift supervisors
- Freight-forwarder / carrier customer-service teams
- Enterprise operations managers
- Customers receiving authorized status updates

### Candidate capabilities
1. **Intake:** multilingual text/voice request capture, ticket creation, urgency tagging and identity-safe triage.
2. **Work queue:** assign tasks to available human staff, show priority and dependencies, track acceptance/completion.
3. **Porter copilot:** concise instructions, location-aware only when lawful and necessary, accessible interface, translation and escalation.
4. **Shipment support:** read-only tracking from authorized carrier/port APIs; explain status and flag missing paperwork without altering declarations.
5. **Document assistant:** checklist for invoices, packing lists, permits and certificates; detect missing fields but never fabricate or submit them autonomously.
6. **Customer communications:** draft multilingual status messages for human review; log delivery and consent.
7. **Operations dashboard:** workload, queue age, service levels, incidents, exception reasons and audit trails.
8. **Compliance guardrails:** jurisdiction and party screening workflow, restricted-goods escalation, data minimization, retention and human sign-off.

### Architecture principles
- Start as a web/mobile workflow assistant, not an autonomous robot or vehicle.
- Separate tenant data; enforce least privilege and role-based access.
- Use explicit API allowlists, signed webhooks, idempotency keys and audit logs.
- Store only necessary personal data; encrypt in transit and at rest; define retention and deletion.
- Treat external documents, messages and model outputs as untrusted input.
- Use retrieval with citations for policies; never let a model invent legal requirements.
- Fail closed on sanctions, export-control, customs, identity, safety and payment exceptions.
- Require a human operator for cargo release, declarations, route exceptions, safety incidents and contractual commitments.
- Build offline/degraded-mode procedures for connectivity loss and clear manual fallback.

### MVP sequence
- Phase 0: discovery interviews, process maps, risk register and jurisdiction selection.
- Phase 1: clickable prototype with synthetic data only.
- Phase 2: read-only integration to one authorized sandbox carrier or warehouse system.
- Phase 3: staff task queue and customer status drafts with human approval.
- Phase 4: limited supervised pilot after local counsel, security, privacy, labor and safety reviews.
- Later automation requires a separate hazard analysis, regulator review and owner authorization.

## 6. Required product artifacts before implementation
- Product requirements document and explicit non-goals
- APAC country-by-country activity and data-flow map
- Stakeholder and user-research notes with consent
- Threat model and abuse-case analysis
- Data inventory, lawful-basis analysis, retention and deletion plan
- Human factors, accessibility and worker-safety assessment
- API inventory and vendor authorization evidence
- Incident response, audit and business-continuity plans
- Counsel-reviewed licensing, customs, sanctions and employment matrix
- Acceptance tests proving prohibited actions are blocked

## 7. Quality bar
A feature is not “autonomous” merely because an LLM proposes an action. Autonomy must be described precisely by action, permissions, scope, reversibility, monitoring and human override. Use the least autonomy needed to deliver the user value.
