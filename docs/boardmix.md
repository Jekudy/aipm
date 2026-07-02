<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# Boardmix — workflow visualization (render, not source)

**Board:** https://boardmix.com/app/editor/0-eAIKHBAwExdyUODNn1-A

## Role
Boardmix visualizes the **workflow trees** (the "how" / skill-tree, with proof-depth per process) for humans. It is a **render of this repo**, not a source of truth.

- **Source of truth = this repo** (STATE.md + specs + GitHub Project).
- **Board = a picture** you update by hand (or import a generated Mermaid diagram from the repo). Repo → board, never board → repo.

## Why not automate it / reverse-engineer the desktop app — NO
- No official public Boardmix API surfaced (only a third-party marketplace wrapper of unclear provenance — don't rely on it).
- Reverse-engineering the desktop app = weeks of brittle work that breaks on every update = exactly the over-engineering we avoid. Boardmix is a slow-changing human artifact; a 2-minute manual update beats an automation pipeline.

## Deferred (only if manual updates become painful)
- 30-min check for an official API + agree a manual board format/legend.
- Generate a Mermaid workflow diagram from the specs and import it.

## What to draw
- The 5 components as a value chain, colored by Cynefin domain.
- Per active component: its workflow tree with proof-depth (Q) markers.
- Maturity (M) mirrored from GitHub — but the board's job is the **workflow detail**, not status.
