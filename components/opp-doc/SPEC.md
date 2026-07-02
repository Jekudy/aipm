<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# Opp Doc — component SPEC (CONTAINER)

> **Status: M1 (mapped by hand).** This is a CONTAINER to pour your existing ChatGPT Opp-Doc work into — NOT a finished doc. The diagnosis prompt maps your material onto these 12 sections, scores Q per section, surfaces white spots.

## Intent

CONTAINER/SKELETON for the Opp Doc component (Component 2, the ACTIVE component). NOT a filled-out or competing design — it is the canonical 12-section list + per-section Q-rubric + white-spot triggers that the diagnosis prompt uses to (a) map the PM's EXISTING ChatGPT Opportunity-Doc work onto a known structure, (b) score each section on the fractal Q ladder, (c) surface grounded white spots (ABSENT vs AMBIGUOUS), (d) emit tasks split PM-vs-analyst. Sections are the framework-agnostic spine that Cagan, Amazon Working Backwards PR/FAQ, and Torres OST converge on: OUTCOME/OBJECTIVE -> CUSTOMER+PROBLEM -> EVIDENCE/SIZING -> SOLUTION SPACE -> RISKS/ASSUMPTIONS -> RECOMMENDATION. STRUCTURE-VS-DISCIPLINE reconciliation: the 12-section Cagan/Amazon list is the TARGET SCHEMA; Torres OST's 4-level opportunity/solution SEPARATION (Outcome/Opportunities/Solutions/Assumptions) is a DISCIPLINE nested inside it — enforced at Sections 4 (outcome), 1 (opportunity), 8 (solutions), 9 (assumptions) — not a competing spine. The diagnosis has ONE target structure. The Q ladder is the locked Q0-Q4 evidence-tier ladder applied per section; doc-Q is a conjunctive weakest-link gate so a strong section can never mask a missing one. The doc ends by promoting top-ranked Solution options to the Solution Backlog via a strict intent + invariants + acceptance-criteria contract (Component 3 consumes it).


## Output contract → Solution Backlog (Component 3)

The Opp Doc hands each PROMOTED solution option to the Solution Backlog / Solution Doc (Component 3) as a doc contract with three slots. (1) INTENT: one line of 'after this ships, [outcome/metric] holds for [segment]', derived from Sections 1+3+4 (problem + customer + success metric). The Solution Doc's north star and its postcondition-level guarantee. (2) INVARIANTS: guardrails that must ALWAYS hold — seeded from Section 4 counter-metrics + Section 9 business-viability/legal constraints — expressed as EARS-UBIQUITOUS statements 'The <system> shall <always-true property>' (Design-by-Contract class invariants: hold before AND after every operation, distinct from per-scenario postconditions). (3) ACCEPTANCE-CRITERIA SEED: from the promoted option's riskiest assumption (Section 8 Q4) + success target (Section 4), stubbed as EARS unwanted-behaviour ('If <trigger> then the <system> shall <response>') + event-driven ('When <trigger> the <system> shall <response>') so the Solution Doc inherits the correct three-slot precondition/postcondition/invariant shape, not a vague 'falsification condition'. DOC-LEVEL GATE (single system — conjunctive weakest-link ONLY, no redundant second checklist): the Opp Doc's overall Q = min(Q of all MANDATORY sections: 0,1,2,3,4,5,6,8,9,11; optional 7,10 gate only if attempted). A doc cannot claim level T unless every mandatory section reaches T; the compensatory average is reported ONLY as a secondary '% toward next gate' progress bar. Promotion to the Solution Backlog is gated by the SAME conjunctive gate reaching Q2 on the mandatory set (which already requires a success metric + counter-metric in Section 4, >=2 ranked options with a top riskiest-assumption in Section 8, and an explicit go decision in Section 11) PLUS all three contract slots filled per promoted option — the gate is NOT restated as a separate four-item checklist. The Opp Backlog is updated in the same step (opportunity status -> assessed/promoted/parked). This is the only interface between Component 2 and Component 3; two PMs compose through committed contract files in separate folders, never shared live context.


## Pour-in / reconciliation rules

This skeleton is a CONTAINER, not a competing Opp Doc. The user already has real Opportunity-Doc work produced in ChatGPT; the plugin POURS that existing work into these sections, not regenerates it. Reconciliation rules for the diagnosis prompt: (1) MAP FIRST, don't rewrite — parse the PM's messy pasted material and place each fragment into the closest canonical section BY THE QUESTION each answers, not by heading text; keep the PM's own wording. Never auto-generate plausible-sounding prose to fill an empty section (the neuroslop failure). (2) A section the PM's material doesn't cover is scored Q0 ABSENT and surfaced as a white spot with a targeted question — the engine reports the hole, it does not backfill it. (3) EXTRACTIVE EVIDENCE — every mapped claim must carry a verbatim quote from the PM's source; if the quote isn't found, drop the claim and cap the section's Q (keeps the mapping honest). (4) The PM's structure won't match these 12 sections 1:1 — expected; map by the QUESTION, and content that fits no section goes to an 'unmapped' bucket to ASK about, never force-fit or discard. (5) The rubric SCORES and DIAGNOSES; it never grades the PM down for STYLISTIC choices (prose polish). Q descriptors are about evidence tier and completeness — with ONE named exception: customer-POV framing in Section 1 IS graded substance (Amazon/OST treat customer-voice as content, not style), so 'company-POV' caps at Q1. (6) State lives in a plain Markdown file the PM keeps wherever they work (path passed as an argument); git is optional, not required; the engine re-reads it every invocation. (7) Sections 7 and 10 are OPTIONAL — an explicit 'N/A because…' passes the gate; only silent omission is flagged. (8) GLOBAL ABSENT/AMBIGUOUS rule: every section's white-spot triggers distinguish ABSENT (grounded scan of the PM's material found nothing) from AMBIGUOUS (hinted, PM must confirm) — never assert a gap from the model's prior about what such docs 'usually lack'. (9) Report UX: lead with what mapped successfully, THEN the ranked white-spots as targeted questions routed PM-vs-analyst — never a bare ABSENT badge-wall (serves 'hard to use' + 'confusing slop' fears). (10) The diagnosis prompt is the SAME shape later reused by Solution Doc — only the frozen artifacts (this section list + these Q-rubrics + these white-spot triggers) are swapped. Do NOT pre-build the far four components' rubrics.


## The 12 sections

### 0. Header / Metadata *(mandatory — gates the doc Q)*
**Answers:** What is this doc, who owns it, what state is it in, and what upstream signal triggered it? (Presence checklist, NOT a graded Q ladder — a field either exists or doesn't; nothing to score on an evidence tier.)

**Q-rubric:**

- **PRESENT-CHECK** — Checklist, not rungs: owner named? doc status field (draft/assessed/promoted/archived)? triggering signal source linked to a real artifact? last-reviewed / evidence-as-of date? Each is pass/fail. Section 0 is MANDATORY and gates the doc — a doc with everything else filled but no owner/status must NOT pass.

**White-spot triggers:**
- No owner named -> cannot route tasks to a PM. ABSENT.
- No doc status field -> Backlog manager and Planning cannot tell a draft from a committed opportunity (breaks isolation between parallel PMs). ABSENT.
- Triggering signal described but not linked to a real source -> ABSENT-source, ask PM for the origin.
- No last-reviewed / evidence-as-of date -> flag STALE-RISK; the conjunctive gate uses it to surface a business-case-as-theatre doc that was drafted once and never revisited (Torres living-artifact discipline).

### 1. Problem / Opportunity Statement *(mandatory — gates the doc Q)*
**Answers:** What problem, for whom, and why does it matter? (Cagan Q1 + Amazon PR problem paragraph + OST opportunity node.)

**Q-rubric:**

- **Q0 ABSENT** — No problem statement, or the section holds a feature/solution instead of a problem.
- **Q1 ASSERTED** — A problem is stated but from the company's POV, or as a vague wish ('improve engagement'); no segment or cause named. NOTE: customer-POV framing IS a graded SUBSTANCE criterion here (Amazon/OST mandate customer-voice as substance, not prose polish) — company-POV framing caps at Q1.
- **Q2 STRUCTURED** — Crisp customer-framed statement of the shape '[specific segment] struggles with [job/problem] because of [cause] which impacts [outcome/metric]'; written in the customer's language; a need, not a hidden single solution.
- **Q3 DATA-BACKED** — Q2 plus at least one cited observation (interview quote, ticket, analytics) that the problem is really experienced this way.
- **Q4 VALIDATED** — Q3 plus a root-cause check (the stated problem is a cause, not a symptom; a 5-whys or equivalent has been run).

**White-spot triggers:**
- Statement phrased as a solution ('add a filter') -> Torres flag: 'if it has only one possible solution you've written a solution'. Kick back to problem framing.
- Written from company POV / corporate jargon, no customer voice -> caps at Q1 (framing is graded substance, not style).
- 'All users' or a diverse blanket segment -> too broad; force segment narrowing (also gates Section 3 sizing).
- Problem looks like a symptom (raw metric drop) with no cause -> flag missing root-cause, task for analyst.

### 2. Business Objective & Strategic Fit *(mandatory — gates the doc Q)*
**Answers:** What business objective / OKR does this serve, and why now — and why are WE best suited to pursue it? (Cagan modern Q1 + classic Q6 market window + classic Q5 right-to-win; ties to product vision/scorecard.)

**Q-rubric:**

- **Q0 ABSENT** — No link to any objective; the doc floats free of strategy.
- **Q1 ASSERTED** — A vague strategic hand-wave ('supports growth') with no specific objective, timing rationale, or right-to-win.
- **Q2 STRUCTURED** — Explicitly names the team objective / OKR this serves, a 'why now' (market window, dependency, cost of delay), AND a 'why us' right-to-win (our capability/asset advantage); traceable to the vision or scorecard.
- **Q3 DATA-BACKED** — Q2 plus evidence for the 'why now' and 'why us' (a trend, competitor move, cost-of-delay figure, or a named internal asset) rather than assertion.

**White-spot triggers:**
- No objective / OKR link -> flag; the doc's tie to Component 1 (yearly goals). Ask PM which goal it serves.
- 'Why now' absent -> flag; opportunities with no timing rationale silently deprioritize themselves.
- 'Why us / right-to-win' absent -> flag; Cagan classic Q5 — the doc can't rank an opportunity we have no advantage in. Distinct from Section 7's 'what do customers use today'.

### 3. Target Customer / Persona & Segment *(mandatory — gates the doc Q)*
**Answers:** Which specific customer are we solving for, and are user and buyer distinguished? (Cagan Q2 + Amazon subheading 'precise segment is critical' + OST customer framing.)

**Q-rubric:**

- **Q0 ABSENT** — No target customer named.
- **Q1 ASSERTED** — A broad or hand-wavy audience ('sellers', 'everyone'); user vs buyer not separated.
- **Q2 STRUCTURED** — As narrow a segment as the problem allows; user vs buyer distinguished where they differ; consistent with the segment in Section 1.
- **Q3 DATA-BACKED** — Q2 plus the segment is quantified from real data (who, how many, from analytics/CRM, not invented).

**White-spot triggers:**
- Segment here contradicts the segment in Section 1 -> cross-reference mismatch, flag.
- User == buyer assumed without check where they plausibly differ -> flag adoption/viability risk.
- Segment so broad that sizing (Section 6) would be meaningless -> flag; force narrowing.

### 4. Success Criteria & Metrics (with counter-metrics) *(mandatory — gates the doc Q)*
**Answers:** How will we know if we succeeded, and what must NOT get worse? (Cagan Q2 'Key Results' + Amazon 'what needs to be true'; the link to Component 1 metrics. This section also carries the OST OUTCOME discipline.)

**Q-rubric:**

- **Q0 ABSENT** — No success metric, or 'we'll know it when we see it'.
- **Q1 ASSERTED** — A metric is named but it is an output/vanity/lagging metric, or has no target, or no counter-metric.
- **Q2 STRUCTURED** — A measurable primary key result (ideally a leading behaviour metric) with a target AND at least one named counter-metric / guardrail that must not regress.
- **Q3 DATA-BACKED** — Q2 plus a current baseline for each metric pulled from real data, AND each metric maps to a metric defined in Component 1 (Context) and is instrumentable. NOTE: mapping + instrumentation is a Q3 property — traceability/instrumentability is NOT falsification.
- **Q4 VALIDATED** — Q3 plus the success target is an EXPERIMENTALLY-VALIDATED claim or a pre-committed pass/fail falsification condition defined before testing (not merely 'the metric is instrumented and traceable' — that is Q3). Guards against falsifiability theater.

**White-spot triggers:**
- No success metric -> the #1 post-mortem failure; hard flag, cannot promote to Solution Backlog without it.
- Success metric present but NO counter-metric -> mandatory flag (rubric forces a guardrail per success metric).
- Metric is a lagging/output number with no leading behaviour proxy -> flag for a better metric.
- Metric not found among Component 1's defined metrics -> flag possible orphan metric, task for PM to reconcile.

### 5. Evidence & Problem Validation *(mandatory — gates the doc Q)*
**Answers:** How do we know this is a real, material problem and not a nice-to-have? (Amazon internal FAQ 'what data drives this' + OST research provenance.)

**Q-rubric:**

- **Q0 ABSENT** — No evidence; the problem rests entirely on one person's opinion or a stakeholder request.
- **Q1 ASSERTED** — Anecdote / gut feel / a single unverifiable claim of evidence.
- **Q2 STRUCTURED** — Named sources of evidence with explicit assumptions and open questions listed, but not yet quantified ('several interviews suggest…').
- **Q3 DATA-BACKED** — Correlational evidence cited concretely: N customer interviews, ticket volumes, cohort/analytics numbers with links.
- **Q4 VALIDATED** — Q3 plus materiality triangulated across sources (qual + quant agree) so the problem's size is not an artifact of one channel.

**White-spot triggers:**
- Evidence claimed but no citable source (quote not found in the PM's material) -> drop the claim, cap Q, flag as unverifiable.
- Only stakeholder opinion, zero customer contact -> flag; task for analyst to gather primary evidence.
- ABSENT (no evidence in provided material) vs AMBIGUOUS (evidence hinted but PM must confirm source) marked separately — never assert a gap from 'docs like this usually lack evidence' (GLOBAL rule applies here as everywhere).

### 6. Opportunity Sizing *(mandatory — gates the doc Q)*
**Answers:** How big is it, how many have this problem, and how confident are we? (Cagan Q3 + Amazon TAM; Opportunity Score and/or RICE.)

**Q-rubric:**

- **Q0 ABSENT** — No sizing at all.
- **Q1 ASSERTED** — A number pulled from thin air with false precision; Reach/Impact invented, Confidence ignored.
- **Q2 STRUCTURED** — A sizing method is applied and shown (Opportunity Score = Importance + max(Importance-Satisfaction,0), or RICE = Reach*Impact*Confidence/Effort) with each input's source stated and a Confidence factor that honestly penalizes weak evidence.
- **Q3 DATA-BACKED** — Q2 plus Reach comes from real analytics over a fixed time window and Impact/Effort are grounded, not guessed.

**White-spot triggers:**
- RICE Reach/Impact present but no data source -> flag invented sizing.
- Confidence factor missing or pinned at 100% on a weakly-evidenced bet -> flag; Confidence exists to brake exactly this.
- Over-precise numbers ('17.3% uplift') on thin evidence -> flag false precision.

### 7. Alternatives & Competitive Landscape (optional) *(optional — gates only if attempted)*
**Answers:** What do customers use today, and how does this differentiate? (Cagan Q4 + Amazon 'today customers use x/y/z… those fall short…'. Distinct from Section 2's 'why us' — this is 'what they use now', not 'our advantage'.)

**Q-rubric:**

- **Q0 ABSENT** — No mention of current workarounds or competitors.
- **Q1 ASSERTED** — A throwaway 'no real alternatives' with no evidence.
- **Q2 STRUCTURED** — Current workarounds / competitors named, with why they fall short and where differentiation lies.
- **Q3 DATA-BACKED** — Q2 plus evidence customers actually use those alternatives (usage data, interview mentions).

**White-spot triggers:**
- 'What do customers use today' missing entirely -> flag; without it the behaviour-change / adoption risk is invisible.
- Differentiation asserted with no acknowledged alternative -> flag unstated baseline.
- Optional: if the PM marks it N/A, require an explicit 'N/A because…' rather than silent omission.

### 8. Solution Options (ranked, NOT one committed feature) *(mandatory — gates the doc Q)*
**Answers:** What candidate solutions address this opportunity, and which rank highest? (OST solution branches — keeps the Opp Doc from collapsing into a spec.)

**Q-rubric:**

- **Q0 ABSENT** — No options, or a single committed feature written as 'the solution'.
- **Q1 ASSERTED** — One idea plus token 'alternatives' that are not real options; no comparison basis.
- **Q2 STRUCTURED** — 3+ genuinely distinct candidate solutions, each traced to the opportunity, compared on a stated basis, and ranked. Machine rubric SPLITS this into 4 separate one-criterion items: distinct? traced? compared-on-stated-basis? ranked? — SKILL prose stays narrative.
- **Q3 DATA-BACKED** — Q2 plus the ranking uses the sizing/risk inputs from Sections 6 and 9 rather than preference.
- **Q4 VALIDATED** — Q3 plus each top option names its riskiest assumption and the cheapest test that could disprove it (hand-off-ready to Solution Doc).

**White-spot triggers:**
- Only one solution -> hard flag; the top-options-to-Solution-Backlog step is impossible with a single option.
- Options exist but ranking is by opinion, not by sizing/risk -> flag.
- A 'solution' that is actually a restatement of the problem, or an 'opportunity' with exactly one solution -> Torres reversal flag.
- Top option has no riskiest-assumption named -> caps at Q3, flag for the Solution Doc hand-off.

### 9. Risks, Assumptions & Dependencies *(mandatory — gates the doc Q)*
**Answers:** What must be true, and what could kill this? (Cagan four risks: value/usability/feasibility/viability + Amazon dependencies + OST assumption mapping.)

**Q-rubric:**

- **Q0 ABSENT** — No risks or assumptions listed.
- **Q1 ASSERTED** — A generic risk line ('might not work') with no category and no dependencies.
- **Q2 STRUCTURED** — Each top option scored against the four risks (value/usability/feasibility/business viability) with 'what must be true' and 'why this might NOT succeed' stated, plus internal + external + legal/regulatory dependencies enumerated. Machine rubric SPLITS into separate items: four-risk-scored? what-must-be-true? why-might-fail? dependencies-enumerated? — SKILL prose stays narrative.
- **Q3 DATA-BACKED** — Q2 plus the riskiest assumptions are mapped on risk x evidence and ordered, so the highest-risk least-evidenced ones are visible.
- **Q4 VALIDATED** — Q3 plus the riskiest assumptions are expressed as falsifiable hypotheses with pre-committed pass/fail criteria.

**White-spot triggers:**
- Business-viability risk and cross-team / third-party / legal dependencies not enumerated -> flag; the most-skipped and most-fatal.
- 'Why might this NOT succeed' (Amazon 'top-3 reasons it fails') absent -> flag.
- External dependency on prototyping team or AI-analyst not named where relevant -> flag (real third-party deps for this org).
- Assumptions listed but none falsifiable -> caps at Q3.

### 10. Economics / Viability (optional, where relevant) *(optional — gates only if attempted)*
**Answers:** Does this work for our business? (Amazon internal-FAQ economics + Cagan Q8.)

**Q-rubric:**

- **Q0 ABSENT** — No economic consideration where money/cost clearly matters.
- **Q1 ASSERTED** — A vague 'should be profitable' with no numbers.
- **Q2 STRUCTURED** — Cost-to-build/operate and the value or revenue mechanism stated, with a rough per-unit or aggregate frame.
- **Q3 DATA-BACKED** — Q2 plus pro-forma figures grounded in real cost/price data.

**White-spot triggers:**
- Marked N/A on an opportunity that plainly has cost/revenue stakes -> challenge the N/A.
- Optional: an explicit 'N/A because non-monetary outcome' passes the gate; silent omission does not.

### 11. Recommendation & Next Actions *(mandatory — gates the doc Q)*
**Answers:** Go or no-go, and what happens next? (Cagan Q10 + the hand-off to Opp/Solution Backlog.)

**Q-rubric:**

- **Q0 ABSENT** — The doc ends as analysis with no decision.
- **Q1 ASSERTED** — A soft 'seems worth doing' with no owner and no next step.
- **Q2 STRUCTURED** — Explicit go / no-go / park, which Solution option(s) get promoted to the Solution Backlog, and next actions split into tasks-for-PM vs tasks-for-analyst vs discovery.
- **Q3 DATA-BACKED** — Q2 plus the recommendation cites the doc's own sizing/risk to justify the call, and each promoted option carries the three contract slots (intent + invariants + acceptance-criteria seed) for the Solution Doc.

**White-spot triggers:**
- No explicit go/no-go -> hard flag; Cagan requires a clear decision, and Backlog/Planning cannot act on analysis-only.
- Options promoted to Solution Backlog without the intent+invariants+acceptance-criteria seed -> flag; the contract is incomplete.
- Next actions not split PM-vs-analyst -> flag; the workflow must emit routed tasks.

