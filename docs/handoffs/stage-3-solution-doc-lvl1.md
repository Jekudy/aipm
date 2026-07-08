<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# Stage 3 handoff — Solution Doc lvl1 (M0 → M1 → M2, two-phase)

> Self-contained ТЗ for a FRESH Fable session with no access to prior conversations. You will run a multi-agent Workflow pipeline (this is expected and proven — stage 1 was built this way). Two phases with a **hard STOP gate between them**: Phase A designs the SPEC (M0→M1), the user approves it, Phase B builds the skill (M1→M2). Never start Phase B on an unapproved SPEC.
>
> Destination of this file: `docs/handoffs/stage-3-solution-doc-lvl1.md` in `~/Vibe/products/aipm/`.

## 0. Boot list (read in this order, before anything else)

1. `~/Vibe/products/aipm/CLAUDE.md` — project rules (language policy, M ⟂ Q ⟂ lvl, container discipline).
2. `~/Vibe/products/aipm/STATE.md` — current stage. You never edit it (orchestrator owns it).
3. `~/Vibe/products/aipm/docs/target-solution.md` — North-Star frame (entities, derived readiness, module map).
4. `~/Vibe/products/aipm/docs/model-axes.md` — LOCKED axes + the r (work-item readiness) addendum. Your ladder design MUST mirror this addendum's pattern.
5. `~/Vibe/products/aipm/docs/architecture.md` — esp. #Interfaces (opp-doc → solution-doc entry = YOUR INPUT contract; context-file contract) and the shared-diagnosis-reference section (solution-doc reuses the SAME 6-step diagnosis shape with swapped frozen artifacts — this is locked).
6. `~/Vibe/products/aipm/components/opp-doc/SPEC.md` — the proven container shape to mirror structurally (12 sections + per-section Q-rubric + white-spot triggers) and the promotion contract that produces your input.
7. `~/Vibe/products/aipm/components/solution-doc/SPEC.md` — current M0 stub you will replace in Phase A.
8. `~/Vibe/products/aipm/docs/design-log/2026-07-04-reconciliation.md` — locked decisions D-1…D-6 + conflict register (esp. C1 derived-readiness, C8 promotion contract, C9 two-tier enforcement).
9. **The learnings corpus (MANDATORY — this is why stage 3 looks the way it does):**
   - `~/Vibe/products/aipm/docs/worklog.md` — how stage 1 was built, tested, fixed: 3 build runs, 2 stress waves (12+8 cases), the 4 skill fixes (S-1, S-2, X-1, W2-1), spec-tensions.
   - `~/Vibe/products/aipm/docs/handoffs/stage-1-hand-back.md` — spec-friction items A–G (each one is a trap your SPEC must pre-resolve, §4 below).
   - The built, stress-tested skill itself: `~/.claude/local-plugins/pm-flow/skills/opp-doc/` (SKILL.md v0.1.3 + references/) — the proven artifact structure to replicate: lean body + `references/{<module>-spec.md, <module>-rubric.md, gap-report.tmpl.md, task-schema.md, modes-and-checks.md}`.
10. `~/Vibe/products/aipm/docs/handoffs/stage-1-opp-doc-lvl1.md` — the stage-1 ТЗ (structure template for your Phase-B work packages; its §3 registration block and §8 execution method apply verbatim).

## 1. Goal

Solution Doc module lvl1: take a PROMOTED solution candidate and lead the SOLUTION ITEM toward a PRD. **PRD = the mature state of the Solution Doc, not a separate artifact** (mega-scenario 2 in STATE.md). Этап-3 goal sentence: a PM holding a promoted entry in `docs/solution-backlog.md` is led through a living Solution Doc to a PRD-ready state, with honest readiness, gaps, and routed tasks — same discipline as opp-doc, new frozen artifacts.

## 2. Phase A — design the SPEC (M0 → M1)

Author `components/solution-doc/SPEC.md` lvl1, replacing the M0 stub. Required content (mirror the opp-doc SPEC's structure):

1. **Section container** for the Solution Doc: the canonical section list with, per section, the QUESTION it answers.
2. **Per-section Q-rubric** (Q0–Q4 evidence ladder from model-axes.md, applied per section) + **white-spot triggers** (ABSENT vs AMBIGUOUS, grounded-scan rule) + the doc-level conjunctive weakest-link gate with a named mandatory set.
3. **Readiness ladder** for the solution item: define the semantics of the reserved vocabulary (sol-s0..s2 / prd-r1..r3) **as a DERIVED projection of the doc's Q profile + decision state** — mirror the r-addendum pattern exactly: derived, dated, demotable, never "maturity", floor rung explicitly worded. Decide with arguments whether two ladders (sol-s + prd-r) survive or collapse into ONE dial — don't inherit the split blindly.
4. **Entry points**: (i) promoted entry in `docs/solution-backlog.md` (the three-slot contract + folded sub-fields is your ONLY admission path — a bare idea NEVER enters; «напиши prd» without a promoted candidate stays opp-doc/router territory); (ii) an existing draft PRD/solution doc to diagnose (map-by-question, like opp-doc entry B); (iii) repeat pass / task-result intake with DIFF report. Define entry tiebreaks for mixed inputs.
5. **Exit contract**: what the doc updates in `docs/solution-backlog.md` (status enum + readiness claim on the entry) and what (if anything) it hands to planning — keep planning M0, name the seam only.
6. **Context contract consumption**: declare your fields (architecture.md names `guardrails`-related slots for solution-doc) + degrade-if-absent behavior per the contract's single home.
7. **Transition gates**: claim reserved names c6+ with the four-question frame (what must be known / what output / what errors / where human approval).

**Grounding (container discipline — the hard rule):** every section, rubric rung, and trigger must be traceable to (in priority order): (1) the canon contracts above; (2) **citable PRD practice** — named sources, the way the opp-doc container cites Cagan/Amazon/Torres; never parametric "docs like this usually have"; (3) **the user's real Avito PRDs** — ASK the user for 1–3 real PRDs at Phase-A start; if none arrive, proceed on (1)+(2) and record rubric calibration on ≥3 real PRDs as the blocking M2→M3 gate (same as opp-doc). Where the material is silent → explicit open question in the hand-back, never invented content.

**Phase-A hand-back (then STOP):** SPEC draft + grounding evidence (source per design choice) + the §4 trap checklist with per-item resolution + open questions. **Wait for explicit user/orchestrator approval. The approved SPEC is then FROZEN for Phase B.**

## 3. Phase B — build the skill (M1 → M2), only after approval

Build `skills/solution-doc/` in `~/.claude/local-plugins/pm-flow/` against the frozen SPEC, replicating the proven opp-doc artifact structure (boot item 9): lean SKILL.md (soft budget 2000–2500 words — stage 1 landed at ~2366; state the must-stay-inline list explicitly) + references/ (frozen spec + rubric + report template + task schema + modes-and-checks).

**Run the stage-1-proven pipeline (see worklog for the exact shape):** plan → adversarial AC-coverage verify → build with per-deliverable independent verification → smoke tests by prompt-simulation with independent judges + **strict-derivation discipline** (judges/simulators over-claim readiness otherwise — proven failure mode) → fix loop → 3-lens audit (verbatim-Russian / guardrails / doneness) → hand-back. Then **stress waves**: wave 1 = coverage of entry scenarios on a real user story (7-axis judge rubric: routing / readiness honesty / plan / container / verbatim / gate / domain; 0–2 each, pass = no zeros on critical axes ∧ total ≥ 10); wave 2 = adversarial probes on exits and pressure points (kill/park, genuinely-strong-doc false-ABSENT probe, PM pressure on hard gates «промоуть, ответственность моя», forced demote, stale conflicts) with an in-loop fixer and a **chief-orchestrator gate that verifies done-criteria against ACTUAL FILES, not judge narration**. Fixtures: `.fixtures/stage-3/{pristine,run,transcripts}` convention; every fixture must have a REACHABLE oracle (derive the expected landing from the frozen rubric before running — wave-2 case-3 lesson).

**Skill-design rules baked in from day one** (each was a stage-1 fix; do not rediscover them):
- **Full-inventory mutation gate** (fix S-1): the gate presents the COMPLETE list of files to be written, one line each; confirmation scoped to one file never authorizes another.
- **Next-rung completeness rule** (fix S-2): every plan enumerates EVERY unmet requirement of the next rung's conjunction (task or explicit already-met mark).
- **All-5-fields-mandatory** on every task: `task / role / why needed (which transition it unblocks) / acceptance criteria / linked gap` (fix X-1).
- **Post-write readiness leads the report** (fix W2-1): when a pass's own write moves the doc to a higher rung, header + card readiness show the POST-write value and name the transition; header and card must match within one pass.
- **Version bump + cache refresh on ANY post-registration edit** (both manifests in sync + `claude plugin update`), else the live skill runs stale prompts. `/reload-plugins` (Claude Code ≥2.1.195) picks up mid-session changes; the build session cannot live-invoke a skill it created — live verification is the user's step.
- Hardcode consts in Workflow scripts — `args.*` silently became undefined in the stage-1 build (project memory).

**Router hook — the ONLY permitted cross-module edit:** wiring solution-doc into router-lite means ONE minimal entry in `skills/opp-doc/SKILL.md` (promoted-candidate input → route to solution-doc), as an explicitly-scoped versioned edit (bump + cache refresh) with a regression re-run of 1–2 stage-1 fixtures proving existing branches unchanged. Everything else in opp-doc (and all other modules, canon files, STATE.md) is frozen — spec-friction protocol instead of edits.

## 4. Known-trap checklist (from stage-1 friction A–G + stress P1–P3 — your Phase-A SPEC must state a resolution for EVERY item)

1. **Floor rung** explicitly worded ("a doc MAY exist but has not yet earned rung 1") + complete readiness enum incl. the floor value (friction A + C).
2. **Reachable test expectations**: every smoke-case expected landing derivable from the locked conjunctions + rubric as written (friction B — stage 1 wrote a CASE-2 check its own rubric made unreachable).
3. **AMBIGUOUS-vs-ABSENT precedence** stated ONCE in the SPEC, rubric wording consistent with it (friction D).
4. **Realistic word budget** + explicit must-stay-inline / movable-to-references lists (friction E).
5. **Format ownership**: name which artifact owns each card/report layout; template previews must match the owner (friction F).
6. **Demote vs stay-low** naming defined (friction G).
7. **Split procedure** analog (one candidate → multiple docs?): define the write-procedure or declare it out of lvl1 scope explicitly (P1).
8. **Materiality gate**: demote triggers must cover "evidence STRONGER but magnitude collapsed", not only "evidence removed" (P2 — the S6 wording gap).
9. **Decision-at-any-rung**: park/kill legitimate below the top rung; the prose says so (P2).
10. **Entry tiebreaks** for mixed inputs defined (wave-1 spec-tension).

## 5. Hard guardrails (unchanged canon)

v1 PROMPT-ONLY (no Python/subagents/JSON/infra) · container discipline (map, never backfill; skeleton = empty container + white spots) · state = plain Markdown at PM-supplied paths (never the aipm repo, never the plugin dir; fixtures in `.fixtures/`) · PM-facing strings Russian, machine layer English · M lives ONLY in GitHub Project · reports lead with what mapped, never a bare ABSENT badge-wall · never "maturity" for work items · all mutations behind the full-inventory gate · two-tier enforcement (advisory while drafting, HARD at promotion-grade boundaries).

## 6. Done-criteria

- **Phase A done** = SPEC draft + grounding evidence + trap checklist resolved + open questions, handed back; **STOP received approval**.
- **Phase B done (M2)** = skill + references in the plugin; registered (version-bumped, cache-verified); smoke suite pass (prompt-simulation, independent judges); both stress waves SATISFIED by the chief-gate against actual files; 3 audits pass; hand-back written to `docs/handoffs/stage-3-hand-back.md`-style notes for the orchestrator (deliverable paths, smoke/stress results with the explicit "M2 smoke ≠ M3 gate" line, spec-friction log, open TODOs, fixture paths).
- **M2→M3 gate (NOT this stage):** calibration on ≥3 REAL PRDs with false-ABSENT rate checked.

## 7. Hand-back

Report to the orchestrator (never edit STATE.md / GH Project yourself): deliverable paths · Phase-A approval reference · smoke + stress tallies · spec-friction log (canon-side items listed separately) · open questions · the router-hook regression evidence. The orchestrator updates STATE.md and advances M.
