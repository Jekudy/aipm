<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# Design log — 2026-07-04 reconciliation

> The ChatGPT design line (docs/architecture/*.md, docs/opportunity-doc-plugin/*) reconciled with the repo canon (docs/model-axes.md, docs/architecture.md, components/*/SPEC.md). Products of this round: docs/target-solution.md, docs/handoffs/stage-1-opp-doc-lvl1.md, docs/handoffs/stage-2-opp-backlog-lvl1.md, components/opp-backlog/SPEC.md (lvl1), canon amendments to docs/architecture.md + docs/model-axes.md. On any conflict: locked decisions below + docs/target-solution.md win over the source material.

# Orchestrator decisions (LOCKED for this design round, 2026-07-04)

Adjudication of the 6 open decisions from the reconciliation pass. These are FINAL inputs for all drafts — do not re-litigate.

## D-1. r↔Q threshold table — LOCKED as proposed
- **opp-r0** (raw signal): pre-doc intake state — card exists with signal + source + rough domain; no doc required. Variant `r0-solution-signal` carries a problem-unknown flag.
- **opp-r1** (framed): framing sections S1 Problem, S2 Strategic fit, S3 Segment, S4 Success metrics each ≥ Q2.
- **opp-r2** (evidence-backed): r1 AND evidence sections S5 Evidence, S6 Sizing each ≥ Q3, alternative explanations addressed.
- **opp-r3** (decision-ready): doc-level conjunctive gate ≥ Q2 on the mandatory set (0,1,2,3,4,5,6,8,9,11) AND S11 explicit decision from the closed set {kill / park / continue-discovery / generate-solutions} AND S8 holds 1–3 candidates. **Identical to the existing promotion gate — the locked canon gate is NOT tightened.**
- Explicit note to include in specs: the ladder is a set of NAMED MILESTONES on one dial, not strictly nested by construction (an r3 doc may hold S5 at Q2 without ever earning the r2 label; the gap report always names blocking sections, so nothing is hidden). r is derived, dated, demotable, never stored as machine state, NEVER called "maturity".

## D-2. docs/solution-backlog.md in Этап 1 — CONFIRMED as write-only contract target
opp-doc appends promoted candidates at promotion; no consumer module exists yet. The file must exist for the composability acceptance criterion. Admission invariant applies from day one: no entry without a parent opportunity and an if-then-because product hypothesis.

## D-3. Dedupe-lite split — CONFIRMED
The router (Architecture lvl1) EXECUTES the similarity scan; opp-backlog lvl1 DEFINES the match keys + read contract. Both specs must reference the SAME match-key list: segment, scenario, metric/outcome, problem hypothesis, source/signal type, keywords. Scope: that PM's own folder only; cross-PM dedupe explicitly out of scope (isolation model).

## D-4. Amending locked docs — APPROVED, additive only
(a) `docs/model-axes.md`: ADD an addendum section defining r = work-item readiness as a DERIVED projection of doc-level Q + decision state (r↔Q table from D-1, never-"maturity" naming rule, clean-separation test). M ⟂ Q ⟂ lvl text untouched.
(b) `docs/architecture.md`: split skills/backlog-manager into skills/opp-backlog + skills/solution-backlog (matches components/); add router-lite under the Architecture module; apply the 8 contracts_updates items.

## D-5. Candidate generation policy — STRICT merge CONFIRMED
Verify/tidy existing PM hypotheses always. GENERATE new candidates only on explicit PM request AND after the r3 gate, grounded in the opportunity, capped 1–3, PM-confirmed before promotion. Detox always records the original idea as one candidate. Named anti-outputs kept: "15 идей ради креатива", solutions without parent opportunity.

## D-6. Status enums — card authoritative, container untouched
Backlog card status: `new | in_discovery | assessed | promoted | parked | killed`. Doc S0 keeps its frozen 4-value enum (draft/assessed/promoted/archived); card is authoritative for lifecycle; killed renders as archived in S0. The frozen 12-section container is NOT touched this round.

## Additional standing constraints for all drafts
- Этап framing per user (2026-07-04): **Этап 1 = Opp Doc lvl1 (+ Architecture lvl1: router-lite, contracts). Этап 2 = Opp Backlog lvl1.** Context-collection module stays M0, but the context-FILE contract is fixed NOW (forward-compat, no refactor later).
- Both ТЗ (build specs) must be self-contained handoffs executable by a fresh Fable session with no access to this conversation: boot list, scope owned/not-owned, steps, hard guardrails, done-criteria, acceptance smoke tests, hand-back protocol.
- Plugin home: `~/.claude/local-plugins/pm-flow/` (per existing brief). v1 prompt-only. One user-facing invocation surface.
- Language: spec/skeleton English; PM-facing strings verbatim Russian from the source docs.
- M2 smoke tests ≠ M3 gate (≥3 real docs, false-ABSENT rate) — always stated.
- `docs/sessions/oppdoc-build-brief.md` will be reduced to a pointer at the stage-1 handoff (superseded).


# Conflict register (reconciled)

## C1: Work-item ladder r0-r3 as a fourth axis vs locked M ⟂ Q ⟂ lvl [major]
- CANON: Exactly three axes: M (tooling build-state, GitHub Project only), Q (output quality, runtime rubric only, non-monotonic), lvl (module scope contract). No work-item axis exists.
- CHATGPT: All 6 docs build on a stored readiness ladder for work items (opp-r0..r3, sol-s0..s2, prd-r1..r3) as the central organizing axis, with a 'maturity engine' assigning it.
- RESOLUTION: Adopt r as WORK-ITEM READINESS, a DERIVED projection of the doc's Q profile + decision state — not an independently scored axis. Mapping: r0 = pre-doc intake card; r1 = sections 1,2,3,4 ≥Q2; r2 = r1 + sections 5,6 ≥Q3 + alt-explanations; r3 = the existing conjunctive promotion gate (≥Q2 mandatory set + S11 decision + 1-3 candidates). Cached on the backlog card as a dated claim, re-derived and demotable every pass. Add an r definition addendum to model-axes.md.
- WHY: The rungs retrace the Q evidence ladder (framed≈Q2, evidence-backed≈Q3, decision-ready≈promotion gate) — an independent r would be a shadow Q violating single-source-of-truth; but r0 (pre-doc) and the lifecycle-position semantics are genuinely absent from Q, so the concept survives as a projection. Q stays the single scoring machine; r is a cheap named view PMs can navigate by.

## C2: Word 'maturity' used for work items [terminology-only]
- CANON: 'Maturity' is reserved for M (build-state of OUR tooling, M0-M5).
- CHATGPT: All docs pervasively say 'maturity' for the item ladder ('maturity engine', 'maturity assessment', 'maturity milestones', 'weekly maturity plan').
- RESOLUTION: Rename to 'readiness (r)' in every downstream spec, contract, and PM-facing string. Derived phrases: readiness assessment, readiness milestones.
- WHY: Pure terminology collision; substance already resolved in C1. Leaving the word would corrupt the GitHub Project M semantics over time.

## C3: Engine-language core layers (entity graph, state engine, contract engine, backlog store, renderer/parser) vs prompt-only v1 [major]
- CANON: v1 = prompt-only: no Python engine, no subagents, no infra until a REAL doc demands it; state = plain Markdown; interfaces = committed files.
- CHATGPT: d2: 'нужны entity graph, maturity model, artifact renderer/parser'; handoff lists 8 core system layers incl. a backlog state store ('простая база' as an option).
- RESOLUTION: Keep the layers as conceptual VOCABULARY; realize each as a file convention or prompt behavior (graph→link-list card fields; state engine→readiness step in the diagnosis prompt; contract engine→c1-c5 gate checklists in SPEC prose; registry→router table in Architecture lvl1; store→the two committed .md files; renderer/parser→the MAP step; quality layer→Q-rubric + M3 gate). Workflow registry YAML stays a deferred backlog sketch.
- WHY: The docs themselves defer most of it ('machine-readable format можно прорабатывать позже') — the conflict is language, not intent. The target-solution doc must not inherit engine wording or someone will build it.

## C4: Flat opportunity-item YAML / 9-part doc structure vs the frozen 12-section container [major]
- CANON: Opp Doc = frozen 12-section container + per-section Q-rubric; gap report is a separate rendered output; never a second competing structure.
- CHATGPT: phase-1 doc defines a flat entity YAML the plugin 'parses docs into'; opportunity-doc-plugin proposes a 9-part MVP structure with gaps/tasks/claim-map inside the doc as an 'operational metadata layer'.
- RESOLUTION: 12-section container wins as the ONLY schema. The YAML survives as (a) the documented field→section mapping used by the MAP step (problem_hypotheses→S1, segments→S3, metric→S4, evidence→S5, sizing/confidence→S6, candidates→S8, unknowns→S9, recommendation→S11, owner/status/source→S0) and (b) the thin backlog card. The 9-part 'operational layer' (gaps/tasks/claim-map) maps onto the existing gap-report file opp-report-<n>.md — which realizes the two-layer intent without forking the container. Backlog packaging = the card appended to docs/opp-backlog.md, not a doc section.
- WHY: Two sources of truth for the same content is the exact failure canon's container discipline guards; the gap-report file already IS the operational layer the ChatGPT doc wants.

## C5: Persistent orchestrator with 8 machine workflow-statuses vs stateless skill [major]
- CANON: Stateless prompt-only skill, re-reads the doc each pass; no running process; no stored machine state.
- CHATGPT: opportunity-doc-plugin: an orchestrator keeps 8 machine statuses (needs_problem_framing … needs_backlog_packaging) behind 5 human statuses.
- RESOLUTION: No stored machine state: each pass DERIVES the single 'next step' (the machine-status equivalent) from the diagnosis and writes it into the card/doc header. Keep the 5 human statuses (new / in progress / needs input / ready for next step / parked) as a plain card field. Revisit only on a real failure (deferred-infra discipline).
- WHY: The doc's own rationale ('люди не должны руками вести много статусов') is fully served by a derived next-step field; a persistent orchestrator is infra v1 forbids.

## C6: Stored monotonic r vs non-monotonic never-stored Q [major]
- CANON: Q is non-monotonic and lives only in the runtime rubric; never stored.
- CHATGPT: r-levels read as stored, forward-progressing lifecycle states on items.
- RESOLUTION: The cached r on the backlog card is a DATED CLAIM ('r2, assessed <date>'), authoritative source = the doc via the rubric; every pass re-derives and MAY DEMOTE. Never store per-section Q values anywhere.
- WHY: next-steps.md itself says readiness is 'recalculated after each task-result intake' — the ChatGPT line already treats r as derived; pinning the demotion rule prevents r becoming a stored shadow Q.

## C7: HTML prototype / result screen as delivery vehicle [major]
- CANON: v1 = prompt-only Claude Code plugin; output = Markdown gap report via gap-report.tmpl.md; no UI.
- CHATGPT: next-steps.md plans 5 milestones culminating in an LLM-backed HTML prototype; 'result screen' is the product's center.
- RESOLUTION: Keep the result screen's INFORMATION ARCHITECTURE (top summary: readiness/status/scenario/diagnosis/next-step/priority-data; body: re-mapped doc, gaps, tasks, claim warnings, backlog card; 8 fixed questions; state-dependent CTA) and pour it into gap-report.tmpl.md. Quarantine the HTML milestones as an optional demo/comms track outside plugin scope. The milestone-3 prompt set (classifier/detox/gap-detection/rewrite/task-gen/claim-warning) folds into the single SKILL.md loop.
- WHY: The IA is the transferable asset; the vehicle conflicts with the locked prompt-only rule. Nothing of substance is lost by rendering the 'screen' as the Markdown report.

## C8: Promotion contract shape (5 ad-hoc fields / 8-field card) vs three-slot contract [major]
- CANON: solution-backlog.md entries carry INTENT + INVARIANTS (EARS-ubiquitous, from S4 counter-metrics + S9 constraints) + ACCEPTANCE-CRITERIA seed (EARS-shaped, from S8 riskiest assumption + S4 target).
- CHATGPT: Candidate card = solution_hypothesis/target_behavior/metric/assumptions/risks/mvp_hint (no invariants slot); opportunity-doc-plugin promotion = parent opp / target component / chosen hypothesis / expected mechanism / before-prd tasks.
- RESOLUTION: Three-slot contract stays normative. The richer card is the WORKING shape inside Opp Doc S8; promotion = transformation: intent ← parent opp + segment + target_behavior + metric + expected mechanism; invariants ← S4 counter-metrics + S9 constraints (add a guardrails field to the working card); AC seed ← riskiest assumption + expected effect + before-PRD tasks, EARS-stubbed. Field names survive as sub-fields, not a competing shape.
- WHY: The card is good drafting UX but lacks guardrails — exactly the slot that keeps a candidate composable across PMs; folding preserves both.

## C9: Fast-track / low-confidence bet vs hard promotion gate + no-generation anti-goal [minor]
- CANON: Promotion is a HARD conjunctive Q2 gate; never auto-generate prose to fill gaps.
- CHATGPT: Quality checks 'возвращают к дисциплине, но не блокируют'; refusal UX offers fast-track-with-risks and a low-readiness prd-r1 draft.
- RESOLUTION: Two-tier: during drafting all checks are ADVISORY (low-confidence-bet marking adopted as UX); at the promotion boundary the gate is HARD — flagged bets live in the opp backlog but never enter solution-backlog.md. Options (b)/(c) of the refusal UX produce ONLY the empty container + white spots + explicit warning, never synthesized content.
- WHY: Reconciles the docs' never-hard-block UX principle with the anti-slop gate; both survive at different boundaries.

## C10: Solution-candidate generation by the plugin [minor]
- CANON: Anti-goal: no doc generation from nothing; container discipline.
- CHATGPT: Architecture line puts 'solution candidate generation' in phase 1 as a plugin output; opportunity-doc-plugin line says 'если их нет — не генерируем без просьбы pm'.
- RESOLUTION: Merge the two ChatGPT lines: existing hypotheses are verified/tidied; generation happens ONLY on explicit PM request AND after the r3 gate, grounded in the opportunity, capped at 1-3, PM-confirmed before promotion. Detox always records the original idea as one candidate. Named anti-outputs kept: '15 идей ради креатива', 'solutions without parent opportunity'.
- WHY: The stricter opp-doc-plugin rule is the one consistent with canon; the architecture line's own anti-output lists already require grounding, so this is a tightening, not a loss.

## C11: Backlog store medium 'файл / json / таблица' [minor]
- CANON: Interfaces = committed plain-Markdown files only.
- CHATGPT: Mock store may be file/json/table; milestone-4 config is JSON.
- RESOLUTION: Markdown wins for backlogs AND the context file. 'Mock' means seeded/simplified content, never a different medium. JSON/output-schema go to the deferred-infra backlog.
- WHY: Direct canon rule; zero cost to comply since the files must exist anyway.

## C12: Phase-1 bundle (mock context + router lite + opp doc + both mock backlogs + dedupe lite) vs Этап 1 = Architecture lvl1 ∥ Opp Doc lvl1 [minor]
- CANON: Этап 1 = focused wave: Architecture lvl1 ∥ Opp Doc lvl1; far components stay M0.
- CHATGPT: Phase 1 bundles five things into the opp-doc increment.
- RESOLUTION: Absorb, don't expand: router-lite → Architecture lvl1 (canon already homes the router there); mock opp backlog → opp-backlog lvl1 (being specced now); mock solution backlog → docs/solution-backlog.md as a write-only contract target (no module); mock context → the context file per contract; dedupe-lite → router step + opp-backlog read contract. No wave redefinition.
- WHY: Every phase-1 element maps 1:1 onto something Этап 1 already contains or a file that must exist anyway.

## C13: Four 'AI specialists' + two user-facing skills vs one invocation surface, no subagents [minor]
- CANON: ONE command runs the whole pass; no subagents in v1.
- CHATGPT: 4 specialists (signal interpreter, detoxer, reviewer, candidate generator); 2 user-facing skills (intake&framing, gap resolution) + quality pass.
- RESOLUTION: One user-facing skill; router classification selects the internal branch; specialists = behavioral MODES (goal + desired/anti-output guardrails) inside the prompt; quality pass = inline instructions. Name the specialist seams as the designated future subagent split in the deferred-infra backlog.
- WHY: Packaging-only change; the anti-output lists are directly reusable as prompt guardrails.

## C14: Two backlog modules vs one backlog-manager skill stub [minor]
- CANON: architecture.md skill layout: ONE skills/backlog-manager stub; but components/ already has separate opp-backlog and solution-backlog SPEC dirs (canon internally split).
- CHATGPT: d10/d11: two separate user-visible, explicitly-activated backlog modules.
- RESOLUTION: Follow components/: spec opp-backlog lvl1 as its own module; solution-backlog stays M0. Update architecture.md's skill layout to two skills when next touched.
- WHY: components/ layout + d10/d11 agree; only the architecture.md skill list lags.

## C15: Raw r0 signals inside docs/opp-backlog.md [minor]
- CANON: opp-backlog.md holds problems/outcomes, NOT committed features.
- CHATGPT: A raw signal IS an opp-backlog item at r0 (signal = a state of the item); cards created even at r0/r1; solution-signals stored pre-problem.
- RESOLUTION: Admit r0 cards as an intake tier WITH: explicit readiness marker (r0 / r0-solution-signal with problem-unknown flag) and a mandatory next-step field. 'Potential solutions' on cards = unvetted signal content / links only. The problems-not-features invariant applies to what may be PROMOTED, not to intake.
- WHY: Nothing-gets-lost (backlog ≠ graveyard) and problems-discipline both survive; the readiness marker keeps the tiers legible.

## C16: Mock simulations as success criteria vs M2→M3 real-doc gate [minor]
- CANON: M2→M3 requires ≥3 REAL PM docs with false-ABSENT rate checked.
- CHATGPT: Phase-1 success = 4 simulations on mock context/backlogs.
- RESOLUTION: Keep the 4 simulations as M2 smoke tests / build-spec acceptance checks, explicitly stating they do NOT satisfy M3.
- WHY: Both are useful at different gates; conflating them would un-calibrate the white-spot detector (the neuroslop risk canon names).

## C17: 'Contract' terminology: transition gates vs file interfaces [terminology-only]
- CANON: Contracts = committed file interfaces with the three-slot shape.
- CHATGPT: c1-c10 'contracts' = stage-transition gates (what must be known / output / errors / human approval), explicitly not wiki pages.
- RESOLUTION: Split the term: 'interfaces / doc-contracts' for committed files; 'transition gates' (c1-c5 in Этап 1) inside module SPECs. Both kept.
- WHY: No substantive conflict — the docs object to bureaucracy, not to file interfaces.

## C18: Status enum for the opportunity item [terminology-only]
- CANON: S0 doc status: draft/assessed/promoted/archived; backlog status: assessed/promoted/parked.
- CHATGPT: new / in_discovery / decision_ready / solutions_generated / parked / killed (richer discovery side + kill semantics).
- RESOLUTION: Card status enum = new | in_discovery | assessed | promoted | parked | killed. Doc S0 keeps its 4 values; card is authoritative for lifecycle, S0 mirrors the coarse state (killed renders as archived in S0). Written into both lvl1 specs consistently.
- WHY: Merged enum covers the intake tier canon lacked and the kill decision d7 requires; keeping S0 stable avoids touching the locked container.

## C19: Team-tunable 'readiness preferences' (r-transition thresholds) [minor]
- CANON: One hand-authored, frozen Q-rubric; no runtime regeneration.
- CHATGPT: Milestone-4 config includes per-team readiness preferences.
- RESOLUTION: Reject for v1: the r↔Q mapping is locked with the rubric. 'readiness_preferences' stays a named reserved slot in the context contract, unread until M4+.
- WHY: Tunable thresholds before calibration on real docs would make r meaningless across PMs; contradicts the locked-rubric rule.

## C20: Russian source language for machine-layer content [terminology-only]
- CANON: Machine/instruction layer = English; PM-facing output = Russian.
- CHATGPT: All 6 docs written in Russian including structural content.
- RESOLUTION: Translate structural skeletons (state names, gate criteria, card fields) to English in specs; keep PM-facing strings VERBATIM Russian (detox questions, router dialogue with opp-123 options a/b/c, refusal scripts, low-confidence-bet message, kill/park/continue labels) — they are excellent PM-facing copy.
- WHY: Direct canon policy; the Russian dialogue examples are the best PM-facing material in the batch and must not be re-invented in translation.