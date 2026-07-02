<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# VISION — AI-for-PM

## The picture
A PM says: *"есть сигнал X, я знаю то-то"* and invokes the plugin. The plugin assembles a draft doc, says **what's missing** and what to find out, offers help forming tasks for the PM and the analyst. The PM does that work **outside** the plugin, returns, re-invokes. The plugin re-assembles the doc, scores readiness, offers to raise quality or promote to backlog. Several passes. Then the same shape for the Solution. Then, at quarter end: *"давай спланируем квартал"* — decompose into waves, pick activities (signal research / Opp Doc / Solution Doc / build+A/B / research), check the quarter yields expected impact with sane capacity.

## Mega-scenarios (North Star)
1. У продакта нет достаточно качественного **Opportunity Doc** — он хочет его получить.
2. У продакта нет достаточно качественного **PRD** — он хочет его получить (PRD = зрелый Solution Doc).
3. У продакта нет поспринтово корректно спланированного **квартала для диско** — он хочет его получить.

Entry scenarios (~10: плохой/неполный opp doc, сигнал, каша в голове, уточнение беклога, идея решения, идея для существующей возможности, слабый solution doc, сразу PRD при незрелом солюшне, квартал без инициатив) all reduce to **one router pattern**: diagnose where the PM is in the cycle → route to a module.

## Scope
- **In:** from **signal received** → **quarter planned**. Seven modules: Architecture & contracts, Context collection, Opp Doc, Opp Backlog, Solution Doc (→PRD), Solution Backlog, Planning.
- **Out (other teams):** prototyping; the AI-analyst. We may consume both.

## What must be true (the cubes)
1. A shared, un-mergeable **model of levels** (M ⟂ Q) so we never ship confusing/non-scalable slop → `docs/model-axes.md`.
2. Components **isolated + composable** so two PMs work in parallel; the only interface is a committed doc contract (intent + invariants + acceptance criteria).
3. A **diagnosis engine** that maps messy input onto structure and reports grounded white spots — never backfills (anti-neuroslop).
4. **Transparent tracking** (GitHub Project) + **workflow visualization** (Boardmix) so we — and other PMs — always know what this is and where we are.
5. **Progressive JPEG:** detail near, sketch far; ship iterable pieces, not a 6-month build.

## Principles (from the user's fears, inverted into rules)
- Detail one level down, only for the active component. Far = coarse M0.
- Smallest testable v1 is a prompt. Defer Python/subagents/infra until a real doc demands it.
- Study real experience before designing (see `docs/reference-digest.md`).
- Every component's "done" is objective (Q-gate / M-gate), not a feeling.
