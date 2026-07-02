<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# VISION — AI-for-PM

## The picture
A PM says: *"есть сигнал X, я знаю то-то"* and invokes the plugin. The plugin assembles a draft doc, says **what's missing** and what to find out, offers help forming tasks for the PM and the analyst. The PM does that work **outside** the plugin, returns, re-invokes. The plugin re-assembles the doc, scores readiness, offers to raise quality or promote to backlog. Several passes. Then the same shape for the Solution. Then, at quarter end: *"давай спланируем квартал"* — decompose into waves, pick activities (signal research / Opp Doc / Solution Doc / build+A/B / research), check the quarter yields expected impact with sane capacity.

## Scope
- **In:** from **signal received** → **quarter planned**. Five components: Context collection, Opp Doc, Solution Doc, Backlog manager, Planning.
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
