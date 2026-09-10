# AIPM

AIPM is the plugin project at `~/Vibe/work/avito/growth/aipm`.
BB project: `aipm` (`proj_sbt9f7qqqv`); source: `src_8j857yb77p`.
Git origin remains `https://github.com/Jekudy/aipm.git`.
Parent: [Growth](~/Vibe/work/avito/growth/CLAUDE.md).

## Goal

Help Avito PMs manage their product backlog and review initiatives before choosing a solution or handing work to a team, using the AIPM skills. This describes the existing [plugin manifest](plugins/aipm/.codex-plugin/plugin.json); the directory move adds no product requirements or success metrics.

## Navigation

- [Current worklog](docs/worklog.md) and [readable-report specification](docs/specs/spec-readable-report/SPEC.md).
- [Plugin skills](plugins/aipm/skills/) and [local marketplace](.agents/plugins/marketplace.json).
- [Local research](~/Vibe/work/avito/growth/aipm/local-research/ai-for-pm/README.md) and [review index](~/Vibe/work/avito/growth/aipm/local-research/ai-for-pm/runs/INDEX.md): local-only, ignored, not publication inputs.
- [Existing project memory](~/.claude/projects/-Users-eekudryavtsev-Vibe-products-aipm/memory/MEMORY.md): retain this legacy namespace; verify dated claims against the current checkout.
- [Owner worktree worklog](~/Vibe/work/avito/growth/aipm/.worktrees/review-skills/docs/worklog.md): the pending `feat/walkthrough-db09` branch retains its own later decisions and code. This migration does not merge it.

## Context decision

Decision (2026-09-10, AVT-13): move AIPM physically under Growth while retaining its name, independent Git history, BB project/source IDs and existing worktrees. Keep local research ignored and preserve both old-path aliases.
Reason: colocate the complete project without publishing research, merging pending work or breaking existing sessions and evidence links.
Source: user/root thread `thr_4qem5ekfpp`, AVT-13 EXECUTE authorization.

`~/Vibe/products/aipm` points to the new repository; `~/Vibe/work/avito/raw/drafts/ai-for-pm` points to its local research. Do not remove these compatibility aliases while old sessions or links use them.

## Startup status

The explicit chain is AIPM → Growth → Avito → Vibe. `CLAUDE.md` is canonical and `AGENTS.md` is its alias. No `.bb/AGENTS.md` is used.

The relocation prepares context on `infra/avt-13-growth-context`; main and the two original worktrees keep their original HEADs. AIPM SessionStart hooks are not activated by this change. Old worktrees do not have this new leaf canon: never inject main's file as a substitute. Hook activation and fresh startup acceptance require a separate, worktree-safe step; manual validation alone does not prove native delivery.

## Historical sources

Commit `3d0f370` removed the old design documents on 2026-09-02; their previous versions remain in `3d0f370^`. The current plugin tree is authoritative for implemented skill behavior. The global `pm-flow` plugin is a separate legacy implementation and is not relocated or reinstalled by AVT-13.
