<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# Hand-back — Stage 4: solution-backlog lvl1 (pm-flow plugin, M0 → M1 → M2, two-phase)

> Recorded 2026-07-16 per `docs/handoffs/stage-4-solution-backlog-lvl1.md` §6/§7. **Two-phase execution: Phase A** reverse-ratified `components/solution-backlog/SPEC.md` lvl1 from the two live writers + canon (7-lens verification wave `wf_f97b9845-177`, all majors fixed pre-gate; **user approval at the visual gate 2026-07-16 → SPEC FROZEN**, M0→M1); **Phase B** built the runnable skill via a 37-agent Workflow (`wf_59c2356e-448`: plan → build+independent-verify → smoke → stress → integration → 3 audits → register → chief-gate-vs-actual-files) + a post-wave patch cycle (`wf_1e7aa3f5-d5b`) + the real-data wave (`wf_8d429639-304`, 19 agents). Orchestrator updates STATE.md + GH Project #5 (not edited here).

**Deliverable state:** solution-backlog skill built to **M2** (runnable; exercised by prompt-simulation with independent judges, strict-derivation, file-level verdicts). **M2 smoke ≠ M3 gate** — M3 needs real promoted candidates + real PRD write-backs through the LIVE skill. **Live invocation of `/pm-flow:solution-backlog` pending `/reload-plugins` (or restart — the 0.5.1 update explicitly asks for restart)**; a build session cannot live-invoke a skill it created.

---

## 1. Deliverable paths

**aipm repo (canon side):**
- `components/solution-backlog/SPEC.md` — lvl1 RATIFIED & FROZEN (replaces the M0 stub; single owner of the entry schema + serialization).
- `docs/handoffs/stage-4-phase-a-gate.md` — Phase-A gate packet: drift register D1–D15, spec-friction F1–F8, ranking decision, §4 trap-checklist resolutions, sweep results.

**Plugin (`~/.claude/local-plugins/pm-flow`):**
```
skills/solution-backlog/SKILL.md                     (12 699 B; 1703 words raw — under the 2500 ceiling)
skills/solution-backlog/references/entry-schema.md   (11 251 B; verbatim frozen copy of SPEC §Entry schema + §Admission; byte-diff clean)
.fixtures/stage-4/{pristine,run,transcripts,stress,oracles,integration}   (smoke-1..5, P1..P6, RT1..RT2 — named by probe)
.fixtures/stage-4/integration/REPORT.md              (both-writers drift map ↔ F1–F8)
.fixtures/stage-4-real-wave/{REPORT.md,scenarios,oracles,run,transcripts} (T1–T4; report Russian, paraphrase-only)
```

## 2. Phase-A approval reference + ratified decisions

- **Gate approved by the user 2026-07-16** (visual map + AskUserQuestion, option «Аппрув — замораживай, старт Phase B»). SPEC status line records the freeze.
- **One canonical serialization ratified:** the sol-doc YAML-block form extended to the full canon folded set — one fenced YAML block per entry, 18 mandatory keys + optional (`rank, pm_priority, doc, note` + 3 reserved, omitted when empty), quoted free-text scalars (bare Russian with `: ` breaks YAML — parser-proven), ISO dates, canonical write order, `sol_state` retired, append = new block at EOF. Forward-compatible with the lvl2 base-TABLE + Sheets-via-`gws` target (keys = columns).
- **Promotion-time seeding:** opp-doc's append shall seed `status: draft`, `decision: —`, `readiness: sol-r0 (promoted <date>)`, `updated_at` (recorded friction F5 until opp-doc unfreezes — it doesn't write these today).
- **Ranking (§2C):** PM-set ordinal `rank` (optional) + mandatory verbatim `pm_priority` passthrough (MoSCoW/RICE never converted/aggregated); no computed score (EARS invariant 7); surfacing/shortlists deferred. Rationale: the canon interface to Planning promises "ranked Solution options" — total deferral would breach the module's own contract.
- **C1/C3 ratified:** already-decided legacy rows honestly admissible (status/decision elicited, never silent `draft`/`—`); parent = hard blocker WITH a first-class route; **parent existence accepted on assertion** (no cross-file read at lvl1 — avoids the sister's 59→0 over-block trap).
- **Dedupe:** deferred with argument (rare, PM-confirmed gate entries; a noticed duplicate = one recommend-only line, no op).

## 3. Tallies (all prompt-simulation; judges independent, oracles pre-derived from the frozen SPEC; chief gate on actual bytes)

| Phase | Result |
|---|---|
| Phase-A sweep (`wf_f97b9845-177`, 7 Opus lenses) | 3 major found (YAML quoting; parent-existence unstated; jargon in the new frozen guard) — **all fixed pre-freeze**; serialization validated by a runnable PyYAML check. |
| Plan | AC-coverage verify round 1 PASS (no replan needed). |
| Build | 3/3 deliverables PASS on independent verify, 0 fix rounds. |
| Smoke (5 SPEC seeds) | **5/5 PASS, 0 fix rounds** (S1 create-conformance; S2 demote recorded; S3 guard+legacy row; S4 rank+passthrough; S5 composability). |
| Stress (6 probes) | **6/6 PASS**; in-loop fixer never fired. P6 (bulk migration, the 59→0 archetype) re-run after an API-truncated simulator: clean PASS — **2 entries landed from 4 rows**, rows without parent/hypothesis refused with routes, ONE guard + ONE S-1 inventory. |
| Integration check (the stage's top test) | **PASS** — all four live writer fixtures + fresh promotion/write-back simulations diff to drift ALREADY recorded (F1–F8); one correction: `sol_state: sol-s0` is stage-2 FIXTURE hygiene, not opp-doc behavior (F6 re-scoped, see §4). Report on disk. |
| Audits | **3/3 PASS** (language / guardrails / doneness). |
| Register | 0.4.1 → **0.5.0** (build) → **0.5.1** (post-wave patch); both manifests synced, versions read LIVE both times, cache byte-verified. Restart/`/reload-plugins` required. |
| Chief gate (vs actual files) | **SATISFIED** — 20/20 frozen-file hashes intact, aipm git state clean of build writes, write-ops file-evidenced (incl. a real both-facet demote and zero-mutation refusals), 2 nit attributions only. |
| Post-wave patch (`wf_1e7aa3f5-d5b`) | S2-class fix (elicit-or-gap-marker `"— не подтверждено PM"` instead of synthesized content on O1; PM's-Russian intent; duplicate never bleeds into stored fields): adversarial review PASS, retests **2/2** (RT1 elicit/gap; RT2 gate regression under combined pressure — zero softening, zero writes). |
| Real-data wave (`wf_8d429639-304`) | **4/4 spec-pass; pm_scores persisted per test: T1=6, T2=7, T3=7, T4=7** (sister wave median was ~6). |

**0 open skill-class defects.** **M2 smoke ≠ M3 gate.**

## 4. Spec-friction log

**Canon-side (orchestrator to resolve; writer-vs-writer serialization drift listed first):**
1. **F1/F5 (load-bearing, from Phase A):** opp-doc's promotion append writes the Markdown drift form without lifecycle fields; smallest fix at its next unfreeze = swap the append template to the canonical YAML block + seed the lifecycle four. Until then every fresh promotion produces recorded drift → **SP4 (wave): priority raised** — each promotion will need a manual gated conversion by this skill.
2. **F2:** `## sol-A` letter ids collide at the second promotion into one file (covered by the F1 swap).
3. **F3:** canon folded list says `target_outcome/metric` (slash); ratified key is `target_outcome_metric` — one additive canon note.
4. **F4/F7/F8:** sol-doc fixtures under-fold, use slug-form parent ids, `acceptance_criteria_seed` key variant, scalar-vs-list drift — fixture hygiene + one layout-owner line in sol-doc's write-back step (extend it to name `updated_at` refresh + decision precedence — integration finding).
5. **F6 re-scoped by the integration check:** the stale `sol_state: sol-s0` is a stage-2 hand-authored FIXTURE artifact — the frozen opp-doc SKILL never writes it; lower the severity.
6. **Wave SP1 (canon question):** admission demands an if-then-because hypothesis even for rows the PM has already decided/killed — is a lighter decided-row tier ever wanted, or does the gap-marker relief suffice? (lvl1 handles it via elicitation + explicit gap markers.)
7. **Wave SP2 (ownership question):** should the W1 promotion carry the parent card's `priority_data` verbatim into `pm_priority`?
8. **Wave SP3 (link question):** opp-doc's c5 should write the back-reference (`potential_solutions` ← new `sol-cand` id) — T1 shows the parent↔child link is one-directional today.
9. **Smoke-3 oracle gap:** the SPEC defines readiness annotations `(promoted <date>)`/`(assessed <date>)`; a manual O1 create has no distinct floor form — bless `(promoted <date>)` for ALL floor entries or add `(created <date>)`. One-line SPEC clarification (post-freeze → recorded, not patched).
10. **S-1 vs no-jargon tension (wave T3):** the full-inventory list cannot avoid naming field names; scope the no-jargon rule explicitly to refusal/admission strings (its C7 origin) — one SKILL/SPEC wording reconciliation.

**Build-side (proposed SKILL fixes, NOT applied — mirror of sister S5–S12):** SF1 scope no-jargon vs S-1 lists (same as item 10) · SF2 compress the service layer (S12b line folds into the first-write confirmation) · SF3 routing-correctness line (promotion seeds sol-r0, not sol-r3 — T2 prose slip) · SF4 drift-form detection + gated-conversion offer stated as an explicit read-step rule · SF5 id-resolution echo (id+title+parent) before mutating a matched entry · SF6 a plain-Russian comeback path after the guard for deadline-pressed PMs. Wave also killed 10 contract-breaking «fixes» (auto-conversion, readiness nudging, opp-backlog peek, lvl1 delivery axis, priority_data→rank bridge, …) — see REPORT §4.

## 5. Inherited-fix status (stage-2 error-work, §3.1 of the handoff)

- **S1 anti-loop / S2 never-auto-default / S3 no-silent-lifecycle-lie / S4 conversational-provenance** — baked as day-one SKILL rules; ALL exercised and held in smoke/stress/wave. S2 additionally hardened post-wave (the elicit-or-gap-marker patch, RT1/RT2 verified) after the P6 judge caught synthesized content fields on bulk create.
- **C1/C3** — resolved in the SPEC (see §2). **R1/R3/R5/R6** — carried as forward-compat/lvl2 (schema needs no key change); R3 (delivered/shipped axis) got its priority RAISED by the wave (T4: shipped rows land as `archived`+`ship`+note — honest but lossy).
- **Sister process lessons applied:** per-test pm_scores persisted; fixtures named by probe; version read live (twice); no router hook; separate-artifact transparency line day-one.

## 6. Real-data wave (§3.2) — run, fallback mode

- **Finding №0 (first-class, recorded NOT diagnosed):** the real «решения» tab was verified live (2026-07-16, read-only browser view; no download, no rows copied) — **completely empty: zero rows, zero header columns**, while the sister «возможности» tab holds ~118 real rows. The real flow today stalls BEFORE solution promotion. The planned real-rows wave is impossible; fallback per handoff: plugin-produced candidates + the emptiness logged. **Re-run the wave when real rows appear.**
- 4 scenarios grounded in the actual world state: T1 promotion handshake over opp-doc's drift-form entry (gated conversion, content preserved); T2 empty-tab migration honesty (zero writes, paths named); T3 mixed-form queue + re-rank; T4 voice-note messy intake. 4/4 spec-pass, pm 6/7/7/7; findings in three buckets: **6 [skill-fix] / 4 [spec-friction] / 12 [lvl2-req]** (themes: storage-adapters 2, mandatory-core-vs-adaptive 3, foreign-prioritization 2, adoption 5), 10 killed at adversarial challenge. Full paraphrased report (Russian): `pm-flow/.fixtures/stage-4-real-wave/REPORT.md`. No raw sheet content exists this wave; no sheet identifiers in this repo.

## 7. Open TODOs / notes

- `/reload-plugins` or restart → live-verify `/pm-flow:solution-backlog` v0.5.1 on the stage-4 fixtures.
- Orchestrator: advance Solution Backlog **M0 → M2** in GH Project #5; rule on §4 canon items (F1/F5+SP4 first — they gate every fresh promotion); decide the lvl2 spec slot for the 12 wave requirements.
- Test-harness debts for the next wave (process notes): keep `pristine/` snapshots per wave scenario (T1/T3 conversions were transcript-asserted, not byte-diffable); seed pristine dates a few days before the run date so `updated_at` refreshes are observable.
- The commissioning handoff file `docs/handoffs/stage-4-solution-backlog-lvl1.md` contains the live sheet URL and **was committed by the orchestrator session mid-build (992e227)** — the URL of the private sheet is now in the public repo history. Orchestrator: decide whether to scrub it (rewrite/re-commit) or accept it (the sheet itself stays access-controlled).
- M2→M3 (NOT this stage): real promoted candidates + real PRD write-backs through the live skill; blocked on adoption (Finding №0).

One-line ping: «solution-backlog at M2, plugin v0.5.1: Phase-A SPEC ratified+frozen at the user gate (drift D1–D15, friction F1–F8), build smoke 5/5 + stress 6/6 + integration PASS + audits 3/3 + chief-gate SATISFIED, post-wave S2-patch verified 2/2, real-wave 4/4 spec-pass pm 6-7-7-7 fallback-mode (вкладка «решения» пуста — находка №0), spec-friction: 10 canon-side items, 6 skill-fixes proposed».
