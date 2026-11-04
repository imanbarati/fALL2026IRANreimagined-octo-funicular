# HANDOFF — The Half-Life of the Islamic Republic, 1984–2026

**Directory:** research/half-life-1984-2026/  
**Parent repository:** https://github.com/imanbarati/fALL2026IRANreimagined-octo-funicular  
**Branch:** main only  
**Last updated:** 4 November 2026

## Read this first
This is a separate research series added alongside the existing Iran Reborn manuscript. The parent repository already contains chapters 1–23, an Atlas registry and tools. Grok and other contributors may be editing those files concurrently.

## Non-negotiable collaboration rules
1. Never delete, rename, move, rewrite or overwrite anything outside this directory.
2. Never edit an existing file in this directory. Add a new file for a new chapter, correction, source note or erratum. Corrections belong in a dated addendum.
3. Use main only. Never force-push, reset, rebase or replace branch history.
4. Before every write, fetch the latest main head and tree. Build a new tree on top of that latest tree, create a normal child commit, and update the branch only if the expected head still matches. If the head changed, stop, fetch again and reapply only additive changes.
5. Do not update the root README, root HANDOFF, existing manuscript, Atlas CSV files or tools. Keep this work isolated here.
6. Never claim to have run local project tests if you have not. This directory currently contains research Markdown only.
7. No questions to the owner; make careful editorial decisions and record them in a new dated note.
8. Do not insert AI self-attribution into manuscript prose.

## Current files
README, 00-method-and-chronology, H01–H08, SOURCES and this HANDOFF. Eight new chapters have been added as an independent series.

## Research thesis
The Islamic Republic's endurance from 1984 through 2026 cannot be explained by popularity alone. The state combined constitutional veto points, security organizations, parastatal economic networks, elite bargaining, external-threat framing and adaptive repression. These mechanisms could preserve governing capacity while legitimacy, public trust and administrative performance deteriorated. “Half-life” is a metaphor, not a prediction or mathematical estimate.

## Next work queue — add, never replace
- H09: 1984–2026 master timeline, year-by-year, with primary-source links.
- H10: 1988 prison executions — evidence, victims, legal standards and truth-seeking.
- H11: Law as governance — penal code, compulsory veiling, press law, internet regulation, elections and security legislation.
- H12: IRGC/Basij organizational history, command structure, budget and provincial variation.
- H13: Oil, gas, sanctions evasion, shipping, currency and household-level effects.
- H14: Water, energy, environment, agriculture and climate stress.
- H15: Education, universities, censorship, science and professional emigration.
- H16: Women, family law, labour and the long contest over compulsory hijab.
- H17: Regional networks, allied armed groups, strategic depth and the costs to Iran.
- H18: Relations with China, Russia, Turkey, Gulf states, India, Pakistan, Europe and the United States—government actions, not ethnic stereotypes.
- H19: Protest database 1984–2026 with event definitions and source confidence.
- H20: Sanctions and counter-sanctions chronology, law by law.
- H21: Nuclear file 2002–2026, IAEA document-by-document.
- H22: 2025–2026 war dossier, verified chronology, civilian impact and contested claims.
- H23: Succession, elite coalitions and constitutional procedures in 1989 and 2026.
- H24: Comparative study of late Soviet Union, South Africa, Chile, Indonesia, Tunisia and other transitions; avoid false equivalence.
- H25: Evidence-based assessment of resilience and possible transition pathways, with no date predictions.

## Quality standard
- Target 1,500–3,000 words once the source base is deep enough.
- Use an opening scene or concrete event, chronology, institutional analysis, counterarguments and implications.
- Add linked citations for factual claims. Mark disputed claims [DISPUTED], incomplete evidence [VERIFY], and inference [ANALYSIS].
- Never invent quotes, casualty figures, laws, official programmes or dates.
- Use primary documents wherever possible: Iranian legal texts, UN reports, IAEA reports, court documents, official budgets, parliamentary research and archived statements.
- If a source is paywalled, cite only what its abstract supports.
- Record exact access dates for changing country pages.

## Decision log
- 2026-11-04: Chose a separate research/half-life-1984-2026 directory to prevent collision with the parent manuscript and Grok's work.
- 2026-11-04: Interpreted “half-life” as a metaphor for legitimacy erosion and institutional persistence, not a forecast of collapse.
- 2026-11-04: Started in 1984 because the requested range begins there; retained 1979–1983 as necessary context for a future prequel.
- 2026-11-04: Used dated public research sources. 2026 conflict and succession claims require further corroboration.
- 2026-11-04: Added H01–H08 as new files only. No existing file was modified.

## Safe continuation procedure
1. Fetch latest main branch head and recursive tree.
2. Confirm target filename does not already exist. If it exists, choose a new dated/addendum filename; never overwrite.
3. Create blobs for new files.
4. Create a tree using the latest tree SHA as base_tree_sha.
5. Create a commit whose parent is the latest main commit.
6. Update refs/heads/main with expected_sha set to the head fetched. If rejected, another contributor pushed; fetch and rebuild on top of the new head.
7. Confirm the resulting commit and tree contain both pre-existing files and the new additions.
