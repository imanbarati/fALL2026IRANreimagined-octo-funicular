# HANDOFF — "Iran Reborn" ebook (National Iran Activists Coalition)

Last updated: 2026-11-01. Read this whole file before writing anything.

**Repository layout (source of truth is this repo):** chapter files live in `manuscript/`; the subject registry lives in `atlas/registry/`; checks live in `tools/`. Paths below that say `chNN-*.md` mean `manuscript/chNN-*.md`. Run `make check` before every push.

## 1. What this project is
An ebook credited to **National Iran Activists Coalition** about national rejuvenation and recovery after the war and after the damage done by the Islamic Republic: how to undo the damage and rebuild Iran. Working title: **Iran Reborn: A National Recovery Manual**. Advocacy voice (the coalition's), but evidence-based and honest about risks.

Related earlier project by the same owner: https://github.com/imanbarati/effective-carnival (Iran-collapse research framework, exported Duck.ai chat). Its collapse case studies (Yugoslavia, Lebanon, Syria, Venezuela, USSR), three-phase cascade model, and "five voices" narrative device were reused here (Ch. 2 and Ch. 14). Its numbers are UNVERIFIED (see section 6).

## 2. Hard rules from the owner (do not break)
1. **Append-only: ALWAYS ADD NEW CHAPTERS, NEVER REWRITE EXISTING CHAPTERS.** Do not edit, shorten, reorder or renumber published chapter files. Corrections go in `ERRATA.md` or in a new chapter/addendum. New chapters take the next number.
2. **Never ask the owner questions.** Make the best decision, note it in the Decision Log (section 7), and continue.
3. **Byline is the coalition only.** No "co-authored by AI" lines or AI attribution inside the manuscript files.
4. Owner works in English and Persian. Manuscript is English first; Persian edition can be added later as separate files in `/fa/` (never overwrite English files).
5. Keep this HANDOFF.md current: update the status table (section 4) after every chapter you add.

## 3. Style and quality guide
- Voice: serious, urgent, humane; "we" = the coalition. No hate. **Criticize governments, institutions, policies and operations, never peoples, ethnicities or religions.** Respect believers of every faith and non-believers alike.
- Each chapter: ~1,200–2,500 words; opening scene or hook; claims; what we propose; a short **"Objections and Honest Limits"** section giving the strongest counter-arguments; end with **"What We Will Do / What You Can Do"**.
- Every factual number gets either a source or a `[VERIFY]` tag. Do not invent statistics, quotes, or documents. Fiction (Ch. 14) must be labeled as composite fiction.
- File naming: `chNN-short-slug.md` (two-digit number). Front matter in `00-front-matter.md`. Ongoing appendix of risks in `appendix-A-risks-and-objections.md` (append-only too).
- Do not write the closing "Call to Action" chapter until the queue is exhausted or the owner declares the book complete; leave the last number free for it.

## 4. Status (update after each chapter)
| # | File | Title | Status |
|---|------|-------|--------|
| 00 | 00-front-matter.md | Title page, coalition statement, how to read | DONE (v1) |
| 01 | ch01-ledger-of-damage.md | The Ledger of Damage | DONE (v1) |
| 02 | ch02-lessons-from-elsewhere.md | Lessons From Elsewhere (collapse patterns, recovery patterns) | DONE (v1) |
| 03 | ch03-principles-of-rejuvenation.md | Principles of National Rejuvenation | DONE (v1) |
| 04 | ch04-first-hundred-days.md | The First Hundred Days | DONE (v1) |
| 05 | ch05-rebuilding-the-economy.md | Rebuilding the Economy | DONE (v1) |
| 06 | ch06-justice-and-reconciliation.md | Justice and Reconciliation | DONE (v1) |
| 07 | ch07-state-and-civil-society.md | Rebuilding the State and Civil Society | DONE (v1) |
| 08 | ch08-language-culture-memory.md | Language, Culture and Memory | DONE (v1) |
| 09 | ch09-exodus-and-return.md | The Great Exodus: Migration, Brain Drain, Reverse Migration | DONE (v1) |
| 10 | ch10-foreign-hands.md | Foreign Hands: Influence Operations (China, Turkey, Arab states, Pakistan, India) | DONE (v1) |
| 11 | ch11-population-and-scarcity.md | Population Cliffs and the Empty Granary | DONE (v1) |
| 12 | ch12-a-sick-planet.md | A Sick Planet, a Thirsty Country | DONE (v1) |
| 13 | ch13-hollow-mosque.md | The Hollowed Mosque: Religious Control and the Death of the Congregation | DONE (v1) |
| 14 | ch14-five-voices.md | Five Voices (composite fiction, inspired by effective-carnival) | DONE (v1) |
| 15 | ch15-the-world-beyond-iran.md | The World Beyond Iran: Children in the Mines, Chinese on the Moon, a Narrow Strait (Hormuz; the old order is dead) | DONE (v1) |
| 16 | ch16-in-the-beginning.md | In the Beginning: How the Gods Were Written (scripture's divine violence, who gets targeted; scholarly + believers' views) | DONE (v1) |
| 17 | ch17-nobody-knows-more.md | "Nobody Knows More Than Me": claims of secret knowledge (Trump case study + same test for Iran) | DONE (v1) |
| 18 | ch18-preface-atlas-part-a.md | Preface to Atlas Part A: Timeline of Iran 1906–2026 | DONE (v1) |
| 19 | ch19-preface-atlas-part-b.md | Preface to Atlas Part B: Laws and Decrees of Iran | DONE (v1) |
| 20 | ch20-preface-atlas-part-c.md | Preface to Atlas Part C: Programs and Institutions of the Iranian State | DONE (v1) |
| 21 | ch21-preface-atlas-part-d.md | Preface to Atlas Part D: Wars, Sanctions and Diplomacy | DONE (v1) |
| 22 | ch22-preface-atlas-part-e.md | Preface to Atlas Part E: Recovery, Transition and Justice Programs Worldwide | DONE (v1) |
| 23 | ch23-preface-atlas-part-f.md | Preface to Atlas Part F: World Laws and Programs (migration, labor, environment, space, sea, religion/state, information, corruption) | DONE (v1) |
| A | appendix-A-risks-and-objections.md | Risks and Objections (append-only) | DONE (v1) |

## 5. Chapter queue (next numbers: 24, 25, ...)
Pick in this order; add more as needed. Each is a NEW chapter.
- 24 **The Information Blackout**: internet shutdowns, VPNs, surveillance tech, how to rebuild a free and safe information space.
- 25 **Women, Youth and the Generation That Refused**: gender apartheid laws, the 2022 and 2025–26 uprisings, youth NEET figures, what policies undo the damage.
- 26 **Minorities and the Unity of Iran**: Kurds, Baluch, Azeris, Arabs of Khuzestan, Turkmen, Baha'is, Christians, Jews, Sunnis; federalism vs unitary state debate (present both sides).
- 27 **The IRGC Economy**: dismantling monopolies, privatization without oligarchs, lustration limits.
- 28 **Energy, Oil and the Post-Oil Iran**: blockade, exports, gas, renewables, solar potential.
- 29 **Health, Medicine and the Doctors Who Left**.
- 30 **Universities, Science and the Return of Knowledge** (pair with Ch. 9).
- 31 **Heritage Destroyed and Heritage Saved**: war damage to cultural sites, Persepolis-era to Qajar, diaspora museums.
- 32 **The Diaspora Question**: roles, limits, legitimacy, the risk of an "exile government".
- 33 **Money from Abroad**: reconstruction financing, Gulf reluctance (~$300bn estimates `[VERIFY]`), sanctions relief sequencing, anti-corruption guardrails.
- 34 **Constitution-Making**: referendum designs, transitional authority, 100-day plan comparisons (Iran Prosperity Project, other opposition blueprints; treat all fairly).
- 35 **A Reading List and Source Atlas** (bibliography, living document).
- Possible extra chapters on request: Russia, the US and Israel as actors; other religions' pictures of divine justice (Hindu, Buddhist, Baha'i, Yazidi, Zoroastrian in depth); child labor inside Iran; Hormuz settlement design; space/AI race and Iran's tech future; AI and surveillance.
- LAST: **Call to Action / The Day After** (only when owner/book is declared complete).

- ATLAS ENTRY CHAPTERS (new chapters, one per batch): once registry rows are `sourced`, write them as Atlas chapters, for example `ch24-atlas-a1-iran-1906-1941.md`, `ch25-atlas-a2-iran-1941-1979.md`, and so on, following `atlas/ENTRY_TEMPLATE.md`. Each Atlas chapter starts with a short note linking to its Part preface (ch18–ch23). Never edit the preface chapters; if the scope grows, write a new addendum chapter.

## 6. Facts, sources, and verification
Context found on 2026-11-01 (from web search; re-check before citing):
- Al Jazeera (3 Aug 2026), "Who will shape post-war Iran?": describes a six-month US-Israeli war on Iran and competing visions for recovery; warns about IRGC-linked organisations dominating reconstruction; mentions Mojtaba Khamenei. https://www.aljazeera.com/opinions/2026/8/3/who-will-shape-post-war-iran
- Jerusalem Post: Gulf states hesitant to fund ~$300bn Iran reconstruction. https://www.jpost.com/middle-east/article-899829
- Iran International (16 Feb 2026): Iran Prosperity Project transition framework (backed by Reza Pahlavi, linked to NUFDI). https://www.iranintl.com/en/202602168645 ; framework PDF at https://fund.nufdiran.org/downloads/Foundational_Stabilization_Introduction.pdf
- Cambridge UP: "The Reconstruction Jihad, 1989–1997" (Iran's earlier post-war rebuilding; reform stalled). https://www.cambridge.org/core/product/174E8F2F8FB3FFFCFEC5A24B8FD84176
- Other opposition blueprints exist (e.g., NCRI's Ten-Point Plan, monarchist and republican proposals). Present ALL fairly; the coalition book is not tied to any one leader or faction unless the owner says so.

**Unverified claims inherited from the effective-carnival README (treat as `[VERIFY]` until checked):** inflation 88.6% (June 2026), food inflation 130.5%, rial at 2,020,000/USD (24 Aug 2026), oil exports falling to ~220–255k bpd after a July 2026 US naval blockade, "Operation Economic Fury", protest death toll range 3,117–36,500, 57% malnourishment, brain-drain 115,000/yr, 110,000 scholars abroad with ~2% returned. Also its timeline starts with the June 2025 "Twelve-Day War", while 2026 reporting describes a separate six-month US-Israeli war (Feb–Aug 2026). **Reconcile these timelines against primary sources before stating either in final text.**

## 6b. Sources added in round 2 (re-check before citing)
- Hormuz: Lloyd's List Intelligence briefs (30 Sep 2026), UANI shipping update (26 Oct 2026), straits.live daily briefs (IMF PortWatch transit counts; conflicting with US-facilitated convoy counts), The Vibes/Reuters-style report on record weekly attacks (17 Oct 2026), 24/7 Wall St (31 Oct 2026: Iran FM demands single Oman-agreed corridor). Some SEO sites claim the strait is "open": treat as low quality.
- Chang'e-7: AP/Reuters/CBS reports, 23 Aug 2026 postponement, possibly to 2027; China merged crewed and robotic lunar programs (CMSA, 23 May 2026); crewed landing target 2030.
- Child labor in cobalt: DRC >70% of cobalt; artisanal share ~15-30% of DRC cobalt; 2022 hearing testimony ~40,000 children; ILO COTECCO >9,000 children removed by Dec 2024; June 2026 reports of children still on spoil heaps in Kolwezi. Berkeley CEGA report (Faber & Krause).
- Trump claims: AP fact check on the 2000 book / bin Laden claim; CNN's Daniel Dale on "nobody knew"; Slate 2017 decoding piece; Lead Stories, Snopes, MBFC on the fake "nobody knows God better" post (May 2026).

## 6c. The Atlas and the subject registry
Owner's request: pick roughly 6,000–7,000 subjects (timeline events, laws, and programs of world governments and of the Iranian government), write a preface for each chapter group, and make the repo GitHub-ready. Nothing may be omitted; always add, never rewrite.

- **Parts:** A Iran timeline · B Iran laws and decrees · C Iranian state programs and institutions · D Wars, sanctions and diplomacy · E World recovery/transition/justice programs · F World laws and programs on migration, labor, environment, space, sea, religion-state, information, corruption, population. Prefaces are ch18–ch23.
- **Current registry:** 327 seeded subjects (A 84, B 52, C 40, D 30, E 57, F 64), all `status=queued`, `verify=VERIFY`. Target about 6,500 (see `tools/stats.py` for per-part targets: A 1200, B 900, C 900, D 800, E 1300, F 1400). **We are at about 5% of target; do not claim otherwise.**
- **How to grow it:** use `python tools/new_entry.py ...`. Add well-known, verifiable subjects only. Do not invent laws, dates, numbers, quotes or bill names. Good expansion sources: parliamentary and official gazette indexes, UN treaty collection, US Federal Register and Congress.gov, EU EUR-Lex, ICRC and OHCHR databases, transitional-justice databases, Wikipedia timelines (verify against primary sources), academic chronologies. Add roughly 100–300 rows per session, sorted by theme. Re-run `make check`.
- **Never** delete, renumber or retitle a row. Retire with `status=withdrawn`.
- **Quality ladder:** queued → drafted → sourced (source URL attached) → published (written into an Atlas chapter, no VERIFY tag).
- **Persian names:** add later in a new column in a new file; do not change existing CSV headers (the validator checks them).

## 7. Decision log
- 2026-11-01: Language = English first (owner said "do what's best"). Persian later in `/fa/`.
- 2026-11-01: Chapters 10 (foreign influence) and 13 (religion) are written as policy/analysis critiques of states and institutions, with `[VERIFY]` flags and objections sections, not as attacks on peoples or faiths.
- 2026-11-01: No fixed closing chapter yet, so append-only numbering is never broken.
- 2026-11-01: Ch. 14 reuses the five-voices device from effective-carnival but as a rejuvenation narrative (return, rebuilding), labeled as composite fiction.

- 2026-11-01 (round 2): Owner asked for chapters on (a) children in mines / Chinese Moon program / Hormuz / 'old world god is dead no more', (b) how God was in the beginning, what he said, how he picked and killed targets, (c) analysis of Trump saying he knows secrets more than anyone. Interpreted (a) 'old world god' as the fading old world order (Nietzsche-style 'God is dead' used in Ch. 16 as cultural diagnosis). Ch. 16 = analytical/historical treatment of scripture with believers' and critics' views, no mockery, includes Zoroastrian tradition. Ch. 17 = even-handed case study; no verified 'secrets' quote was found, and the viral 'nobody knows God better than me' post was fact-checked as not authentic (Lead Stories; Snopes: not verifiable). Added sources in Section 6b.

- 2026-11-01 (round 3): Created the Atlas and registry (see 6c), preface chapters 18–23, tools, CI and GitHub docs. Honest scope decision: 6,000–7,000 well-sourced subjects cannot be produced accurately in one session; 327 were seeded and the pipeline, schema and checks were built so any agent can keep appending. Chose CC BY-SA 4.0 for text and MIT for code as defaults (owner may change). Registry is sharded by part to avoid merge conflicts. CI enforces append-only on manuscript and registry.

## 8. How to export
`make epub` (requires pandoc), or run pandoc over `manuscript/00-front-matter.md manuscript/ch*.md manuscript/appendix-*.md`. PDF via pandoc + LaTeX or via the pdf skill.

## 9. If you are the next agent
1. Read this file, `00-front-matter.md`, and skim the last two chapters for voice.
2. Add the next queue chapter as a NEW file. Do not touch existing chapters.
3. Update the table in section 4 and the decision log. Commit/push if a repo exists.
4. Do not ask the owner questions.
