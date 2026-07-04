<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# STAGE 1 BUILD SPEC — opp-doc lvl1 (pm-flow plugin, M1 → M2)

> **Self-contained handoff.** You are a fresh build session with NO memory of the orchestrator conversation. Boot from the files below, then execute this spec top to bottom. This document SUPERSEDES `docs/sessions/oppdoc-build-brief.md` — the **orchestrator** reduces that brief to a pointer at this handoff when committing it (canon-edits pack, EDIT 13); the build session never touches `docs/sessions/`.
>
> Destination of this file: `docs/handoffs/stage-1-opp-doc-lvl1.md` in `~/Vibe/products/aipm/`.

---

## 1. Boot (read in order, before anything else)

1. `~/Vibe/products/aipm/CLAUDE.md` — project rules, language policy, non-negotiable model.
2. `~/Vibe/products/aipm/STATE.md` — current stage (Этап 1: Architecture lvl1 ∥ Opp Doc lvl1). You do NOT edit it.
3. `~/Vibe/products/aipm/docs/target-solution.md` — the reconciled target model (goal frame, entities, r-derivation, router, module map, flow, backlogs, gates, anti-goals). **If this file does not exist yet** (it lands from a parallel orchestrator task), proceed on THIS handoff — it carries the locked model content verbatim (r-table §4.7, router §4.2, scripts, card fields §9.1, context contract §9.3) — and report the absence in your hand-back (§11), same treatment as items 4–5 below.
4. `~/Vibe/products/aipm/docs/model-axes.md` — LOCKED M / Q / lvl axes, **including the r-addendum** (readiness as a derived projection of doc-level Q + decision state). If the addendum section is not yet present in the file, use the r-definition in §4.7 of THIS handoff verbatim (it is the locked wording) and note the absence in your hand-back.
5. `~/Vibe/products/aipm/docs/architecture.md` — v1 = prompt-only plugin, 6-step shared diagnosis loop, state model, interfaces. Note: it is being amended in parallel (Track A) to split `skills/backlog-manager` into `skills/opp-backlog` + `skills/solution-backlog` and to add router-lite; if the amendments are not yet in the file, THIS handoff's layout (§3, §4.12, §4.13) wins for the plugin tree. Router semantics (entry classes A–E, §4.2) are IDENTICAL between this handoff and the amended architecture.md — there is nothing to tiebreak.
6. `~/Vibe/products/aipm/components/opp-doc/SPEC.md` — the FROZEN 12-section container + per-section Q-rubric + white-spot triggers. You implement AGAINST it; you never change it.
7. `~/Vibe/products/aipm/components/opp-backlog/SPEC.md` — the SINGLE OWNER of the opp-backlog card schema; stage 1 APPENDS/UPDATES cards conforming to it (§9.1). If the file is not yet committed, the §9.1 field list (fixed by the locked decisions) is your interim contract; note the absence in your hand-back.
8. This handoff.

---

## 2. Role and what lvl1 promises (the scope contract)

You implement the **prompt-only** opp-doc skill of the `pm-flow` plugin. This moves the Opp Doc module **M1 → M2** (built into a runnable skill; not yet tested on real cases).

### 2.1 Intent (lvl1)

Lead an opportunity item from ANY entry state to **opp-r3 (decision-ready)** and, on PM confirmation, promote 1–3 solution candidates into `docs/solution-backlog.md`.

Acceptance seed (the Этап-1 goal sentence): *a PM arrives with a signal / weak opp doc / solution idea; the plugin leads them to opp-r3; the output is an opp doc + decision summary + 1–3 candidates placeable in the solution backlog.*

The doc's end state is NOT one chosen solution. It is:
1. a decision-ready opportunity;
2. an explicit recommendation in Section 11 from the closed set **{kill / park / continue-discovery / generate-solutions}**;
3. 1–3 candidates in Section 8.

Opp doc = candidate SPACE; PRD begins from the chosen candidate and is out of scope.

### 2.2 Invariants

- The plugin is NOT a document generator: it moves the work item to its next meaningful decision; the doc is a rendering of item state. It never starts by writing — diagnose first.
- Container discipline: map the PM's material, never backfill; a skeleton is ALWAYS the empty 12-section container + marked white spots, never synthesized prose.
- Stateless: each pass re-reads the doc from the PM-supplied path; no memory of prior runs; nothing written to CLAUDE.md.
- Readiness (r) is derived, dated, demotable — never stored as machine state, NEVER called "maturity" (that word is reserved for M).
- All quality checks are ADVISORY during drafting; the ONLY hard gate is at promotion into `docs/solution-backlog.md`.
- PM-facing output is Russian; the doc keeps the PM's own wording.

### 2.3 Acceptance criteria

The done-criteria in §7 plus the smoke tests in §8 pass end-to-end, prompt-only, via one user-facing invocation.

### 2.4 Hard non-PRD boundary

The opp doc must NOT contain: detailed solution description, UX mockups, acceptance criteria for delivery, architecture, experiment economics, roadmap/sprint plan, full solution success metrics. Allowed: high-level affected metrics + relevance. The skill enforces this boundary via the §4.6 non-slop writing checks («no delivery language», «no PRD language») for in-doc content, plus quality check 10 («PRD straight from an idea») for the workflow path.

---

## 3. Plugin home and layout

Build at **`~/.claude/local-plugins/pm-flow/`** (global, per vault global-plugin policy — dogfoodable after registration + restart, see below). Distribution/packaging for Avito is a LATER decision; do not solve it. If you disagree with the location, raise it with the orchestrator before building.

**Registration (per the global local-plugins policy in `~/.claude/CLAUDE.md`):** a local plugin needs `.claude-plugin/marketplace.json` alongside `plugin.json` (versions ALWAYS in sync), registration via `claude plugin update "pm-flow@<marketplace-name>"`, an `enabledPlugins` entry, and a Claude Code RESTART before the skill appears. Consequence: **the newly built skill cannot be live-invoked inside the build session itself** — live invocation (`/pm-flow:opp-doc`) is verified by the user/orchestrator after restart; the build session verifies behavior by prompt-simulation (§8 execution method).

Standard plugin layout:

```
~/.claude/local-plugins/pm-flow/
  .claude-plugin/
    plugin.json                      ← manifest
    marketplace.json                 ← local-plugins convention, version-synced
  skills/
    opp-doc/
      SKILL.md                       ← the ONE active skill (this spec, §4.1–4.8)
      references/
        opp-doc-spec.md              ← frozen 12-section container (§4.10)
        opp-doc-rubric.md            ← frozen Q-rubric + white-spot triggers (§4.10)
        gap-report.tmpl.md           ← report template with the refined IA (§4.11)
    opp-backlog/SKILL.md             ← M0 stub (§4.12)
    solution-doc/SKILL.md            ← M0 stub
    solution-backlog/SKILL.md       ← M0 stub
    planning/SKILL.md                ← M0 stub
    context-collection/SKILL.md      ← M0 stub
```

Note: this layout follows `components/` (two separate backlog modules), not architecture.md's older single `backlog-manager` stub — the split is an approved architecture amendment (Track A applies it to the doc).

---

## 4. Deliverables and their content specs

### 4.1 skills/opp-doc/SKILL.md — one user-facing entry

Lean body (~1500–2000 words, per architecture.md), PROMPT-ONLY. Frontmatter contract (concrete — no other trigger mechanism exists): `name: opp-doc` (registers as `/pm-flow:opp-doc`); `description:` carrying the auto-invocation trigger phrases ('signal received', 'opportunity doc', 'map my discovery' — carry over from architecture.md; Russian equivalents at builder's choice) — in Claude Code plugin skills, auto-invocation matching is driven by the description text, there is NO separate `triggers:` key; `argument-hint: [doc-path]` — the PM supplies the path to their plain-Markdown material/doc.

Points at `references/`, inlines none of the frozen artifacts. To keep the body inside the word budget, you MAY author additional non-frozen reference files (e.g. `references/modes-and-checks.md`, `references/task-schema.md`) that the body points to: the mode desired/anti lists, the 10+9 check lists, and worked examples may move out of the body; branch selection (§4.2), the r-table + gate logic (§4.7), and the mutation gate MUST stay inline.

**Mutation gate (the concrete prompt-level mechanism):** before ANY write to the PM's doc or the backlog files, the skill presents the intended change and obtains explicit PM confirmation in-dialogue; auto-triggered passes are read/diagnose-only until that confirmation. This is how "mutations gated behind manual invocation" is implemented in a prompt-only skill — never auto-clobber carried state.

ONE invocation surface runs the whole pass. Internally the skill first runs **router-lite branch selection** (§4.2), then the branch, then the shared closing steps (readiness derivation §4.7, gap report §4.11, card update §4.8, doc write-back).

The persona frame (prompt preamble): product buddy / critic of thinking / structuring helper / readiness navigator / discipline guard — never a micromanager, never merely a reviewer. Motto: «не ускорять хаос, а возвращать продакта к дисциплине».

### 4.2 Router-lite branch selection (inside SKILL.md)

Before ANY action, run the **pre-action intake protocol** (8 questions, answered internally, surfaced in the report): what did the user bring; which entity (opportunity vs solution vs plan-level); duplicate in backlog?; current readiness; next meaningful step; what's missing; what can AI do; what must the PM confirm. This intake realizes transition gate **c1** (raw input → classified entry) of the target model. Question 3 (duplicate?) is answered by running the dedupe-lite scan (below) at intake for **new-item entries** — A, C, E, and B when the doc is not yet carded; it is **skipped for D and repeat passes**, where the item is already identified by its card.

Then classify the input into one of five classes and run that branch:

- **A — raw signal**: separate fact from interpretation; propose problem hypotheses + affected segments + validation questions; dedupe scan (below); assemble an **r1 SKELETON** — empty container sections + mapped fragments only, NO generated prose. Output: r1 draft, hypotheses, validation questions, dedupe/link suggestions, next tasks.
- **B — weak opp doc**: the canon **6-step diagnosis loop unchanged** (per docs/architecture.md): load frozen artifacts → MAP fragments by the QUESTION each answers → quote-check inline (every mapped claim carries a verbatim quote; unfound quote → drop claim, cap section Q) → score Q per section (one criterion at a time, length-neutral; multi-construct rungs split per the rubric's machine-facing note) → detect white-spots ABSENT vs AMBIGUOUS (grounded scan only, never parametric belief) → capped Socratic elicitation → report + write. MAP-step aid (the documented field→section mapping from the reconciled model, C4 — a mapping aid for field-shaped input, NOT a schema change): `problem_hypotheses→S1, segments→S3, metric→S4, evidence→S5, sizing/confidence→S6, candidates→S8, unknowns→S9, recommendation→S11, owner/status/source→S0`. Output: readiness assessment, gaps, restructured doc (PM's own wording only), tasks for r2/r3.
- **C — solution idea → detox** (§4.3).
- **D — existing backlog item**: read card + doc; derive readiness; name what's missing for the next rung; propose continuation workflow.
- **E — duplicate-like signal**: similarity scan over `docs/opp-backlog.md` by the match keys (below); explain the similarity; then the human gate **merge / link / create-new**. LINK (append to the matched card's `linked_signals[]`) and CREATE are executed; MERGE is recommend-only at lvl1 (D-3 / the opp-backlog SPEC read contract — never execute a merge).

(Task-result intake is NOT an entry class — it is the **repeat-pass flow**, §4.4, triggered when a D/B invocation brings a new task result.)

The 15-step canonical flow behind these branches (from the target model — a MENTAL MAP, enter anywhere, NEVER a step-script; respects the no-micromanagement constraint): capture signal → classify input → check duplicates → frame problem hypothesis → segment+scenario → current vs desired behavior → connect to metric/outcome/intent → validation questions → plan evidence checks → review evidence → alternative explanations → impact+confidence → decision-ready opportunity → (on PM request) 1–3 candidates → push candidates to solution backlog. The model infers known-vs-missing on entry; stateless re-read each pass.

**Dedupe-lite step** (at intake for A, C, E, and uncarded B): a prompt scan over THAT PM's own `docs/opp-backlog.md` by the match keys **segment, scenario, metric/outcome, problem hypothesis, source/signal type, keywords** (this exact key list is owned by the opp-backlog SPEC's read contract — do not invent others). Scope: the PM's own folder ONLY; cross-PM dedupe is explicitly out of scope (isolation model) — state this limitation in the skill. On a match, the dialogue depends on what the PM brought:

- **Solution-idea match (entry C)** — canonical dialogue, Russian, verbatim:

  > «похоже, ты пришел с solution idea. я нашел похожую opportunity: opp-123 про активацию новых продавцов. (a) привязать как solution candidate к opp-123 (b) создать новую opportunity (c) пройти solution detox»

- **Signal-vs-signal match (entries A, E)** — the read-contract pattern, Russian, verbatim:

  > «нашел похожие items: 1. opp-123 — похожий сегмент и метрика; 2. opp-087 — похожий сценарий. это продолжение существующей opportunity или новая?»

  → PM chooses merge / link / create-new; on LINK, append to the matched card's `linked_signals[]`; MERGE is only recommended.

Both choices are a HUMAN GATE — always the PM's call.

### 4.3 Solution-idea detox (entry C)

Goal: «не дать фиче притвориться проблемой». The plugin does not forbid the idea — it walks back with the detox questions (Russian, verbatim):

> какую проблему решаем? для кого? в каком сценарии? какое поведение хотим изменить? какую метрику/outcome сдвинуть? какие альтернативные решения есть? есть ли похожая opportunity в backlog?

Result: the idea is DEMOTED to ONE solution candidate attached to a recovered or new opportunity — «исходная идея становится solution candidate, а не истиной». Detox ALWAYS records the original idea as one candidate. If the problem stays unclear → save as an **opp-r0 `r0-solution-signal` card** (problem-unknown flag) in `docs/opp-backlog.md`. There is NO path from a bare idea to the solution backlog.

### 4.4 Task-result intake — the repeat-pass flow (mandatory re-analysis + DIFF)

Not an entry class: this flow fires whenever an invocation (typically entry D or B) brings a completed task result. The gap-resolution loop is the heart of the module:

```
gap analysis → tasks → offline work → task-result intake → doc update
  → gap analysis AGAIN (mandatory, NEVER skip) → readiness re-derived → DIFF report
```

After a task result the skill may NOT proceed directly: it updates the doc, re-runs the full diagnosis (stateless re-read), re-derives r (which MAY demote), and emits a **DIFF report**: what changed / which gaps closed / which NEW gaps appeared / updated backlog card. DIFF reports use the same `opp-report-<n>.md` audit-trail convention as first-pass reports.

### 4.5 Refusal UX (never hard-block, never pretend chaos is mature)

On «напиши prd» (or any premature-generation request) the skill diagnoses first, then offers a menu:
- **(a)** пройти detox;
- **(b)** fast-track, explicitly marked as a **low-confidence bet** with the risks listed. Russian script verbatim: «можно продолжить fast-track, но я помечаю это как low-confidence bet: parent opportunity не подтверждена; target behavior не сформулирован; success metric не определен.» (adapt the listed unconfirmed items to the actual diagnosis);
- **(c)** a skeleton with a low-readiness warning.

Options (b)/(c) produce ONLY the empty 12-section container + marked white spots + explicit warning — never synthesized prose. Two-tier enforcement: everything during drafting is ADVISORY; the conjunctive-Q2 gate at PROMOTION is HARD — a low-confidence bet may live in the opp backlog but may NOT enter `docs/solution-backlog.md`.

Missing-context refusal script (anti-bullshit, verbatim): «мне не хватает контекста, чтобы нормально оценить opportunity. минимально нужно уточнить: сегмент, сценарий, метрику/outcome и источники evidence.»

### 4.6 Claim discipline + quality checks (inline prompt instructions)

**Claim discipline:** every claim in the doc is classified as exactly one of **fact / assumption / unknown** (fact requires Q3-grade evidence; explicit assumption ≈ Q2; unknown → white spot). The claim map renders as a short summary + warnings in the report — never a giant table. The plugin must not: invent facts; write confidently without evidence; inflate weak evidence; paper over unknowns.

**10 quality checks** (advisory during drafting, re-discipline don't hard-block): (1) problem formulated as a feature; (2) no segment; (3) no scenario; (4) no behavior/metric link; (5) weak/absent evidence; (6) impact claimed not grounded; (7) no alternative explanations; (8) candidates don't follow from the opportunity; (9) duplicate creation; (10) PRD straight from an idea.

**9 non-slop writing checks** (applied to any text the skill emits/restructures): concrete user; concrete scenario; concrete problem; no «улучшение опыта» without a named behavior; no unlabeled claims; no delivery language; no PRD language; short tl;dr; gaps not hidden. Acceptance bar: «документ читается как рабочая записка pm, а не как ai-generated corporate soup».

**Elicitation calibration — 9 universal questions** (domain-independent, Russian verbatim, used when generating targeted questions): кто затронут? в каком сценарии? что идёт не так? как мы это видим? какой объём? какая часть addressable? почему это важно? что мы пока не знаем? что можно попробовать сделать? Domain metric sets (marketplace / jobs / automated support / antifraud) are CONTEXT-FILE content, not skill logic — do not embed them in the prompt.

**Specialist behavioral MODES** (prompt guardrails, NOT subagents — name them in SKILL.md as the designated future subagent seam, deferred-infra). Frame per mode: role / goal / desired output / anti-output / errors caught / human gates («не микроменеджить сильные модели» — no 40 micro-steps):

1. **signal interpreter** (entry A) — wants: fact-vs-interpretation split, hypotheses, segments, metrics, validation questions, create/merge/ignore suggestion. Anti: confident conclusion without evidence; ready-made solution; feature-as-problem; ignoring similar items.
2. **solution idea detoxer** (entry C) — wants: problem hypothesis, segment, scenario, target behavior, metric, original idea as candidate, alternatives. Anti: PRD from air; confident «фича нужна»; stretching a problem onto a pet solution; ignoring similar opportunities.
3. **opp doc reviewer** (entries B/D + task-result repeat passes) — wants: readiness, weak/missing/unclear areas, unsupported claims, alt explanations, tasks, continue/park/kill/generate recommendation. Anti: pretty rewrite only; «все хорошо»; style-only critique; per-paragraph micromanagement.
4. **candidate generator** (PM-request-only, post-r3-gate) — wants: if-then-because hypotheses, target behavior, metric link, why-it-might-work, assumptions, risks, mvp hint. Anti: random features; no parent opportunity; «15 идей ради креатива»; ignoring constraints.

**Candidate generation policy (STRICT merge — locked):** verify/tidy the PM's existing hypotheses ALWAYS. GENERATE new candidates only on explicit PM request AND after the r3 gate, grounded in the opportunity, capped 1–3, PM-confirmed before promotion.

### 4.7 Readiness (r) derivation — the LOCKED table

r = work-item READINESS, a derived, dated, demotable projection of the doc's Q profile + decision state. NEVER call it "maturity" anywhere (maturity is reserved for M). Re-derived every pass via the frozen rubric; never stored as machine state; the backlog card caches it only as a DATED CLAIM (`readiness: r2 (assessed 2026-07-04)`), which a later pass may DEMOTE.

| r | name | derivation over the 12-section container |
|---|---|---|
| **opp-r0** | raw signal | pre-doc intake state: card exists with signal + source + rough domain; no doc required. No Q derivation. Variant `r0-solution-signal` carries a problem-unknown flag. |
| **opp-r1** | framed | framing sections S1 Problem, S2 Strategic fit, S3 Segment, S4 Success metrics each ≥ Q2 |
| **opp-r2** | evidence-backed | r1 AND evidence sections S5 Evidence, S6 Sizing each ≥ Q3, alternative explanations addressed |
| **opp-r3** | decision-ready | doc-level conjunctive gate ≥ Q2 on the mandatory set (0,1,2,3,4,5,6,8,9,11) AND S11 carries an explicit decision from the closed set {kill / park / continue-discovery / generate-solutions} AND S8 holds 1–3 candidates. **Identical to the existing promotion gate — the gate is NOT tightened.** |

**S8 reconciliation note (read before implementing the r3 row / promotion — do not skip):** «S8 holds 1–3 candidates» in the locked D-1 row is the cap on candidates SELECTED for promotion (D-5), NOT S8's content count. The frozen rubric stays the scoring authority for S8: its Q2 rung requires 3+ genuinely distinct options CONSIDERED (a single option is a hard white-spot flag; the frozen SPEC's promotion prose speaks of ≥2 ranked options and promoting the top-ranked ones). Read the two together as: options considered — per the rubric; candidates promoted — 1–3. If a concrete case still pits the two locked sources against each other (e.g. a doc with 2 considered options claiming r3), do NOT resolve silently and do NOT alter the locked table text: implement the SPEC/rubric as written and record the friction under Spec-friction (§11).

These r-transitions realize the target model's transition gates: signal→r1 = **c2**, r1→r2 = **c3**, r2→r3 = **c4** (intake = c1, §4.2; promotion = c5, §4.9). c6–c10 are reserved names — undefined, lazy fractal, out of scope. Gates are behavior frames, not step-scripts.

Include this note in the skill/report logic verbatim in spirit: the ladder is a set of NAMED MILESTONES on one dial, not strictly nested by construction — an r3 doc may hold S5 at Q2 without ever earning the r2 label; the gap report always names the blocking sections, so nothing is hidden.

Rules the skill enforces:
- readiness ≠ filled block: «сегмент = все пользователи авито» stays Q1 and cannot fake r.
- readiness ≠ priority ≠ workflow status (three separate card facets, never merged).
- Never per-paragraph statuses; never downstream invalidation; no revision log.

Report phrasing template (Russian, the shape to follow): «похоже на opp-r1, но не opp-r2: есть гипотеза проблемы; есть сегмент; но нет evidence; impact не обоснован; альтернативные объяснения не проверены.»

### 4.8 Gap model, task schema, backlog writes

**Gap severity:** **critical** (blocks an r-transition and promotion — canonical list: user unclear; scenario unclear; problem unclear; solution without opportunity; no evidence at all; no rough sizing for r2; no decomposition for a broad opportunity; no addressability understanding; no parent component for a hypothesis) / **major** (lowers confidence, doesn't block) / **minor**. Rule: critical gaps NEVER block storage in the opp backlog — only transitions.

**Every emitted task — 5-field schema:** `task / role / why needed / acceptance criteria / linked gap`. Roles: **pm** | **evidence** (= canon 'analyst') | **rewrite-edit** (executed by the PM with skill assistance, gated behind explicit invocation). `why needed` is phrased as WHICH r-transition it unblocks. Worked example (include in SKILL.md or template as the reference shape): task «оценить rough affected volume»; role: evidence; why: «без rough sizing opportunity не может перейти r1→r2»; AC: «диапазон affected volume за месяц + источник + confidence low/med/high»; linked gap: «нет sizing».

**Backlog writes (each pass, mutation-gated):**
- `docs/opp-backlog.md` — append a new card or update the existing one: readiness claim (dated), `status`, `next_step`, `updated_at` — every pass (see §9.1 for the card contract; use the SPEC's exact field names).
- `docs/solution-backlog.md` — append ONLY at promotion (§4.9).

**Context-file read** — per the contract in §9.3, at pass start, read-if-present / degrade-if-absent.

**Outputs per pass (minimal set — the skill emits exactly these, as applicable):** (1) updated opp doc (PM wording, re-structured); (2) readiness assessment + why; (3) gaps (ABSENT/AMBIGUOUS, severity); (4) validation tasks (5-field, routed); (5) decision summary at r3 (kill/park/continue-discovery/generate-solutions); (6) 1–3 candidates on request post-gate; (7) opp-backlog card append/update; (8) solution-backlog append at promotion.

### 4.9 Candidate working card (S8 drafting shape) + promotion transform

**Working card fields** (the human-readable drafting shape inside Section 8; field list verbatim from the reconciled inputs — the ChatGPT working-card shape per resolution C8, plus `guardrails` added by that resolution): `solution_id, parent_opp_id, name, problem, segment, scenario, solution_hypothesis, target_behavior, target_metric_or_outcome, why_it_might_work, main_assumptions, expected_effect, confidence, risks, guardrails, mvp_hint, status`.

`solution_hypothesis` MUST have the if-then-because shape. Bad: «сделать ai-помощника». Good: «если мы добавим inline-подсказки…, то повысим first successful listing rate, потому что…».

`guardrails` is seeded from S4 counter-metrics + S9 constraints — it exists specifically to feed the INVARIANTS slot below.

**Promotion = transition gate c5** (HARD gate: doc-level conjunctive ≥ Q2 on the mandatory set — see the §4.7 S8 reconciliation note — + PM confirmation per candidate; cap 1–3 candidates, never more). Each confirmed candidate is TRANSFORMED into the canonical three-slot contract and appended to `docs/solution-backlog.md`:
- **INTENT** ← parent opp + segment + target_behavior + metric + expected mechanism ('after this ships, [outcome/metric] holds for [segment]').
- **INVARIANTS** ← guardrails (S4 counter-metrics + S9 constraints), expressed EARS-ubiquitous ('The <system> shall <always-true property>').
- **AC SEED** ← riskiest assumption + expected effect + before-PRD tasks, EARS-stubbed ('If <trigger> then the <system> shall <response>' / 'When <trigger> the <system> shall <response>').

**Folded sub-fields (mandatory, per the opp-backlog SPEC's sister-file contract):** alongside the three slots, the appended entry carries the human-readable sub-fields folded in — `parent_opportunity, problem, segment, solution_hypothesis` (the if-then-because line, VERBATIM from the working card), `target_behavior, target_outcome/metric, why_it_might_work, key_assumptions + guardrails`. This is what makes the §9.2 admission invariant (parent opportunity + if-then-because hypothesis) checkable from the entry itself, without the opp doc or its author present (composability AC).

In the same step: opp-backlog card status → `promoted`; doc S0 status updated.

### 4.10 references/opp-doc-spec.md and references/opp-doc-rubric.md

- `opp-doc-spec.md` — the frozen 12-section container, transcribed faithfully from `components/opp-doc/SPEC.md` (sections 0–11, what each answers, mandatory/optional marking, pour-in rules). No edits, no additions.
- `opp-doc-rubric.md` — the per-section Q0–Q4 rungs + white-spot triggers from the same SPEC, plus: the length-neutrality clause; the machine-facing note that multi-construct rungs (e.g. S8 Q2 'distinct+traced+compared+ranked') are split into separate one-criterion-one-failure-mode checklist items when scored; the GLOBAL ABSENT/AMBIGUOUS rule. Hand-authored copy of the frozen M1 map — never regenerated at runtime.

If, while transcribing, you find the SPEC ambiguous or contradictory — do NOT resolve it silently; record it under Spec-friction (§11).

### 4.11 references/gap-report.tmpl.md — refined information architecture

The report template (PM-facing strings Russian). Structure, in order:

**TOP SUMMARY:** readiness (r + WHY, using the §4.7 phrasing shape) / workflow status / scenario / main diagnosis / **NEXT STEP** (the single primary CTA) / priority data needed.

**BODY:**
1. What mapped successfully — FIRST, always (canon anti-slop UX; never a bare ABSENT badge-wall).
2. Per-section Q badges + the doc-level conjunctive gate (min of mandatory sections; the compensatory average only as secondary '% toward next gate').
3. Ranked white-spots, each phrased as ONE targeted question routed pm-vs-evidence (ABSENT vs AMBIGUOUS marked; capped count).
4. Tasks (5-field schema).
5. Claim warnings (summary form).
6. The opp-backlog card (as appended/updated).

**The report must answer 8 questions:** what do I have / what readiness / WHY this readiness / what blocks the next transition / which tasks / what improved in the doc / backlog-ready? / next step.

**State-dependent primary CTA** (the 'next step' logic): r0 + unclear → answer elicitation questions; r1 + critical gaps → create tasks; waiting on tasks → add task result; after a result → update doc; r2/r3 → package backlog card + (r3) promote candidates.

**Repeat passes** (task-result intake, §4.4) emit the DIFF shape: what changed / closed gaps / NEW gaps / updated card.

### 4.12 M0 stubs (far skills)

Each = frontmatter + one-paragraph coarse stub, ~100 tokens, NOT designed:
- `skills/opp-backlog/SKILL.md` — store of problems/outcomes (`docs/opp-backlog.md`), intake/dedupe-read-contract/status ops. **Note in the stub: Этап 2 fleshes this module out to lvl1; the card schema is owned by `components/opp-backlog/SPEC.md` (see §9.1).**
- `skills/solution-backlog/SKILL.md` — store of promoted candidates with the three-slot contract; `docs/solution-backlog.md` is already a write-only contract target in Этап 1.
- `skills/solution-doc/SKILL.md` — reuses the same diagnosis reference shape when activated; target output = PRD; reserved vocabulary sol-s0..s2 / prd-r1..r3 (named, undefined).
- `skills/planning/SKILL.md` — decompose/sequence over consumed inputs; reserved vocabulary: discovery/delivery bet, delivery_mode, 5 intent types; "planning schedules movement of items up the readiness ladder, not tasks".
- `skills/context-collection/SKILL.md` — will PRODUCE the context file per the context-file contract whose single durable home is `docs/architecture.md#Interfaces` (context-collection → opp-doc entry; §9.3 below is a verbatim copy of it — the stub must reference the durable home, not this handoff); real module built LAST.

### 4.13 .claude-plugin/ manifests

`plugin.json` — minimal valid manifest (name `pm-flow`, version, description). `marketplace.json` — per the vault local-plugins convention, version ALWAYS in sync with plugin.json (§3 registration). Nothing else in `.claude-plugin/`.

---

## 5. Step plan

1. Boot (§1). Verify `docs/target-solution.md` and the frozen SPECs exist; note any missing prerequisite.
2. Scaffold the plugin tree (§3) + `plugin.json` + `marketplace.json` (version-synced).
3. Register the plugin per the global local-plugins policy (§3): `claude plugin update "pm-flow@<marketplace-name>"`; note in the hand-back that a Claude Code RESTART is required before live invocation — the user/orchestrator verifies `/pm-flow:opp-doc` after restart. If registration is blocked, say so in the hand-back; it does not block the remaining steps.
4. Transcribe the frozen artifacts into `references/opp-doc-spec.md` + `references/opp-doc-rubric.md` (§4.10).
5. Write `references/gap-report.tmpl.md` (§4.11).
6. Write `skills/opp-doc/SKILL.md` (§4.1–4.9): persona + intake protocol + router-lite branches A–E + 6-step loop + detox + refusal UX + claim discipline + modes + r table + task schema + candidate card + promotion transform + context read + backlog writes.
7. Write the five M0 stubs (§4.12).
8. Author minimal mock fixtures in a scratch folder (LABELED as mocks): a hand-authored `context.md` per the §9.3 schema stub; an empty-but-headed `opp-backlog.md` and `solution-backlog.md`; sample inputs for the smoke tests (§8), including the seller-price-uncertainty demo material.
9. Run the smoke tests (§8) via the prompt-simulation execution method defined there; fix rough edges in the prompt.
10. Hand back per §11.

---

## 6. Hard guardrails

- **v1 is PROMPT-ONLY.** No Python engine, no subagents, no infra, no JSON stores, no structured-output requirement. State = plain Markdown files at PM-supplied paths. All deferred-infra items (Python parse/score, deterministic quote-verify, subagent fork, workflow-registry YAML, subagent specialist split) stay in the architecture backlog — add NOTHING from it.
- **Container discipline / no backfill.** Map, never generate prose to fill a gap; an empty section is Q0 ABSENT + a targeted question; skeletons = empty container + white spots only.
- **Mutations behind manual invocation.** The skill never auto-writes the PM's doc or the backlog files without the explicit invocation gate.
- **Report leads with what mapped.** Never a bare ABSENT badge-wall; ABSENT only from a grounded scan of the PM's actual material, never from parametric belief («docs like this usually lack X» is forbidden).
- **No "maturity" wording for work items.** Only "readiness (r)". Derived phrases: readiness assessment, readiness milestones.
- **Language:** SKILL.md instruction layer in English; ALL PM-facing strings (detox questions, dedupe dialogue, refusal scripts, low-confidence-bet marking, report phrasings, kill/park/continue-discovery/generate-solutions labels) in Russian, verbatim as given in this handoff. Provenance: every «verbatim» Russian string and every enumerated list here (10 quality checks, 9 non-slop checks, 9 elicitation questions, critical-gap list, 8 report questions, working-card fields) is a verbatim copy from the reconciled ChatGPT-source inputs behind `docs/target-solution.md` — locked copy, not drafter invention; do not re-invent or translate them.
- **Frozen artifacts are frozen.** You implement against `components/opp-doc/SPEC.md`; propose changes only via Spec-friction (§11), never edit.
- **Do not touch:** `STATE.md`, `components/*`, `docs/model-axes.md`, `docs/architecture.md`, `docs/target-solution.md`, `docs/sessions/*` (orchestrator-owned), the ingest examples. You OWN only the plugin tree + your scratch fixtures. NOTE the path-base rule in §9: the `docs/…` interface paths there are PM-workspace paths, NOT these aipm-repo files.
- **Read-never inputs:** `docs/architecture/` and `docs/opportunity-doc-plugin/` (the committed ChatGPT source digests) are SUPERSEDED source material — never boot from or cite them; the reconciled canon is `docs/target-solution.md` + this handoff, and on any conflict those win.

---

## 7. Done-criteria (M2)

- The skill runs the whole pass end-to-end (read → classify → map → quote-check → score → white-spots → elicit → report → write doc + card) against the frozen artifacts on a sample doc, prompt-only, via one invocation surface. In the build session this is verified by the §8 prompt-simulation method; live invocation via `/pm-flow:opp-doc` is verified by the user/orchestrator after registration + restart (§3).
- Each acceptance smoke test in §8 is runnable (per the §8 execution method) and passes its stated checks.
- Far-skill M0 stubs present at ~100 tokens each.
- `references/` artifacts are faithful transcriptions of the frozen SPEC (no silent edits).

---

## 8. Acceptance smoke tests

> **These are M2 smoke tests on MOCK fixtures. They explicitly do NOT satisfy the M2→M3 gate, which requires ≥3 REAL PM docs with the white-spot detector's false-ABSENT rate checked.** State this in your hand-back.
>
> **Execution method (M2, build session):** a newly created skill is NOT live-invocable in the session that creates it (registration + Claude Code restart required, §3). Run each smoke test by **prompt-simulation**: load the SKILL.md content and follow it literally against the fixtures, recording the transcript as evidence. State in the hand-back that the tests were simulated and that live-invocation verification happens after restart — never report a simulated pass as a live pass.

- **CASE 1 — raw signal (entry A):** a raw signal in → r1 skeleton + hypotheses + validation plan out; iterate to an r2/r3 draft (see the §4.7 S8 reconciliation note before asserting r3). Check: no generated prose in empty sections; dedupe scan ran; card appended (to the backlog path declared in context.md or elicited per §9.3) with dated readiness + mandatory `next_step`.
- **CASE 2 — solution-idea detox (entry C):** input «давайте сделаем ai-помощника» → detox questions (verbatim) → problem hypothesis → r1 + the original idea recorded as ONE candidate. Check: idea demoted, not promoted; if problem unclear the fallback is an r0-solution-signal card.
- **CASE 3 — weak opp doc (entry B):** readiness assessment → gaps (ABSENT/AMBIGUOUS, severity) → improvement plan (5-field tasks) → restructured doc in the PM's own wording. Check: report leads with what mapped; conjunctive gate named the lowest section.
- **CASE 4 — duplicate-like signal (entry E, eval case 4):** a new signal similar to a seeded card → scan surfaces similar cards with an explanation using the verbatim pattern («нашел похожие items…», §4.2) → PM chooses merge / link / create-new. Check: LINK updates the matched card's `linked_signals[]`; CREATE makes a new card; MERGE only recommended, never executed.
- **CONNECTED DEMO — seller price uncertainty:** «нужно сделать рекомендованную цену» → detox → signal «продавцы не понимают, какую цену поставить» → weak doc → tasks → an evidence task-result fed back (repeat pass, §4.4) → re-analysis with recalculated readiness + DIFF report. Check: gap analysis re-ran after the result (never skipped); r re-derived (demote path possible).
- **CONTEXT-ABSENT DEGRADATION:** run any case with no `context.md` / missing `key_metric`. Check: no invented defaults; absence becomes a white spot (hard S4 white-spot for key_metric/counter_metrics; S2 objective-link white-spot for yearly_goals; AMBIGUOUS elicitation for recommended fields); with the file absent, the skill ELICITS the backlog file paths from the PM before any backlog read/write (the test supplies the fixture paths through that elicitation — this is how the card-append checks stay satisfiable) and never invents a path; the missing-context refusal script fires verbatim when critical per the §9.3 definition.
- **PROMOTION-GATE REFUSAL + PASS:** attempt promotion below the conjunctive Q2 gate (or via «напиши prd» on a weak doc). Check: refusal menu (a)/(b)/(c) offered; fast-track marked low-confidence bet verbatim; NOTHING appended to `docs/solution-backlog.md`; a flagged bet may still live in the opp backlog. Then, on a fixture doc that clears the gate, promote ONE confirmed candidate. Check: the appended entry carries the three slots AND the folded sub-fields (§4.9), including the parent-opportunity reference and the if-then-because `solution_hypothesis` line verbatim-checkably.

---

## 9. Interfaces this build must respect (exact paths + shapes)

**Path base (normative):** every `docs/…` path in this section is relative to the **PM's own working folder** (architecture.md state model: "whatever folder the PM uses"), resolved via the invocation argument and the context file's `backlog_locations` — NEVER the aipm repo (whose `docs/` is orchestrator-owned and untouchable per §6) and never the plugin dir. During smoke tests these files live in your scratch fixtures folder.

### 9.1 `docs/opp-backlog.md` — opportunity cards (append/update only)

**Schema owner: `components/opp-backlog/SPEC.md`** (boot item 7). The stage-2 handoff (`docs/handoffs/stage-2-opp-backlog-lvl1.md`) implements that schema; it never owns it. Stage 1 only APPENDS/UPDATES cards conforming to the owner schema. Fields fixed by the locked decisions (use these; anything more is the SPEC's call):
- `id`; `readiness` — DATED claim, e.g. `r2 (assessed 2026-07-04)`, demotable; `r0-solution-signal` variant carries the problem-unknown flag;
- `status` — `new | in_discovery | assessed | promoted | parked | killed` (card is authoritative for lifecycle; doc S0 keeps its frozen 4-value enum; `killed` renders as `archived` in S0);
- `next_step` — MANDATORY for r0/r1 cards (no dump-without-graveyard);
- link-list fields: `linked_signals[]`, `potential_solutions` (solution-candidate ids / unvetted signal content — the opp card carries NO `parent_opp` field; `parent_opportunity` lives only on solution-backlog entries, §9.2); match-key content (segment, scenario, metric/outcome, problem hypothesis, source/signal type, keywords) readable for the dedupe scan;
- `updated_at` — refreshed on EVERY pass that touches the card (the SPEC requires it; stage-2 operations act on it);
- readiness ≠ priority ≠ status: three separate facets, never merged.
- r0 cards ARE admitted (critical gaps block transitions, never storage); `potential solutions` on a card = unvetted signal content / hypothesis links, never a commitment.

### 9.2 `docs/solution-backlog.md` — three-slot entries (append at promotion only)

Write-only contract target in Этап 1 (no consumer module yet; the file must exist for the composability acceptance criterion). Each entry = the three-slot contract (INTENT / INVARIANTS EARS-ubiquitous / AC SEED EARS-stubbed) per §4.9, **plus the folded human-readable sub-fields** (§4.9): `parent_opportunity, problem, segment, solution_hypothesis` (if-then-because, verbatim), `target_behavior, target_outcome/metric, why_it_might_work, key_assumptions + guardrails`. **Admission invariant (EARS-ubiquitous, from day one): the solution backlog shall accept no entry without a parent opportunity and an if-then-because product hypothesis** — checkable directly from the entry's `parent_opportunity` + `solution_hypothesis` sub-fields. Markdown only.

### 9.3 `docs/context.md` — the context-file contract (read-if-present / degrade-if-absent)

**Provenance + single home:** this section is a VERBATIM COPY of the context-file contract whose single durable home is `docs/architecture.md#Interfaces` (context-collection → opp-doc entry, applied by the Track-A canon-edits pack). Slot vocabulary = the union of the ChatGPT context field lists, deduplicated in the reconciliation (aliases from the same dedup: `main_metric` ≡ key_metric, `guardrail_metrics` ≡ counter-metrics, `current_goals` ≡ yearly goals); canon added `backlog_locations`. The contract is FIXED per the locked decisions — do not extend or rename slots here; on any divergence the architecture.md copy wins.

ONE plain-Markdown file at a PM-supplied path, sectioned; produced by hand today (labeled mock when used as a fixture), by the context-collection module later. Schema stub:

```markdown
# PM Context — <owner>
## Core (mandatory — canon 4)
- yearly_goals / current_goals: ...
- key_metric (main_metric): ...
- counter_metrics (guardrail_metrics): ...
- backlog_locations: docs/opp-backlog.md, docs/solution-backlog.md
## Product (optional named slots)
- product_area, team, pm_level, user_segments, core_scenarios,
  input_metrics, strategic_context, constraints, domain_profile
## Evidence (optional)
- data_sources, research_sources, dashboards, metrics_dictionary
## Org (optional)
- stakeholders, delivery_cadence, capacity, artifact_templates, task_templates
## Reserved (named, UNREAD in v1)
- readiness_preferences, scoring_preferences, decomposition_axes, event_taxonomy
```

**opp-doc's DECLARED fields:** the core 4 (S4 success-criteria mapping + counter-metric seeding + S2 objective link) + recommended subset: `product_area, user_segments, core_scenarios, data_sources, research_sources`.

**Degradation rules (no-fallbacks) — complete per core-4 field:** absence of the file or a declared field NEVER produces an invented default — it becomes a WHITE SPOT in the gap report, kicked back to context-collection.
- `key_metric` / `counter_metrics` absent → hard S4 white-spot.
- `yearly_goals` absent → S2 objective-link white-spot (architecture's kicked-back-to-context-collection rule; the elicitation question is the S2 trigger's own «which goal does it serve»).
- `backlog_locations` absent (field or whole file) → the skill ELICITS the backlog file paths from the PM before ANY backlog read/write (human gate, consistent with the re-invocation triggers below) — it never invents a default path, never silently skips the backlog write; the absence is also recorded as a context white spot.
- A recommended field absent → degrades to AMBIGUOUS elicitation questions, not a hard stop.
- Undeclared absent fields are silently ignored (no noise).

**«Critical absence» (the refusal-script trigger, defined):** the refusal script (§4.5, verbatim) fires when the minimal items it names — сегмент, сценарий, метрика/outcome, источники evidence — cannot be established from the PM's material AND the context file combined; context-field absence alone (with the doc supplying the item) does not fire it. Reserved slots (incl. `readiness_preferences`) stay UNREAD until M4+. Re-invocation triggers mid-flow (context callable again, per the contract's single home): main metric unclear / evidence sources unknown / decision-maker unknown.

---

## 10. Explicit non-goals for lvl1

Do NOT build any of: full context module; full backlog operations (prioritization, stale detection, merge execution, shortlists, readiness views); solution/PRD module; planning; tech decomposition; revision/invalidation log; integrations (stash/jira/bi); readiness-preference tuning; HTML anything. Also out of scope: cross-PM dedupe (isolation model); unsolicited candidate generation; MERGE execution in entry E (recommend-only at lvl1 — stage 2 owns the backlog-side operations).

---

## 11. Spec-friction protocol + hand-back

**Spec-friction:** if implementing reveals a contradiction, ambiguity, or a real need to change the frozen container/rubric, the r-table, the card fields, or the context contract — do NOT edit any locked file and do NOT improvise a resolution. Record each item in a `## Spec-friction` section of your hand-back note: what rubbed, where (file + section), the smallest proposed change, what you did meanwhile (the spec-as-written wins during the build).

**Hand-back to the orchestrator** (STATE.md stays untouched by you — the orchestrator updates it and the GitHub Project, Opp Doc → M2; the orchestrator also records the hand-back summary — including the absolute fixture-folder path — next to this handoff file in `docs/handoffs/`, so the stage-2 session can find the stage-1 fixtures). Report:
1. Plugin path + file tree as built + the absolute fixture-folder path.
2. Which smoke tests ran, on which fixtures, and their outcomes (explicitly restating: M2 smoke tests only, executed by prompt-simulation per §8, M2→M3 gate NOT satisfied; live invocation pending user/orchestrator restart).
3. Spec-friction: yes/no + the list.
4. Any missing boot prerequisites you degraded around (e.g. target-solution.md absent, r-addendum not yet in model-axes.md, architecture.md amendments not yet applied).
5. Open TODOs left in deliverables (each must be an explicit TODO in the file, never silently filled).

One-line ping format: «opp-doc skill at M2, plugin at <path>, smoke tests <n>/7 passed on mock fixtures (simulated), spec-friction: yes/no».
