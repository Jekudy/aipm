#!/usr/bin/env python3
"""check_quotes.py — mechanical quote verification for aipm-problem-audit runs.

Usage: check_quotes.py <run-report.md> <source.md> <checklist.md>

Every ID from checklist.md must appear in the report exactly once.
A missing or duplicated ID aborts with exit code 1 — no verdict is printed.
A skipped question must never silently become «нет».

For every answer «да» in the report table, each quoted fragment (inside «...»
or "...") must appear verbatim in the source after normalization
(whitespace collapsed, markdown markup stripped). Fragments separated by
ellipsis (…, ..., ...) are checked independently.

A «да» whose quote is not found is counted as «нет» for verdict recomputation.
Prints flagged rows and the recomputed verdict (MVP failures decide).

Exit code: 0 always; verdict line is the last output line.
"""
import re
import sys

def normalize(text):
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)  # [t](url), ![t](url)
    text = re.sub(r"[*_~`#|]+", " ", text)
    text = re.sub(r"[«»\"'“”„]", "", text)
    text = re.sub(r"[–—−→]", "-", text)
    text = re.sub(r"[^\w\s%]", " ", text)  # punctuation -> space
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()

def fragments(cell):
    cell = re.sub(r"\((?:стр|с|lines?|строки?)\.?\s*[^)]*\)", " ", cell)  # locators
    cell = cell.strip()
    if cell.startswith(("не найдено", "родитель")):
        return []
    quoted = re.findall(r"[«\"]([^«»\"]+)[»\"]", cell)
    parts = quoted if quoted else [cell]
    out = []
    for p in parts:
        for frag in re.split(r"…|\.\.\.| — | — ", p):
            frag = normalize(frag)
            if len(frag) >= 15:  # ignore crumbs too short to be evidence
                out.append(frag)
    return out

def main():
    report = open(sys.argv[1], encoding="utf-8").read()
    source = normalize(open(sys.argv[2], encoding="utf-8").read())
    cl_text = open(sys.argv[3], encoding="utf-8").read()
    expected = re.findall(r"^\| ([A-Z]+-\d+) \|", cl_text, re.M)
    assert len(expected) == len(set(expected)), "duplicate IDs in checklist"
    # declared "must not reuse a quote from" pairs: column «Не опирается на цитату из»
    noquote = {}
    for cl in cl_text.splitlines():
        cc = [x.strip() for x in cl.strip().strip("|").split("|")]
        if len(cc) >= 7 and re.match(r"^[A-Z]+-\d+$", cc[0]):
            noquote[cc[0]] = cc[6] if re.match(r"^[A-Z]+-\d+$", cc[6]) else None
    seen, bad, rows, qfrags = [], [], [], {}
    dupq = []
    for line in report.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5 or not re.match(r"^[A-Z]+-\d+$", cells[0]):
            continue
        qid, answer, quote, level = cells[0], cells[2].lower(), cells[3], cells[4]
        seen.append(qid)
        rows.append((qid, answer, level))
        if answer != "да":
            continue
        frags = fragments(quote)
        qfrags[qid] = frags
        missing = [f for f in frags if f not in source]
        if missing or not frags:
            bad.append((qid, quote[:80], missing[:1]))
    for qid, frags in qfrags.items():
        other = noquote.get(qid)
        if other and other in qfrags and set(frags) & set(qfrags[other]):
            dupq.append((qid, other))
    missing = [q for q in expected if q not in seen]
    dup = [q for q in seen if seen.count(q) > 1]
    extra = [q for q in seen if q not in expected]
    if missing or dup or extra:
        print(f"INCOMPLETE: пропущены {missing or '—'} | дубли {dup or '—'} | "
              f"лишние {extra or '—'} — вердикт не выдан")
        sys.exit(1)
    for qid, other in dupq:
        print(f"DUPQUOTE {qid}: цитата совпадает с {other} — уходит в ремонтный "
              f"проход: своя цитата под «Да, если» или «нет»")
    for qid, quote, miss in bad:
        print(f"BAD {qid}: «{quote}» — не найдено дословно: {miss or ['<нет цитаты>']}")
    flagged = {b[0] for b in bad} | {d[0] for d in dupq}
    mvp_no = [qid for qid, a, lvl in rows if lvl == "MVP"
              and (a == "нет" or qid in flagged)]
    post_flagged = [qid for qid, a, lvl in rows
                    if lvl != "MVP" and (a == "нет" or qid in flagged)]
    verdict = ("Дальше нельзя" if mvp_no else
               "В MVP идти можно, до масштабирования закрыть пробелы"
               if post_flagged else "Готово")
    print(f"VERDICT {verdict} | MVP-нет: {', '.join(mvp_no) or '—'} | "
          f"битых цитат: {len(bad)} | одинаковых цитат: {len(dupq)}")
    # self-test
    assert normalize("« Доля  заказов»") == normalize("\"доля заказов\""), "normalize"
    assert fragments('«кот»') == [], "crumb filter"
    assert len(expected) > 0, "checklist IDs not parsed"

if __name__ == "__main__":
    main()
