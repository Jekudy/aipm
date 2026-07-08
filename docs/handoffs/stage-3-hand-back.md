<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# Hand-back — Stage 3: solution-doc lvl1 (pm-flow plugin, M1 → M2)

> Recorded 2026-07-07 per `docs/handoffs/stage-3-solution-doc-lvl1.md` §7. Two-phase execution: **Phase A** designed `components/solution-doc/SPEC.md` lvl1 (approved at the gate, one-dial `sol-r0..r3`); **Phase B** built the runnable skill via a 58-agent Workflow (`wf_47bc1c21-aee`): plan → build → smoke → 3-lens audit → 2 stress waves → chief-gate vs ACTUAL FILES. Orchestrator/user updates STATE.md + GH Project (not edited here, per §7).

**Deliverable state:** solution-doc skill built to **M2** (runnable skill; not yet tested on ≥3 real PRDs). Smoke + stress passed by prompt-simulation with independent judges. **M2→M3 gate NOT satisfied** (requires ≥3 REAL PRDs with the white-spot detector's false-ABSENT rate checked — 1/3 secured: the real Avito «Холдирование Откликов» PRD is saved as an eval fixture). **Live invocation of `/pm-flow:solution-doc` pending `/reload-plugins`** (a build session cannot live-invoke a skill it created).

---

## 1. Plugin path + file tree as built

**Plugin home:** `/Users/eekudryavtsev/.claude/local-plugins/pm-flow`
**New skill:** `skills/solution-doc/`
**Fixtures (absolute):** `/Users/eekudryavtsev/.claude/local-plugins/pm-flow/.fixtures/stage-3`

```
skills/solution-doc/SKILL.md                         (18831 B; body ~2490 words, must-stay-inline set complete)
skills/solution-doc/references/solution-doc-spec.md  (frozen 10-section container, transcribed from the SPEC)
skills/solution-doc/references/solution-doc-rubric.md(frozen Q0–Q4 rungs + white-spot triggers + 3 global rules)
skills/solution-doc/references/gap-report.tmpl.md    (report/DIFF template, PM-facing Russian)
skills/solution-doc/references/task-schema.md        (5-field task schema, X-1)
skills/solution-doc/references/modes-and-checks.md   (4 modes + 9 non-slop checks)
```

Fixtures: `.fixtures/stage-3/pristine/` (8 case dirs + README with reachable oracles), `run/` (working copies + `sol-report-*.md`), `transcripts/` (18: S1–S7, P1–P5, W1-1..W1-5, W2-1).

**Router-hook (the ONLY cross-module edit):** ONE 9-line pure insertion in `skills/opp-doc/SKILL.md` (STEP 3, above the A–E list) — "Downstream hand-off (checked FIRST): if the input IS a promoted solution candidate → route to /pm-flow:solution-doc and stop". All five A–E branches byte-for-byte unchanged (diff verified: single insertion hunk, no deletions/modifications). Explicit exclusion protects entry C (bare solution idea → detox, never this hand-off).

---

## 2. Registration outcome

**REGISTERED** `pm-flow@pm-flow-marketplace` **0.1.7 → 0.2.0** (both `plugin.json` + `marketplace.json` synced; `claude plugin update` succeeded; cache dir `~/.claude/plugins/cache/pm-flow-marketplace/pm-flow/0.2.0/` materialized with the full solution-doc skill + the router-hook string present in the 0.2.0 cached opp-doc SKILL). Note: the brief said bump 0.1.3→0.2.0, but the real current version was 0.1.7 (sibling sessions bumped 0.1.4–0.1.7); the wiring agent bumped the ACTUAL 0.1.7→0.2.0. **Run `/reload-plugins`** (or restart) before `/pm-flow:solution-doc` is live-invocable.

---

## 3. Smoke + stress tallies

> **M2 smoke ≠ M3 gate.** All results by prompt-simulation with independent judges + strict-derivation. Live invocation verification is the user's step after `/reload-plugins`.

| Phase | Result |
|---|---|
| **Build** | 6 deliverables + router-hook, each independently verified (+1 in-loop fix on task-schema, +1 word-budget fix on SKILL.md). |
| **Smoke (7 entry scenarios)** | **7/7 PASS**, 0 fix-rounds. S1 promoted→sol-r0-floor skeleton; S2 draft diagnose; S3 repeat-pass DIFF; S4 admission-guard refuse; S5 PRD-ready→sol-r3; S6 context-absent degradation; S7 hard-gate refusal. |
| **3-lens audit** | **PASS/PASS/PASS** (verbatim-Russian: admission refusal byte-identical to SPEC; guardrails: container discipline + two-tier + full-inventory gate held; doneness: all deliverables, no TODO). |
| **Stress-1 (real story, 7-axis judge)** | **5/5 PASS**, all **14/14**. Entry-scenario coverage on «Холдирование Откликов». |
| **Stress-2 (adversarial probes)** | **5/5 real PASS** (P1 materiality-demote, P2 single-option, P3 invariant-as-postcondition, P4 PM-pressure-on-gate, P5 gold-plating). **P6 = fixture-naming artifact, NOT a skill defect** — the W2-1 stale-conflict probe ran and PASSED (skill re-derives from the doc, lands sol-r2, post-write readiness leads), but its transcript saved as `W2-1.md` while the judge looked for `P6.md`. Classified `fixture`, not `skill`; 0 skill-class defects → fix-loop correctly did not fire. |
| **Chief-gate (vs ACTUAL FILES)** | **SATISFIED** — 7/7 criteria PASS (files exist non-trivial; 0.2.0 synced + cached; router-hook scoped-clean; no TODO; must-stay-inline complete; fixtures present; references faithful to the SPEC). |

**0 open skill-class defects.**

---

## 4. Spec-friction (canon-side; orchestrator to resolve — locked files NOT edited)

1. **[P1 · friction-B class] SPEC entry-(i) output label "sol-r1 skeleton" is loosely worded — sol-r1 is unreachable from the promoted seeds alone.** `components/solution-doc/SPEC.md` calls entry-(i)'s output a "sol-r1 skeleton" and names c6 "promoted candidate → sol-r1", but the sol-r1 conjunction (S1,S2,S3 each ≥Q2) cannot be met from the three-slot seeds, which seed S0/S1/S3/S6/S7/S8 but **not S2 Context&Scope**. The built skill handled this honestly (S1 smoke landed **sol-r0-floor**, named the S2 framing gap, did not over-claim sol-r1 — exactly the stage-1 friction-B lesson). *Smallest orchestrator fix:* relabel the SPEC entry-(i) output "**sol-r0-floor skeleton (framing toward sol-r1)**" and soften c6 to "promoted candidate → sol-r0-floor, framing started", OR add S2 to the seed map. Do not leave "sol-r1 skeleton" as an implied achieved rung.

2. **[P2] S7-guardrail ABSENT trigger vs the context counter_metrics-absence degrade rule — reconcile the "unless the doc supplies a carve-out/kill-switch" guard.** The S7 ABSENT white-spot fires only when there is no carve-out AND no kill-switch AND no counter-metric; but the Context-contract degrade note ("counter_metrics absent → S7 guardrail white-spot") reads unconditionally. They should be reconciled the same way S9/key_metric already is (doc-supplies-the-item wins). The build pinned the S6 smoke fixture to a doc lacking both, so the oracle stayed reachable; the wording reconciliation is a canon touch-up, not a skill defect.

3. **[minor] Reserved-vocab canon reconciliation (from Phase A).** The one-dial `sol-r0..r3` collapse means `docs/model-axes.md`, `docs/architecture.md#Interfaces` (reserved `sol_state`), and `docs/target-solution.md` still name the superseded `sol-s0..s2 / prd-r1..r3` split. Additive reconciliation to the single `sol-r` ladder.

---

## 5. Open TODOs / non-blocking items

- **SKILL.md soft-budget:** body ~2490 words (in-range); raw `wc -w` incl. YAML frontmatter ~2628 (~128 over the 2500 ceiling). Same class as stage-1 friction E (opp-doc landed 2712/2814). Chief-gate PASS; the file is leaner than its proven sibling. Trim ~130 words only if the ceiling is enforced on the raw total.
- **P6/W2-1 fixture naming:** rename the P6 assignment to W2-1 (the probe whose oracle it quotes) in a future stress run, or author distinct P6 artifacts. Cosmetic.
- **`grep -rn TODO` under `skills/solution-doc/`** → no genuine stub markers (one instructional "Placeholders <…>" line in the template is legitimate).

---

## 6. Done-criteria (Stage 3, M2) — MET

- ✅ skill + 5 references in the plugin; ✅ registered (0.2.0 synced, cache verified); ✅ smoke 7/7 (prompt-simulation, independent judges); ✅ both stress waves SATISFIED by the chief-gate against actual files (0 open skill defects); ✅ 3 audits pass; ✅ router-hook regression green (stage-1 case-1/case-3 fall through unchanged); ✅ hand-back written.
- **M2→M3 gate (NOT this stage):** calibration on ≥3 REAL PRDs with false-ABSENT rate checked. 1/3 secured («Холдирование Откликов», `scratchpad/real-prd-holdirovanie.md`).

---

## 7. Next moves (orchestrator/user)

1. `/reload-plugins` (or restart) → live-verify `/pm-flow:solution-doc` on a promoted candidate.
2. Update STATE.md + GH Project #5: Solution Doc M0 → M2 (mirror).
3. Resolve the §4 spec-friction (esp. item 1 — the sol-r1-label relabel).
4. Collect 2 more real PRDs for the M2→M3 false-ABSENT calibration.

One-line ping: «solution-doc skill at M2, plugin at `~/.claude/local-plugins/pm-flow` v0.2.0, smoke 7/7 + stress 10/10 (P6=fixture-naming) simulated, chief-gate SATISFIED, spec-friction: yes (3 canon-side)».
