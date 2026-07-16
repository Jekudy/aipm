<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# Stage 4 · Phase-A gate packet — solution-backlog lvl1 reverse-ratification

> Produced 2026-07-16 per `docs/handoffs/stage-4-solution-backlog-lvl1.md` §2F. Contents: the drift register (writer-vs-writer-vs-canon), the ranking decision, the §4 trap-checklist resolutions, open questions. The ratified schema itself lives in `components/solution-backlog/SPEC.md` (draft → FROZEN on gate approval). Nothing frozen was edited; every unreconciled divergence below is spec-friction for the orchestrator.

## 1. Evidence base

- **Writer #1 (opp-doc, promotion append):** SKILL.md §PROMOTION + live fixtures `.fixtures/stage-1/run/case-7-round-1/solution-backlog.md`, `.fixtures/stage-2/pristine/solution-backlog.md`.
- **Writer #2 (solution-doc, pass write-back):** SKILL.md pass step 2 + §PLANNING HANDOFF + live fixtures `.fixtures/stage-3/run/W2-1/solution-backlog.md`, `.fixtures/stage-3/pristine/case-9-p3/solution-backlog.md`.
- **Canon:** `docs/architecture.md#Interfaces` (opp-doc → solution-doc; solution-backlog → planning), `components/solution-doc/SPEC.md` (§Input/Output contract, §Readiness, rule 8 format-ownership), `components/opp-backlog/SPEC.md` (§Sister file), design-log C8/C9/D-5, model-axes r-addendum (sol-r collapse note).

## 2. Drift register

Ratified target = the sol-doc YAML-block form, extended to carry the full canon folded set (handoff §2A.2 directive: a backlog is structured data; the YAML form already carries `status`/`readiness`/`decision`).

| # | Dimension | opp-doc writes | sol-doc writes | Canon says | Ratified | Friction |
|---|---|---|---|---|---|---|
| D1 | Serialization | Markdown `## sol-A` + `###` subsections | fenced YAML block, single-item list | silent (three slots + folded set, no concrete form) | YAML block per entry | **F1** (opp-doc side must converge at its next unfreeze) |
| D2 | Entry id | none — H2 letter label `sol-A` (collides across opportunities in one file!) | `candidate_id: sol-cand-NNN-slug` | silent | `sol-cand-NNN-<slug>`, NNN=max+1 per file; sol-A/B/C = doc-internal labels only | **F2** (letter-id collision defect named) |
| D3 | Outcome-metric key | `target_outcome/metric` (slash) | `target_outcome_metric` (underscore) | slash, in the folded list | underscore (YAML/Sheets-safe key) | **F3** (canon text uses slash) |
| D4 | Folded set | full canon 8 (incl. `target_behavior`, `why_it_might_work`); `key_assumptions + guardrails` combined | reduced set — no `target_behavior`/`why_it_might_work`; `key_assumptions` present in W2-1, ABSENT in case-9-p3; `guardrails` in 1 of 2 fixtures only | full 8, `key_assumptions + guardrails` as a pair | full set, as SEPARATE keys `key_assumptions[]` + `guardrails[]` | **F4** (sol-doc fixtures under-fold, presence-inconsistent) |
| D5 | Lifecycle fields at promotion | none (no status/readiness/decision/updated_at) | expects them present to update | silent | opp-doc seeds all four: `status: draft`, `decision: —`, `readiness: sol-r0 (promoted <date>)`, `updated_at` | **F5** (opp-doc SKILL doesn't write them today) |
| D6 | Reserved fields | stage-2 fixture emits **stale `sol_state: sol-s0`** (pre-collapse vocab); stage-1 emits none | none | `sol_state` superseded 2026-07-07 by `sol-r0..r3` | `sol_state` RETIRED, never written; `bet_type`/`delivery_mode`/`intent_type` named optional UNREAD | **F6** (stale vocab in a live writer's output) |
| D7 | `parent_opportunity` form | `opp-201` / `opp-123` (opp-NNN, matches opp-backlog SPEC) | `opp-041-vacancies-pf-detective-window` (NNN-slug) | opp-backlog owns `opp-NNN` | `opp-NNN` | **F7** (sol-doc fixtures use a slug form) |
| D8 | invariants / AC shape | bullets under bold labels | W2-1: YAML lists of quoted strings; case-9-p3: folded scalars + key `acceptance_criteria_seed` | EARS-shaped, form silent | YAML lists of strings; ONE key `acceptance_criteria` (seed matures in place) | **F8** (sol-doc internal inconsistency, incl. the `_seed` key variant) |
| D9 | `decision` axis | absent | W2-1: `decision: —`; case-9-p3: absent | S9 closed set {ship/experiment-first/hold/drop} | mandatory, `—` when undecided; SEPARATE from status | part of F5/F8 |
| D10 | `title` | H2 heading carries it | absent | silent | mandatory `title:` key (top Sheets column; the H2 title survives as a field) | — |
| D11 | File preamble | H1 pre-exists (file-owner's line, not the append's output); `(<scope>)` suffix inconsistent — present stage-1, absent stage-2 | same H1 convention, `(<scope>)` present | silent | single H1 `# Solution Backlog — <owner>`; existing PM H1 accepted as-is (suffix tolerated) | — |
| D12 | `guardrails` placement | inside combined field, human-readable Russian | case-9-p3 scalar / W2-1 absent | folded pair | separate `guardrails[]` list (PM-facing mirror of `invariants[]`) | F4/F8 |
| D13 | Reason slot | n/a | W2-1 uses YAML comments for demote reasons | none (sister wave friction C4: "reason with no slot") | optional `note:` field (comments don't survive a Sheets migration) | — |
| D14 | Multi-entry layout | append H2 sections | single-entry files only (untested at N>1) | silent | one YAML block per entry; append = new block at EOF | — |
| D15 | Key order | n/a (prose form) | fixture order differs from ratified (readiness before status; hypothesis right after intent) | silent | canonical WRITE order pinned; lvl1 conformance = keys+values (order = hygiene note, load-bearing only at lvl2 Sheets) | — |

**Net:** the two writers agree on the CONTENT model (three slots + hypothesis fields) and disagree on nearly every SERIALIZATION decision; sol-doc additionally disagrees with itself across its two fixtures. This is the doubled version of exactly the defect the opp-backlog integration check surfaced (stage-2 hand-back §4.3). The SPEC now owns every one of these decisions.

## 3. Spec-friction for the orchestrator (canon/writers frozen — recorded, not patched)

1. **F1/F5 (load-bearing):** opp-doc's promotion append (SKILL §PROMOTION + `references/task-schema.md`) writes the Markdown form without lifecycle fields. Smallest fix at its next unfreeze: swap the append template to the ratified YAML block (content unchanged — same slots, same folded values) + seed the lifecycle four. Until then every fresh promotion produces recorded drift; Phase-B integration check will quantify it.
2. **F6 (re-scoped by the Phase-B integration check, 2026-07-16):** the stale `sol_state: sol-s0` is a hand-authored STAGE-2 FIXTURE artifact — the frozen opp-doc SKILL/task-schema contain no `sol_state` instruction, so a literal execution never writes it. Severity lowered to fixture-hygiene; no writer-side fix needed beyond F1.
3. **F3:** `docs/architecture.md#Interfaces` folded list says `target_outcome/metric`; ratified key is `target_outcome_metric`. Additive one-line canon note when next unfrozen ("serialized as `target_outcome_metric`, owner: components/solution-backlog/SPEC.md").
4. **F7/F8 (sol-doc side):** fixtures carry slug-form parent ids, an `acceptance_criteria_seed` key variant, scalar-vs-list invariants, missing guardrails/decision. sol-doc's SKILL prose is compatible with the ratified form (it names fields, not serialization) — the fix is fixture-hygiene + one line in its write-back step pointing at this SPEC as the layout owner. No behavioral change.
5. **F2:** `## sol-A` letter ids collide the moment a second opportunity promotes — a real defect independent of this ratification; covered by the F1 template swap.

## 4. Ranking decision (§2C) — summary

**PM-set ordinal `rank` (optional) + verbatim `pm_priority` passthrough; no computed score; everything else deferred.** Full argument in SPEC §Ranking. Key points: the canon interface to Planning already promises "ranked Solution options", so total deferral (opp-backlog's route) would breach the module's own contract; anything beyond an ordinal violates the no-aggregate-score precedent; foreign-prioritization passthrough is mandatory day-one behavior (real-wave R2 — the user's real sheet ranks by MoSCoW, its RICE columns sit empty: imposed scoring dies).

## 5. Trap checklist (handoff §4) — per-item resolution

1. **One canonical serialization** — ratified (YAML block, §Entry schema); all drift recorded in §2/§3. ✔
2. **Admission guard** — verbatim-Russian refuse-AND-route, three named paths, once-per-block; never synthesize a parent. ✔ (SPEC §Admission)
3. **Writer/owner separation** — ownership table W1/W2/O1–O6; no double-own (status/decision resolved by pass-context), no orphan op. ✔
4. **status enum = sol-doc S0 4-value; decision separate** — ratified; hold/drop never auto-map to archived (invariant 6). ✔
5. **Reserved-vocab reconciliation** — `sol_state` retired; single `sol-r0..r3` dial; dated/demotable/never-maturity (invariant 5). ✔
6. **Demote vs stay-low** — the pair is now NAMED in the SPEC readiness note: `(promoted <date>)` floor standing = stay-low (no reason expected); an `(assessed <date>)` rung replaced by a lower one = demote (dated, reason in `note`); this recording store does not derive either — it records the given claim. ✔
7. **Ranking scope decision** — made with argument (§4 above); deferred features forward-compatible. ✔
8. **Word budget** — Phase-B target ≈1500 words (sister landed 1513); must-stay-inline: admission guard, S-1 gate, ops list, enums, anti-loop UX, passthrough rule; movable: entry schema → `references/entry-schema.md` (verbatim SPEC copy). ✔
9. **No aggregate score** — EARS invariant 7. ✔
10. **Cross-consistency sweep before freezing** — run 2026-07-16 as a 7-lens multi-agent wave (`wf_f97b9845-177`; results in §7 below); all majors fixed pre-gate. ✔
11. **Real-data-fit ratified** — C1 (park/kill-at-intake admissible, status/decision elicited); C3 (parent = hard blocker WITH first-class route, incl. batch provenance-once); passthrough (invariant 7); R5/R6 as forward-compat periphery. ✔

## 6. Open questions (gate input, non-blocking unless flagged)

1. **`note` + `title` + `doc` keys** go one step beyond the literal canon folded list (rationale: C4 reason-slot friction, Sheets top column, sister `doc:` mirror). Confirm or strike at the gate.
2. **Promotion seeding (D5)** asks opp-doc to write four fields it doesn't today — accepted as recorded friction until opp-doc unfreezes? (Alternative — schema tolerates absent lifecycle keys — was rejected: it forces per-reader defaults, the no-fallbacks violation.)
3. **Delivery-outcome axis:** lvl1 records `decision: ship` + `note`; the real «решения» tab will surely contain shipped rows — is that honest-enough until lvl2 R3?
4. The «решения» tab is currently EMPTY — the real-data wave (Phase B §3.2) will run on plugin-produced promotions, and the emptiness itself is logged as a first-class finding (not diagnosed).
5. **Parent existence accepted on assertion (lvl1):** the admission gate checks presence + `opp-NNN` well-formedness, NOT existence (no cross-file read; avoids the sister's over-block trap). Dangling parents possible by design; existence validation = declared lvl2. Confirm at the gate.
6. **C7 (jargon in frozen verbatim strings), sister lesson:** resolved proactively for the NEW admission guard — it was de-jargoned BEFORE freeze (no internal field lists, no `r0-solution-signal` label; command names kept as actionable routes).

## 7. Cross-consistency sweep results (wave `wf_f97b9845-177`, 2026-07-16, 7 Opus lenses)

7/7 lenses returned; verdicts: 5 pass / 2 fail; findings: 3 major, 3 minor, 5 nit — ALL applied to the draft before this gate:

| Lens | Verdict | Applied fixes |
|---|---|---|
| opp-doc-writer | pass | D11 corrected (H1 is file-owner's, scope suffix inconsistent across fixtures) |
| sol-doc-writer | pass | D15 key-order drift row added; SPEC order qualified as WRITE order (conformance = keys+values); D4 notes `key_assumptions` presence-inconsistency |
| canon | pass | trap-6 wording made honest (see §5.6) |
| sister-mirror | pass | no findings |
| trap-checklist | pass | ISO-8601 dates mandated everywhere; stay-low vs demote named in the readiness note |
| red-team | **fail → fixed** | (major) quoting discipline: all free-text scalars double-quoted — bare Russian prose with `: ` broke YAML parse; (major) parent-existence decision ratified explicitly (accept-on-assertion, §6.5); (minor) W2-vs-O4 decision precedence sentence added |
| inherited-fixes | **fail → fixed** | (major) admission guard de-jargoned pre-freeze (C7); (nit) S12b separate-artifact transparency line added to day-one notes |
