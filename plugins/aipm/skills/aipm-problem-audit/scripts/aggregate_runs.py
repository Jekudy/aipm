#!/usr/bin/env python3
"""aggregate_runs.py — merge independent audit runs into one verdict.

Usage: aggregate_runs.py <checklist.md> <run1.md> <run2.md> <run3.md> [...]

All runs must be on the same document (full protocol: N independent runs).
Rules:
- «да» counts only when every run answered «да».
- Anything else («нет», mixed) collapses to «нет», marked «спорно, k/N да»
  when at least one run said «да» — the per-run answers are printed so the
  user sees which run disagreed.
- «н/п» stays «н/п» only when unanimous; mixed н/п collapses to «нет».
- A run that lacks an ID makes the merge abort with exit code 1.
- Verdict: any MVP «нет» -> «Дальше нельзя»; only ПОСЛЕ-MVP «нет» ->
  «В MVP идти можно»; otherwise «Готово».

Exit code: 0 on success, 1 on incomplete input. Verdict is the last line.
"""
import re
import sys

def parse_run(path):
    answers = {}
    for line in open(path, encoding="utf-8").read().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3 or not re.match(r"^[A-Z]+-\d+$", cells[0]):
            continue
        ans = cells[2].lower().strip("*` ")
        answers[cells[0]] = {"да": "да", "нет": "нет"}.get(ans, "н/п")
    return answers

def main():
    checklist = open(sys.argv[1], encoding="utf-8").read()
    ids = re.findall(r"^\| ([A-Z]+-\d+) \|", checklist, re.M)
    levels = dict(re.findall(r"^\| ([A-Z]+-\d+) \|[^|]*\|[^|]*\|[^|]*\| (MVP|ПОСЛЕ-MVP) \|",
                           checklist, re.M))
    assert len(ids) == len(set(ids)) > 0, "checklist IDs not parsed"
    runs = [parse_run(p) for p in sys.argv[2:]]
    incomplete = [p for p, r in zip(sys.argv[2:], runs) if any(i not in r for i in ids)]
    if incomplete:
        print(f"INCOMPLETE: прогоны без всех ID: {incomplete} — сведение отменено")
        sys.exit(1)
    merged, n_yes = {}, {}
    for qid in ids:
        votes = [r[qid] for r in runs]
        n_da = n_yes[qid] = votes.count("да")
        if n_da == len(votes):
            merged[qid] = "да"
        elif set(votes) == {"н/п"}:
            merged[qid] = "н/п"
        else:
            merged[qid] = "нет" if n_da == 0 else f"нет (спорно, {n_da}/{len(votes)} да)"
    # dependency collapse AFTER merge: parent «нет» -> child «н/п»
    parents = dict(re.findall(r"^\| ([A-Z]+-\d+) \|[^|]*\|[^|]*\|[^|]*\| (?:MVP|ПОСЛЕ-MVP) \| ([A-Z]+-\d+) \|",
                            checklist, re.M))
    for qid in ids:
        p = parents.get(qid)
        if p and merged.get(p, "").startswith("нет"):
            merged[qid] = "н/п"
    assert not any(merged[c] == "да" and merged.get(p, "").startswith("нет")
                   for c, p in parents.items()), "child да under parent нет"
    mvp_no, post_no = [], []
    for qid in ids:
        if merged[qid].startswith("нет"):
            (mvp_no if levels[qid] == "MVP" else post_no).append(
                f"{qid}{f' ({n_yes[qid]}/{len(runs)})' if n_yes[qid] else ''}")
        votes = " / ".join(r[qid] for r in runs)
        print(f"{qid}: {merged[qid]}  <- [{votes}]")
    verdict = ("Дальше нельзя" if mvp_no else
               "В MVP идти можно, до масштабирования закрыть пробелы" if post_no
               else "Готово")
    print(f"VERDICT {verdict} | MVP-нет: {', '.join(mvp_no) or '—'} | "
          f"ПОСЛЕ-MVP-нет: {', '.join(post_no) or '—'}")

if __name__ == "__main__":
    main()
