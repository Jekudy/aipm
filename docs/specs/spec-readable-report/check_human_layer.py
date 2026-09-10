#!/usr/bin/env python3
"""Проверка человеческого слоя отчёта review-скиллов (SPEC-readable-report, CAP-1).

Использование: check_human_layer.py report.md [report2.md …]
Выход 1, если в человеческом слое есть коды машинного слоя, ID критериев
или он длиннее 25 строк. Без аргументов запускает самопроверку.
"""
import re
import sys

DETAILS = re.compile(r"<details>.*?</details>", re.S)
QUOTE = re.compile(r"«[^»]*»")            # дословные цитаты из документа не проверяем
CODE = re.compile(r"\b[A-Z][A-Z0-9_]{2,}\b")  # NOT_READY, BLOCKED, PROVIDE_EVIDENCE …
CRIT = re.compile(r"\b(?:DB|S|P|V|REL|ER|INF|CONF|Q|R|ST)-[A-Z0-9-]+\b|\bD[34]\.\d+\b")
# ponytail: аббревиатуры домена, разрешённые в прозе; расширять по итогам прогонов
ALLOWED = {"PRD", "MVP", "SQL", "PF", "SLA", "API", "KYC", "AB", "KILL", "HIGH"}
MAX_LINES = 25
# ponytail: жаргон, утекавший в калибровке 2026-09-10; расширять по прогонам
FORBIDDEN = ("атом", "assets/", "шапка воздействий", "manifest", "машинн")


def violations(report: str) -> list[str]:
    human = QUOTE.sub("«…»", DETAILS.sub("", report))
    bad = [t for t in CODE.findall(human) if t not in ALLOWED]
    bad += CRIT.findall(human)
    bad += [w for w in FORBIDDEN if w in human.lower() and not (w == "машинн" and human.lower().count("машинн") <= human.lower().count("в машинном слое"))]
    lines = [l for l in human.strip().splitlines() if l.strip()]
    if len(lines) > MAX_LINES:
        bad.append(f"строк без машинного слоя: {len(lines)} > {MAX_LINES}")
    return bad


def demo() -> None:
    old = "NOT_READY / CONTINUE_CANDIDATE; candidate_available=true; d5_mode=null\n1. [PREFLIGHT-DB-01] …"
    assert violations(old), "старый формат должен проваливаться"
    new = (
        "## Проверка: Документ\n**Что проверяли:** можно ли принять решение «признать проблему» (D2).\n"
        "**Вердикт:** Недостаточно: 1 препятствие\n### Чего не хватает (показано 1, ещё 0 в машинном слое)\n"
        "1. **Нет ссылки на источник**\n   Где: «S-02 SOURCE_REF_MISSING внутри цитаты допустим», §1.\n"
        "<details><summary>Машинный слой</summary>\naudit:\n  dossier_status: NOT_READY\n</details>"
    )
    assert violations(new) == [], violations(new)
    assert violations(new + "\nЧто сделать: дописать недостающие атомы"), "жаргон должен ловиться"
    print("self-check OK")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        demo()
        sys.exit(0)
    rc = 0
    for path in sys.argv[1:]:
        bad = violations(open(path, encoding="utf-8").read())
        print(f"{path}: {'OK' if not bad else 'FAIL ' + ', '.join(bad)}")
        rc |= bool(bad)
    sys.exit(rc)
