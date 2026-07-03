# decision log v0.1 — ai pm plugin

дата: 2026-07-03  
статус: рабочий список ключевых архитектурных решений

этот файл — компактный decision log. подробный контекст лежит в `full-context-v0.4.md` и `ai-pm-plugin-handoff-v0.3.md`.

---

## d1. строим не генератор документов, а систему движения по зрелости

решение:

```text
ai pm plugin помогает продакту двигать продуктовую работу по maturity flow.
```

неправильная рамка:

```text
сгенерировать opportunity doc / prd / quarter plan.
```

правильная рамка:

```text
diagnose state → choose workflow → fill gaps → move entity to next meaningful decision.
```

следствие:

```text
документ — это representation of entity state.
```

---

## d2. документ — не главная сущность

решение:

```text
opportunity doc = представление opportunity item.
prd = представление solution item.
quarter plan = представление набора bets / commitments.
```

следствие:

```text
нужны entity graph, maturity model, artifact renderer/parser.
```

---

## d3. сначала диагностика, потом генерация

решение:

```text
плагин не должен начинать с “сейчас напишу документ”.
```

он должен сначала понять:

```text
что принес пользователь;
какая это сущность;
есть ли дубль в backlog;
какой maturity level;
чего не хватает;
какой workflow применим;
что должен подтвердить человек.
```

---

## d4. есть два разных backlog-а

решение:

```text
opportunity backlog и solution / prd backlog — две разные очереди принятия решений.
```

opportunity backlog отвечает:

```text
какие проблемы / opportunities достойны внимания?
```

solution / prd backlog отвечает:

```text
какие решения / гипотезы достойны prd / delivery / test?
```

---

## d5. signal и opportunity doc — состояния одного opportunity item

решение:

```text
opportunity item:
raw signal → framed opportunity → evidence-backed opportunity → decision-ready opportunity.
```

maturity:

```text
opp-r0: raw signal
opp-r1: framed opportunity
opp-r2: evidence-backed opportunity
opp-r3: decision-ready opportunity
```

---

## d6. solution candidate и prd — состояния одного solution item

решение:

```text
solution item:
solution candidate → framed solution → prd-ready solution → prd-r1 → prd-r2 → prd-r3.
```

prd не рождается из воздуха. он начинается с выбранного solution candidate.

---

## d7. opportunity doc заканчивается decision-ready opportunity + 1–3 solution candidates

решение:

```text
opportunity doc не обязан выбрать одно финальное решение.
```

он должен довести работу до:

```text
validated / decision-ready opportunity;
рекомендации kill / park / continue / generate solutions;
1–3 solution candidates.
```

---

## d8. prd начинается с выбранного solution candidate

решение:

```text
prd — следующий уровень зрелости solution item.
```

prd не должен начинаться с сырого сигнала или просто хотелки.

---

## d9. solution idea detox — обязательный паттерн

решение:

```text
если pm приходит с фичей, плагин должен развернуть ее обратно в проблему.
```

пример:

```text
“сделаем ai-помощника” → какую проблему решаем, для кого, в каком сценарии, какое поведение меняем, какую метрику двигаем?
```

цель:

```text
не дать фиче притвориться проблемой.
```

---

## d10. user-facing модули шире, чем 3 презентационных модуля

решение:

```text
пользовательская архитектура:
0. context collection / onboarding
1. entry / router
2. opp doc module
3. opp backlog module
4. solution / prd module
5. solution / prd backlog module
6. planning module
```

три модуля `opp doc / solution-prd / planning` — хороший фасад для простого объяснения, но для продукта нужны еще context, router и backlog management.

---

## d11. backlog modules — не только internal storage

решение:

```text
opp backlog module и solution/prd backlog module пользователь должен видеть и явно активировать.
```

они управляют:

```text
duplicates;
merge/link/create decisions;
prioritization;
stale items;
readiness;
park / kill / continue;
shortlists.
```

---

## d12. context module сначала мокаем

решение:

```text
real context module не строим первым.
```

сначала делаем mock context pack, потому что неизвестно, какие контекстные поля реально нужны workflow.

real context module — phase 5.

---

## d13. planning делаем последним

решение:

```text
planning module зависит от всего остального.
```

он должен смотреть на:

```text
context;
opp backlog;
solution/prd backlog;
maturity;
capacity;
dependencies;
intent type;
readiness.
```

поэтому сначала opp doc, потом solution/prd, потом backlog-и, потом planning.

---

## d14. в planning пока два типа ставок

решение:

```text
discovery bet:
signal / opportunity → solution candidates

delivery bet:
solution / hypothesis / prd → prod / test
```

эксперимент пока остается внутри delivery bet через `delivery_mode`.

---

## d15. не все ставки обязаны быть metric bets

решение:

```text
каждая ставка должна иметь intent, но не каждая должна быть напрямую связана с метрикой квартала.
```

intent types:

```text
metric;
strategic_learning;
capability_platform;
risk_quality_compliance;
business_stakeholder.
```

---

## d16. не делаем downstream invalidation / heavy revision log

была идея:

```text
если старый блок переписан, инвалидировать downstream-блоки и писать revision log.
```

решение:

```text
не берем это сейчас.
```

причина:

```text
переусложняет систему и может сделать ux тяжелым.
```

---

## d17. maturity не равна заполненности блоков

решение:

```text
maturity = готовность сущности к следующему meaningful decision.
```

не:

```text
заполнены 7 из 10 секций.
```

пример:

```text
“сегмент: все пользователи” формально заполнено, но качественно слабое.
```

---

## d18. не микроменеджим сильные модели

решение:

```text
не проектируем специалистов через сверхдетальные микрошаги.
```

проектируем через:

```text
role;
goal;
desired output;
anti-output;
quality guardrails;
human gates.
```

---

## d19. workflow registry нужен позже

решение:

```text
workflow registry — полезная идея как machine-readable каталог движений системы, но не первый приоритет.
```

сначала надо понять canonical flows и module behavior.

---

## d20. первый инкремент — opp doc module

решение:

```text
phase 1 = mock context + router lite + opp doc module + mock backlogs.
```

цель:

```text
signal / weak opp / solution idea → opp-r3 → 1–3 solution candidates → mock solution backlog.
```

---

## d21. simulations / evals — в backlog

решение:

```text
позже нужно взять примеры доков / кейсов и прогнать flow с нуля до конца.
```

кейсы:

```text
raw signal;
solution idea without problem;
weak opportunity doc;
duplicate-like signal;
solution candidate to prd;
messy initiatives to quarter shortlist.
```
