<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# Tracking — GitHub Project #5 (axis M)

**Board:** https://github.com/users/Jekudy/projects/5 — "AI for PM — foundation"

This is the home of **axis M only** (our tooling maturity). Q never goes here (it lives in `components/*/SPEC.md` as a runtime rubric).

## Fields
| Field | Type | Options |
|---|---|---|
| Component | single-select | Context · Opp Doc · Solution Doc · Backlog · Planning |
| M-status | single-select | M0 · M1 · M2 · M3 · M4 · M5 |
| Wave | single-select | W0 · W1 · W2 · later |
| Owner | text | for parallel work across PMs |

M-status meaning (full ladder in `docs/model-axes.md`): **M0** not-studied · **M1** mapped by hand · **M2** built into skill · **M3** tested on real cases · **M4** daily use by 1 PM · **M5** used by several PMs.

## Current items
5 components seeded. Opp Doc = **M1, Wave W0**. The other four = **M0, later** (lazy fractal — they stay one coarse box until activated).

## How to use
- Board view grouped by `M-status` or `Component` = the `component × maturity` grid.
- Advance M **only** when a real gate is passed (see the ladder). M is monotonic — it never goes backward.
- New sub-workflow rows appear **only** when a component is actively being built (don't pre-populate the fractal).

## Not here on purpose
- No Q values, no per-section scoring, no per-element cards. That would re-introduce the fractal we keep lazy and turn the board into slop.
