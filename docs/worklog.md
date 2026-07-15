<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# Worklog — pm-flow / aipm

> Append-only chronological log of build, test, and fix work. The orchestrator appends an entry
> after every major step (build run, test wave, fix batch, canon decision). Newest entry LAST.
> Format per entry: date · what happened · defects/decisions · artifacts · next.
> This log complements STATE.md (STATE = where we are now; worklog = how we got here).

---

## 2026-07-04 → 05 · Stage-1 build: opp-doc lvl1, M1 → M2

**What:** Executed `docs/handoffs/stage-1-opp-doc-lvl1.md` via a 3-run multi-agent workflow
(plan → adversarial AC-coverage verify → build with per-deliverable independent verification →
§8 smoke tests with independent judges → 3-lens audit → §11 hand-back).

**Runs:**
- Run 1 (`wf_55c8b7b1-530`): all deliverables built. Bug: Workflow `args` did not propagate
  (paths rendered "undefined") — agents recovered from context; lesson saved to project memory
  (hardcode consts in workflow scripts).
- Run 2 (`wf_2a879d3d-583`): fixtures verify 14/14 PASS; plugin registered
  (`pm-flow@pm-flow-marketplace` v0.1.0, CLI-only). Smoke round 1: CASES 1/4/7 PASS; 2/3/5/6
  failed → smoke-fix found exactly ONE genuine skill defect (`task-schema.md` misquoted
  `priority_data` vs opp-backlog SPEC — fixed); rest were simulator errors (readiness inflation).
  Run died on session rate limit.
- Run 3 (`wf_f4de60cf-309`): re-ran 2/3/5/6 with strict-derivation discipline — all PASS
  (7/7 total); 3 audits PASS (verbatim / guardrails / doneness).

**Error-work:** priority_data schema misquote (fixed); r0-floor wording resolved inline in
SKILL.md (canon-side residual → spec-friction item A); simulator readiness-inflation pattern
neutralized by strict-derivation discipline in prompts.

**Spec-friction (7 items, orchestrator to resolve):** see `docs/handoffs/stage-1-hand-back.md#3-spec-friction`.
Key: (A) r0 = floor rung wording in canon; (B) §8 CASE 2 «→ r1» vs r1-conjunction; (D) §9.3
AMBIGUOUS-vs-ABSENT; (E) SKILL.md body ~2366 words vs soft budget.

**Artifacts:** plugin at `~/.claude/local-plugins/pm-flow/`; hand-back
`docs/handoffs/stage-1-hand-back.md`; fixtures `~/.claude/local-plugins/pm-flow/.fixtures/stage-1/`.
STATE.md updated; GH Project #5: Opp Doc → M2, Architecture → M2.

---

## 2026-07-05 · Registration live, live-verify, stale-cache fix → v0.1.1

**What:** After user restart the plugin skills registered live (`/pm-flow:opp-doc` + 5 stubs).
Live-verified by real invocation on the case-3 mock fixture (weak doc «отзывы покупателей»):
full pass ran — intake → dedupe → branch B → 6-step loop → honest r0 → gap report; stopped at
the mutation gate awaiting PM confirmation (gate works live).

**Error-work:** found the plugin CACHE was stale vs source (registration in run 2 predated the
run-2/3 fixes to SKILL.md + task-schema.md). Fixed per global policy: version bump 0.1.0 →
0.1.1 in both manifests + `claude plugin update`. Lesson: any post-registration edit to skill
files requires bump + cache update, or the live skill runs old prompts.

**Note:** `/reload-plugins` exists in Claude Code ≥2.1.195 and picks up mid-session installs
(no full restart needed); unavailable in the desktop session env — user restarted instead.

---

## 2026-07-05 · Stress wave 1: 12 antifraud entry scenarios → 12/12 PASS

**What:** Workflow `wf_2b625e2c-172` (28 agents): the user's real AF story (детективы скипают
кейсы → пропускаем живой фрод; 2 problem mechanisms; model fires at chat start; 3 solution
hypotheses) cut into 12 entry scenarios covering router classes A/B/C/E/D + repeat-pass +
refusal + context-absent + mixed input + full path to promotion. Each case: simulator follows
SKILL.md v0.1.1 literally + independent judge with a 7-axis rubric (routing / readiness honesty /
plan / container / verbatim / gate / domain; 0–2 each, pass = no zeros on critical axes ∧
total ≥ 10). Coverage critic compared the suite against canon entry scenarios.

**Result:** 12/12 pass, avg 13.75/14; routing 12/12; honest demote observed (case 7); hard
promotion gate held everywhere (incl. PRD-refusal case 8 and full-path promotion case 9).

**Defects found (root cause = skill):**
- **S-1** mutation-gate under-scoping: gate prompt confirmed the card write, but doc write-back
  + report file rode along unconfirmed (SKILL.md gate section).
- **S-2** next-rung plan incompleteness: case 12 surfaced sizing but not S5→Q3 quantification
  and alternative-explanations as r1→r2 requirements.
- **X-1** case-9 task emitted without «Критерии приёмки» (judge blamed fixture; synthesis
  reclassified as skill — same family as S-2).

**Spec-tensions (canon, not skill):** router has no A-vs-C tiebreak for mixed signal+idea
input; S1 Q2 scoring on a bundled two-problem statement (cases 2 vs 3 scored same material
differently).

**Coverage gaps (top-5 high):** kill/park exits at r3; strong-doc-on-entry (false-ABSENT
probe — direct M2→M3 gate metric); opportunity-that-should-split; PM pressure on the hard
gate; forced-demote on repeat pass. +8 medium/low in the report.

**Artifacts:** `~/.claude/local-plugins/pm-flow/.fixtures/stress-af/REPORT.md` (+ transcripts).

---

## 2026-07-05 · Fix batch: S-1 / S-2 / X-1 → v0.1.2

**What:** Two rules added, three defects closed:
- SKILL.md MUTATION GATE → **Full-inventory rule**: the gate presents the COMPLETE list of
  files to be written (PM doc, card, solution-backlog, opp-report audit file), one line each;
  confirmation scoped to one file never authorizes another (closes S-1).
- SKILL.md SHARED CLOSING STEPS + task-schema.md §2 → **Next-rung completeness rule**: the plan
  enumerates EVERY unmet requirement of the next rung's conjunction (task or explicit
  already-met mark) + **ALL-5-fields-mandatory** on every task (closes S-2, X-1).

Version 0.1.1 → 0.1.2, cache refreshed, fixes verified present in cache.

**Next:** stress wave 2 — 8 adversarial scenarios (kill/park, strong-doc false-ABSENT probe,
split, PM-pressure, forced-demote, merge-pressure, card-doc conflict) against v0.1.2, with a
chief-orchestrator quality gate and a fix loop until done-criteria hold.

---

## 2026-07-05 → 07 · Stress wave 2 (adversarial): SATISFIED → v0.1.3

**What:** Workflow `wf_b0b5f391-a1b` (24 agents, 9 rounds = 8 cases + 1 retry): adversarial
probes on the exits and pressure points wave 1 did not touch — kill/park recommendations,
genuinely strong doc on entry (false-ABSENT probe), split of a bundled opportunity, PM
pressure on the hard promotion gate («промоуть, ответственность моя» ×2), forced demote on a
corrected measurement (22% → 3–4%, join error), merge pressure («слей их в одну» ×2), stale
card-vs-doc readiness conflict. Chief-orchestrator gate agent verified done-criteria against
actual files (not judge narration): 8/8 pass ∧ 0 open skill defects ∧ falseAbsent=0 ∧ hard
gates held ∧ demotes honest/dated.

**Result: SATISFIED.** All 8 cases 14/14 on the final round. Solution-backlog byte-clean under
PM pressure; merge never executed (recommend-only held, limitation explained); demotes honest
and dated; false-ABSENT = 0.

**Error-work (1 fix, applied by the in-loop fixer, closes case-2 round-1 13/14):**
- **W2-1 «Post-write readiness leads the report»** (SKILL.md, READINESS block): when a pass
  writes content that moves the doc to a higher rung (e.g. an S11 park/kill decision closing
  the r3 conjunction), the report header and «Готовность (r)» lead with the POST-WRITE carded
  readiness and name the transition explicitly; header value and card `readiness` must match
  within one pass. Version 0.1.2 → **0.1.3**, cache refreshed.

**Notable honest-behavior findings (gate accepted, correctly):**
- case-6: oracle expected r2→r1/r0 demote, but the frozen rubric has NO materiality gate in
  S6 Q3 and the opp-backlog SPEC demote trigger reads «evidence REMOVED» (here evidence got
  STRONGER while magnitude collapsed ≈5% → ~0.1%). The skill kept r2 per spec-as-written,
  led the DIFF with the materiality collapse, routed park/kill to an explicit PM decision, and
  recorded the friction. Spec-tension, not a skill defect.
- case-3: fixture engineered S4=Q1 (no numeric target), so the oracle's r2 was unreachable;
  the skill's r0 verdict was rubric-faithful. Fixture defect; falseAbsent still 0.

**Residual (no open skill defects):** 6 spec-tensions, 2 fixture, 1 false skill-tag. New
canon-side items for the spec-friction backlog:
1. **[P1] Split write-procedure absent from canon** — «no decomposition» is a canonical
   critical gap, but no procedure defines the split resolution (docs per child, sibling
   cross-linking via linked_signals vs notes, parent archiving).
2. **[P2] S6/S5 materiality**: rubric has no magnitude gate; demote trigger wording
   («evidence REMOVED») doesn't cover evidence-stronger-but-immaterial.
3. **[P2] S11-decision-at-r3 prose**: SPEC/handoff wording implies S11 decisions only at r3;
   park/kill on a low-r doc is legitimate and the skill handles it — prose should say so.
4. **[P3] assessed-date on re-confirm**; loose '[discovery]' label in next-actions prose.

**Verdict:** dogfood-ready at v0.1.3. **M2→M3 NOT closed** — formal gate still requires ≥3
real PM docs with measured false-ABSENT rate (wave 2 is adversarial mocks, n=1 on falseAbsent).

**Artifacts:** `~/.claude/local-plugins/pm-flow/.fixtures/stress-af2/REPORT.md` (+ transcripts,
9 rounds). Workflows: wave 1 `wf_2b625e2c-172`, wave 2 `wf_b0b5f391-a1b`.

**Next:** user dogfoods a real AF signal through `/pm-flow:opp-doc` (deadline 2026-07-16);
collect ≥3 real docs for the M2→M3 calibration; orchestrator resolves the spec-friction
backlog (stage-1 hand-back §3 + the 4 wave-2 items above); stage-2 build (opp-backlog lvl1).

---

## 2026-07-07 · Stage 3 Phase A: solution-doc lvl1 SPEC — designed, reviewed, APPROVED

**What:** Executed `docs/handoffs/stage-3-solution-doc-lvl1.md` Phase A (M0→M1). Boot list read;
3 background agents (2 grounding-research on solution/PRD practice + the rigor layer, 1 read a
real Avito PRD from Confluence). Authored `components/solution-doc/SPEC.md` lvl1 — 10 sections
S0–S9, mirror of opp-doc — replacing the M0 stub.

**Key decision (handoff §2.3):** ONE readiness dial `sol-r0..sol-r3` — collapsed the reserved
`sol-s0..s2` / `prd-r1..r3` split. Rationale: PRD = mature Solution Doc (one artifact,
mega-scenario 2); a second family = shadow axis (C1/C2). Canon reserved-vocab reconciliation
→ spec-friction (canon NOT edited).

**Grounding:** first-party-verified named sources (Cagan 4 risks, Amazon PR-FAQ, Torres OST/5
assumptions, Shape Up no-gos, Google design-doc, ADR/MADR, EARS, Gherkin GWT, RFC 2119, DbC
invariant≠postcondition). Domain calibration from the real Avito PRD «Холдирование Откликов»
(Confluence 701170801) — used as an EVAL example (per user: not a gold standard), saved as a
Phase-B fixture (`scratchpad/real-prd-holdirovanie.md`).

**Review:** independent adversarial review vs the §4 10-trap checklist → NEEDS-FIXES (3 major +
4 minor, all 1–2 lines), all applied: word-budget note, split-out-of-scope, PRD provenance,
S8-Q3 self-ref typo (friction-B class), c9/Reforge/gloss cleanups, sol-r3=Q2-gate note.

**Gate:** presented with a visual readiness-ladder map; user APPROVED the one-dial design
2026-07-07. SPEC frozen for Phase B.

**Next:** Phase B — build `skills/solution-doc/` via a multi-agent Workflow (plan → build →
smoke → 3-lens audit → 2 stress waves → chief-gate vs ACTUAL FILES), all stage-1 learnings baked
in as day-one rules. Phase-B design: `scratchpad/phase-b-workflow-design.md`.

## 2026-07-07 — solution-doc SKILL.md built (Stage-3, lvl1)

- Built `~/.claude/local-plugins/pm-flow/skills/solution-doc/SKILL.md` (2808 words) — lean prompt-only body mirroring opp-doc structure. references/ (spec, rubric, gap-report.tmpl, modes-and-checks, task-schema) already present; SKILL points at them, inlines none of the frozen artifacts.
- Must-stay-inline verified present: persona, ADMISSION GUARD (verbatim RU refusal + route to opp-doc), FULL-INVENTORY mutation gate (S-1), router 3 entry points + tiebreaks, sol-r0..r3 table + conjunctive doc-gate, S-2 next-rung completeness, X-1 all-5-fields, W2-1 post-write-leads. Frontmatter: name solution-doc (registers /pm-flow:solution-doc), RU+EN triggers, argument-hint [doc-path].
- Version bump 0.1.5→0.1.6 in plugin.json + marketplace.json (synced); `claude plugin update` refreshed cache. Restart required before live invocation.
- Prompt-simulation smoke on real Avito PRD «Холдирование Откликов» fixture: admission guard fires on bare «напиши prd»; 6-step loop maps «Паспорт фичи» headings by question; false-ABSENT test PASSES — S7 carve-outs+kill-switch graded Q2 (not ABSENT), S8 register in Appendix A grounds S8 to Q3 (not ABSENT despite primary-doc pointer), S9 caps below sol-r3 (no explicit ship/experiment/hold/drop decision, mid-experiment). Verdict: sol-r2, blocked from sol-r3 by S9.

## 2026-07-07 — solution-doc SKILL.md word-count fix
- Sole failing verify criterion (body 2662→over the 2500 ceiling) fixed: trimmed prose redundancy across persona, prompt-only note, admission guard, mutation gate, 6-step loop, readiness prose, closing steps, planning handoff, context read; removed one duplicated pass-chain line. Body now **2490 words** (target 2000–2500).
- No semantic requirement dropped: verified intact — v1 prompt-only, container discipline (never backfill prose), RU/EN layer split, readiness≠maturity, full-inventory mutation gate (S-1), next-rung completeness (S-2), all-5-fields (X-1), post-write-readiness-leads (W2-1), verbatim RU admission-refusal, LOCKED sol-r0..r3 table (untouched), two-tier hard boundary, Planning M0 seam.
- Version bump 0.1.6→0.1.7 in plugin.json + marketplace.json (synced); `claude plugin update pm-flow@pm-flow-marketplace` refreshed cache (0.1.6→0.1.7). Restart required before live invocation.

---

## 2026-07-07 · Stage 3 Phase B: solution-doc lvl1 M1→M2 — Workflow SATISFIED → v0.2.0

**What:** Ran the full build pipeline as one 58-agent Workflow (`wf_47bc1c21-aee`, ~6.4M tokens):
plan → adversarial AC-coverage verify → build (6 deliverables, per-deliverable independent verify
+ fix) → wire+register → smoke (7 entry scenarios, prompt-simulation, independent judges,
strict-derivation) → 3-lens audit → stress wave 1 (real story, 7-axis judge) → stress wave 2
(6 adversarial probes + in-loop fixer) → chief-orchestrator gate vs ACTUAL FILES. All stage-1
learnings baked in as day-one rules (S-1/S-2/X-1/W2-1 + bump/cache + hardcoded consts). The
solution-doc SKILL.md + 5 references were built by the build-phase agents (see the two entries
above); this Workflow verified, tested, wired, and registered them.

**Results:** Smoke **7/7** (0 fix-rounds). Audits **3/3** (verbatim / guardrails / doneness).
Stress-1 **5/5** all 14/14. Stress-2 **5/5 real PASS** (P1 materiality-demote, P2 single-option,
P3 invariant-as-postcondition, P4 PM-pressure-on-gate, P5 gold-plating); **P6 = fixture-naming
artifact, NOT a skill defect** (the W2-1 stale-conflict probe ran and PASSED — skill re-derives
from the doc → sol-r2, post-write readiness leads — but saved its transcript as `W2-1.md` while
the judge sought `P6.md`; classified `fixture`, 0 skill-class defects). **Chief-gate SATISFIED**
(7/7 criteria vs actual files). **0 open skill defects.**

**Registration:** wiring agent bumped the ACTUAL current 0.1.7 → **0.2.0** (both manifests synced),
registered + cache verified; router-hook = ONE 9-line insertion in opp-doc SKILL.md (A–E branches
byte-unchanged, regression clean on stage-1 case-1/case-3). Live invocation pending `/reload-plugins`.

**Spec-friction (3 canon-side, orchestrator to resolve — see `docs/handoffs/stage-3-hand-back.md#4`):**
(1) [friction-B class] SPEC entry-(i) label "sol-r1 skeleton" is loose — sol-r1 unreachable from
the promoted seeds (S2 not seeded); skill honestly landed sol-r0-floor. Relabel needed.
(2) S7-guardrail ABSENT trigger vs the context counter_metrics-absence degrade rule — reconcile
the "unless the doc supplies a carve-out/kill-switch" guard. (3) reserved-vocab collapse
(`sol-s0..s2 / prd-r1..r3` → single `sol-r`) still to land in model-axes/architecture/target-solution.

**Non-blocking:** SKILL.md body ~2490 words (in-range); raw incl. frontmatter ~2628 (~128 over the
2500 ceiling — same class as stage-1 friction E; leaner than opp-doc 2814). P6/W2-1 rename cosmetic.

**Artifacts:** skill `~/.claude/local-plugins/pm-flow/skills/solution-doc/`; fixtures
`.fixtures/stage-3/{pristine,run,transcripts}` (18 transcripts); hand-back
`docs/handoffs/stage-3-hand-back.md`; real-PRD eval fixture `scratchpad/real-prd-holdirovanie.md`.

**Verdict:** solution-doc at **M2**, dogfood-ready after `/reload-plugins`. **M2→M3 NOT closed** —
needs ≥3 real PRDs with false-ABSENT rate (1/3: «Холдирование Откликов»).

**Next:** `/reload-plugins` → live-verify `/pm-flow:solution-doc`; orchestrator updates STATE.md +
GH Project (Solution Doc M0→M2) and resolves the 3 spec-friction items; collect 2 more real PRDs.

---

## 2026-07-07 · Stage 3 wrap-up: STATE + GH synced, all 3 spec-friction resolved, editing-extensibility validated

- **STATE.md** Solution Doc → M2 + Track D; **GH Project #5** Solution Doc M-status → **M2** (gh CLI, verified).
- **Spec-friction all 3 resolved:** (1) sol-r1 relabel — entry-(i)/c6 now read "sol-r0-floor; skeleton targets sol-r1; S2 not seeded" in SPEC + SKILL.md; plugin 0.2.0 → **0.2.1** (bump + cache). (2) S7-guardrail degrade rule gained the "unless the doc supplies a carve-out/kill-switch" reconciliation in the SPEC context-contract. (3) reserved-vocab collapse `sol-s0..s2 / prd-r1..r3` → single `sol-r0..sol-r3` landed as additive notes in model-axes.md + target-solution.md (×2) + architecture.md#Interfaces (`sol_state`).
- **Editing-extensibility validated** (user asked: "are we building legacy that blocks a future active-edit/restructure stage?") — 2 independent analyses (red-team + constructive) → **EASY-TO-EXTEND**. Active editing = **lvl2** of the doc components (not a new component/mode); reuses MAP-by-question (restructure engine), the `rewrite-edit` role, the non-slop "…or restructures" checks, the Q-rubric as edit-target, and the full-inventory mutation gate. Neuroslop stays out via the founding **ABSENT (never edit) / AMBIGUOUS (editable)** line + extractive-quote provenance. Two known lvl2 additions (NOT refactors): a within-pass before/after edit-diff view; a "false-edit rate" companion to the M2→M3 false-ABSENT gate. Analyses in scratchpad task outputs.

**Next:** `/reload-plugins` → live-verify `/pm-flow:solution-doc`; dogfood a real promoted candidate; collect 2 more real PRDs for the M2→M3 gate.

---

## 2026-07-08 · Repo push + issue backlog seeded on GitHub

- **Pushed** all pending doc work to `origin/main` (commit `docs: stage-3 solution-doc lvl1 build + team-digest module + worklog`): solution-doc SPEC, STATE, team-digest SPEC, stage-1/3 hand-backs, worklog, canon touch-ups.
- **Seeded 10 GitHub issues** in `Jekudy/aipm` — **labels-only mode**. These are work-items, deliberately kept OUT of Project #5 (which tracks module M-maturity, not tasks — putting tasks there would distort the component × M grid).
  - lvl1 wave, priority-ordered in the titles (`[PN]`): #1 [P1] Opp Backlog on real Google Doc · #2 [P2] Sol Backlog on real Google Doc · #3 [P3] context module · #4 [P4] mandatory modules + validation + setup · #5 [P5] docs-structure sweep · #6 [P6] test on 5 PMs + feedback.
  - epics (coarse container-discipline stubs, scope deferred): #7 lvl2 · #8 lvl3 · #9 lvl4 · #10 lvl5.
- All issues `state/triage` (raw inbox, AC filled later). P1/P2 carry an explicit TODO to attach the real Google Doc links (not invented — no-fallbacks).

**Next:** refine #1 (opp-backlog) — stage-2 handoff is ready & unblocked; attach Google Doc examples to #1/#2.

---

## 2026-07-12 · Stage 2 build DONE (opp-backlog lvl1 → M2) + real-data test wave on the PM's actual sheet

- **Build workflow `wf_bfd4e478-625`** (43 agents; survived 2 interruptions — session restart + token limit — resumed twice from journal cache; model routing per user directive: Fable = plan/chief-gate/curation, Opus = judges/audits/fixers, Sonnet = simulators, Haiku = mechanics): plan + adversarial AC-coverage (1 replan round) → 3 deliverables built+independently verified → registered **0.2.1 → 0.4.0** (one minor eaten by a resume artifact; both manifests synced, cache byte-verified) → **smoke 4/4, audits 3/3, stress 5/5 — all 0 fix rounds** → **chief-gate SATISFIED 9/9 vs actual files** (215/215 frozen hashes OK, aipm repo untouched, all 5 write ops file-evidenced). SKILL.md 1513 words. Hand-back → `docs/handoffs/stage-2-hand-back.md`.
- **Integration check** (live opp-doc card writes vs frozen SPEC): PARTIAL — **8 canon frictions**, top: SPEC↔task-schema disagree on card `id` location; two incompatible card serializations coexist in live writes (breaks any mechanical reader incl. the router dedupe scan).
- **Scope decision with user (2026-07-10):** the Google-Docs/table voice note does NOT unfreeze the SPEC — Stage 2 built strictly to the frozen Markdown contract; the note captured as structured lvl2 requirements (storage adapters via gws / mandatory-core-vs-adaptive fields / foreign prioritization) in hand-back §8.
- **Real-data test wave `wf_6f88626c-1cd`** (70 agents; user-requested mechanics: 5 independent input-designer lenses → Fable curator picks 12 of 23 scenarios → oracles pre-derived from frozen SPEC → strict Sonnet sims on rows of the PM's REAL working backlog sheet (118 rows, read-only CSV snapshot, identifiers scrubbed for the public repo; gws blocked by proxy — Chrome export used) → 3 judges per run → Opus clustering → Fable adversarial challenge): **spec_pass 12/12** (1 skill-class violation total), **PM-score median ~6, minima 4** (migration + bulk: 59 rows → 0 cards). Verdict frame: correctness anchors trust; failure is landing on real data. Output: **12 in-contract skill-fixes (S1–S12), 7 spec-friction questions (C1–C7; load-bearing: C3 source-gate, C1 park/kill-at-intake), 8 lvl2 requirements (R1–R8)**; 4 findings killed at challenge. Full paraphrased report: `pm-flow/.fixtures/stage-2-real-wave/REPORT.md` (raw sheet rows never leave local disk).

**Next:** `/reload-plugins` → live-verify `/pm-flow:opp-backlog`; orchestrator: Opp Backlog M1→M2 in GH Project, rule on C1–C7 + the 8 build-side frictions, decide lvl2 spec slot (R1–R8 map to GH issue #1 «Opp Backlog on real Google Doc»); apply S1–S12 as a follow-up skill patch (needs re-verify + version bump).

---

## 2026-07-13 · Wave priority-1 fixes S1-S4 applied to opp-backlog SKILL (patch 0.4.1)

- **Applied in-contract** (no schema/ops/enum changes): REFUSAL UX anti-loop section (verbatim string once per block; on same-point pushback acknowledge + one-sentence legal path + inline offer; "the gate holds, only the wording stops looping"); `owner` never auto-defaulted (PM's words only, else explicit gap); conversational/batch-level `source` counts for every card it covers; declared outcome at intake elicits status from the legal enum instead of silent `new` (delivered/done has no enum slot — surfaced, PM picks, gap noted).
- **Verify workflow `wf_2c6fd549-8c2`** (11 agents; Opus verify/judges, Sonnet sims): adversarial patch review PASS (all 4 intents faithful; frozen contract intact — enums byte-exact, S-1 un-softened, next_step still blocks, anti-loop not readable as skip-first-verbatim; wc -w 1738). Retests **3/3 PASS**: RT1 batch+source+outcome+anti-loop; RT2 owner probe; RT3 gate-REGRESSION under combined pressure (no pre-confirmation writes, no readiness negotiation). Registered **0.4.0 → 0.4.1**, cache byte-verified; chief check 215/215 frozen hashes OK.
- Open: S5-S12 (priority 2-3) proposed-not-applied; RT3's positive confirm→write branch out of probe scope (covered by build-time stress-P4).

**Next:** `/reload-plugins` → live-verify `/pm-flow:opp-backlog` v0.4.1; orchestrator rules on C1-C7 (source-gate C3 first) before any real migration attempt.
