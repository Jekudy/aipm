<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# STATE — where are we right now

_Last updated: 2026-07-02. This is the single source of truth for "what stage, which component, which tasks, which done-criteria." Update it every session._

## Stage
**Этап 1 (Wave 0): two parallel tracks — Architecture lvl1 ∥ Opp Doc lvl1.** Foundation is done (model locked, tracking live, containers ready). If the tracks don't reconcile cleanly, reconciliation is planned into lvl2 — don't block on it now.

## Mega-scenarios (North Star, from 2026-07-02 inter-module session)
The plugin exists to close three PM pains:
1. Нет достаточно качественного **Opportunity Doc** → хочет его получить.
2. Нет достаточно качественного **PRD** → хочет его получить. (**PRD = зрелый Solution Doc** — one module, its target output is called PRD.)
3. Нет поспринтово корректно спланированного **квартала** для диско → хочет его получить.

~10 entry scenarios ("пришёл с плохим/неполным opp doc / с сигналом / с кашей / с идеей решения / за беклогом / сразу за PRD / за кварталом без инициатив...") all reduce to ONE pattern: **diagnose where the PM is in the cycle → route to a module**. The router is part of the Architecture module (single entry point), not ten separate workflows.

## Active tracks
- **Track A — Architecture lvl1** (owner: orchestrator session + user). Plugin skeleton, module contracts, router. Input: user's ChatGPT findings on levels/architecture — pour them HERE.
- **Track B — Opp Doc lvl1** (owner: ingest + build sessions). Container fill + prompt-only skill.
Everything else is a coarse M0 stub (lazy fractal).

## Sessions (how we split work across windows)
Three roles, run in separate Claude Code windows. Ingest and Build are **independent → parallel**; they converge at the M2→M3 calibration.
| Session | Root | Owns | Brief | Status |
|---|---|---|---|---|
| **Orchestrator** (this) | `~/Vibe/products/aipm` | STATE.md, roadmap, GitHub Project, review | — | active |
| **Ingest** | `~/Vibe/products/aipm` | `components/opp-doc/examples/` (filled real docs) | `docs/sessions/ingest-brief.md` | ready to launch |
| **Opp Doc build** | `~/Vibe/products/aipm` | the `pm-flow` plugin (`~/.claude/local-plugins/pm-flow/`) | `docs/sessions/oppdoc-build-brief.md` | ready to launch |

No git worktrees: the three touch disjoint file trees (STATE vs examples vs the global plugin), so plain parallel windows suffice — worktrees of the whole Obsidian vault would be over-engineering. Non-orchestrator sessions never edit STATE.md; they hand results back and the orchestrator updates it.

## Module maturity (mirror of GitHub Project #5)
| Module | M | Wave | Note |
|---|---|---|---|
| Architecture & contracts | **M1** | W0 (now) | Hand-mapped in `docs/architecture.md`. lvl1 = skeleton + router + contracts. Track A. |
| Opp Doc | **M1** | W0 (now) | 12-section container + Q-rubric + white-spots. Next: prompt-only skill (M1→M2). Track B. |
| Context collection | M0 | later | Detail once Opp Doc ~M3 keeps asking for missing context. |
| Opp Backlog | M0 | later | Store of problems/outcomes; detail at Opp Doc M3+. |
| Solution Doc (→ PRD) | M0 | later | Detail right after Opp Doc emits its first ranked options. Target output = PRD. |
| Solution Backlog | M0 | later | Store of ranked options w/ three-slot contract; trigger = first promotion. |
| Planning | M0 | later | Detail LAST — consumes the others. |

_"Ways of working" is NOT a module — it's this repo's docs layer (STATE, model-axes, briefs)._

## Wave 0 deadline (from 2026-07-02 grill)
**First run of the user's own real signal through the opp-doc skill by 2026-07-16.** This is the existential done-criterion: the project's #1 risk is the user (sole engine) switching away; historically his projects survive only when living users wait. First living user = the user himself (dogfood). Plan for 1 week of work (x2 estimation rule).

## Current tasks & done-criteria
0. **Track A: pour ChatGPT architecture/levels findings into the orchestrator session.** Done = findings reconciled with `docs/architecture.md`, Architecture lvl1 scope contract written (intent + invariants + acceptance criteria), router (single entry → diagnose → route) included. _Owner: user + orchestrator._
1. **Track B: pour ChatGPT Opp-Doc work into `components/opp-doc/SPEC.md`.** Done = your existing material mapped onto the 12 sections; conflicts reconciled (map by the QUESTION each section answers). _Owner: user + ingest session._
2. **Build prompt-only `pm-flow` opp-doc skill (M1→M2).** Done = a SKILL.md running the 6-step diagnosis loop against the frozen spec/rubric. _Not started._
3. **Collect ≥3 real Opp Docs for calibration (M2→M3 BLOCKING gate).** Done = false-ABSENT rate of the white-spot detector checked on real docs. The user's own dogfood docs count. _Blocked on: real docs._
4. **Set external anchors (anti-burnout).** Done = (a) public commitment posted in the Mattermost working group ("покажу первый прогон 16.07"), (b) a named co-owner from the group in the GH Project Owner field. _Owner: user._

## Blocked on
- User's ChatGPT Opp-Doc dump (for task 1).
- ≥3 real Opp Docs (for the M2→M3 calibration gate).

## Decisions locked
- M ⟂ Q (`docs/model-axes.md`). Lazy fractal. Container discipline.
- v1 = prompt-only (no Python/subagents/infra until a real doc demands it).
- State = plain Markdown at a PM-supplied path; git optional.
- Tracking = GitHub Project #5. Boardmix = render of the repo.
- Language: PM-facing output in Russian; machine/instruction layer in English (see CLAUDE.md).
- **lvl ≠ M ≠ Q**: `lvl N` = the SCOPE CONTRACT of a module version (what it promises: intent + invariants + acceptance criteria; lives in the module SPEC). M tracks how far the current lvl is BUILT. Q scores how well the OUTPUT solves the task. Three words, three questions: "что обещали / докуда построили / насколько хорошо решает".
- Этап N = a wave picking a FOCUS subset of modules at target lvls (Этап 1 = Architecture lvl1 + Opp Doc lvl1). Not all modules advance every этап.
- PRD.md waived: `docs/architecture.md#Interfaces` plays the cross-phase-contracts role (no hollow templates).
- Boardmix API check dropped (stays as deferred note in `docs/boardmix.md`); `Owner` field in GH Project filled when the second PM joins.

## Next move
Fill the Opp Doc container with your ChatGPT work → then build the prompt-only skill → then calibrate on real docs.
