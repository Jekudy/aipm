<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# STATE — where are we right now

_Last updated: 2026-07-05. This is the single source of truth for "what stage, which component, which tasks, which done-criteria." Update it every session._

## Stage
**Этап 1 (Wave 0): Architecture lvl1 ∥ Opp Doc lvl1 — BUILD DONE (2026-07-05), Opp Doc at M2.** Stage-1 handoff executed by a multi-agent build workflow: plugin `pm-flow` built at `~/.claude/local-plugins/pm-flow/`, registered (`pm-flow@pm-flow-marketplace` v0.1.0), 7/7 §8 smoke tests passed (prompt-simulation on mock fixtures), 3 final audits passed. Hand-back: `docs/handoffs/stage-1-hand-back.md` (spec-friction: YES — 7 items, see orchestrator task 6). **Run `/reload-plugins`** (no restart needed, Claude Code ≥2.1.195) before `/pm-flow:opp-doc` is live. **Этап 2 = Opp Backlog lvl1** (unblocked, handoff ready).

## Canon reading order (new sessions)
1. `docs/target-solution.md` — reviewed North-Star frame (куда идём).
2. `docs/model-axes.md` — M ⟂ Q ⟂ lvl + the r (work-item readiness) addendum.
3. `docs/architecture.md` — plugin architecture: router-lite, interfaces (incl. context-file contract), state model.
4. `docs/design-log/2026-07-04-reconciliation.md` — locked decisions D-1…D-6 + conflict register C1…C20.

## Mega-scenarios (North Star, from 2026-07-02 inter-module session)
The plugin exists to close three PM pains:
1. Нет достаточно качественного **Opportunity Doc** → хочет его получить.
2. Нет достаточно качественного **PRD** → хочет его получить. (**PRD = зрелый Solution Doc** — one module, its target output is called PRD.)
3. Нет поспринтово корректно спланированного **квартала** для диско → хочет его получить.

~10 entry scenarios reduce to ONE pattern: **diagnose where the PM is in the cycle → route to a module**. The router (router-lite lvl1) is part of the Architecture module — normative description in `docs/architecture.md#Skill layout`.

## Active tracks
- **Track A — Architecture lvl1**: DONE incl. build — router-lite + intake protocol + transition gates are embedded in the built stage-1 skill (2026-07-05). The "M2 when embedded in the built skill" criterion is met → advance Architecture M1→M2 in GH Project.
- **Track B — Opp Doc lvl1**: **BUILT, M2, STRESS-TESTED (v0.1.3, 2026-07-07).** Live-verified. Wave 1: 12 AF entry scenarios 12/12; wave 2 adversarial: 8/8 at 14/14, chief-orchestrator gate SATISFIED (hard promotion gate held under PM pressure; merge recommend-only held; honest demotes; false-ABSENT=0). Fix history in `docs/worklog.md`. Ingest of ≥3 real example docs still pending (M2→M3 gate).
- **Track C — Opp Backlog lvl1 (Этап 2)**: lvl1 SPEC designed (`components/opp-backlog/SPEC.md`, card schema = single owner). Build handoff ready → `docs/handoffs/stage-2-opp-backlog-lvl1.md`. **Unblocked** — stage-1 hand-back recorded; stage-1 fixtures for reuse at `~/.claude/local-plugins/pm-flow/.fixtures/stage-1/`.
- **Track D — Solution Doc lvl1 (Этап 3)**: **BUILT, M2 (2026-07-07).** SPEC `components/solution-doc/SPEC.md` (10 sections S0–S9, one dial `sol-r0..r3`, approved at gate 2026-07-07). Skill `skills/solution-doc/` + a router-hook in opp-doc; plugin v0.2.0. Workflow `wf_47bc1c21-aee` (58 agents): smoke 7/7, 3 audits, stress-1 5/5, stress-2 5/5 (P6 = fixture-naming artifact), chief-gate SATISFIED. Hand-back `docs/handoffs/stage-3-hand-back.md`. **3 spec-friction open** (sol-r1 relabel — RESOLVED 2026-07-07; S7-guardrail reconcile; reserved-vocab collapse). M2→M3 = ≥3 real PRDs (1/3: «Холдирование Откликов», eval fixture). Live-verify pending `/reload-plugins`.

## Sessions (how we split work across windows)
| Session | Root | Owns | Brief | Status |
|---|---|---|---|---|
| **Orchestrator** (this) | `~/Vibe/products/aipm` | STATE.md, canon docs, design-log, GitHub Project, review | — | active |
| **Ingest** | `~/Vibe/products/aipm` | `components/opp-doc/examples/` (filled real docs) | `docs/sessions/ingest-brief.md` | ready to launch |
| **Stage 1 build** | `~/.claude/local-plugins/pm-flow/` | the pm-flow plugin (opp-doc lvl1 + stubs) | `docs/handoffs/stage-1-opp-doc-lvl1.md` | **done 2026-07-05** (hand-back recorded) |
| **Stage 2 build** | `~/.claude/local-plugins/pm-flow/` | skills/opp-backlog lvl1 | `docs/handoffs/stage-2-opp-backlog-lvl1.md` | ready to launch |

Non-orchestrator sessions never edit STATE.md; they hand results back and the orchestrator updates it (stage handoffs define the hand-back protocol).

## Module maturity (mirror of GitHub Project #5 — authoritative M lives THERE)
| Module | M | Wave | Note |
|---|---|---|---|
| Architecture & contracts | **M2** | W0 (now) | Router-lite + interfaces + gates embedded in the built stage-1 skill (2026-07-05). Mirror to GH Project. |
| Opp Doc | **M2** | W0 (now) | Built into runnable skill `/pm-flow:opp-doc` (2026-07-05); 7/7 smoke simulated. M2→M3 gate = ≥3 real docs ingest. |
| Opp Backlog | **M1** | Этап 2 | lvl1 SPEC hand-designed (2026-07-04): card schema, match keys, admission rules. M1→M2 = execute stage-2 handoff. GH Project: advance M0→M1. |
| Context collection | M0 | later | Module stays M0, but the context-FILE contract is FIXED (single home: `docs/architecture.md#Interfaces`) — no refactor when the module activates. |
| Solution Doc (→ PRD) | **M2** | Этап 3 | lvl1 BUILT 2026-07-07 (`/pm-flow:solution-doc`, plugin v0.2.0). 10-section container S0–S9; ONE readiness dial `sol-r0..r3` (collapsed the reserved sol-s0..s2 / prd-r1..r3 split). Smoke 7/7 + 2 stress waves + chief-gate SATISFIED. M2→M3 = ≥3 real PRDs (1/3). Mirror to GH Project. |
| Solution Backlog | M0 | later | `docs/solution-backlog.md` is already a WRITE-ONLY contract target in Этап 1 (admission invariant live). |
| Planning | M0 | later | Reserved vocabulary: bet types, delivery_mode, 5 intent types. Detail LAST. |

## Wave 0 deadline (from 2026-07-02 grill)
**First run of the user's own real signal through the opp-doc skill by 2026-07-16.** Existential done-criterion (dogfood; anti-burnout anchors in task 4).

## Current tasks & done-criteria
0. ~~Track A: reconcile ChatGPT architecture/levels findings.~~ **DONE 2026-07-04** (target-solution.md + canon edits + design-log).
1. ~~Execute stage-1 handoff.~~ **DONE 2026-07-05**: pm-flow built + registered, 7/7 smoke (simulated), audits pass, hand-back → `docs/handoffs/stage-1-hand-back.md`.
2. **Live-verify `/pm-flow:opp-doc` after `/reload-plugins`** (no restart needed; the build session cannot invoke a skill it created), then dogfood the user's own real signal (deadline 16.07). _Owner: user + orchestrator._
3. **Ingest ≥3 real Opp Docs** into `components/opp-doc/examples/` (M2→M3 BLOCKING gate: false-ABSENT rate of the white-spot detector). _Owner: user + ingest session._
4. **Execute stage-2 handoff** (`docs/handoffs/stage-2-opp-backlog-lvl1.md`): build opp-backlog lvl1 (M1→M2). UNBLOCKED. _Owner: stage-2 build session (Fable)._
5. **Set external anchors (anti-burnout).** Done = (a) public commitment in the Mattermost working group («покажу первый прогон 16.07»), (b) named co-owner in the GH Project Owner field. _Owner: user._
6. **Resolve spec-friction backlog** (stage-1: 7 items in `docs/handoffs/stage-1-hand-back.md#3-spec-friction`; stress waves added more — full list in `docs/worklog.md`). Key decisions: (A) r0 = floor rung wording in canon; (B) §8 CASE 2 «→ r1» vs r1-conjunction; (D) §9.3 AMBIGUOUS-vs-ABSENT; (E) SKILL.md word budget; **[P1] split write-procedure** (decomposition resolution: docs per child, sibling cross-links, parent archiving); **[P2] S6 materiality gate / demote-trigger wording** («evidence REMOVED» doesn't cover evidence-stronger-but-immaterial); **[P2] S11-decision-at-r3 prose** (park/kill on low-r doc is legitimate); router A-vs-C tiebreak for mixed input. _Owner: orchestrator + user (locked files)._
7. **GitHub Project #5**: advance Opp Doc M1→M2, Architecture M1→M2, Opp Backlog M0→M1; add Этап-2 wave column/label. _Owner: orchestrator._

## Blocked on
- ≥3 real Opp Docs (for the M2→M3 calibration gate).
- `/reload-plugins` run (for live invocation of `/pm-flow:opp-doc` — no restart needed).

## Decisions locked
- M ⟂ Q ⟂ lvl (`docs/model-axes.md`) **+ r = work-item readiness as a DERIVED projection** (r addendum, 2026-07-04): r0–r3 computed from the Q profile + decision state; dated, demotable; never "maturity", never in GH Project.
- Orchestrator decisions D-1…D-6 + conflict resolutions C1…C20: `docs/design-log/2026-07-04-reconciliation.md`. Highlights: r3 ≡ promotion gate (canon NOT tightened); solution-backlog.md = write-only target in Этап 1; dedupe = router executes / opp-backlog owns match keys; candidate generation only on explicit PM request post-r3, cap 1–3; card status enum authoritative, frozen S0 enum untouched.
- v1 = prompt-only. Container discipline. Lazy fractal. State = plain Markdown at a PM-supplied path.
- Tracking = GitHub Project #5. Boardmix = render of the repo.
- Language: PM-facing output Russian; machine/instruction layer English.
- Этап 1 = Architecture lvl1 + Opp Doc lvl1; **Этап 2 = Opp Backlog lvl1** (re-scoped 2026-07-04 by user, overrides "detail at Opp Doc M3+").
- PRD.md waived: `docs/architecture.md#Interfaces` plays the cross-phase-contracts role.

## Next move
Run `/reload-plugins` → live-verify `/pm-flow:opp-doc` → dogfood the user's own signal through it (deadline 16.07) → resolve spec-friction items (task 6) → stage-2 build (opp-backlog lvl1) → ingest real docs for M3 calibration.
