<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# Build playbook — principles / anti-principles / improvements

> Cross-cutting build wisdom extracted from the Opp Doc (Stage 1) and Solution Doc (Stage 3) builds. **Every build handoff references this file** instead of restating process. Items are tagged `[applies-to]` — a handoff greps the tags relevant to its module. Every item is cited to a real line in `docs/worklog.md`, `docs/handoffs/stage-{1,3}-hand-back.md`, or `components/solution-doc/SPEC.md`. This is extraction, not invention (grounding adversarially verified 2026-07-07).
>
> **Scope note for rubric-less modules (backlogs):** items about Q-rubrics, rung conjunctions, seed-reachability, gap reports, and next-rung plans apply ONLY to the diagnosis-shaped doc modules (opp-doc, solution-doc). The backlog and planning modules are mutate/re-rank shapes with NO Q-rubric — they RECORD a given readiness claim, never derive or re-score it. Skip the diagnosis-only items when building a backlog.

---

## PRINCIPLES (do)

### SPEC design
- **Two-phase build:** design SPEC → hard STOP gate → freeze, THEN build the runnable skill from the frozen SPEC. The gate paid off: 7/7 smoke, 0 fix-rounds, because the container was already reviewed. (worklog:166-193; stage-3 hand-back §1) `[all-modules]`
- **Mirror the proven sibling SPEC** verbatim for structure + reconciliation rules; design fresh ONLY the frozen artifacts (section list + Q-rubrics + white-spot triggers). Do NOT invent new engine logic. (SPEC.md:36-45) `[all-modules]`
- **One work-item = one derived readiness dial.** Reject a second readiness family UNLESS a genuine ARTIFACT boundary (not a lifecycle stage) separates them. `sol-s/prd-r` collapsed to one `sol-r0..r3` because "PRD = the mature Solution Doc, one artifact"; a second ladder = shadow axis duplicating Q (C1) + maturity collision (C2). (SPEC.md:47-51; worklog:173-176) `[solution-backlog · planning · all-modules]`
- **State ABSENT/AMBIGUOUS precedence ONCE globally** so every per-section trigger inherits it, and forbid parametric belief explicitly: ABSENT only when a grounded scan of ACTUAL material returns nothing; any material that maps → AMBIGUOUS; "docs like this usually lack X" is banned. (SPEC.md:41 rule 6) `[all-modules]`
- **Ground every rubric rung and trigger in a NAMED source** (framework or real doc), never in parametric "docs usually have X". First-party-verified in Stage 3: Cagan, Amazon PR-FAQ, Torres, Shape Up, Google design-doc, ADR/MADR, EARS, Gherkin, RFC 2119, DbC. (SPEC.md:156/200/214; worklog:178-182) `[all-modules]`
- **Use a real domain artifact as an EVAL fixture + format orientation ONLY**, never a gold standard — and say so in the SPEC. The real Avito PRD «Холдирование Откликов» calibrated S7 without one uneven doc setting the bar (that IS the false-ABSENT test). (SPEC.md:44; worklog:180-182) `[all-modules]`
- **Conjunctive weakest-link gate:** doc-Q = min(Q of mandatory sections); the compensatory average is reported ONLY as a secondary progress bar; always name the single lowest gating section (the actionable white spot + task source). (SPEC.md:96) `[all-modules]`
- **Gate the TOP readiness rung at Q2** (structured + decided), reserving Q3/Q4 as scoring headroom for honest DIFF/demote detection — not as admission bars. "Ready" = structured-and-decided, not fully-validated. Prevents smuggling a Q4 requirement into the gate (an unreachable-oracle trap). (SPEC.md:60) `[solution-backlog · planning]`
- **"The doc supplies the item" beats a context white-spot:** an ABSENT trigger fires only when neither the context field NOR an in-doc equivalent exists (S7 fires only when no carve-out AND no kill-switch AND no counter-metric). (SPEC.md:81, 210) `[solution-backlog · planning]`

### SKILL design
- **Keep the SKILL body lean:** point at frozen artifacts in `references/`, inline ONLY must-stay-inline control logic — never copy rubric/spec/schema into the body. (worklog:197) `[all-modules]`
- **Name the must-stay-inline vs movable split up front** and re-verify every inline item is present after any trim: persona, admission/mutation gates, router branches, the readiness table, day-one rules stay inline; rubric/spec/schema/template/modes move to references. (worklog:198) `[all-modules]`
- **Bake every prior stage's hard-won learning in as day-one rules with stable IDs** — S-1 full-inventory mutation gate, S-2 next-rung completeness, X-1 all-5-fields, W2-1 post-write-readiness-leads. They held: chief-gate SATISFIED, 0 skill defects. (worklog:216-226) `[all-modules]` *(S-2 and W2-1 are diagnosis/report-emission rules — apply only to modules that emit a gap report and compute a next-rung plan; a backlog uses only S-1.)*
- **Admission guard = inline verbatim-Russian refusal that BOTH refuses AND routes**, and forbids synthesizing the missing upstream link — a bare «напиши prd»/idea never renders a report. (SKILL L52-68; SPEC.md:24,77) `[solution-backlog · opp-backlog]`
- **Mark a divergence from the sibling as an explicit INVERSION, not a silent difference** (sol-doc inverts opp-doc's "no PRD language" checks into a PRD-theater/altitude guard). (modes-and-checks L12-16) `[all-modules]`
- **Make W2-1 self-enforcing:** the report header «Готовность (r)» and the entry `readiness` MUST be the identical post-write value in the same pass — header == card, no drift. (SKILL L192-198) `[diagnosis-docs]`
- **Cross-module wiring = a single reviewable additive insertion.** The router-hook was ONE 9-line pure insertion into the sibling skill, all other branches byte-for-byte unchanged, regression-verified. Modules connect by an additive hook, not a rewrite. (stage-3 hand-back §1) `[all-modules]`
- **Version-bump BOTH manifests in sync + refresh the plugin cache on every SKILL change;** `/reload-plugins` is required before live invocation. (worklog:199/205/228) `[process · all-modules]`

### Stress & verification
- **Chief gate verifies ACTUAL FILES against fixed criteria, not judge/transcript narration** — a build session cannot live-invoke its own skill, so it must diff real bytes on disk. (stage-3 hand-back §3/§6/§7) `[process · all-modules]`
- **Every fixture oracle MUST be REACHABLE** from the frozen rubric + conjunctions as written — derive the expected landing BEFORE running, or the case tests nothing. (pristine/README:10) `[process · diagnosis-docs]`
- **Enforce STRICT-DERIVATION in every judge/simulator run:** readiness comes ONLY from the frozen conjunctions, never from the doc's mature surface, never inflated to relieve PM pressure — state this in the transcript header. (P1/P4/S7 headers) `[process · diagnosis-docs]`
- **Re-derive readiness statelessly every pass** so a later pass can DEMOTE a rung already earned/cached — the cache is NEVER a source of readiness. (P1 §6; W2-1 Step5; P3 §4) `[solution-backlog · planning · process]`
- **Build the adversarial probe suite around NAMED failure archetypes,** each with a one-line oracle: materiality-demote, single-option/Torres, invariant-as-postcondition/DbC, PM-pressure-on-gate, gold-plating/theater. (stage-3 hand-back §3 Stress-2) `[all-modules · process]`
- **Design each probe so the doc is deliberately STRONG everywhere except the trap** — isolating one defect proves both the catch AND false-positive discipline (no hallucinated ABSENT elsewhere). (P3 §0; P2:20; S7 §3.5) `[all-modules · process]`
- **Keep the hard gate answerable ONLY by the doc's conjunction** — refuse PM authority/urgency/repetition, and record the counterfactual (same pressure below the gate = refuse) even when the gate clears on merit. (P4 §5; S7 §5) `[solution-backlog · planning · process]`
- **Length-neutrality is a scored rule:** Q measures the answered question, so the longest section can be the lowest-scored; volume never buys a rung. (P5 §4) `[all-modules · process]`
- **Full-inventory mutation gate (S-1):** list EVERY file to be written before any write, scope confirmation to exactly that list, never grow the inventory mid-pass — a confirmation on one file never authorizes another. (P1 §7; P4 §6) `[all-modules · process]`
- **Two-tier enforcement:** advisory while drafting, HARD at the promotion/planning-admission boundary — a below-gate doc MAY live in the backlog but may NOT be handed downstream. (SPEC.md:89, 58) `[solution-backlog · planning]`
- **Run an independent adversarial review against the commissioning handoff's own trap checklist before handing back** — the checklist IS the review rubric. It caught the recurring friction-B class. (worklog:184-186) `[all-modules · process]`
- **Distinguish a skill-class defect from a fixture/simulator artifact;** let the fix-loop fire ONLY on skill-class defects (P6/W2-1 naming mismatch = fixture, not skill → loop correctly did not fire). (stage-3 hand-back §3 P6 row) `[all-modules · process]`

### Meta-process
- **Run the whole build as ONE multi-agent Workflow** with a fixed pipeline: plan → adversarial AC-coverage verify → per-deliverable build+independent-verify+fix → wire/register → smoke → 3-lens audit → 2 stress waves → chief-gate-vs-actual-files. (worklog:209-226) `[all-modules · process]`
- **When the skill honestly UNDER-claims a rung the SPEC implied, treat it as a WIN** (honest floor) and file the SPEC label as friction — never patch the skill to inflate. S1 landed sol-r0-floor, named the S2 gap, did not over-claim sol-r1. (stage-3 hand-back §4.1) `[all-modules · process]`
- **Approve the readiness ladder with a VISUAL map, not prose, at the human gate** — the user thinks in images under load. The one-dial collapse was carried by a visual walkthrough. (worklog:188) `[process · planning]`
- **Bake the sibling's hard-won build fixes into the SPEC as day-one non-normative build notes** so Phase B never rediscovers them. (SPEC.md:30) `[all-modules · process]`

---

## ANTI-PRINCIPLES (don't)

- **Don't let a rubric rung reference a value the rung itself defines** — a self-referential Q descriptor makes the test expectation unreachable. This friction-B class RECURRED (stage-1 r1, stage-3 S8-Q3) despite being pre-listed, and was only caught by adversarial review. (worklog:186; stage-3 hand-back §4 trap 2) `[diagnosis-docs · process]`
- **Don't let the SPEC promise an achievable rung from seed slots that structurally cannot satisfy that rung's conjunction** — the "SPEC row unreachable from partial seeds" defect recurred stage-1 (r1) → stage-3 (sol-r1, S2 not seeded) and each time forced an after-the-fact canon edit. (stage-1 §3 A/B; stage-3 hand-back §4.1) `[diagnosis-docs · process]`
- **Don't inherit a canon vocabulary split blindly** just because the reserved names exist — an unexamined second ladder becomes a shadow axis duplicating Q. (stage-3 hand-back §2.3) `[all-modules]`
- **Don't auto-generate plausible prose to fill an empty section, and don't grade down for stylistic choices** — the container reports the hole, never backfills it (one named substance exception: solution-first INTENT caps at Q1). Held under adversarial pressure: the engine did not invent a ship-decision to rescue a cached r3. (SPEC.md:36-40; P3 §5; P4) `[all-modules]`
- **Don't let a bare item enter a downstream module without its upstream contract** — refuse and route back with a verbatim message, never synthesize the missing parent. (SPEC.md:24,77) `[solution-backlog · opp-backlog]`
- **Don't define demote triggers as only "evidence removed"** — cover the materiality case where evidence got STRONGER but effect/appetite collapsed below target (route to a park/kill PM decision, not a silent stay). (SPEC.md:66) `[solution-backlog · planning]`
- **Don't force a low-readiness doc UP the ladder before it can be killed** — park/kill is legitimate at any rung below the top the moment a risk proves fatal. (SPEC.md:64) `[solution-backlog · planning]`
- **Don't demand a specific evidence shape where the domain legitimately expresses the same obligation operationally** — grade the operational form on its own rung (S7: carve-out/kill-switch=Q2, numeric threshold=Q3). (SPEC.md:44,205) `[solution-backlog · planning]`
- **Don't let a white-spot degrade rule read unconditionally while a sibling rubric trigger is conditional** ("unless the doc supplies…") — the mismatch forces a reconciliation later. Cross-check every ABSENT trigger against the context-degrade rules BEFORE freezing. (stage-3 hand-back §4.2; stage-1 §3 friction D) `[all-modules · process]`
- **Don't let a naive scorer collapse a conjunction to doc-Q=min(mandatory)** — optional-section gating terms and independent sub-conditions (testable-AC, explicit-decision) must gate SEPARATELY or the doc climbs silently. (P2:21-24) `[diagnosis-docs · process]`
- **Don't confuse "design proven / de-risked" with "ready"** — a de-risked design whose measured effect is below target still DEMOTES. (P1 §0) `[solution-backlog · planning · process]`
- **Don't hardcode the target version in the build handoff** ("bump 0.1.3→0.2.0") — sibling sessions bump the shared manifest concurrently, so the number is stale by build time. Instruct the wiring agent to read the ACTUAL current version and bump the minor. (stage-3 hand-back §2: 0.1.3→0.2.0 quoted, 0.1.7 actual) `[all-modules · process]`
- **Don't name a probe's transcript after the case-assignment rather than the probe that produced it** — a P6-vs-W2-1 mismatch masquerades as a failed/missing case and can trip or suppress the fix-loop. (stage-3 hand-back §3 P6) `[all-modules · process]`
- **Don't let a doc that WRITES a downstream entry also claim to OWN that entry's schema** — the sol-doc pass writes conforming solution-backlog entries; the layout is owned by `components/solution-backlog/SPEC.md`. A writer that claims the schema is a container-discipline leak. (SPEC.md:43) `[solution-backlog · opp-backlog]`
- **Don't treat the ~2500-word SKILL.md body ceiling as auto-satisfied:** the raw total (incl. frontmatter) lands over budget EVERY stage and needed a reactive trim pass each time. Budget frontmatter+body together from the first draft. (stage-3 hand-back §5; stage-1 friction E) `[all-modules · process]` *(open: is the ceiling on body-only ~2490 or raw-total ~2628? unresolved in canon — resolve once.)*

---

## IMPROVEMENTS (do-better, for the remaining handoffs)

- **Add a Phase-A mechanical "seed-reachability check":** cross every SPEC entry-point seed map against each rung's conjunction and label the GUARANTEED FLOOR rung, not the aspirational one. The unreachable-rung defect recurred because the LESSON was baked as a skill rule but the SPEC-DESIGN CHECK was not. (stage-3 hand-back §4.1) `[diagnosis-docs · process]`
- **Add a pre-authoring mechanical scan of every rubric rung for self-reference** — the friction-B trap recurred despite being a pre-listed checklist item, so listing is not enough; make it a scan. (worklog:186) `[diagnosis-docs · process]`
- **Do a single design-time cross-consistency sweep BEFORE freezing:** reconcile every ABSENT/AMBIGUOUS trigger against the context-degrade rules AND the entry-point rung labels. Both stage-3 canon-side frictions were internal-consistency mismatches a one-pass sweep would have caught pre-freeze. (worklog:232-237) `[all-modules · process]`
- **Make the wiring step version-drift-proof by contract:** the handoff says "read the CURRENT version live and bump the minor," never a quoted from→to pair; add a manifest-read as the first wiring action. (stage-3 hand-back §2) `[all-modules · process]`
- **Add a mechanical fixture-integrity precheck** (filename == probe-id; oracle-derivable-from-frozen-SPEC) so P6/W2-1-class and label-class mismatches are caught before the run, not classified after. (stage-3 hand-back §3/§5) `[process]`
- **Codify the one-dial collapse rule into the remaining handoffs:** one item = one derived dial; reject a reserved second family unless a real ARTIFACT boundary exists. (SPEC.md:51) `[solution-backlog · planning · all-modules]`
- **Codify "editing = lvl2, not a new component" into the remaining SPECs now** so backlog/planning inherit the active-edit seam for free. Reuses MAP-by-question, the rewrite-edit role, the …or-restructures checks, the Q-rubric as edit-target, the full-inventory mutation gate; two known lvl2 additions (before/after edit-diff view; false-edit-rate companion to the false-ABSENT gate). (worklog:258) `[all-modules · editing-lvl2]`
- **Secure the remaining real docs EARLY and record the false-ABSENT RATE, not just pass/fail:** M2→M3 stays blocked on ≥3 real docs and only 1/3 is secured for BOTH opp-doc and sol-doc — a data/dogfood wait the build stage cannot manufacture, so decouple it from build sequencing. (stage-3 hand-back §6; STATE.md) `[process]`
- **Ratify the exact solution-backlog entry shape** the sol-doc already WRITES against (three slots + folded sub-fields + status enum `{draft/assessed/prd_ready/archived}` + dated `readiness`) when solution-backlog is built — the writer is live against an M0 owner, a latent contract-drift risk. (SPEC.md:28,43) `[solution-backlog]`
