<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# Solution Doc — component SPEC (CONTAINER)

> **Status: M1 (mapped by hand).** This is a CONTAINER to pour a PM's existing solution/PRD work into — NOT a finished PRD. The diagnosis prompt maps the PM's material onto these 10 sections, scores Q per section, surfaces white spots, and leads a PROMOTED solution candidate toward a PRD-ready state. Same diagnosis shape as Opp Doc, new frozen artifacts (swap the section schema + Q-rubric + white-spot triggers; no new logic — see `docs/architecture.md`, shared diagnosis reference).
>
> **PRD = the mature state of the Solution Doc, not a separate artifact** (mega-scenario 2, `STATE.md`). One item, one dial, its target output is called PRD.

## Intent

CONTAINER/SKELETON for the Solution Doc component (Component 4). It takes a **promoted solution candidate** (the three-slot contract in `docs/solution-backlog.md`) and leads the SOLUTION ITEM toward a PRD-ready state — the same discipline as Opp Doc, applied to a chosen solution instead of an opportunity. The diagnosis prompt uses this file to (a) map the PM's EXISTING solution/PRD material onto the 10-section structure, (b) score each section on the fractal Q0–Q4 ladder, (c) surface grounded white spots (ABSENT vs AMBIGUOUS), (d) emit tasks split PM-vs-analyst/engineer, (e) at PRD-ready, update the solution-backlog entry and name the seam to Planning.

The section spine is the framework-agnostic backbone that Cagan (four product risks), Amazon Working Backwards (PR-FAQ), Teresa Torres (assumption testing / compare-and-contrast), Basecamp Shape Up (appetite / no-gos / rabbit holes), and the Google design-doc convention (goals / non-goals / alternatives) converge on: INTENT → CONTEXT/SCOPE → GOALS/NON-GOALS → DESIGN+TRADE-OFFS → ALTERNATIVES → RISKS/ASSUMPTIONS → INVARIANTS → ACCEPTANCE CRITERIA → ROLLOUT/MEASUREMENT. It is calibrated against a real Avito PRD (the "Паспорт фичи" template — see `Pour-in rules` §Avito-fit). The Q ladder is the locked Q0–Q4 evidence-tier ladder applied per section; doc-Q is a conjunctive weakest-link gate so a strong section can never mask a missing one. The doc is NOT a solution generator — it moves the solution item to its next meaningful decision; the PRD is a rendering of item state (anti-goal: no synthesized prose to fill a gap).

## Input contract ← Opp Doc promotion (the ONLY admission path)

A Solution Doc NEVER starts from a raw signal, a wish, or «напиши prd». It starts ONLY from a **promoted solution candidate** — an entry appended to `docs/solution-backlog.md` by Opp Doc at its r3 promotion gate (`components/opp-doc/SPEC.md`, output contract; `docs/architecture.md#Interfaces`). That entry carries the three-slot contract + folded sub-fields, which SEED this doc:

- **INTENT slot** → seeds **S1 Intent** ("after this ships, [outcome/metric] holds for [segment]", from parent opp Sections 1+3+4).
- **INVARIANTS slot** (EARS-ubiquitous, from opp S4 counter-metrics + S9 constraints) → seeds **S7 Invariants/Guardrails**.
- **ACCEPTANCE-CRITERIA SEED** (EARS-stubbed, from opp S8 riskiest assumption + S4 target) → seeds **S8 Acceptance Criteria**.
- **Folded sub-fields** (`parent_opportunity, problem, segment, solution_hypothesis` if-then-because, `target_behavior, target_outcome/metric, why_it_might_work, key_assumptions + guardrails`) → seed **S0 Header**, **S1**, **S3**, **S6**.

The Solution Doc's job is to take these seeds from a one-line contract to a PRD-ready doc. Admission invariant (checked at entry): **no Solution Doc without a parent opportunity and an if-then-because product hypothesis** — checkable directly from the entry's `parent_opportunity` + `solution_hypothesis`. A bare idea / «напиши prd» without a promoted candidate is REFUSED and routed back to opp-doc (see `Entry points`, admission guard). **One promoted candidate → exactly one Solution Doc; splitting one candidate across multiple docs is out of lvl1 scope (spec-friction if a real case demands it).**

## Output contract → Planning (seam only; Planning stays M0)

At **sol-r3 (PRD-ready)** the doc updates its solution-backlog entry (`status: prd_ready` + dated `readiness` claim) and becomes a wave-candidate for Planning. The hand-off shape is the SAME three slots the doc already carries, now matured: INTENT (S1) + INVARIANTS (S7, EARS-ubiquitous) + ACCEPTANCE CRITERIA (S8, Given-When-Then / EARS). Planning consumes `prd_ready` entries as wave contents (each wave boundary is itself an intent+invariants+acceptance-criteria contract, per `docs/architecture.md#Interfaces` solution-backlog → planning). **Planning is M0 — not built. Name the seam, do not design it.** No PRD content is generated for Planning; Planning reads the matured slots from the file.

**Phase-B build note (non-normative, mirrors opp-doc handoff §4.1):** the skill body soft budget is 2000–2500 words; must-stay-inline = admission guard + router branch selection + the sol-r table & doc-gate + the full-inventory mutation gate; movable to `references/` = the per-section rubric, check-lists, task schema, gap-report template. This is Phase-B guidance, recorded here so the trap is not silently skipped.

## Pour-in / reconciliation rules

This skeleton is a CONTAINER, not a competing PRD. Reconciliation rules for the diagnosis prompt (mirror opp-doc; only the frozen artifacts differ):

1. **MAP FIRST, don't rewrite** — parse the PM's messy solution/PRD material and place each fragment into the closest section BY THE QUESTION each answers, not by heading text; keep the PM's own wording. Never auto-generate plausible prose to fill an empty section (the neuroslop failure).
2. A section the PM's material doesn't cover is scored **Q0 ABSENT** and surfaced as a white spot with a targeted question — the engine reports the hole, it does not backfill it.
3. **EXTRACTIVE EVIDENCE** — every mapped claim carries a verbatim quote from the PM's source; if the quote isn't found, drop the claim and cap the section's Q.
4. The PM's structure won't match these 10 sections 1:1 — expected; map by the QUESTION; content that fits no section goes to an 'unmapped' bucket to ASK about, never force-fit or discard.
5. The rubric SCORES evidence tier and completeness; it never grades DOWN for stylistic choices — with ONE named exception mirrored from opp-doc: customer/outcome-framed INTENT in S1 IS graded substance (a solution-first "сделать фичу X" with no problem/outcome caps at Q1).
6. **GLOBAL ABSENT/AMBIGUOUS precedence (stated ONCE, applies to EVERY section's triggers):** a gap is **ABSENT** only when a grounded scan of the PM's ACTUAL material returned nothing; it is **AMBIGUOUS** when the material hints at it but the PM must confirm. Never assert a gap from "PRDs like this usually lack X" (parametric belief is forbidden). Precedence when both could apply: if any material maps to the item → AMBIGUOUS (confirm); only a truly empty scan → ABSENT. Recommended-context-field absence degrades to AMBIGUOUS elicitation, not ABSENT (see `Context contract`).
7. **Report UX:** lead with what mapped successfully, THEN ranked white-spots as targeted questions routed PM-vs-analyst/engineer — never a bare ABSENT badge-wall.
8. **Format ownership (single owner per layout):** the solution-backlog ENTRY layout (three slots + folded sub-fields) is owned by `components/solution-backlog/SPEC.md` (M0) with the shape fixed NOW by `docs/architecture.md#Interfaces` + the opp-doc promotion transform — this doc WRITES conforming entries, it does not own their layout. The gap-report / DIFF layout is owned by the solution-doc gap-report template (Phase B). Template previews must match the owner.
9. <a id="avito-fit"></a>**Avito-fit (format orientation + EVAL examples, NOT a correctness reference — source: the real Avito PRD «Холдирование Откликов», Confluence pageId 701170801, read 2026-07-07; saved as a Phase-B EVAL fixture). The "Паспорт фичи" template is used only as an orientation for WHICH sections a real Avito PRD carries; the actual content quality of any one real PRD is NOT a gold standard — a real PRD may itself be uneven, and the rubric must HONESTLY diagnose its gaps (that is exactly the false-ABSENT test). The formal calibration on ≥3 real PRDs remains the blocking M2→M3 gate:** the 10 sections cover the real template — `Предпосылки`→S2, `Какую проблему решаем?`/`какая цель?`→S1+S3, `Предлагаемое решение`→S4, `Риски`→S6 (trade-offs live here as accepted-risk judgements), `Критерии приёмки`→S8 (a MoSCoW×status FR/NFR register), `Q&A`/open questions→S6, `Техническая информация` (NFR: monitoring, feature-toggle, graceful degradation, RT budgets)→S9, passport metadata→S0. **DoR/DoD role-gates in the real template are NOT a content section — they ARE the readiness ladder + the conjunctive doc-gate (the "cut score"), same as opp-doc has no DoR section.** `WON'T`-priority items express **non-goals** (S3). Guardrails in a real antifraud PRD appear as **carve-outs + kill-switch** (e.g. CPA/CPR never sanctioned; emergency toggle), NOT as a numeric counter-metric — the S7 rubric grades a carve-out/kill-switch as Q2 and a numeric monitored threshold as Q3 (do not demand a numeric FP-rate where an operational guardrail exists).
10. The diagnosis prompt is the SAME shape Opp Doc uses — only the frozen artifacts (this section list + these Q-rubrics + these triggers) are swapped. Do NOT invent new engine logic.

## Readiness (r) — ONE dial, DERIVED (mirror the model-axes r-addendum)

r = work-item READINESS of the SOLUTION ITEM: a **derived, dated, demotable projection** of the doc's Q profile + decision state, computed through THIS file's Q-rubric. NEVER called "maturity" (reserved for M). Re-derived every pass; the solution-backlog entry caches it as a DATED CLAIM (`readiness: sol-r2 (assessed 2026-07-07)`), demotable on a later pass. Same properties as opp-r (model-axes.md addendum): derived / dated / demotable; readiness ≠ priority ≠ workflow status; never stored as machine state; never in the GitHub Project.

**ONE dial, not two — reserved `sol-s0..s2` / `prd-r1..r3` are COLLAPSED into `sol-r0..sol-r3`.** Rationale: mega-scenario 2 fixes "PRD = the mature Solution Doc, one artifact" — there is no artifact boundary between "solution candidate" and "PRD" to justify two families; a second family would be a shadow axis duplicating Q (conflict C1) and would recycle the "maturity" collision (C2). The named reserved vocabulary in canon (`docs/model-axes.md`, `docs/architecture.md#Interfaces` reserved `sol_state`, `docs/target-solution.md`) should be reconciled to the single `sol-r` ladder — recorded as **spec-friction** (this doc does not edit canon).

| r | name | derivation over the 10-section container |
|---|---|---|
| **sol-r0** | promoted candidate (FLOOR) | The three-slot contract exists in `docs/solution-backlog.md` (parent opp + if-then-because hypothesis + intent/invariants/AC seeds); the PRD has NOT yet earned sol-r1. **Floor rung: a Solution Doc MAY exist but has not yet earned sol-r1.** No Q derivation required at the card level. |
| **sol-r1** | framed | Framing sections **S1 Intent, S2 Context & Scope, S3 Goals & Non-Goals each ≥ Q2** (what/why/boundaries are clear; the solution may still be sketchy). |
| **sol-r2** | designed & de-risked | r1 AND **S4 Solution Design & Trade-offs ≥ Q3** AND **S6 Risks & Assumptions ≥ Q3** AND **S5 Alternatives addressed** (≥ Q2 or an explicit "N/A: единственный жизнеспособный вариант, потому что…"). |
| **sol-r3** | PRD-ready | Doc-level conjunctive gate **≥ Q2 on the mandatory set (0,1,2,3,4,6,7,8,9)** AND **S8 holds ≥1 testable acceptance criterion** AND **S9 carries an explicit decision from the closed set {ship / experiment-first / hold / drop}**. This is the HARD Planning-admission gate — the analog of opp-r3's promotion gate. |

**sol-r3 is a Q2 gate by design** (mirrors opp-r3): the doc-level gate needs Q2 on the mandatory set + one testable AC + an explicit decision. Q3/Q4 rungs are scoring headroom for honest DIFF reporting and demote detection — NOT admission requirements. "PRD-ready" is a structured-and-decided bar, not a fully-validated one.

**Non-nesting note (mirror opp-r):** the ladder is a set of NAMED MILESTONES on one dial, not strictly nested by construction — a sol-r3 doc may hold S5 at Q2 without ever earning the sol-r2 label; the gap report always names the blocking sections, so nothing is hidden.

**Decision at any rung:** `hold` / `drop` are legitimate BELOW sol-r3 — a solution may be parked or killed mid-design the moment a risk proves fatal (e.g. S6 surfaces an unmovable viability/legal blocker). The report says so; a low-r doc is not forced up the ladder before it can be dropped.

**Demote vs stay-low (naming, mirror opp friction G):** a **demote** is a later pass UNDERCUTTING a rung the doc had ALREADY earned (e.g. an assumption believed Q3-tested turns out unfounded → S6 drops → sol-r2 → sol-r1). A **stay-low** is a rung never earned. Both are honest and dated. **Materiality demote (from opp wave-2 case-6):** demotion triggers cover not only "evidence removed" but "evidence STRONGER yet effect/appetite collapsed" — if the design is still sound but the measured impact falls below the S2 appetite / S9 success target, that is a materiality demote routed to a park/kill PM decision, not a silent stay.

## Entry points (3) + tiebreaks + admission guard

- **(i) Promoted solution-backlog entry** — the ONLY admission path. The doc reads the three-slot contract + folded sub-fields and assembles the **container skeleton** (empty container + mapped seeds, white spots marked — NO generated prose). **Readiness stays `sol-r0-floor` at admission** and is only *earned* up to sol-r1 once S1–S3 reach Q2 — the three-slot seeds seed S0/S1/S3/S6/S7/S8 but NOT S2 Context&Scope, so sol-r1 is never reachable from admission alone. The skeleton targets sol-r1; it does not claim it.
- **(ii) Existing draft PRD / solution doc to diagnose** — the 6-step diagnosis loop (map-by-question, like opp-doc entry B). MUST reconcile against a promoted candidate: if a matching `solution-backlog` entry exists → validate the draft against its parent opp + hypothesis; if none exists → the admission guard fires (below).
- **(iii) Repeat pass / task-result intake** — after offline work (design spike, prototype result, analyst evidence), re-read stateless, re-derive r (may demote), emit a **DIFF report** (what changed / gaps closed / NEW gaps / updated entry). Not an entry class — the repeat-pass flow.

**Tiebreaks (mixed inputs):**
- (i)+(ii) both present (a promoted entry AND a draft PRD) → treat as (ii): diagnose the draft, validate it against the promoted contract.
- task-result + existing doc/entry → (iii) repeat-pass DIFF.
- **«напиши prd» / bare idea with NO promoted candidate → ADMISSION GUARD, refuse + route** (verbatim Russian): «этот PRD ещё не привязан к promoted solution candidate. solution-doc начинается только с кандидата, прошедшего opportunity-гейт: нужны parent opportunity и product-гипотеза в форме if-then-because. варианты: (a) вернуться в opp-doc и довести opportunity до промоушена; (b) указать существующую запись в solution-backlog.md, из которой растёт этот PRD.» Never synthesize a parent opportunity to admit the doc.

## Context contract consumption (read-if-present / degrade-if-absent)

Per the single-home context contract (`docs/architecture.md#Interfaces`, context-collection → consumers). Solution Doc's **DECLARED fields**: `key_metric` + `counter_metrics` (S9 success metric + S7 guardrail seed), `constraints` (S6 risks + S7 invariants), `current_goals`/`strategic_context` (S3 goals alignment) + recommended subset `user_segments, core_scenarios, data_sources, research_sources` (S1 intent + S6 evidence). Degrade rules (no-fallbacks, mirror opp §9.3): absence never invents a default — it becomes a white spot kicked to context-collection. `key_metric` absent → hard **S9** white-spot; `counter_metrics` absent → **S7** guardrail white-spot **unless the doc itself supplies a carve-out / kill-switch** (doc-supplies-the-item wins — same reconciliation as S9/`key_metric`; the S7 ABSENT trigger fires only when there is no carve-out AND no kill-switch AND no counter-metric); `constraints` absent → AMBIGUOUS elicitation; a recommended field absent → AMBIGUOUS; undeclared fields silently ignored. `readiness_preferences` stays reserved-unread until M4+.

## Transition gates (c6–c8; c9 reserved) — the four-question frame

Gates are behavior frames, not step-scripts («контракты не должны травмировать работу сильных моделей микроменеджментом»). Claiming the reserved names c6+ (opp-doc used c1–c5):

- **c6 — promoted candidate → sol-r0-floor → sol-r1 (framed).** Admission assembles the skeleton at **sol-r0-floor** (not a granted rung); sol-r1 is *earned*, not granted at admission. *Known to proceed to sol-r1:* S1 Intent, S2 Context/Scope, S3 Goals/Non-Goals each ≥ Q2, consistent with the parent opp (S2 in particular must be filled by the PM — it is not seeded). *Output:* a framed solution-doc skeleton + updated entry. *Errors caught:* bare idea / no parent opp → reject to opp-doc; backfilled prose; intent drifted from the promoted candidate; claiming sol-r1 from seeds alone. *Human approval:* PM confirms the framing matches the candidate's intent.
- **c7 — sol-r1 → sol-r2 (designed & de-risked).** *Known:* S4 Design & Trade-offs ≥ Q3, S6 Risks ≥ Q3 (four Cagan risks assessed), S5 Alternatives addressed. *Output:* a de-risked design with the riskiest assumptions named + cheapest tests. *Errors caught:* gold-plating / over-specification (PRD-theater); single-option "whether-or-not" framing; assumptions asserted as fact. *Human approval:* PM confirms the riskiest assumptions and their test plan.
- **c8 — sol-r2 → sol-r3 (PRD-ready).** *Known:* doc-level conjunctive ≥ Q2 on the mandatory set + ≥1 testable acceptance criterion + invariants expressed + an explicit ship/experiment/hold/drop decision. *Output:* a PRD-ready doc + `solution-backlog` entry `status: prd_ready`. *Errors caught:* AC not testable; an invariant mislabeled as a per-scenario postcondition; no success metric; PRD-theater / spec bloat. *Human approval (HARD gate = Planning-admission):* PM makes the explicit ship-decision; advisory while drafting, HARD at this boundary — a doc below the gate may live in the solution-backlog but may NOT be handed to Planning.
- **c9 — sol-r3 → Planning handoff.** Reserved name; the seam itself is the "Output contract → Planning" section above (not restated here). Planning is M0 — not designed.

---

## The 10 sections

> Mandatory-gating set (the conjunctive doc-Q gate) = **S0, S1, S2, S3, S4, S6, S7, S8, S9**. **S5 Alternatives is OPTIONAL** — it gates only if attempted; an explicit "N/A: единственный жизнеспособный вариант, потому что…" passes, silent omission is flagged. Doc-Q = min(Q of mandatory sections); the compensatory average is reported ONLY as a secondary "% toward next gate". The report always names the single lowest gating section (the actionable white spot + source of routed tasks). Grounding is cited inline per section; full source map in the Phase-A hand-back.

### 0. Header / Metadata *(mandatory — gates the doc Q)*
**Answers:** What is this solution doc, who owns it, what state is it in, and which promoted candidate + parent opportunity does it grow from? (Presence checklist, NOT a graded Q ladder — calibrated to the Avito "Паспорт фичи" metadata block.)

**Q-rubric — PRESENT-CHECK (pass/fail per item):**
- owner / feature-driver named? doc status field (draft/assessed/prd_ready/archived)?
- **`parent_opportunity` + source `solution_candidate` id** linked to a real `solution-backlog` entry? (the admission invariant — without it the doc cannot be admitted)
- intent line carried from the promoted contract?
- last-reviewed / evidence-as-of date? links to schemes/mockups/epic if present (Avito passport — optional, presence-only)?

**White-spot triggers:**
- No owner → cannot route tasks. ABSENT.
- No doc status → Planning/Backlog cannot tell a draft from a PRD-ready item (breaks parallel-PM isolation). ABSENT.
- **No parent_opportunity / candidate link → the doc has no admission basis. ABSENT — fire the admission guard, do not synthesize a parent.**
- No last-reviewed date → STALE-RISK flag (living-artifact discipline).

### 1. Intent *(mandatory — gates the doc Q)*
**Answers:** What customer problem / outcome does this solution serve, and for whom? (Amazon PR problem paragraph, customer-POV; Torres outcome→opportunity; Cagan value risk. Seeded by the promoted INTENT slot.)

**Q-rubric:**
- **Q0 ABSENT** — No intent, or the section holds a feature description instead of a problem/outcome.
- **Q1 ASSERTED** — Solution-first framing ("сделать ai-помощника") or company-POV; no outcome or segment. NOTE: customer/outcome framing IS graded substance here — solution-first caps at Q1.
- **Q2 STRUCTURED** — Crisp "after this ships, [outcome/metric] holds for [segment]", consistent with the parent opportunity; a problem/outcome, not a hidden single feature.
- **Q3 DATA-BACKED** — Q2 plus the intent inherits the parent opp's cited evidence (baseline metric for the outcome).

**White-spot triggers:**
- Intent is a feature, not an outcome → Torres flag (kick back to the problem). ABSENT/AMBIGUOUS per the scan.
- Segment/outcome contradicts the parent opportunity → cross-ref mismatch. ABSENT.
- No traceable link to a parent opportunity → breaks the admission invariant (also S0). ABSENT.

### 2. Context & Scope *(mandatory — gates the doc Q)*
**Answers:** What's the situation, the appetite/boundary, and what's in play (reach, dependencies)? (Shape Up appetite-as-constraint; Amazon internal-FAQ TAM + dependencies; design-doc "context is objective background". Avito `Предпосылки`.)

**Q-rubric:**
- **Q0 ABSENT** — No context; the solution floats free of situation and constraints.
- **Q1 ASSERTED** — Vague "надо улучшить" with no boundary, reach, or dependencies.
- **Q2 STRUCTURED** — Situation stated as objective background + an appetite/boundary (time-box or scope constraint, Shape Up) + dependencies named (internal / external / legal, Amazon FAQ).
- **Q3 DATA-BACKED** — Q2 plus reach/TAM sized from real data over a fixed window; dependencies confirmed with named owners.

**White-spot triggers:**
- No scope boundary / appetite → scope-creep risk. AMBIGUOUS (confirm the boundary).
- Cross-team / third-party / legal dependency not named → ABSENT (the most-skipped, Cagan viability; real Avito PRDs carry a "ключевая работа в другой команде" row).
- Reach asserted with no source → flag invented sizing (AMBIGUOUS).

### 3. Goals & Non-Goals *(mandatory — gates the doc Q)*
**Answers:** What does success look like, and what are we explicitly NOT doing? (Shape Up no-gos; Google design-doc explicit Goals/Non-Goals; Atlassian "what we're not doing"; Avito `WON'T`-priority = non-goals.)

**Q-rubric:**
- **Q0 ABSENT** — No goals, or goals only with no non-goals at all.
- **Q1 ASSERTED** — Vague goals ("улучшить опыт"), no measurable target, no non-goals.
- **Q2 STRUCTURED** — Measurable goal(s) tied to the S1 outcome + an EXPLICIT non-goals list (deliberate exclusions named, not implied).
- **Q3 DATA-BACKED** — Q2 plus each goal ties to a metric with a target and a baseline from real data.

**White-spot triggers:**
- No non-goals → scope-creep exposure. ABSENT (a doc that only says what's in scope invites creep — named anti-pattern).
- Goals not measurable → AMBIGUOUS (force a measurable target).
- Non-goals only implicit (via struck items / WON'T) with no dedicated list → AMBIGUOUS (surface them explicitly).

### 4. Solution Design & Trade-offs *(mandatory — gates the doc Q)*
**Answers:** How does the solution work (at the right altitude), and what trade-offs did we make? (Shape Up breadboard/fat-marker altitude — structure & flow, not pixel spec; Amazon solution paragraph "in detail"; Cagan usability+feasibility; ADR Context→Decision→Consequences incl. the negative ones. Avito `Предлагаемое решение`.)

**Q-rubric:**
- **Q0 ABSENT** — No design, or the "solution" is a restatement of the problem.
- **Q1 ASSERTED** — A solution named with no mechanism and no trade-offs ("сделаем помощника").
- **Q2 STRUCTURED** — Design at breadboard altitude (structure + flow), the mechanism explained ("почему это сработает"), and trade-offs named WITH their negative consequences (ADR: not just the positives).
- **Q3 DATA-BACKED** — Q2 plus design decisions cite constraints/data (a feasibility spike, a named technical constraint, ADR "forces in tension").
- **Q4 VALIDATED** — Q3 plus the design is de-risked by a prototype/test result on the highest usability/feasibility risk (Cagan: evidence, not judgement alone).

**White-spot triggers:**
- No trade-offs / only positives listed → ADR flag. ABSENT.
- Pixel-spec / over-specification / gold-plating → PRD-theater flag ("product management theater"). AMBIGUOUS — pull the altitude up.
- "Solution" is the problem restated → Torres reversal flag.

### 5. Alternatives Considered *(OPTIONAL — gates only if attempted; explicit N/A passes)*
**Answers:** What else could we have done, and why this over those? (Torres compare-and-contrast / generate-multiple-solutions; Google design-doc "Alternatives considered" as a fixed part; MADR considered-options + pros/cons.)

**Q-rubric:**
- **Q0 ABSENT** — No alternatives, and no explicit "N/A because…".
- **Q1 ASSERTED** — Token alternatives that are not real options; no comparison basis.
- **Q2 STRUCTURED** — ≥1 real alternative named with its trade-off / reason for rejection (compare-and-contrast). An explicit "N/A: единственный жизнеспособный вариант, потому что…" passes at Q2.
- **Q3 DATA-BACKED** — Q2 plus rejected options scored against named decision drivers with data (MADR drivers), not preference.

**White-spot triggers:**
- Single-option "whether-or-not" framing with no N/A mark → Torres anti-pattern. ABSENT (if attempted-but-empty) / silent omission flagged.
- Alternatives named but no reason-for-rejection → AMBIGUOUS.

### 6. Risks & Assumptions *(mandatory — gates the doc Q)*
**Answers:** What has to be true, what could kill this, and how risky is each — plus what's still an open question? (Cagan four risks: value / usability / feasibility / business viability; Torres five assumption types incl. ethical + assumption testing; Amazon "what has to be true" / "why might it fail"; Shape Up rabbit holes. Avito `Риски` table + `Q&A`.)

**Q-rubric:**
- **Q0 ABSENT** — No risks or assumptions listed.
- **Q1 ASSERTED** — A generic "might not work" with no category.
- **Q2 STRUCTURED** — The FOUR Cagan risks (value/usability/feasibility/viability) each named + assumptions tagged (desirability/feasibility/usability/viability/ethical) + "what has to be true" + "why might it fail" + open questions logged. *Machine rubric SPLITS into one-criterion items: four-risks-covered? assumptions-tagged? what-must-be-true? why-might-fail? open-questions-logged? — SKILL prose stays narrative.*
- **Q3 DATA-BACKED** — Q2 plus the riskiest assumptions ranked on risk × evidence, and existing evidence per assumption catalogued.
- **Q4 VALIDATED** — Q3 plus the riskiest assumptions expressed as falsifiable hypotheses with pre-committed pass/fail + the cheapest test that could disprove each (Torres assumption test).

**White-spot triggers:**
- Business-viability / legal / cross-team dependency risk absent → ABSENT (the most-fatal and most-skipped).
- "Why might this fail" absent → ABSENT (Amazon top-reasons-it-fails).
- Assumptions listed but none falsifiable → caps at Q3.
- Trade-off accepted as a risk judgement without stating the accepted downside → AMBIGUOUS (real PRDs carry "нам ОК перерасходовать лимит, профит больше" — the downside must be named).

### 7. Invariants / Guardrails *(mandatory — gates the doc Q)*
**Answers:** What must stay true no matter how we build it? (Feeds the downstream INVARIANTS slot. EARS ubiquitous/state-driven syntax; RFC 2119 MUST/SHOULD obligation grading; Design-by-Contract *class invariant* — always-true across all scenarios, distinct from a per-scenario postcondition. Seeded by the promoted INVARIANTS slot + context `counter_metrics`.)

**Q-rubric:**
- **Q0 ABSENT** — No guardrails where the solution plainly needs them (e.g. an antifraud action with no legit-user protection).
- **Q1 ASSERTED** — Vague "должно быть безопасно"; not shaped as an always-true property.
- **Q2 STRUCTURED** — Guardrails as EARS clauses ("The <system> shall <always-true property>" / "While <state>, the <system> shall…"), each correctly UNIVERSAL across scenarios (a class invariant, not a disguised postcondition), graded MUST vs SHOULD (RFC 2119). **A carve-out or kill-switch counts here** (e.g. "CPA/CPR отклики never sanctioned", "emergency toggle for instant shutdown") — a real Avito antifraud PRD expresses guardrails this way.
- **Q3 DATA-BACKED** — Q2 plus each invariant has a measurable predicate / monitored counter-metric threshold (the numeric guardrail).

**White-spot triggers:**
- Guardrail phrased as a one-scenario outcome (mislabeled postcondition) → Design-by-Contract flag. AMBIGUOUS.
- No legit-user / counter-metric guardrail AND no carve-out AND no kill-switch in a solution that clearly affects legitimate users → ABSENT (the false-positive blind spot).
- Guardrail not EARS-shaped / obligation not graded (MUST vs SHOULD) → caps at Q1.

### 8. Acceptance Criteria *(mandatory — gates the doc Q)*
**Answers:** How will we know it's done and correct — testably? (Feeds the downstream AC seed. BDD Given-When-Then with an assertable outcome; EARS event-driven / unwanted-behaviour clauses; a pre-committed pass/fail threshold = the falsifiable top tier. Avito `Критерии приёмки` → MoSCoW×status FR/NFR register.)

**Q-rubric:**
- **Q0 ABSENT** — No acceptance criteria; no definition of done.
- **Q1 ASSERTED** — "должно работать" with no context and nothing assertable.
- **Q2 STRUCTURED** — Each AC as Given-When-Then (assertable `Then` on an observable, user-facing outcome) OR an EARS event-driven / unwanted-behaviour clause; obligation graded (MoSCoW MUST/SHOULD).
- **Q3 DATA-BACKED** — Q2 plus the `Then` names a concrete expected value (a specific threshold / state), and cases are enumerated (Examples / a MoSCoW×status register).
- **Q4 VALIDATED** — Q3 plus the core success AC carries a pre-committed pass/fail threshold fixed BEFORE build (falsifiable, not negotiable-after) — e.g. "снятие санкции по TTL 24 часа со статусом passed — MUST — Approved".

**White-spot triggers:**
- AC vague / not testable → ABSENT (no definition of done — named anti-pattern).
- AC tests implementation internals, not an observable outcome → Gherkin flag. AMBIGUOUS.
- No pass/fail threshold on the core success AC → caps at Q3.

### 9. Rollout & Measurement *(mandatory — gates the doc Q)*
**Answers:** How do we ship it, measure whether it worked, and keep it safe in production? (Atlassian PRD rollout/measurement section; Cagan business viability; Amazon economics; operational-readiness NFR — monitoring, feature-toggle, graceful degradation, rollback. Avito `A/B project` + `DoD` + `Учесть после выкатки`.)

**Q-rubric:**
- **Q0 ABSENT** — No rollout and no success metric ("выкатим и посмотрим").
- **Q1 ASSERTED** — A metric named with no target, or a rollout with no plan.
- **Q2 STRUCTURED** — A rollout approach (experiment / mvp / staged) + a success metric with a target + the explicit {ship / experiment-first / hold / drop} decision + operational-readiness named (monitoring, feature-toggle, rollback).
- **Q3 DATA-BACKED** — Q2 plus the success metric has a baseline from real data, is instrumented, maps to the context `key_metric`, AND the counter-metrics are monitored during rollout.
- **Q4 VALIDATED** — Q3 plus rollout is gated by a pre-committed success/kill threshold (the experiment's pass/fail defined before it runs).

**White-spot triggers:**
- No success metric → ABSENT (the #1 post-mortem failure; cannot reach sol-r3).
- No counter-metric monitoring / no kill-switch in rollout → ABSENT (operational-readiness gap).
- No explicit ship-decision → caps below sol-r3 (the decision-state condition of the r3 gate).
