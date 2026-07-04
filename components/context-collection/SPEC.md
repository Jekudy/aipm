<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# Context collection — component SPEC (COARSE STUB)

> **Status: M0.** Deliberately a ~one-paragraph sketch (lazy fractal). Do NOT design further yet.

## One-line intent

Fix a specific PM's working context — where their backlogs live, which channels/signals to read, yearly goals, and the key metrics + counter-metrics — so every downstream component reads from one grounded source instead of re-deriving it.


## When to detail

Detail only once Opp Doc reaches ~M3 (tested on real cases) and its metrics/backlog-location section keeps hitting white-spots it must ask for inline — i.e. when missing context becomes the actual bottleneck. Until then: one SKILL.md stub + a one-paragraph 'what a filled context profile contains' pointer. No schema, no rubric.

## Contract fixed now (Этап 1)

The context FILE contract is fixed NOW — schema stub, declared consumers, and the read-if-present / degrade-if-absent rule live in `docs/architecture.md#Interfaces` (context-collection → opp-doc entry; the contract's single home — not duplicated here). This module stays M0: in Этап 1 the file (`context.md`, e.g. `docs/context.md` — location PM-supplied per the state model) is hand-authored (labeled as a fixture when used in demos); when this module is eventually detailed, it will PRODUCE that file — the contract is this module's future acceptance target (forward-compat, no refactor later).

