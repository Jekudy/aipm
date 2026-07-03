# phase 1: opp doc module v0.1

дата: 2026-07-03  
статус: первый целевой инкремент архитектуры

## 0. зачем этот документ

этот документ фиксирует первый реальный инкремент ai pm plugin.

мы договорились не начинать с planning, real context или полной платформенной архитектуры. первый кирпич — это opp doc module, потому что он создает дисциплину на входе всей продуктовой работы.

цель phase 1:

```text
пользователь приходит с signal / weak opportunity doc / solution idea;
плагин диагностирует вход;
ведет opportunity item до opp-r3;
на выходе есть opportunity doc и 1–3 solution candidates;
solution candidates можно положить в mock solution backlog.
```

---

## 1. scope phase 1

входит:

- mock context pack;
- entry / router lite;
- opportunity entity model;
- opp maturity r0/r1/r2/r3;
- canonical flow для opp doc;
- solution idea detox;
- weak opp doc review;
- duplicate detection lite;
- generation of 1–3 solution candidates;
- mock opportunity backlog;
- mock solution backlog;
- lightweight quality checks.

не входит:

- полноценный context module;
- полноценные backlog-модули;
- solution / prd module;
- planning module;
- tech decomposition;
- тяжелый revision / invalidation log;
- production-grade integrations со stash / jira / bi.

---

## 2. главный принцип phase 1

плагин не начинает с генерации opportunity doc.

он начинает с диагностики:

```text
1. что принес пользователь?
2. это signal, solution idea, weak doc или existing backlog item?
3. есть ли похожий item в backlog?
4. какой maturity level сейчас?
5. какой следующий meaningful step?
6. чего не хватает?
7. что может сделать ai?
8. что должен подтвердить pm?
```

только потом он помогает писать / улучшать / двигать item.

---

## 3. mock context pack

на первом этапе context module мокаем.

минимальный context pack:

```yaml
product_area:
team:
pm_level:
user_segments:
core_scenarios:
main_metric:
input_metrics:
guardrail_metrics:
current_goals:
strategic_context:
data_sources:
research_sources:
stakeholders:
known_constraints:
artifact_templates:
```

минимум для запуска opp doc workflow:

```text
product_area
user_segments
core_scenarios
main_metric или target outcome
current_goals / intent
data_sources
research_sources
```

если критического контекста нет, плагин не должен выдумывать уверенно. он должен сказать:

```text
мне не хватает контекста, чтобы нормально оценить opportunity.
минимально нужно уточнить: сегмент, сценарий, метрику/outcome и источники evidence.
```

---

## 4. entity: opportunity item

phase 1 работает с `opportunity item`.

это не просто doc. это рабочая сущность, которая может начинаться как сырой сигнал и взрослеть до decision-ready opportunity.

примерная структура:

```yaml
id:
type: opportunity_item
maturity: opp-r0 | opp-r1 | opp-r2 | opp-r3
status: new | in_discovery | decision_ready | solutions_generated | parked | killed
linked_signals: []
source:
owner:
product_area:
segments: []
scenarios: []
target_metric_or_outcome:
problem_hypotheses: []
evidence_summary:
alternative_explanations: []
impact_estimate:
confidence:
unknowns: []
recommended_decision:
solution_candidates: []
created_at:
updated_at:
```

важно: не надо делать это сразу тяжелой схемой. это ориентир для mock store и будущего entity graph.

---

## 5. maturity ladder

### opp-r0: raw signal

что есть:

```text
сырой сигнал: метрика, жалоба, наблюдение, инсайт, запрос стейкхолдера, идея, аномалия.
```

минимально полезное состояние:

```text
что произошло;
источник сигнала;
когда / где замечено;
кого потенциально касается;
почему обратили внимание;
какая метрика / сценарий может быть связан.
```

пример:

```text
просела конверсия новых продавцов из начала подачи объявления в успешную публикацию.
источник: dashboard activation funnel.
сегмент: новые private sellers.
```

### opp-r1: framed opportunity

что есть:

```text
сигнал превращен в первичную problem / opportunity hypothesis.
```

должно появиться:

```text
problem / opportunity hypothesis;
affected segment;
user scenario;
current behavior;
desired behavior;
связь с метрикой / outcome;
первые validation questions.
```

пример плохой формулировки:

```text
нужно сделать ai-помощника.
```

пример хорошей формулировки:

```text
новые продавцы в категории x не доходят до первой успешной публикации,
потому что не понимают требования к фото и описанию,
из-за чего бросают flow на шаге заполнения объявления.
```

### opp-r2: evidence-backed opportunity

что есть:

```text
opportunity проверена на реальности хотя бы базово.
```

должно появиться:

```text
evidence из данных / исследований / саппорта / наблюдений;
размер affected segment;
частотность проблемы;
связь с метрикой;
альтернативные объяснения;
оценка confidence;
примерный impact;
список unknowns.
```

важно: opp-r2 — это не “док выглядит убедительно”. это “основные claims не висят в воздухе”.

### opp-r3: decision-ready opportunity

что есть:

```text
opportunity готова к решению: kill / park / continue discovery / generate solutions.
```

должно появиться:

```text
четкое opportunity statement;
сегмент;
сценарий;
current behavior;
desired behavior;
metric / outcome;
impact estimate;
confidence;
strategic fit или intent;
risk of doing nothing;
recommendation;
1–3 top solution candidates.
```

выход:

```text
opportunity doc;
decision summary;
1–3 solution candidates;
обновление opp backlog;
запись solution candidates в mock solution backlog.
```

---

## 6. key entry points

### entry point a: raw signal

пользователь приходит с сырым сигналом:

```text
просела метрика;
пользователи жалуются;
аналитик принес аномалию;
саппорт принес боль;
стейкхолдер сказал “надо разобраться”.
```

плагин делает:

- отделяет факт от интерпретации;
- формулирует возможные problem hypotheses;
- предлагает affected segments;
- предлагает validation questions;
- ищет похожие opportunities в mock backlog;
- предлагает создать новый item или привязаться к существующему;
- собирает opp-r1 skeleton.

выход:

```text
opp-r1 draft;
problem hypotheses;
validation questions;
duplicate/linking suggestions;
next tasks.
```

### entry point b: weak opportunity doc

пользователь приносит черновик opportunity doc.

типичные проблемы:

- много воды;
- мало evidence;
- проблема похожа на решение;
- непонятен сегмент;
- непонятен impact;
- неясно, что делать дальше.

плагин делает:

- парсит doc в opportunity item state;
- оценивает maturity;
- находит weak / missing / unclear parts;
- предлагает, что нужно для следующего maturity level;
- улучшает формулировки;
- формирует validation tasks.

выход:

```text
maturity assessment;
gaps;
улучшенный opp doc;
next tasks для r2/r3.
```

### entry point c: solution idea detox

пользователь приходит с решением:

```text
давайте сделаем ai-помощника;
давайте изменим форму;
давайте добавим подсказки;
давайте переделаем onboarding.
```

плагин не дает фиче притвориться проблемой.

он спрашивает / помогает вывести:

- какую проблему это решение пытается решить;
- для какого пользователя;
- в каком сценарии;
- какое поведение должно измениться;
- какую метрику / outcome хотим сдвинуть;
- какие есть альтернативные решения;
- есть ли похожая opportunity в backlog.

выход:

```text
opp-r1 draft;
problem hypothesis;
original solution as candidate;
alternative solution directions;
duplicate/linking suggestions.
```

### entry point d: existing backlog item

пользователь хочет продолжить существующую opportunity.

плагин делает:

- читает current state;
- определяет maturity;
- показывает, чего не хватает до следующего уровня;
- предлагает workflow продолжения.

выход:

```text
current maturity;
recommended next workflow;
gaps;
next tasks.
```

### entry point e: duplicate-like signal

пользователь приносит новый сигнал, который похож на старую opportunity.

плагин делает:

- ищет похожие items;
- объясняет сходство;
- спрашивает: merge / link / create new;
- помогает сформулировать, чем это новое отличается.

выход:

```text
merge/link/create recommendation;
обновленный linked_signals;
или новый opportunity item.
```

---

## 7. canonical flow для opp doc

идеальный путь:

```text
1. capture signal
2. classify input
3. check duplicates
4. frame problem / opportunity hypothesis
5. identify segment and scenario
6. define current behavior and desired behavior
7. connect to metric / outcome / intent
8. create validation questions
9. plan evidence checks
10. review evidence
11. identify alternative explanations
12. estimate impact and confidence
13. form decision-ready opportunity
14. generate 1–3 solution candidates
15. push solution candidates to solution backlog
```

важно: это canonical flow, а не жесткий микроскрипт. пользователь может входить в середине. модель должна понимать, что already known, а что missing.

---

## 8. solution candidate output

opp-r3 должен породить 1–3 solution candidates.

минимальная структура:

```yaml
solution_id:
parent_opp_id:
name:
problem:
segment:
scenario:
solution_hypothesis:
target_behavior:
target_metric_or_outcome:
why_it_might_work:
main_assumptions:
expected_effect:
confidence:
risks:
mvp_hint:
status: new_solution_candidate
```

solution backlog не должен принимать голые идеи.

плохо:

```text
сделать ai-помощника.
```

лучше:

```text
если мы добавим inline-подсказки новым продавцам на шаге заполнения объявления,
то повысим first successful listing rate,
потому что сейчас пользователи бросают flow из-за непонимания требований к фото и описанию.
```

---

## 9. specialist behavior: как не микроменеджить модель

в phase 1 лучше описывать ai-специалистов не через 40 микрошагов, а через desired / anti-output.

### specialist: signal interpreter

цель:

```text
превратить сырой сигнал в набор возможных problem hypotheses и validation questions.
```

хочет получить:

- факт vs интерпретация;
- возможные problem hypotheses;
- affected segments;
- связанные metrics / outcomes;
- first validation questions;
- suggestion: create / merge / ignore / escalate.

не хочет получить:

- уверенное заключение без evidence;
- готовое решение;
- фичу вместо проблемы;
- игнорирование похожих backlog items.

### specialist: solution idea detoxer

цель:

```text
не дать идее решения притвориться проблемой.
```

хочет получить:

- problem hypothesis;
- target user / segment;
- scenario;
- target behavior;
- metric / outcome;
- original idea as solution candidate;
- альтернативные решения.

не хочет получить:

- prd из воздуха;
- уверенное утверждение, что фича нужна;
- натягивание проблемы под любимое решение;
- игнорирование похожих opportunities.

### specialist: opp doc reviewer

цель:

```text
понять maturity документа и показать, чего не хватает для следующего решения.
```

хочет получить:

- current maturity;
- weak / missing / unclear areas;
- unsupported claims;
- missing evidence;
- alternative explanations;
- next tasks;
- recommendation: continue / park / kill / generate solutions.

не хочет получить:

- просто красивый rewrite;
- оценку “все хорошо” без критики;
- фокус только на стиле;
- микроменеджмент каждого абзаца.

### specialist: solution candidate generator

цель:

```text
из decision-ready opportunity получить 1–3 нормальных solution candidates.
```

хочет получить:

- solution hypotheses;
- target behavior;
- metric / outcome link;
- why it might work;
- assumptions;
- risks;
- mvp hint.

не хочет получить:

- random feature ideas;
- решения без parent opportunity;
- 15 идей ради креатива;
- игнорирование constraints.

---

## 10. mock backlog behavior

phase 1 должен иметь mock backlog store, даже если это просто файл / json / таблица.

### mock opp backlog

хранит:

- opportunity items;
- linked signals;
- maturity;
- status;
- owner;
- target metric / outcome;
- updated_at;
- solution candidates generated.

### mock solution backlog

хранит:

- solution candidates;
- parent opportunity;
- target behavior;
- target metric / outcome;
- confidence;
- status.

### duplicate detection lite

при новом input плагин должен искать похожее по:

- segment;
- scenario;
- metric / outcome;
- problem hypothesis;
- source / signal type;
- keywords.

выход:

```text
нашел похожие items:
1. opp-123 — похожий сегмент и метрика
2. opp-087 — похожий сценарий

это продолжение существующей opportunity или новая?
```

---

## 11. quality checks для phase 1

плагин должен ловить основные ошибки:

- проблема сформулирована как фича;
- нет сегмента;
- нет сценария;
- нет связи с behavior / metric / outcome;
- evidence слабый или отсутствует;
- impact просто заявлен, но не обоснован;
- нет alternative explanations;
- solution candidates не вытекают из opportunity;
- создается дубль существующей opportunity;
- pm пытается сразу писать prd из идеи.

важно: checks должны возвращать к дисциплине, но не блокировать без необходимости.

пример:

```text
можно продолжить fast-track, но я помечаю это как low-confidence bet:
- parent opportunity не подтверждена;
- target behavior не сформулирован;
- success metric не определен.
```

---

## 12. phase 1 outputs

минимальные outputs:

```text
1. opportunity doc r1/r2/r3
2. maturity assessment
3. gaps / missing evidence / weak claims
4. validation tasks
5. decision summary
6. 1–3 solution candidates
7. update mock opp backlog
8. update mock solution backlog
```

---

## 13. success criteria phase 1

phase 1 считается успешной, если система умеет пройти 4 симуляции:

### case 1. raw signal

input:

```text
просела метрика / появилась аномалия / пользователи жалуются.
```

expected:

```text
signal → opp-r1 → validation plan → opp-r2/r3 draft.
```

### case 2. solution idea

input:

```text
давайте сделаем ai-помощника.
```

expected:

```text
solution idea detox → problem hypothesis → opp-r1 → original solution as candidate.
```

### case 3. weak opp doc

input:

```text
существующий doc с водой и слабым evidence.
```

expected:

```text
maturity assessment → gaps → improvement plan → improved doc.
```

### case 4. duplicate-like signal

input:

```text
новый сигнал похож на старую opportunity.
```

expected:

```text
duplicate candidates → merge/link/create decision → updated backlog state.
```

---

## 14. что делать сразу после phase 1

после phase 1 логичный следующий инкремент:

```text
phase 2: solution / prd module
```

цель:

```text
solution candidate
→ prd readiness
→ prd-r1/r2/r3
```

но переходить к нему стоит только после того, как opp doc module устойчиво порождает нормальные solution candidates.
