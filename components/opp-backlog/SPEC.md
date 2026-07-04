<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# Opportunity Backlog — module SPEC (lvl1 scope contract)

> **Status: lvl1 DESIGNED.** M0 → M1 when this spec is hand-verified (orchestrator sign-off). M advances ONLY in GitHub Project #5 — never in this file, never in skill frontmatter. This spec replaces the former M0 coarse stub.
>
> **Schema ownership:** this SPEC is the SINGLE OWNER of the opp-backlog card schema. Stage-1 deliverables (opp-doc SKILL, gap-report template) and the router (Architecture lvl1) REFERENCE this schema; they never redefine it. On any divergence, this file wins.

## One-line intent

`docs/opp-backlog.md` is the DECISION QUEUE answering "which problems/opportunities deserve attention and discovery" (distinct from the solution/PRD queue) — a user-facing module realized in v1 entirely as ONE committed plain-Markdown file plus prompt-driven, manually-gated mutations.

## lvl1 scope contract

### Intent

Hold opportunity items across the FULL readiness range r0–r3 — raw signals, opportunity candidates, opportunity docs (by path), validated opportunities, parked/killed opportunities, opportunities that spawned solutions — so that nothing gets lost (backlog ≠ graveyard, no separate dump) and the router can dedupe-scan new input against it. The **r0-in-backlog rule**: a raw signal IS an item state (r0), not a pre-backlog object.

### Invariants (EARS-ubiquitous)

1. The opp backlog shall be a single committed plain-Markdown file (`docs/opp-backlog.md`) — no JSON, no table store, no database.
2. The opp backlog shall admit r0/r1 cards ONLY with an explicit `next_step` (nothing-gets-lost without turning the backlog into a dump/graveyard).
3. Critical gaps shall never block STORAGE in the opp backlog; they shall block r-TRANSITIONS and promotion only.
4. An r0-solution-signal card shall carry a problem-unknown flag; its `potential_solutions` content shall be treated as unvetted signal, never a commitment (preserves the problems-not-features invariant at the promotion boundary — the invariant applies to what may be PROMOTED, not to intake).
5. Three card facets shall never merge: readiness ⟂ workflow status ⟂ priority data (an item can be r3-but-unimportant or r1-but-strategically-urgent).
6. Priority data shall carry NO aggregate numeric score in v1 (false-precision guard); confidence is NOT a priority dimension (kept separate to avoid mixing priority with readiness). Parked future formula (unread in v1): potential = volume × severity × addressability; timing = strategic_fit × urgency.
7. All mutations of the backlog file shall be gated behind manual invocation — no auto-mutations, ever.
8. The `readiness` field shall be a DERIVED, DATED, DEMOTABLE claim (re-computed each opp-doc diagnosis pass via the r↔Q table in the model-axes addendum) — never stored machine state, never in the GitHub Project, NEVER called "maturity".

### Acceptance criteria (lvl1)

- A raw signal can be captured as an r0 card with signal + source + rough domain and a mandatory `next_step`; no doc required at r0.
- On a new duplicate-like input, the router's scan over this file surfaces similar cards with an explanation and the PM resolves merge / link / create-new as a human gate; LINK and CREATE are executed, MERGE is recommend-only at lvl1.
- A card's readiness claim can be demoted (e.g. r2 → r1 after a doc edit removed evidence) with a fresh assessment date.
- The r3 decision made in doc Section 11 — from the D-1 closed set **{kill / park / continue-discovery / generate-solutions}** — is mirrored to the card `status` (doc S11 = source, card = index; see the decision→status note in Schema notes).
- The card is updated every opp-doc pass: readiness claim, status, next_step, updated_at.

## Card schema (OWNED HERE)

```
## opp-NNN: <title>
- status: new | in_discovery | assessed | promoted | parked | killed
- readiness: r0 | r0-solution-signal | r1 | r2 | r3   (assessed <date> — derived claim, re-computed each pass, may regress)
- owner: <PM>
- doc: <path to opp-current.md, absent for r0>
- signal: <one-line raw signal>            (intent slot, part 1)
- problem: <one-line problem statement>    (intent slot, part 2; 'unknown' flag allowed only at r0-solution-signal)
- potential_solutions: [unvetted signal content or hypothesis links at r0–r2; ranked candidate ids at r3 — never a commitment]
- priority_data: volume / severity / addressability / strategic_fit / urgency  (qualitative high|med|low; NO aggregate score)
- linked_signals: [...]
- source: <origin of the triggering signal>
- target_metric_or_outcome: <name, from context metrics if present>
- next_step: <MANDATORY at r0/r1 admission (invariant 2); refreshed every opp-doc pass>
- updated_at: <date>
```

Schema notes:

- **Readiness field (D-1 note, verbatim):** the ladder is a set of NAMED MILESTONES on one dial, not strictly nested by construction (an r3 doc may hold S5 at Q2 without ever earning the r2 label; the gap report always names blocking sections, so nothing is hidden). r is derived, dated, demotable, never stored as machine state, NEVER called "maturity". r0 is assigned at card creation (pre-doc intake state, no Q derivation, per D-1); derivation via the r↔Q table in the model-axes addendum starts at r1.
- **Status enum** (card is authoritative for lifecycle): `new | in_discovery | assessed | promoted | parked | killed`. Doc S0 keeps its frozen 4-value enum (draft/assessed/promoted/archived); `killed` renders as `archived` in S0. The frozen 12-section container is NOT touched.
- **S11 decision → card status:** the r3 decision set is the D-1 closed set {kill / park / continue-discovery / generate-solutions}. Mapping: kill → `killed`, park → `parked`. TODO (open question for the orchestrator): inputs are silent on the status mirror for continue-discovery / generate-solutions — resolve with the orchestrator before build or record as spec friction; do not invent. The backlog skill never writes the doc; the `killed` → `archived` S0 rendering is performed by the opp-doc pass (doc = source, card = index).
- **priority_data lvl1 handling:** populated only from PM-supplied values (optionally elicited at create-card, never invented); no lvl1 operation updates it — the field exists for forward-compat and may stay empty.
- **ID scheme:** `opp-NNN`, unique per PM folder ONLY. Cross-PM uniqueness/dedupe is IMPOSSIBLE under the isolation model (separate folders/repos) — explicit, accepted limitation.
- **target_metric_or_outcome:** validated against the context file's metric slots IF the context file is present (read-if-present / degrade-if-absent per the context-model contract); if absent, no default is invented — the field stays as the PM named it, unvalidated.
- **Forward-compatibility:** later-lvl features (prioritization surfacing, stale detection, merge execution, shortlists, readiness views) operate on THESE fields; the schema is designed so none of them requires a schema change.
- TODO (build-session detail, not design content): exact rule for assigning the next free NNN and any file-level preamble above the first card — inputs are silent; resolve at build time with the smallest convention and record it in the SKILL.
- TODO (build-session detail, same class as the NNN rule): the schema carries no dedicated field for r0's mandatory "rough domain" (D-1: signal + source + rough domain) — inputs are silent on its slot; the least-invasive input-consistent candidate is carrying it in the card `<title>`. Pick at build time, record the convention in the SKILL, never drop the domain.

## Admission rules

- r0/r1 cards: admitted ONLY with explicit `next_step` (invariant 2).
- r0 card minimum content: signal + source + rough domain (+ next_step). No doc required.
- r0-solution-signal: admitted when a solution idea's underlying problem stays unclear after detox; carries the problem-unknown flag (`problem: unknown`); its `potential_solutions` holds the original idea as unvetted signal.
- Critical gaps (user unclear / scenario unclear / problem unclear / etc. — see the gap-severity model in the opp-doc SKILL, built at stage 1 per `docs/handoffs/stage-1-opp-doc-lvl1.md` §4.8) never block admission; they block transitions and promotion.

## Read contract for the router (dedupe-lite; consumed by Architecture lvl1)

This is a real inter-module dependency: **Architecture (router) → the opp-backlog FILE**. The router EXECUTES the similarity scan; this SPEC DEFINES the match keys and the read contract. Both specs reference the SAME match-key list (locked, D-3):

**Match keys (the searchable-fields contract):** segment, scenario, metric/outcome, problem hypothesis, source/signal type, keywords.

The router scans the match keys over card free text (title, signal, problem, source, target_metric_or_outcome, linked_signals) — segment / scenario / problem hypothesis are extracted from the one-line signal/problem/title strings by prompt scan, not from dedicated schema fields.

On every new input the router reads `docs/opp-backlog.md` and scans by the match keys. Output pattern (Russian, verbatim):

> "нашел похожие items: 1. opp-123 — похожий сегмент и метрика; 2. opp-087 — похожий сценарий. это продолжение существующей opportunity или новая?"

→ PM chooses **merge / link / create-new** (human gate). lvl1 executes **LINK** (append to `linked_signals`) and **CREATE**; **MERGE** execution (combining two cards) is deferred — lvl1 may only RECOMMEND it.

Scope: THAT PM's own folder only. Cross-PM dedupe is out of scope by the isolation model (explicit limitation).

## Write operations (lvl1 subset — ALL mutations manually gated)

1. **create card** — from router intake or an opp-doc pass, including r0 intake (admission rules above apply).
2. **update readiness claim** — dated re-assessment; DEMOTION allowed. The r value originates from the opp-doc diagnosis pass (r↔Q derivation over the doc); this operation records the dated claim on the card, it never re-scores independently.
3. **update status** — enum above; includes recording the S11 decision from the D-1 closed set {kill / park / continue-discovery / generate-solutions} at r3 — the decision lives in BOTH the doc's S11 (source) and the card status (index); decision→status mapping per the Schema notes (kill → `killed`, park → `parked`; the rest is an open TODO — do not invent).
4. **append links** — `linked_signals` / `potential_solutions` link entries.
5. **update next_step** + `updated_at` — every pass.

Deferred to a later lvl (schema stays forward-compatible): prioritization surfacing, stale-item detection, merge execution, shortlists for planning, readiness views.

## Link model

Many-to-many, carried as LINK-LIST FIELDS on cards only — no graph store:

- one signal → several opportunities;
- one opportunity ← several signals (`linked_signals`);
- one opportunity → 1–3 solution candidates (`potential_solutions` at r3);
- one candidate may close several opportunities — RESERVED EDGE, not realizable in v1: the only candidate→opportunity link is the singular `parent_opportunity` on the solution-backlog entry (per its admission invariant); activating this edge later is a declared extension, not a silent schema break;
- (reserved) bets and metrics link many items — realization (field names, which card carries them) is deliberately unnamed by the inputs; TODO at the lvl that activates planning; do not invent field names now.

## Sister file: `docs/solution-backlog.md` (write-only contract target in Этап 1)

opp-doc appends promoted candidates here at promotion; NO solution-backlog module exists yet (components/solution-backlog stays M0). The file must exist for the composability acceptance criterion. Normative interface text lives in `docs/architecture.md#Interfaces` (opp-doc → solution-doc); restated here for co-location with the backlog store convention. On any divergence between this restatement and `docs/architecture.md#Interfaces`, the architecture interface text wins (this section is a convenience mirror, not a second home):

- **Entry shape** = the canonical three-slot contract (INTENT + INVARIANTS EARS-ubiquitous + ACCEPTANCE-CRITERIA seed), with the human-readable sub-fields folded in: parent_opportunity, problem, segment, solution_hypothesis (if-then-because), target_behavior, target_outcome/metric, why_it_might_work, key_assumptions + guardrails.
- **Admission invariant (EARS-ubiquitous, from day one):** the solution backlog shall accept no entry without a parent opportunity and a product hypothesis (if-then-because shape; "не помойка идей" — a bare "сделать ai-помощника" may not enter).
- **Reserved forward-compat fields** (named, UNREAD in v1): `sol_state` (sol-s0..s2, prd-r1..r3), `bet_type` (discovery | delivery), `delivery_mode` (experiment | mvp | rollout | full_launch | test), `intent_type` (metric | strategic_learning | capability_platform | risk_quality_compliance | business_stakeholder).

## Acceptance-test seeds (M2 smoke; explicitly NOT the M3 gate)

1. **Eval case 4 — duplicate-like signal:** new signal → similar-card candidates surfaced with explanation → merge/link/create dialogue (Russian pattern above) → `linked_signals` updated OR new card created; merge only recommended. (The router's duplicate-like-signal entry is the same scenario — referenced by name, not letter; stage-1 router lettering differs.)
2. **r0 intake:** an r0 card created from a raw signal with mandatory `next_step`; creation blocked until next_step is supplied.
3. **Demotion path:** a card demoted from an r2 claim to r1 after a doc edit removed evidence — demotion proven, new assessment date recorded.
4. **Composability AC (canon):** PM-B can read PM-A's promoted `docs/solution-backlog.md` entry and act on it WITHOUT PM-A present (three-slot completeness is the demonstrated hand-off).

These are mock/smoke checks. The M2→M3 gate is separate and unchanged: real PM material, false-ABSENT rate checked (≥3 real docs for the diagnosis side).

## Explicit non-goals (lvl1)

- Prioritization ("не магически решить за продакта" — full prioritization is a later phase of its own); no aggregate score, no ranking output.
- Stale-item detection.
- Merge execution (recommend-only).
- Cross-PM dedupe (isolation model).
- Any non-Markdown store.
- Automatic mutations (all writes behind manual invocation).

## Deferred to later lvl (forward-compatible in this schema)

prioritization surfacing · stale-item detection · merge execution · shortlists for planning · readiness views · the parked priority formula (potential = volume × severity × addressability; timing = strategic_fit × urgency) · `readiness_preferences` (reserved-unread in the context contract until M4+).
