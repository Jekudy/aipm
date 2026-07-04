<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# Stage 2 build handoff — Opp Backlog lvl1 (M1 → M2)

> Self-contained ТЗ for a FRESH Fable session with no access to prior conversations. Everything you need is in the boot list below. Этап 2 = Opp Backlog lvl1 (Этап 1 = Opp Doc lvl1 + Architecture lvl1 is already built — you depend on it, you do not touch it).
>
> Destination of this file: `docs/handoffs/stage-2-opp-backlog-lvl1.md` in `~/Vibe/products/aipm/`. This ТЗ is NOT a schema home — the single owner of the card schema is `components/opp-backlog/SPEC.md`; this handoff merely implements it.

## 0. Boot list (read in this order, before anything else)

1. `~/Vibe/products/aipm/CLAUDE.md` — project rules (language policy, M ⟂ Q ⟂ lvl, container discipline).
2. `~/Vibe/products/aipm/STATE.md` — current stage. You never edit this file (orchestrator owns it).
3. `~/Vibe/products/aipm/docs/model-axes.md` — LOCKED axes, including the readiness (r) addendum: r = derived projection of doc-level Q + decision state; dated, demotable, never "maturity".
4. `~/Vibe/products/aipm/docs/architecture.md` — plugin architecture with the canon-edits amendments applied (router-lite under the Architecture module; skills split opp-backlog/solution-backlog; router → opp-backlog READ interface; interfaces vs transition gates).
5. **`~/Vibe/products/aipm/components/opp-backlog/SPEC.md` — THE FROZEN CONTRACT you implement against.** Single owner of the card schema, admission rules, read contract, write operations, link model, sister-file contract. You implement it; you never amend it.
6. `~/Vibe/products/aipm/components/opp-doc/SPEC.md` — frozen 12-section container + Q-rubric (card status mirrors doc S11; readiness derives from the doc via the rubric).
7. `~/Vibe/products/aipm/docs/handoffs/stage-1-opp-doc-lvl1.md` — what stage 1 built and why (context only; if absent, proceed and note the absence in your hand-back). The orchestrator records the stage-1 hand-back summary — including the absolute fixture-folder path — next to that handoff file, see §6.
8. **The stage-1-built plugin: `~/.claude/local-plugins/pm-flow/`** — read `skills/opp-doc/SKILL.md` + `skills/opp-doc/references/` (spec, rubric, gap-report template) and the current `skills/opp-backlog/` M0 stub (stage 1 creates it directly — see its handoff §4.12). If you instead find `skills/backlog-manager/` or no stub at all, record stage-1 friction and create/rename the dir yourself — the plugin dir is your deliverable; architecture docs are not.
9. The context-file contract lives INLINE in `docs/architecture.md#Interfaces` (context-collection → opp-doc entry) — you need only its opp-backlog line: target metric/outcome names validated against context metric slots if present; absent → no validation, no invented default. If the entry is missing, the inline rule in this item is normative for your build; record the absence as "canon-edits pending" (§6).

## 1. Role and lvl1 promise

You are the **Opp Backlog build session**. Your job: take `skills/opp-backlog/` from an M0 stub to **M2** (built into prompt/skill) implementing EXACTLY the lvl1 scope contract in `components/opp-backlog/SPEC.md` — a mutate/append operation set over ONE committed plain-Markdown file (`docs/opp-backlog.md`), all mutations behind manual invocation. This module is NOT diagnosis-shaped: it does not use the shared diagnosis reference. The inputs define no Q-rubric for this module — do NOT author one; record it as an open question for the orchestrator in your hand-back. The SKILL **defines nothing new — it implements the SPEC.** Sole exception: the SPEC's explicit build-time TODOs (the NNN-assignment rule + file preamble; the r0 rough-domain slot), which you resolve with the smallest convention, record in the SKILL, and report in hand-back.

M lives ONLY in GitHub Project #5; you never write M anywhere. The orchestrator advances M after hand-back.

## 2. Deliverables

1. **`~/.claude/local-plugins/pm-flow/skills/opp-backlog/SKILL.md`** — fleshed from the M0 stub. Contents:
   - Frontmatter per plugin conventions; argument-hint for the backlog file path (PM-supplied, like opp-doc's doc-path).
   - **Operations (each gated behind explicit manual invocation, never auto-fired):**
     - `create-card` — from router intake or an opp-doc pass, incl. r0 intake; enforce admission rules (r0/r1 only with explicit `next_step`; r0-solution-signal carries the problem-unknown flag).
     - `update-readiness-claim` — record the dated r claim produced by the opp-doc diagnosis pass; demotion allowed; never re-score independently; never write the word "maturity".
     - `update-status` — the SPEC's 6-value enum; at r3 record the S11 decision from the D-1 closed set {kill / park / continue-discovery / generate-solutions} (doc = source, card = index). Decision→status mapping per the SPEC's Schema notes: kill → `killed`, park → `parked`; the mirror for continue-discovery / generate-solutions is an open TODO in the SPEC — do not invent it, route it through the hand-back. The backlog skill never writes the doc: the `killed` → `archived` S0 rendering is performed by the opp-doc pass.
     - `append-links` — `linked_signals` / `potential_solutions` entries (link model = link-list fields only).
     - `update-next-step` — next_step + updated_at, every pass.
   - **Duplicate-signal backlog operations (dedupe, backlog side only):** the runnable home of the duplicate-like-signal flow is the stage-1 opp-doc SKILL's entry E (scan by the SPEC's match keys + the verbatim Russian dialogue + the merge/link/create human gate — see `docs/handoffs/stage-1-opp-doc-lvl1.md` §4.2 and its smoke CASE 4). This SKILL does NOT re-implement the scan or the dialogue. It implements only the backlog-side WRITE operations that consume the router/opp-doc dialogue outcome as a GIVEN input (the same given-input pattern as demotion in smoke test 3): on LINK — append to the matched card's `linked_signals[]`; on CREATE — create-card; MERGE is recommend-only, never executed. D-3's design-level split is preserved: the router remains the named executing party at the design layer and this skill executes its read contract on the router's behalf — record this designated seam in your hand-back notes so the orchestrator can mirror it in `docs/architecture.md#router-lite`. The skill invents no new keys, no new dialogue.
2. **`skills/opp-backlog/references/card-schema.md`** — verbatim copy of the SPEC's card-schema + admission-rules sections, headed by: source of truth = `components/opp-backlog/SPEC.md`; on divergence the SPEC wins. (Same frozen-artifact pattern as opp-doc references.)
3. **Seeded smoke-test fixtures** — authored in a scratch folder (same convention as stage 1: labeled MOCK; "mock" means seeded content, never a different medium; NEVER inside `~/Vibe/products/aipm/` or at any real PM-facing `docs/` path). Record the absolute fixture paths in the hand-back notes; the SKILL is exercised by passing those paths as the PM-supplied argument. The set:
   - a mock `opp-backlog.md` with a handful of cards, sufficient for smoke tests 1–3;
   - a mock `solution-backlog.md` containing at least ONE complete labeled-MOCK promoted entry (the three-slot contract: INTENT + EARS-ubiquitous INVARIANTS + AC seed, plus the folded sub-fields per the SPEC's sister-file section) — required for smoke test 4. Creating this NEW mock entry does not violate the §4 "don't edit existing `docs/solution-backlog.md` entries" guardrail: you create, you never edit.
4. **Hand-back notes** (see §7).

## 3. Step plan

1. Boot: read the boot list in order. Verify every dependency in §6 exists AND every boot-list item is reachable (items 7 and 9 degrade per their inline fallbacks). Any missing → record it per §6's routing (stage-1 friction vs canon-edits pending), stop the blocked thread only.
2. Flesh the `skills/opp-backlog/` stub (create/rename the dir yourself if stage 1 left `backlog-manager/` or nothing — record friction, per boot item 8); write `references/card-schema.md` as a verbatim copy from the SPEC.
3. Write SKILL.md body: the 5 operations, admission enforcement, the duplicate-signal backlog operations (given-input, deliverable 1), manual-gating language. Machine layer in English; PM-facing strings verbatim Russian from the SPEC.
4. Seed the mock fixtures in the scratch folder (labeled MOCK, per deliverable 3).
5. Run the 4 acceptance smoke tests (§5) end-to-end against the fixture; fix rough edges in YOUR deliverables only.
6. Write hand-back notes; hand back to the orchestrator.

## 4. Hard guardrails

- **Markdown only.** State = plain Markdown files at PM-supplied paths. No JSON store, no table, no database, no Python, no subagents, no infra.
- **No aggregate priority score.** priority_data = 5 qualitative dims (high|med|low); confidence is not a priority dimension; the parked formula stays parked and UNREAD.
- **No auto-mutations.** Every write behind explicit manual invocation. Claude never auto-clobbers carried state.
- **Demotion path must work.** readiness is a dated, derived, demotable claim; a build where r can only go up is a FAILED build.
- **Container discipline.** Never generate prose to fill a card field; a missing field is elicited from the PM or stays an explicit gap. Skeletons = empty structure, never synthesized content.
- **Three facets never merge:** readiness ⟂ status ⟂ priority_data.
- **Never the word "maturity" for items.** r = readiness. Maturity is reserved for M (GitHub Project only).
- **Don't touch stage-1 deliverables** (§6) and don't edit `STATE.md`, `docs/model-axes.md`, `docs/architecture.md`, the opp-doc SPEC, or existing `docs/solution-backlog.md` entries. Friction → protocol in §6, never a silent patch.

## 5. Done-criteria (M2) + acceptance smoke tests

**Done =** SKILL.md + references exist in the plugin; all 5 operations runnable end-to-end on the fixture; the 4 smoke tests below pass; hand-back notes written. (M1→M2 is then advanced by the orchestrator in GitHub Project #5.)

Smoke tests (mock; they do NOT satisfy the M2→M3 gate — M3 requires real PM material, ≥3 real docs / false-ABSENT rate on the diagnosis side — always state this in the hand-back):

1. **Eval case 4 — duplicate-like signal (backlog side):** GIVEN input = a PM decision from the verbatim Russian dialogue ("нашел похожие items: 1. opp-123 — похожий сегмент и метрика; 2. opp-087 — похожий сценарий. это продолжение существующей opportunity или новая?") — produced by the stage-1 opp-doc skill's entry E, the runnable home of the scan + dialogue (not re-run here; same given-input pattern as smoke test 3). Verify: LINK updates the matched card's `linked_signals`; CREATE makes a new card; MERGE is never executed (recommend-only).
2. **r0 card with mandatory next_step:** raw signal → r0 card created with signal + source + rough domain + explicit `next_step`; creation is blocked until next_step is supplied (elicit it, don't invent it).
3. **Demotion r2 → r1 proven:** a seeded card claims r2; the recorded re-assessment demotes the claim to r1 with a fresh date. Procedure: the demoted r1 claim (fresh date + one-line reason: evidence removed → S5 < Q3) is supplied as a GIVEN input to `update-readiness-claim` — the operation records, it never re-scores; running a real stage-1 opp-doc diagnosis pass is NOT required at M2 (that is M3 territory).
4. **Composability AC:** PM-B reads PM-A's promoted entry in the fixture `solution-backlog.md` (the seeded MOCK promoted entry from deliverable 3) and can act on it without PM-A present — verify the entry carries the complete three-slot contract (intent + EARS invariants + AC seed) and the folded sub-fields.

## 6. Dependencies (verify at boot)

**Built by stage 1 (absence = stage-1 friction):**
- `~/.claude/local-plugins/pm-flow/` plugin skeleton with `skills/opp-doc/` at M2 (SKILL.md + references: spec, rubric, gap-report template) + the M0 stubs.
- The write-only `solution-backlog.md` contract target with its admission invariant. NOTE: backlog paths are PM-supplied — there is no repo-level `docs/solution-backlog.md`. Stage-1 fixtures live in a scratch folder (absolute path in the stage-1 hand-back summary the orchestrator records next to `docs/handoffs/stage-1-opp-doc-lvl1.md`) and may be absent; if the path is not recorded, ask the orchestrator for the stage-1 fixture path; if absent, seed your own MOCK file per deliverable 3 and record it as stage-1 friction.

**Applied by the orchestrator's canon-edits pack (Track A; absence = "canon-edits pending", NOT stage-1 friction):**
- `docs/architecture.md` amended: router-lite section, router → opp-backlog READ interface, skills split into opp-backlog + solution-backlog, interfaces/transition-gates terminology.
- `docs/architecture.md#Interfaces` carries the context-file contract EMBEDDED inline (context-collection → opp-doc entry, canon-edits EDIT 4); entry missing → boot item 9's inline rule is normative, record as canon-edits pending.
- `docs/model-axes.md` readiness (r) addendum.
- `components/opp-backlog/SPEC.md` at lvl1 (the frozen contract).

**Must NOT be changed by stage 2:** `skills/opp-doc/` (SKILL.md + references/), the other M0 stubs (`solution-doc`, `solution-backlog`, `planning`, `context-collection`), `plugin.json`, `docs/architecture.md`, `docs/model-axes.md`, `components/opp-backlog/SPEC.md`, the frozen 12-section container, the Q-rubric, `gap-report.tmpl.md`, `STATE.md`, and existing `docs/solution-backlog.md` entries. `skills/opp-backlog/` is explicitly EXCLUDED from this list — it is yours to build.

**Spec-friction protocol (instead of editing):** if implementing the SPEC requires changing a stage-1 deliverable, or you find a contradiction between the SPEC and a stage-1 artifact — STOP that thread; record in the hand-back notes: what file, what contradiction, minimal proposed change, what it blocks; continue on unblocked work. Never patch frozen files, never work around a contradiction silently.

## 7. Non-goals (do not build, do not sketch)

Prioritization surfacing or any ranking output · stale-item detection · merge execution · cross-PM dedupe · shortlists for planning · readiness views · a solution-backlog module (stays M0; the file is write-only) · any non-Markdown store · automatic mutations · readiness-preference tuning · HTML anything.

## 8. Hand-back

Return to the orchestrator (do NOT edit STATE.md or the GitHub Project yourself):

1. Paths of all deliverables (SKILL.md, references, fixtures — absolute scratch-folder paths).
2. Smoke-test results, one line each (pass/fail + evidence), with the explicit "M2 smoke ≠ M3 gate" statement.
3. Spec-friction log (empty is a valid answer).
4. Open questions / TODOs discovered: the NNN-assignment and r0 rough-domain conventions you chose (the SPEC leaves them to you — record what you picked); the Q-rubric open question (§1); the decision→status TODO for continue-discovery / generate-solutions if you hit it; the router-executor seam note (§2, dedupe) for the orchestrator to mirror in architecture.md.

The orchestrator then updates STATE.md and advances Opp Backlog M1 → M2 in GitHub Project #5.
