# APAC Legal Research Plan — Porter Assistance System

**Purpose:** establish a verifiable legal research workstream for a proposed APAC porter/logistics assistance platform. This is a research checklist, not legal advice, a legal opinion, a license, or authorization to operate. APAC is not one legal jurisdiction. No country-specific conclusion should be made until the pilot country, actual services, counterparties, data flows and operating model are identified.

## 1. First define the activity
For each proposed country, document:
- Where the company, staff, customers, servers and vendors are located.
- Whether the product is software-only, a logistics intermediary, freight forwarder, customs broker, carrier, port operator, staffing provider, payment intermediary or some combination.
- Whether it handles cargo, takes custody, arranges transport, issues documents, makes declarations, collects payments, employs workers or controls physical equipment.
- Cargo categories, origin, destination, transit points, end users and beneficial owners.
- Data collected (identity, location, voice, video, biometrics, shipment, payment and employment data), purpose, access, transfers and retention.
- Human decision-makers and the precise actions an automated component may propose, execute or block.

## 2. Legal domains to research in each jurisdiction

### A. Corporate formation and foreign investment
- Entity form, registration, beneficial ownership, directors, local presence and foreign ownership restrictions.
- Foreign investment screening, sector restrictions, local partner requirements and licensing.
- Corporate governance, accounting, tax, permanent establishment and recordkeeping.

### B. Logistics, ports, freight and customs
- Freight-forwarder, carrier, warehouse, port-service and customs-broker licensing.
- Customs declarations, importer/exporter of record, valuation, tariff classification, origin, transit and record retention.
- Port access, security credentials, dangerous goods, cargo handling and chain of custody.
- Cabotage, maritime/aviation/road transport rules where applicable.
- No automated filing or cargo release until the legal role, delegation and accountable declarant are confirmed.

### C. Sanctions, export controls and restricted goods
- Applicable UN and domestic sanctions; relevant US, EU, UK and other regimes where nexus exists.
- Export-control classification, dual-use controls, end-use/end-user restrictions, re-export and transit controls.
- Restricted parties, beneficial ownership, destination and diversion-risk screening.
- Documentary evidence and escalation procedures.
- **Hard prohibition:** no evasion, concealment, false origin/destination, transshipment designed to disguise parties, AIS/GPS spoofing, false manifests, inspection avoidance, bribery or routing around lawful restrictions. Stop and escalate uncertain matches.

### D. AML/CFT, anti-bribery and fraud
- Whether the business is a regulated or obliged entity; customer due diligence and beneficial-owner checks.
- Suspicious transaction reporting, sanctions screening, payment flows and record retention.
- Anti-bribery, gifts, facilitation payments, public-official interactions and third-party due diligence.
- Fraud, identity theft, invoice manipulation and cargo theft controls.

### E. Privacy, cybersecurity and AI governance
- Country privacy statutes, regulator registration/notification, lawful basis/consent, purpose limitation, minimization and retention.
- Cross-border data transfers, localization, subprocessors and data processing agreements.
- Worker monitoring, geolocation, voice/video, biometrics and automated decision-making.
- Cybersecurity obligations, breach notification, critical infrastructure and incident response.
- AI transparency, human oversight, model risk, recordkeeping, bias, explainability and prohibited use cases.
- Do not use personal or shipment data to train models without a documented lawful basis and approved governance.

### F. Employment, labor and occupational safety
- Worker classification, employment contracts, wages, hours, overtime, leave, social insurance and migrant-worker rules.
- Occupational health and safety, manual handling, lifting, fatigue, heat, vehicles, machinery and workplace injury reporting.
- Consultation, unions/worker representation, surveillance and disciplinary use of AI-generated metrics.
- No automated assignment or performance scoring without impact review and human appeal.

### G. Consumer, commercial and competition law
- Consumer protection, electronic transactions, e-signatures, advertising and unfair contract terms.
- Service-level commitments, liability caps, cargo insurance, indemnities and dispute resolution.
- Competition/antitrust, data sharing, exclusivity, platform neutrality and pricing algorithms.
- Accessibility and language requirements.

### H. Payments, insurance and financial services
- Payment-services, stored-value, remittance, lending, insurance distribution and financial-advice licensing triggers.
- If the platform only passes a payment to a licensed provider, verify the precise agency and technical model.
- No custody, wallet, escrow, money transmission, credit or investment execution without separate legal analysis and licensing.

### I. Tax, accounting and records
- Corporate income tax, VAT/GST, withholding, customs duties, transfer pricing and e-invoicing.
- Statutory books, audit, retention and lawful access requirements.

### J. Physical safety, accessibility and product liability
- Product safety and machinery standards if hardware or robotics are introduced.
- Functional safety, human factors, accessibility, emergency stop, fail-safe and incident reporting.
- Product liability, public liability, cargo insurance and professional indemnity.

## 3. Country selection and primary-source research
Do not assume “APAC” means one uniform set of laws. Start a jurisdiction matrix only after pilot markets are chosen. Candidate research queues may include Australia, New Zealand, Singapore, Japan, South Korea, India, Indonesia, Malaysia, Thailand, Vietnam, Philippines, Hong Kong and Taiwan, but listing a market is not a recommendation or finding.

For every country:
1. Identify the official regulator(s) and government legislation portal.
2. Locate the current consolidated law, regulations, regulator guidance and relevant judgments.
3. Record the exact section/article, commencement date, amendment status and territorial scope.
4. Identify local counsel requirements and any mandatory local representative.
5. Record conflicts with cross-border rules and the relevant nexus.
6. Have qualified local counsel review the actual business model and data flows.

## 4. Source register template
Use one row per legal requirement:
| Field | Required value |
|---|---|
| Jurisdiction | Country / state / territory |
| Activity | Exact product activity being assessed |
| Domain | Customs, privacy, labor, sanctions, etc. |
| Instrument | Official title and number |
| Provision | Exact article/section |
| Authority | Legislature, regulator or court |
| Status | In force / amended / repealed / proposed / guidance |
| Effective date | YYYY-MM-DD |
| Official URL | Government or regulator source |
| Access date | YYYY-MM-DD |
| Obligation | Plain-language summary with limits |
| Owner | Named internal reviewer |
| Counsel status | Not reviewed / questions sent / reviewed |
| Confidence | High / medium / low |
| Open issue | What remains unresolved |

## 5. Launch gates
No real-world pilot until all relevant gates are documented:
- [ ] Country and operating entity selected.
- [ ] Exact legal role and regulated activities mapped.
- [ ] Local counsel has reviewed the business model.
- [ ] Customs, sanctions, export-control and restricted-goods controls tested.
- [ ] Privacy impact assessment and cross-border transfer review complete.
- [ ] Labor and occupational safety review complete.
- [ ] Security threat model, incident response and vendor due diligence complete.
- [ ] Insurance and liability allocation confirmed.
- [ ] Human approval and manual fallback tested.
- [ ] Customer terms, worker notices and consent flows reviewed.
- [ ] Owner approves the limited pilot in writing.

## 6. Researcher guardrails
- Quote only what is necessary; cite official sources and preserve legal qualifications.
- Distinguish legislation from regulator guidance and unofficial commentary.
- Never infer that a rule does not exist because a quick search found nothing.
- Do not convert a legal uncertainty into a model-generated yes/no answer.
- Mark unresolved points `[COUNSEL REVIEW REQUIRED]`.
- Do not give users instructions to avoid lawful restrictions or exploit regulatory gaps.
