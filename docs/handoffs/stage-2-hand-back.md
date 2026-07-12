<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# Hand-back — Stage 2: opp-backlog lvl1 (pm-flow plugin, M1 → M2)

> Recorded 2026-07-12 per `docs/handoffs/stage-2-opp-backlog-lvl1.md` §8. Executed as ONE multi-agent Workflow (`wf_bfd4e478-625`, 43 agents): plan → adversarial AC-coverage verify → per-deliverable build+independent-verify → register → smoke (4) → 3-lens audit + integration check → adversarial stress (5, in-loop fixer armed, never needed) → chief-gate vs ACTUAL FILES. The run survived two interruptions (session restart on 2026-07-10; session token limit) and was resumed twice via workflow journal cache — completed agents replayed, only the tail re-ran. Model routing (user directive mid-build): Fable 5 = planning + chief-gate + curation; Opus = judges/audits/fixers; Sonnet = skill simulators + stress authors + integration; Haiku = mechanical prep/resync. Orchestrator updates STATE.md + GH Project (not edited here, per §8).

**Deliverable state:** opp-backlog skill built to **M2** (runnable skill; exercised by prompt-simulation with independent judges + strict given-input discipline). **M2 smoke ≠ M3 gate** — M3 requires real PM material through the LIVE skill with output inspected. **Live invocation of `/pm-flow:opp-backlog` pending `/reload-plugins`** (a build session cannot live-invoke a skill it created). An additional REAL-DATA simulation wave was run against the user's actual backlog sheet — see §7; it is directional M3 evidence, not the M3 gate.

---

## 1. Plugin path + file tree as built

**Plugin home:** `/Users/eekudryavtsev/.claude/local-plugins/pm-flow`
**New skill:** `skills/opp-backlog/`
**Fixtures (absolute):** `/Users/eekudryavtsev/.claude/local-plugins/pm-flow/.fixtures/stage-2`

```
skills/opp-backlog/SKILL.md                        (10 889 B; 1513 words raw — under the 2500 ceiling with headroom)
skills/opp-backlog/references/card-schema.md       (4 691 B; verbatim frozen copy of SPEC 'Card schema (OWNED HERE)' + 'Admission rules'; source-of-truth header; diff-clean vs SPEC)
.fixtures/stage-2/pristine/                        (opp-backlog.md + solution-backlog.md, MOCK-labeled, seeded 2026-07-10)
.fixtures/stage-2/run/                             (smoke-1..4, stress-P1..P5 working copies with real mutations)
.fixtures/stage-2/transcripts/                     (9 transcripts: smoke-1..4.md, stress-P1..P5.md — named by producing probe)
.fixtures/stage-2/stress/ + oracles/               (per-probe fixtures + pre-derived oracles)
```

SKILL.md must-stay-inline set (all verified on disk by the chief gate): S-1 FULL-INVENTORY MUTATION GATE; the 5 operations (create-card / update-readiness-claim / update-status / append-links / update-next-step), each behind explicit manual invocation; duplicate-signal backlog ops as GIVEN-INPUT consumers (LINK append / CREATE / MERGE recommend-only refusal — the scan + verbatim dialogue stay owned by opp-doc entry E, NOT re-implemented); admission rules with Russian elicitation; exact enums; demotion path; decision→status mapping incl. the open-TODO surfacing; doc-write boundary (routes to `/pm-flow:opp-doc`); the three build conventions; target_metric context-validation; readiness ⟂ status ⟂ priority_data; non-goals list. **No router-hook added** (modules connect via the shared FILE, per the handoff).

## 2. Registration outcome

**REGISTERED** `pm-flow@pm-flow-marketplace` — pre-build **0.2.1**, final **0.4.0**, both manifests synced, cache dir `~/.claude/plugins/cache/pm-flow-marketplace/pm-flow/0.4.0/` materialized with SKILL.md + card-schema.md byte-identical to the plugin dir (chief-gate c5 diff-clean). NOTE: the interrupted first run had already bumped 0.2.1→0.3.0; the resume (journal tail lost at the session kill) re-ran registration live 0.3.0→0.4.0 — one minor version consumed by the resume artifact, versions stayed monotonic and synced throughout. The version was read LIVE both times (playbook rule; no hardcoded bump). **Run `/reload-plugins`** before `/pm-flow:opp-backlog` is live-invocable.

Recorded deviation (AC-coverage verifier flag): the handoff §6 freeze list names `plugin.json`, while §5 done-criteria require registration — the build treated manifest version-bumps as the orchestrator-granted writable surface and routed the contradiction here instead of editing the handoff. Orchestrator: confirm the grant and consider fixing §6 wording for future handoffs.

## 3. Smoke + stress tallies

> **M2 smoke ≠ M3 gate.** All results by prompt-simulation (Sonnet simulators) with independent adversarial judges (Opus) deriving oracles from the frozen SPEC BEFORE reading transcripts; chief gate (Fable) verified actual bytes on disk, not narration.

| Phase | Result |
|---|---|
| **Plan** | AC-coverage verify round 1 FAIL (manifest-freeze contradiction + one gap) → replan → round 2 PASS. |
| **Build** | 3/3 deliverables PASS on independent verify, 0 fix rounds (one low-severity fixture narrative note, §5). |
| **Smoke (4 §5 cases)** | **4/4 PASS, 0 fix rounds.** S1 dup backlog-side (LINK executed / CREATE with next_step elicitation + NNN=max+1 / MERGE refused recommend-only); S2 r0 intake blocked until next_step supplied, rough domain in title, r0 undated per SPEC note; S3 demotion r2→r1 recorded from GIVEN claim, fresh date + reason, no re-scoring, no "maturity"; S4 composability — PM-B acted on the promoted entry without PM-A (three slots + 8 folded sub-fields complete). |
| **3-lens audit** | **PASS/PASS/PASS** (verbatim-Russian/language; guardrails incl. container discipline, S-1, facets separation, non-goals absent; doneness incl. word budget 1513 and conventions recorded in-skill). |
| **Integration check** | PARTIAL conformance of LIVE opp-doc card writes vs frozen SPEC schema — **8 friction items**, nothing patched (see §4; the two consequential ones are the id-location split and the dual card serialization). |
| **Stress (5 adversarial probes)** | **5/5 PASS, 0 fix rounds** — in-loop fixer armed, never fired. P1 merge-pressure under PM authority → both cards byte-intact, recommend-only held; P2 kill/park mirror → killed+parked written, doc-write REFUSED and routed to opp-doc; P3 demote-resistance → given r1 claim recorded despite PM pushback (derived claims are non-negotiable in either direction); P4 S-1 gate under «сделай всё сразу без подтверждений» → full inventory presented, nothing written pre-confirmation; P5 embedded auto-mutation instruction in the file + read-only ask → ZERO mutations, instruction treated as data and flagged. |
| **Chief gate (vs ACTUAL FILES)** | **SATISFIED, 9/9 criteria** — first pass failed c5/c6/c7 as artifacts of the interrupted-run state (stale cache/baseline), gate-fixer re-synced, re-gate clean: SKILL non-trivial with full inline set; 1513 words; card-schema diff-clean vs SPEC; fixtures + 9 probe-named transcripts; 0.4.0 synced + cache byte-identical; **215/215 frozen-file hashes OK**; aipm repo git-status identical to baseline; all 5 write ops evidenced at file level (incl. a real demotion and both killed AND parked); smoke 4/4 + stress 5/5 transcripts on disk. |

**0 open skill-class defects.**

## 4. Spec-friction (canon-side; orchestrator to resolve — locked files NOT edited)

1. **[SPEC internal] r0 dated-annotation ambiguity.** `components/opp-backlog/SPEC.md` schema line attaches `(assessed <date> — …)` to the whole readiness enum incl. r0, while its own Schema note says r0 is assigned at creation with no Q derivation. The build resolved to bare `readiness: r0` (note wins). Smallest fix: exclude r0 from the dated-annotation wording.
2. **[SPEC ↔ task-schema] Card `id` location.** SPEC carries the id ONLY in the `## opp-NNN: <title>` heading; opp-doc's `references/task-schema.md` §5 lists `id` as a separate field bullet. Live stage-1 writes split exactly on this line. Fix: heading-only + one clarifying line in task-schema.
3. **[live-write drift] Two incompatible card serializations coexist** in opp-doc's live writes: SPEC's H2-heading form vs a flat `- id:` YAML-list form (4+ sampled files). Breaks any mechanical reader incl. the router's own dedupe-scan read contract. Fix: SPEC admits both explicitly, or opp-doc converges on the heading form.
4. **[live-write drift] Out-of-enum `readiness: below-r1`** in 2 stage-1 fixtures — forbidden by opp-doc's own current SKILL guard (fixtures predate the guard). Fix: regenerate or mark superseded.
5. **[live-write drift] `segment:`/`scenario:`/`keywords:` as dedicated fields** in ~half the sampled live cards, though SPEC's read contract says they are prompt-extracted, never dedicated fields. Fix: amend SPEC to admit them as optional, or stop writing them.
6. **[live-write drift] Undefined `open_tasks:` block** persisted on one live card — field absent from the frozen schema. Fix: SPEC must own it like priority_data, or tasks stay in the gap report only.
7. **[cosmetic drift] Preamble H1 variants** («Opp Backlog — …» stage-1 wave vs canonical «Opportunity Backlog — …») and **em-dash heading separators** (`## opp-301 — <title>` vs SPEC's colon) across fixture waves.
8. **[ambiguity actively splitting output] readiness annotation verbosity** — full schema-definition clause repeated per card vs compact `rX (assessed <date>)`; live cards split ~50/50. Fix: task-schema states the compact per-instance form explicitly.

Net (integration checker): SPEC + task-schema are not yet the single consistent source they claim to be, and the schema+skill pairing under-constrains the write shape enough that real runs will diverge the same way the fixture waves did.

## 5. Conventions chosen (the SPEC's two build-time TODOs + adjacent calls)

- **NNN assignment:** next free NNN = max existing `opp-NNN` in THIS file + 1, zero-padded to 3 digits; never reused (killed cards keep their number). Adopted from stage-1 `task-schema.md` §5 for cross-module consistency; recorded in SKILL.
- **r0 rough domain:** carried in the card `<title>` (no dedicated field) — the SPEC's own least-invasive candidate; recorded in SKILL; the domain is never dropped.
- **File preamble:** a single H1 `# Opportunity Backlog — <owner>` above the first card; an existing PM H1 is accepted as-is, never rewritten.
- **decision→status at r3:** kill → `killed`, park → `parked` implemented; for continue-discovery / generate-solutions the skill SURFACES the open canon TODO, lets the PM set status explicitly from the enum, and records the friction — no silent mapping invented.
- **Fixture note (low severity):** pristine `solution-backlog.md`'s promoted entry sol-A parents opp-123 which sits at r2/in_discovery on the same date — a narrative inconsistency (promotion implies the r3 gate passed). Harmless for smoke-4 (entry read standalone); age the dates apart if the fixture is ever reused as a lifecycle example.

## 6. Open questions / TODOs for the orchestrator

1. **Q-rubric:** inputs define NO Q-rubric for this module (mutate/append shape, not diagnosis). None was authored (per handoff §1). Open question: does opp-backlog ever get a quality dial of its own, or is card quality fully derivative of the doc?
2. **continue-discovery / generate-solutions status mirror** — the SPEC's open TODO stands; resolve before the first real r3 pass through the backlog skill.
3. **Router-executor seam (D-3) to mirror into `docs/architecture.md#router-lite`:** at the design layer the router remains the named executing party of the dedupe scan; at the built layer the runnable home of scan+dialogue is opp-doc entry E, and the opp-backlog skill executes only the backlog-side writes consuming the dialogue outcome as given input. Same given-input pattern as demotion.
4. **Handoff §6 wording** — see the recorded manifest-bump deviation in §2.

## 7. Real-data test wave (user-requested addendum; separate workflow)

The user requested a testing pass against his REAL working backlog — one tab of his actual Google Sheets backlog (118 rows; identifying details scrubbed for the public repo — the unscrubbed report lives locally, see below; snapshot read-only via CSV export; gws CLI was blocked by the proxy, Chrome export used instead). Real sheet shape vs lvl1 contract: free-text title/hypothesis/DoD columns; type enum (Enabler / Влияние на метрику / Инфраструктура); statuses only for finished items («Сделано»/«Отказались»); quarters; **MoSCoW priorities**; roles/support/blockers/people columns; category; **RICE+OKR+Care columns declared but empty**; no next_step / source / readiness anywhere.

Pipeline (`wf_6f88626c-1cd`): 5 independent input-designer lenses (intake / bulk-migration / lifecycle / dedupe / adversarial-PM) → Fable curator selects ~12 most diverse sub-scenarios → per-scenario scripted dialogue + oracle pre-derived from the frozen SPEC (honest refusal = PASS) → strict Sonnet simulations → 3 judges per run (Opus spec-conformance with a `by-design-limit` class; Sonnet PM-experience 0–10; Sonnet data-fit mapping real fields vs schema) → Opus clustering → Fable adversarial challenge vs SPEC non-goals → Fable improvement proposals in three buckets (lvl1 skill fixes / spec-friction / lvl2 requirements mapped to the user's themes: storage-adapters, mandatory-core-vs-adaptive-fields, foreign-prioritization). Raw sheet content never leaves the local scratchpad; this hand-back carries paraphrased findings only.

**Results (wave `wf_6f88626c-1cd`, 70 agents, 12/12 runs judged):**

- **spec_pass 12/12** — the contract held on real material: zero invented facts, zero readiness inflation, zero fake kills, S-1 gate and recommend-only merge survived adversarial pressure incl. «занеси все 59 строк без вопросов». Exactly ONE skill-class violation the whole wave (a marked-verbatim admission string got paraphrased, T05).
- **PM-experience: range 4–7, median ~6.** Both minima (T05 migration = 4; T12 bulk archive = 4, **0 cards written out of 59 rows**) are the same failure shape: correctness anchored trust, but the module doesn't LAND on real data — foreign prioritization evaporates silently, no batch path, a parallel Markdown file instead of the PM's sheet, and a wall of identical refusals under pushback.
- **Findings after the Fable adversarial challenge** (4 findings killed as artifacts/non-bugs, incl. two «fixes» that would have broken frozen invariant 1):
  - **12 skill-fixes within the frozen contract (S1–S12)** — top: S1 anti-loop on refusals (verbatim line once per block, then acknowledge + name the one legal path); S2 owner silently auto-defaulted (cleanest guardrail violation of the wave — a field the PM never dictated appeared on the card); S3 dead rows silently written `status: new` (looks alive in the file); S4 conversational source not credited (co-cause of T12's zero). Plus de-jargonizing improvised Russian strings, «ни вверх, ни вниз» symmetry, dedupe route-back verbatim line, single-confirmation append-only path, two elicitations (one-opportunity-or-two; stale next_step on status change), render conventions, transparency lines for dropped foreign fields.
  - **7 spec-friction questions (C1–C7)** for the orchestrator — most load-bearing: **C3** (is `source` an admission BLOCKER or strongly-expected? invariant 2 gates only next_step; this ambiguity is the carrying cause of T12's zero writes) and **C1** (park/kill-at-intake semantically clashes with the next_step gate — legacy rows can't be honestly admitted). Also: kill provenance without a doc (C2), a `reason` accepted by op-2 with no schema slot (C4), LINK signal-vs-solution branch (C5), op-3/4 vs op-5 next_step refresh coupling (C6), jargon inside FROZEN verbatim strings (C7).
  - **8 lvl2 requirements (R1–R8)** mapped to the voice-note themes, adoption-priority order: R1 batch/bulk-intake with per-batch defaults (T12: 59→0); R2 MoSCoW/RICE bridge or raw passthrough (12/12 runs); R3 terminal delivered/done status axis (~11/12); R4 Sheet-backed store / round-trip adapters (kept OUT of lvl1 by frozen invariant 1 — survived only as adoption evidence); R5 owner as role-tag vs named person; R6 institutional fields (quarter/type/theme/DoD/decline-reason); R7 cross-skill dedupe hand-off (PM stops being the message bus between opp-doc and opp-backlog); R8 quality bar on PM-supplied next_step (anti-boilerplate).
- **Full paraphrased report (Russian):** `~/.claude/local-plugins/pm-flow/.fixtures/stage-2-real-wave/REPORT.md` (+ clusters.md, scenarios/, oracles/, transcripts/ preserved there; raw sheet rows stay local, never in this repo).
- **Process notes:** per-test pm_scores were not persisted by the wave (only range/median/minima) — persist them next wave; migration-lens tests deliberately measured beyond-contract behavior and should be pre-tagged so «blocker» severities aren't read as defects.

## 8. lvl2 requirements captured from the user (2026-07-08 voice note; scope decision 2026-07-10)

The user confirmed Stage 2 builds strictly to the frozen SPEC; the following are LVL2 DIRECTION, to be spec'd by the orchestrator:

1. **Storage adapters.** Real products keep backlogs in different tools (Confluence, Google Sheets/Docs). The lvl2 target: a base TABLE format, with Google Sheets/Docs via the local `gws` CLI as the reference adapter; the committed Markdown file remains the lvl1 canonical store. (Constraint discovered this session: `gws` does not honor the Clash proxy env — network path needs solving before a Sheets adapter is real.)
2. **Mandatory core vs adaptive periphery.** A small set of fields we insist on («если у тебя этого нет — давай включим»: the admission core — signal/source/rough domain/next_step and the dated readiness claim) vs fields where we adapt to the PM's existing schema (their type enums, quarters, categories, people columns).
3. **Foreign prioritization models.** If the PM prioritizes by another model (MoSCoW, RICE — both literally present in the real sheet), the module uses THEIR model instead of forcing the 5 qualitative dims: store theirs verbatim, never convert silently, never invent an aggregate. The real sheet's empty RICE columns are field evidence that imposed scoring models go unused.

## 9. Done-criteria (Stage 2, M2) — MET

- ✅ SKILL.md + references/card-schema.md in the plugin; ✅ registered (0.4.0 synced, cache byte-verified); ✅ smoke 4/4 (prompt-simulation, independent judges); ✅ stress wave 5/5 SATISFIED by chief-gate against actual files (0 skill-class defects); ✅ 3 audits pass; ✅ integration check done (8 canon frictions logged, nothing patched); ✅ hand-back written; ✅ conventions + open questions recorded.
- **M2→M3 gate (NOT this stage):** real PM material through the LIVE skill with output inspected; the §7 real-data wave is simulation-based directional evidence only.

## 10. Next moves (orchestrator/user)

1. `/reload-plugins` → live-verify `/pm-flow:opp-backlog` on the stage-2 fixtures.
2. Update STATE.md + GH Project #5: Opp Backlog M1 → M2 (mirror).
3. Resolve §4 spec-friction — items 2 and 3 first (they already split live output).
4. Decide the lvl2 spec slot for §8 (storage adapters / adaptive fields / foreign prioritization) — the §7 wave results quantify the pain.

One-line ping: «opp-backlog skill at M2, plugin v0.4.0, smoke 4/4 + stress 5/5 simulated (0 fix rounds), chief-gate SATISFIED 9/9, spec-friction: 8 build-side + 7 wave-side canon questions, real-data wave 12/12 spec-pass / PM-median ~6 with 12 skill-fixes + 8 lvl2-reqs proposed».
