<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# Target Solution — pm-flow (North-Star frame)

**Status: v1.0, reviewed.** Reconciled from the ChatGPT design line (6 digests) + repo canon (2026-07-04 reconciliation pass: 20 conflicts resolved, 6 decisions locked by the orchestrator).

**Destination of this file: `docs/target-solution.md` in `~/Vibe/products/aipm/`.**

**Relation to other docs:**
- `docs/architecture.md` — module-level plugin spec (skill layout, diagnosis engine, interfaces). This doc sits ABOVE it.
- `components/*/SPEC.md` — module containers (lvl scope contracts, Q-rubrics).
- `docs/model-axes.md` — LOCKED M / Q / lvl axes + the additive r-addendum (readiness as a derived projection, r↔Q table, never-"maturity" rule; approved per D-4a, landed 2026-07-04). Section 3 of this doc mirrors it.
- Source material: 6 ChatGPT design digests, reconciled 2026-07-04 — committed at `docs/architecture/*.md` and `docs/opportunity-doc-plugin/*`. They are **SUPERSEDED source material**: canon = this doc + the locked decisions; on any conflict THIS doc wins (their READMEs carry a SUPERSEDED banner per the canon-edits pack).
- Decision labels D-1…D-6 and conflicts C1…C20 cited below refer to the reconciliation's decision log + conflict register, committed as `docs/design-log/2026-07-04-reconciliation.md` (the decision content they carry is also inlined where cited).

This doc = the North-Star frame: what the plugin IS, its entities, flow, contracts, and phasing. Detail lives in the SPECs and build handoffs — link, don't duplicate.

---

## 1. Goal frame

The plugin is **NOT a document generator**. It moves WORK ITEMS to their next meaningful decision; documents are renderings of item state.

Formula: **diagnose the input → search the backlog for similar items → determine readiness → route to a workflow → help fill gaps → move the item forward.**

Motto: «не ускорять хаос, а возвращать продакта к дисциплине».

Persona: product buddy / critic of thinking / structuring helper / readiness navigator / discipline guard — never a micromanager, never merely a reviewer. Anti-reviewer principle: the plugin takes work OFF the PM — restructuring, gap detection, task generation, next step, backlog card.

User pains ranked (grounds the build order): квартальное планирование → PRD writing → opp/problem doc writing → prioritization. Opp Doc + Opp Backlog go first because everything upstream feeds them.

**3 mega-scenarios** (North Star, from STATE.md):
1. Нет достаточно качественного **Opportunity Doc** → хочет его получить.
2. Нет достаточно качественного **PRD** → хочет его получить (PRD = зрелый Solution Doc — one module, target output called PRD).
3. Нет поспринтово корректно спланированного **квартала** для диско → хочет его получить.

~10 entry scenarios all reduce to ONE pattern: diagnose where the PM is in the cycle → route to a module. The router is part of the Architecture module (single entry point), not ten separate workflows.

## 2. Entities: the files ARE the entity

Two long-lived work items:

- **OPPORTUNITY ITEM** — a raw signal and a finished Opp Doc are STATES of the same item. Represented by the 12-section Opp Doc (canonical container, unchanged — `components/opp-doc/SPEC.md`) + a card in `docs/opp-backlog.md`.
- **SOLUTION ITEM** — a solution candidate and a PRD are states of the same item. Represented by an entry in `docs/solution-backlog.md` (three-slot contract); later a Solution Doc. A PRD never starts from a raw signal or a wish — only from a chosen candidate.

The ChatGPT "core system layers" survive as ROLES, each realized prompt-only:

| ChatGPT layer | v1 prompt-only realization |
|---|---|
| entity graph | ID + link-list fields on backlog cards (linked_signals[], parent_opp, candidate ids) |
| state/readiness engine | readiness-assessment step inside the diagnosis prompt |
| contract engine | transition-gate checklists (c1–c5) in SKILL prose / SPEC |
| workflow registry | the router table inside Architecture lvl1 (machine-readable YAML deferred) |
| backlog state store | `docs/opp-backlog.md` + `docs/solution-backlog.md` (Markdown ONLY) |
| artifact renderer/parser | the existing MAP step of the shared diagnosis reference |
| quality/eval layer | Q-rubric + the M2→M3 real-doc calibration gate |

No second store, no sync problem: the markdown doc + backlog card IS the entity state. Revisit only if a real case shows the files can't carry it.

**Path root:** all runtime paths in this doc (`docs/opp-backlog.md`, `docs/solution-backlog.md`, the context file, `opp-current.md`, `opp-report-<n>.md`) are relative to the PM's OWN working folder per `docs/architecture.md`'s state model (separate folder per PM = the isolation model). This design repo holds no runtime state; the Этап-1 dogfood files live in the user's own PM folder.

## 3. Axes: M ⟂ Q ⟂ lvl, plus r as a DERIVED view

M / Q / lvl are locked — see `docs/model-axes.md`. In one line each: M = build-state of OUR tooling (GitHub Project only); Q = output quality (runtime rubric only, non-monotonic); lvl = scope contract of a module version (in its SPEC).

**r = work-item READINESS** — the position of a work item on its lifecycle. It is NOT a fourth stored axis: it is a named-milestone **projection of the doc's Q profile plus decision state**. Derive, don't score. Never called "maturity" (reserved for M); derived phrases follow: readiness assessment, readiness milestones.

Locked r↔Q table (decision D-1):

| r | name | derivation over the 12-section container |
|---|---|---|
| **opp-r0** | raw signal | pre-doc intake state: card exists with signal + source + rough domain; no doc required. No Q derivation. Variant `r0-solution-signal` carries a problem-unknown flag. |
| **opp-r1** | framed | framing sections S1 Problem, S2 Strategic fit, S3 Segment, S4 Success metrics each ≥ Q2 |
| **opp-r2** | evidence-backed | r1 AND evidence sections S5 Evidence, S6 Sizing each ≥ Q3, alternative explanations addressed |
| **opp-r3** | decision-ready | doc-level conjunctive gate ≥ Q2 on the mandatory set (0,1,2,3,4,5,6,8,9,11) AND S11 carries an explicit decision from the closed set {kill / park / continue-discovery / generate-solutions} AND S8 holds 1–3 candidates. **Identical to the existing promotion gate — the locked canon gate is NOT tightened.** |

*(Non-normative bridge between two locked texts: the 1–3 candidates are the promotion subset selected from S8's ranked options; S8 itself must still satisfy its own Q2 rubric row in `components/opp-doc/SPEC.md`.)*

Rules:
- The ladder is a set of **named milestones on one dial, not strictly nested by construction**: an r3 doc may hold S5 at Q2 without ever earning the r2 label; the gap report always names blocking sections, so nothing is hidden.
- r is **derived, dated, demotable**: re-computed every pass from the doc via the locked Q-rubric; cached on the backlog card as a dated claim (`readiness: r2 (assessed 2026-07-04)`); a later pass may DEMOTE it. Never stored as machine state; never in the GitHub Project (that's M); never a second rubric (that's Q).
- **readiness ≠ priority ≠ workflow status** — three separate card facets, never merged: an item can be r3-but-unimportant or r1-but-strategically-urgent.
- sol-s0..s2 / prd-r1..r3 stay NAMED but UNDEFINED (lazy fractal) — reserved vocabulary in contracts only. **(SUPERSEDED 2026-07-07: solution-doc lvl1 collapsed these into ONE `sol-r0..sol-r3` ladder — PRD = the mature Solution Doc, one artifact. See `components/solution-doc/SPEC.md` §Readiness.)**

## 4. Router (lives in the Architecture module)

One diagnose-first router; the plugin NEVER starts by writing. Router-lite (Этап 1 minimal version):

**Intake protocol — 8 questions, pre-any-action:** what did the user bring; which entity kind (opportunity vs solution vs plan-level); duplicate in backlog?; current readiness; next meaningful step; what's missing; what can AI do; what must the PM confirm.

**5 input classes (subset of the ~10 entry scenarios):**
- **A raw signal** → separate fact from interpretation, propose problem hypotheses + validation questions, dedupe scan, assemble r1 skeleton (container, not prose).
- **B weak opp doc** → the existing 6-step diagnosis loop (MAP → quote-check → Q → white-spots → elicit → report).
- **C solution idea** → solution-idea detox (below).
- **D existing backlog item** → read card + doc, derive readiness, name what's missing for the next rung, propose continuation.
- **E duplicate-like signal** → similarity scan over `docs/opp-backlog.md`, explain similarity, ask merge / link / create-new, update linked_signals. At lvl1 the plugin EXECUTES link (append to `linked_signals`) and create-new; choosing "merge" yields a recommend-only note — merge execution is deferred to a later lvl (§7).

**Dedupe-lite** = a prompt scan over THAT PM's own `docs/opp-backlog.md` by match keys: segment, scenario, metric/outcome, problem hypothesis, source/signal type, keywords. The router EXECUTES the scan; opp-backlog lvl1 (`components/opp-backlog/SPEC.md` — authored in this reconciliation, built in Этап 2) DEFINES the match keys + read contract (both specs reference the SAME list — decision D-3). Cross-PM dedupe is OUT OF SCOPE by the isolation model — an explicit limitation. Canonical dialogue (verbatim):

> «похоже, ты пришел с solution idea. я нашел похожую opportunity: opp-123 про активацию новых продавцов. (a) привязать как solution candidate к opp-123 (b) создать новую opportunity (c) пройти solution detox»

**Solution-idea detox** (mandatory pattern, eval case 2). PM arrives with a feature → the plugin does not forbid, it walks back:

> какую проблему решаем? для кого? в каком сценарии? какое поведение хотим изменить? какую метрику/outcome сдвинуть? какие альтернативные решения есть? есть ли похожая opportunity в backlog?

Outcome: the idea is DEMOTED to one solution candidate attached to a recovered/new opportunity («исходная идея становится solution candidate, а не истиной»); if the problem stays unclear, it is saved as an `r0-solution-signal` card. No path from a bare idea to the solution backlog.

**Refusal UX** — never hard-block, never pretend chaos is mature. On «напиши prd» the plugin diagnoses first, then offers:
- (a) detox;
- (b) fast-track marked as a **low-confidence bet**, listing what's unconfirmed;
- (c) a skeleton with a low-readiness warning.

Options (b) AND (c) produce ONLY the empty 12-section container + white spots marked + an explicit warning — NEVER synthesized content (C9). Fast-track changes the MARKING, not the generation rules; a "skeleton" is always the empty container, never prose.

**Two-tier enforcement:** all quality checks are ADVISORY during drafting; the conjunctive Q2 gate at the PROMOTION boundary is HARD — a low-confidence bet may live in the opp backlog but may NOT enter `docs/solution-backlog.md`.

## 5. Module map (7 zones)

| Zone (ChatGPT) | Canon home | Этап state |
|---|---|---|
| 0 context/onboarding | components/context-collection | Module stays M0; the context-FILE contract is fixed NOW (hand-authored fixture, labeled; forward-compat, no refactor later). Contract home: the context-collection → opp-doc entry in `docs/architecture.md#Interfaces` — the SINGLE HOME of the full field schema, declared consumers and degrade rules; the Этап-1 build spec (`docs/handoffs/stage-1-opp-doc-lvl1.md`, §9.3) carries a self-containment COPY for the fresh build session — on any divergence the architecture entry wins. Mandatory core = yearly goals, key metric, counter-metrics, backlog locations; MUST include the reserved `readiness_preferences` slot, named but UNREAD until M4+ (C19). Absence of the file or a field degrades to a white spot kicked back to context-collection — never a hard failure, never an invented default. Real module last. |
| 1 entry/router | Architecture module (`docs/architecture.md`) | **Этап 1, lvl1**: router-lite (intake protocol + 5 entries + dedupe + detox + refusal UX) |
| 2 opp doc | components/opp-doc | **Этап 1, lvl1** |
| 3 opp backlog | components/opp-backlog | **Этап 2, lvl1** = the module BUILD (intake ops, dedupe read-contract exercise, status ops). The card schema + the D-3 match-key list are AUTHORED NOW in `components/opp-backlog/SPEC.md` (single schema owner, published with this reconciliation) — Этап-1 card writes and the seeded `docs/opp-backlog.md` use THAT schema; the Этап-2 build implements it unchanged (same-list rule, D-3). |
| 4 solution/prd | components/solution-doc | **M2, lvl1 built 2026-07-07**; ONE `sol-r0..sol-r3` readiness ladder (collapsed the reserved sol-s0..s2 / prd-r1..r3 split) |
| 5 solution/prd backlog | components/solution-backlog | M0 stub; but `docs/solution-backlog.md` is a WRITE-ONLY contract target from day one (opp-doc appends promoted candidates; no consumer yet — exists for the composability acceptance criterion, decision D-2) |
| 6 planning | components/planning | M0 stub, detailed LAST; vocabulary reserved: discovery/delivery bet, delivery_mode (experiment/mvp/rollout/full_launch/test), 5 intent types (metric, strategic_learning, capability_platform, risk_quality_compliance, business_stakeholder); "planning schedules movement of items up the readiness ladder, not tasks" |

M states in this table are a descriptive mirror only — authoritative M lives in GitHub Project #5, never in files.

Backlogs are USER-FACING, explicitly activatable modules — not internal storage. `docs/architecture.md`'s skill layout carries the split (skills/opp-backlog + skills/solution-backlog, matching components/), the router-lite section, and the interface/state-model updates — applied 2026-07-04 per the canon-edits pack (approved amendment, decision D-4b).

**Invocation surface stays minimal:** ONE user-facing entry runs the pass; router classification selects the internal branch (intake&framing vs gap-resolution). The 4 named "AI specialists" (signal interpreter, detoxer, opp-doc reviewer, candidate generator) are behavioral MODES of the single skill prompt — their desired/anti-output lists become prompt guardrails; the subagent split stays on the deferred-infra backlog as the named future seam.

## 6. Work-item flow (end-to-end, Этап 1 slice)

```
input (signal / idea / weak doc / backlog item / task result)
  → ROUTER: classify → dedupe scan → place on r-ladder → pick branch
       (human gate: link vs new vs detox)
  → OPP-DOC loop: map → quote-check → score Q → white-spots (ABSENT/AMBIGUOUS)
       → elicit (capped) → gap report + updated doc
       → tasks (pm / analyst(evidence) / rewrite-edit)
  → PM/analyst work offline
  → TASK-RESULT INTAKE: what changed / closed gaps / NEW gaps /
       readiness re-derived (diff report)
  → repeat until r3: doc gate ≥Q2 + S11 decision {kill|park|continue-discovery|generate-solutions}
       + 1–3 candidates
  → r3 HUMAN GATE (four exits): kill → card status killed (renders archived in S0)
       | park → parked | continue-discovery → loop | generate-solutions → promotion path
  → PROMOTION (hard gate + human gate): each candidate transformed into
       the three-slot contract → appended to docs/solution-backlog.md;
       opp card status → promoted
  → opp-backlog card updated every pass (readiness claim, status, next step)
```

The canonical flow is a MAP, not a micro-script: enter anywhere; the model infers known-vs-missing (stateless re-read each pass). Sequential writing is a design PRINCIPLE only — gently return the PM to weak early sections; NO downstream-invalidation machinery, NO revision log (explicitly rejected); the existing `opp-report-<n>.md` audit trail is the light trace.

The gap-resolution loop is the heart: after a task result you may NOT proceed directly — gaps are re-analyzed and readiness re-derived.

## 7. Two backlogs (two decision queues)

- **`docs/opp-backlog.md`** answers "which problems/opportunities deserve attention and discovery". Holds items across r0–r3 including raw signals. **r0-in-backlog rule:** a signal IS an item at r0; critical gaps block TRANSITIONS, never STORAGE. r0/r1 cards are admitted only with a mandatory explicit `next_step` field (prevents dump-without-graveyard). The problems-not-features invariant is preserved by the readiness marker: `r0-solution-signal` carries a problem-unknown flag; `potential solutions` on a card is unvetted signal content / hypothesis links, never a commitment.
- **`docs/solution-backlog.md`** answers "which solutions/hypotheses deserve PRD/delivery/test". **Admission invariant (EARS-ubiquitous): the solution backlog shall accept no entry without a parent opportunity and a product hypothesis** (no bare ideas; if-then-because shape). Entries carry the canonical three-slot contract; the ChatGPT 8-field card is the human-readable working shape folded into the slots per C8 verbatim: intent ← parent opp + segment + target_behavior + metric + expected mechanism; invariants ← S4 counter-metrics + S9 constraints (the S8 working card gains a `guardrails` field feeding this slot); AC seed ← riskiest assumption + expected effect + before-PRD tasks, EARS-stubbed.

Card status enum (decision D-6): `new | in_discovery | assessed | promoted | parked | killed`. Doc S0 keeps its frozen 4-value enum (draft/assessed/promoted/archived); the card is authoritative for lifecycle; killed renders as archived in S0.

Links are many-to-many, carried as LINK-LIST FIELDS on cards (not a graph store): linked_signals[], parent_opp, solution_candidate ids, (reserved) bet ids, metric names.

lvl1 backlog operations: intake/append, dedupe read-contract, status + readiness-claim updates, park/kill/continue. Deferred to a later lvl (forward-compatible in schema): prioritization dims, stale detection, merge execution, shortlists, readiness views.

## 8. Contracts: two kinds, named apart

- **Interfaces (doc-contracts)** = committed files with the three-slot shape (intent + EARS invariants + acceptance-criteria seed). The ONLY way modules talk. Unchanged — see `docs/architecture.md#Interfaces`.
- **Transition gates (c1–c10)** = stage-transition frames answering: what must be known to proceed / what output appears / what errors to catch / where human approval is required. Этап-1 set, each mapped to its EXISTING home: **c1** raw input → classified entry = the router-lite intake protocol (`docs/architecture.md`, Skill layout); **c2** signal → r1, **c3** r1 → r2, **c4** r2 → r3 = the r-derivation rows in the `docs/model-axes.md` r-addendum; **c5** r3 → solution candidate = the promotion gate in `components/opp-doc/SPEC.md`. c6–c10 reserved names. TODO: the explicit four-question frame per gate is not yet authored anywhere — it lands inside each module's lvl spec as that spec is written; do not invent gate frames to fill the gap. Constraint: «контракты не должны травмировать работу сильных моделей микроменеджментом» — gates are behavior frames, not step-scripts.

**Human gates:** link-vs-new-vs-detox at the router; kill/park/continue/generate at r3; candidate confirmation before promotion; (future) bet commitment.

**Candidate generation policy (decision D-5, strict merge):** verify/tidy the PM's existing hypotheses always. GENERATE new candidates only on explicit PM request AND after the r3 gate, grounded in the opportunity, capped 1–3, PM-confirmed before promotion. Detox always records the original idea as one candidate.

## 9. Phasing

- **Этап 1 = Opp Doc lvl1 + Architecture lvl1** (router-lite, contracts). ChatGPT "phase 1" absorbed without wave redefinition: router-lite → Architecture lvl1; mock opp backlog → the committed file with seeded content, cards shaped per the `components/opp-backlog/SPEC.md` schema (see §5 zone 3; "mock" = seeded content, never a different medium); mock solution backlog → write-only `docs/solution-backlog.md`; mock context → hand-authored context file per contract; dedupe-lite → router step + opp-backlog read contract.
- **Этап 2 = Opp Backlog lvl1** — the module build against the already-authored `components/opp-backlog/SPEC.md` (intake, dedupe read-contract, statuses).
- **Later waves:** solution-doc (→ PRD), solution-backlog module, planning last. Lazy fractal holds — no pre-design.

**Execution artifacts:** each Этап ships as a self-contained fresh-session build handoff (boot list, scope owned/not-owned, hard guardrails, done-criteria, acceptance smoke tests, hand-back protocol — a fresh Fable session must be able to execute it with no access to the design conversation): Этап 1 → `docs/handoffs/stage-1-opp-doc-lvl1.md`; Этап 2 → `docs/handoffs/stage-2-opp-backlog-lvl1.md`. Plugin home: `~/.claude/local-plugins/pm-flow/` — v1 prompt-only, ONE user-facing invocation surface for the diagnosis pass (the Этап-1 skill; router-lite selects the internal branch, per C13); backlog modules remain separately, explicitly activatable per the module map (§5) — they are operations surfaces, not a second diagnosis entry.

**Этап-1 goal sentence (acceptance seed):** a PM with a signal / weak opp doc / solution idea is led to opp-r3, holding an opp doc + 1–3 confirmed candidates placeable into `docs/solution-backlog.md`.

**Eval suite (backlog):** 6 end-to-end cases — (1) raw signal, (2) solution idea without problem, (3) weak opp doc, (4) duplicate-like signal, (5) candidate → PRD, (6) initiatives pile → quarter shortlist. Cases 1–4 exercisable in Этап 1 as **M2 smoke tests; they do NOT satisfy the M2→M3 gate** (≥3 REAL docs, false-ABSENT rate checked). Connected demo case: seller price uncertainty (idea → detox → signal → weak doc → tasks → task-result intake → re-analysis).

**Wave-0 deadline (STATE.md):** first run of the user's own real signal through the opp-doc skill by **2026-07-16** (dogfood; the existential done-criterion).

## 10. Anti-goals (consolidated)

- No water-generator; no chaos acceleration.
- No tech decomposition (product decomposition only, if ever).
- No heavy context module first («богатый профиль pm» = воздушный замок).
- No contracts-as-wiki-bureaucracy; no per-block micromanagement (per-section ≠ per-paragraph; the 12 sections stand).
- No forcing all bets to be metric bets.
- No revision/invalidation log.
- No doc generation from nothing: a skeleton = empty container + white spots, never synthesized prose.
- No unsolicited solution generation: verify/tidy existing hypotheses; generate only on explicit PM request AND post-r3-gate, capped 1–3, PM-confirmed. «15 идей ради креатива» and solutions-without-parent-opportunity are named anti-outputs.
- No new infra in v1: no Python, no subagents, no JSON stores, no HTML UI (the ChatGPT "result screen" information architecture is poured into `gap-report.tmpl.md`; the HTML prototype track is quarantined outside plugin scope).
