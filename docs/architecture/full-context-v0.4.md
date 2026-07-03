# full context v0.4 — ai pm plugin

дата: 2026-07-03  
статус: максимально полный контекст архитектурной проработки  
назначение: сохранить все важные мысли, решения, развилки, ограничения и следующий вектор работы.

этот документ длиннее и менее “полированный”, чем handoff. его задача — сохранить весь набранный контекст, чтобы потом можно было самому резать, переупаковывать, делать prd, prompts, workflow specs, архитектурные docs и roadmap.

---

## 0. исходный запрос

исходная задача: помочь продактам авито быстрее и лучше выполнять базовые продуктовые задачи с помощью ai / llm / claude code / плагина.

первичная формулировка была шире:

```text
нагенерить workflow и skills для продактов;
покрыть путь от ежедневной работы до квартального планирования;
понять гранулярность этапов работы;
понять разнообразие этапов и их взаимосвязи;
описать входные и выходные артефакты;
последовательно усиливать или заменять части работы с помощью ai / llm / claude code.
```

контекст пользователя:

```text
пользователь — senior product в авито.
фокус сначала на всех продактах, особенно junior/middle/senior pm.
цель — помочь продактам быстрее и лучше работать, не просто сделать презентацию.
```

---

## 1. ранняя рамка: не workflow, а product operating system

на старте было предложено думать не как “сгенерить workflow”, а как:

```text
ai-усиливаемая операционная система работы продакта.
```

первичная карта работы pm:

```text
стратегия / цели
→ квартальное планирование
→ discovery
→ opportunity / problem framing
→ solution framing
→ prd
→ delivery
→ launch
→ post-analysis
→ learning / backlog update
```

но затем фокус сузился.

---

## 2. ранняя команда виртуальных специалистов

первично были предложены виртуальные роли:

1. **product workflow architect** — верхнеуровневая карта работы pm.
2. **researcher of pm work** — вытаскивает реальную работу, а не официальную версию процесса.
3. **workflow cartographer** — дробит работу на workflow / task / decision / artifact.
4. **artifact architect** — описывает входы и выходы каждого этапа.
5. **dependency / handoff specialist** — показывает связи между этапами.
6. **product strategy / planning lead** — квартальное планирование и trade-offs.
7. **ai automation architect** — классифицирует ai-fit и уровни автоматизации.
8. **claude code / agent engineer** — переводит workflow в команды / agents / prompts.
9. **product enablement / skill coach** — skills и развитие pm.
10. **governance / quality / security specialist** — качество, безопасность, контроль outputs.

позже роли были ужаты под фактическую архитектуру и принцип “не микроменеджить сильные модели”.

важный итог: виртуального специалиста нужно описывать не как 40 микрошагов, а через:

```text
роль;
цель;
что хотим получить;
чего не хотим получить;
какие ошибки он ловит;
какие решения должен оставить человеку;
какие boundaries соблюдать.
```

---

## 3. ответы пользователя на первичное интервью

ключевые ответы пользователя:

```text
целевая аудитория:
все продакты авито, особенно junior/middle/senior.

главная цель сначала:
ускорить работу продактов.

потом:
сделать ai-copilot для pm;
найти части работы, которые можно заменить / автоматизировать;
потенциально подготовить transformation program.

хороший результат:
карта workflow продакта;
для workflow прописаны шаги и этапы;
сделаны ai-workflow для некоторых этапов;
есть система оценки.

боли:
квартальное планирование;
написание prd;
написание opportunity doc / problem doc;
частично prioritization.

режим описания:
gap map — as-is + to-be + разница.

гранулярность:
уровень 3, иногда 4:
workflow → задачи → иногда микродействия,
но позже появилась важная поправка: не микроменеджить сильные модели.

где жить:
stash / внутренний гид авито,
но контракты не обязательно описывать в stash как отдельные страницы.
```

---

## 4. первая важная развилка: problem doc / opportunity doc / prd

обсуждался вопрос:

```text
на чем должен заканчиваться problem/opportunity doc?
на куче решений?
на ряде проблем?
на выбранной гипотезе проблемы?
на выбранной гипотезе решения?

на чем должен начинаться prd?
```

первичный вывод:

```text
problem/opportunity doc не должен отвечать “что строим?”.
он должен отвечать “какую проблему / opportunity стоит решать, почему, для кого, насколько мы уверены, и что дальше?”.
```

позже это уточнилось:

```text
opportunity doc заканчивается decision-ready opportunity + 1–3 solution candidates.
prd начинается с выбранного solution candidate.
```

важный принцип:

```text
opportunity doc может содержать решения, но как пространство решений / кандидатов, а не как финальную спецификацию.
```

---

## 5. текущие ключевые сущности

сначала пользователь предложил такие сущности:

```text
signal
opportunity doc как проработка сигнала
opportunity backlog
solution backlog
solution candidate
prd
prioritization для каждого backlog-а
```

позже добавились:

```text
context / onboarding
entry / router
planning bets
intent
evidence
assumptions
risks
metrics
```

главная модель:

```text
signal и opportunity doc — состояния одного opportunity backlog item.
solution candidate и prd — состояния одного solution backlog item.
```

то есть:

```text
opportunity item:
raw signal → framed opportunity → evidence-backed opportunity → decision-ready opportunity

solution item:
solution candidate → framed solution → prd-ready solution → prd-r1 → prd-r2 → prd-r3
```

---

## 6. два backlog-а как две очереди принятия решений

сильное решение:

```text
есть 2 разные очереди принятия решений.
```

### opportunity backlog

отвечает на вопрос:

```text
какие проблемы / opportunities достойны внимания и discovery?
```

содержит:

```text
signals;
opportunity candidates;
opportunity docs;
validated opportunities;
parked / killed opportunities;
opportunities, которые породили solutions.
```

критерии приоритизации:

```text
сила сигнала;
размер affected segment;
частотность;
user pain;
metric / outcome connection;
strategic fit;
urgency;
confidence;
cost to learn more;
risk of inaction.
```

### solution / prd backlog

отвечает на вопрос:

```text
какие решения / гипотезы достойны prd / delivery / test?
```

содержит:

```text
solution candidates;
framed solutions;
prd candidates;
prd-r1/r2/r3;
parked / killed solutions;
launched / measured solutions.
```

критерии приоритизации:

```text
expected impact;
confidence;
effort / capacity;
time-to-learn;
dependency complexity;
risk;
reversibility;
mvp clarity;
strategic fit;
metric / intent fit.
```

важное правило:

```text
solution backlog не должен становиться помойкой идей.
голая идея “сделать ai-помощника” не должна попадать туда без parent opportunity и product hypothesis.
```

---

## 7. many-to-many связи

модель должна поддерживать many-to-many, потому что реальная продуктовая работа нелинейна.

связи:

```text
один signal может породить несколько opportunities;
одна opportunity может подтверждаться несколькими signals;
одна opportunity может породить 1–3+ solution candidates;
один solution candidate может закрывать несколько opportunities;
один prd обычно связан с одним главным solution candidate, но может закрывать несколько opportunities;
один quarter bet может включать несколько opportunities / solutions;
одна метрика может связывать много opportunities / bets.
```

важность:

```text
это нужно для dedupe, linking, router-а, planning и будущего entity graph.
```

---

## 8. три контура, потом расширенные user-facing модули

сначала архитектура свелась к трем контурам:

```text
1. opportunity contour
signal → opportunity doc → solution candidates

2. solution / prd contour
solution candidate → prd → delivery/test readiness

3. planning contour
opportunities / solutions / prds → quarterly bets / plan
```

позже стало понятно, что для продукта и разработки нужно больше пользовательских зон:

```text
0. context collection / onboarding
1. entry / router
2. opp doc module
3. opp backlog module
4. solution / prd module
5. solution / prd backlog module
6. planning module
```

важная поправка пользователя:

```text
backlog modules — не только внутренние слои.
пользователь должен явно видеть и активировать управление backlog-ами.
```

---

## 9. context collection / onboarding

модуль сбора контекста нужен как переиспользуемый конфиг для всех остальных модулей.

он собирает с pm информацию о специфике:

```text
product_area;
team;
pm level;
user segments;
core scenarios;
main metrics;
guardrails;
current goals;
strategy;
data sources;
research sources;
stakeholders;
constraints;
delivery cadence;
capacity;
artifact templates.
```

важное решение:

```text
на первом этапе context module мокаем.
```

почему:

```text
если сразу строить полный context module, можно построить красивый воздушный замок.
сначала надо понять, какие контекстные поля реально нужны workflow.
```

но context/onboarding как user-facing вход все равно нужен:

```text
пользователь приходит и говорит: привет, вот проект, я на такой стадии.
система должна понять, какой контекст есть и чего не хватает.
```

---

## 10. entry / router как обязательный слой

важная добавка пользователя: нужен входной интерфейс / router.

пользователь может прийти с любым входом:

```text
сырой сигнал;
идея решения;
слабый opportunity doc;
solution candidate;
prd;
цель / intent;
куча инициатив;
существующий backlog item;
“я не знаю, на какой я стадии”.
```

router должен:

```text
классифицировать input;
понять entity type;
понять stage / maturity;
найти похожие items в backlog;
предложить continue existing / create new / merge / link;
выбрать workflow;
подгрузить нужный context;
не дать плодить дубли.
```

пример:

```text
pm: хочу сделать подсказки новым продавцам.

plugin:
похоже, ты пришел с solution idea.
я нашел похожую opportunity: opp-123 про активацию новых продавцов.
это продолжение opp-123 или новая идея?

a. привязать как solution candidate к opp-123
b. создать новую opportunity
c. пройти solution detox
```

---

## 11. opp doc module

главный первый модуль.

задача:

```text
вести opportunity item от сигнала до opp-r3
и породить 1–3 solution candidates.
```

maturity:

```text
opp-r0: raw signal
opp-r1: framed opportunity
opp-r2: evidence-backed opportunity
opp-r3: decision-ready opportunity
```

entry points:

```text
у меня сырой сигнал;
у меня слабый opportunity doc;
я пришел с решением, но не доказал проблему;
у меня existing backlog item;
у меня новый сигнал, похожий на старую opportunity.
```

выходы:

```text
opportunity doc;
gaps;
validation tasks;
maturity assessment;
decision summary;
1–3 solution candidates;
update opportunity backlog;
create/update solution backlog items.
```

### solution idea detox

один из самых сильных паттернов.

если pm приходит с решением:

```text
давайте сделаем ai-помощника;
давайте добавим подсказки;
давайте переделаем onboarding;
давайте изменим форму.
```

плагин не запрещает, но возвращает к дисциплине:

```text
какую проблему решаем?
для кого?
в каком сценарии?
какое поведение хотим изменить?
какую метрику / outcome хотим сдвинуть?
какие альтернативные решения есть?
есть ли похожая opportunity в backlog?
```

исходная идея становится solution candidate, а не истиной.

---

## 12. solution / prd module

ключевая идея:

```text
prd — это следующий этап solution candidate.
```

maturity path:

```text
sol-s0: solution candidate
sol-s1: framed solution
sol-s2: prd-ready solution
prd-r1: prd skeleton
prd-r2: review-ready prd
prd-r3: delivery/test-ready prd
```

entry points:

```text
у меня есть solution candidate, можно ли писать prd?
я выбрал решение и хочу первый prd;
у меня сырой prd;
prd расползается;
непонятно, готов ли prd к работе.
```

плагин помогает:

```text
проверить parent opportunity;
сформулировать product hypothesis;
понять target behavior;
собрать scope / out of scope;
предложить metrics / guardrails;
найти risks / unknowns;
сжать scope;
понять readiness.
```

выходы:

```text
prd readiness check;
prd-r1 skeleton;
improved prd;
scope / out of scope;
metrics and guardrails;
open questions;
risks;
delivery/test readiness decision.
```

---

## 13. planning module

изначально обсуждали квартальное планирование как сильную боль.

важные решения:

```text
planning делаем последним, потому что он должен смотреть на все:
context, opportunity backlog, solution/prd backlog, maturity, capacity, dependencies, intents.
```

### два типа ставок

для v1 оставляем два типа:

```text
discovery bet:
signal / opportunity → solution candidates

delivery bet:
solution / hypothesis / prd → prod / test
```

эксперимент пока внутри delivery bet:

```text
delivery_mode = experiment | mvp | rollout | full_launch | test
```

### не все ставки metric bets

сначала была мысль, что квартальная цель всегда “изменить метрику”. потом пользователь уточнил: бывают стратегические research, которые могут дать impact только через год.

честная модель:

```text
каждая ставка должна иметь intent.
metric intent — частый, но не единственный.
```

intent types:

```text
metric;
strategic learning;
capability / platform;
risk / quality / compliance;
business / stakeholder.
```

planning output:

```text
candidate bets;
classified discovery/delivery bets;
shortlist;
not-doing list;
rough fit;
weekly/sprint maturity plan;
quarter narrative.
```

важный принцип:

```text
planning раскладывает не просто задачи, а движение сущностей по зрелости.
```

пример:

```text
discovery bet:
opp-r1 → opp-r2 → opp-r3 → solution candidates

delivery bet:
solution candidate → prd → prod/test
```

---

## 14. decomposition module — отложено и ограничено

обсуждался модуль декомпозиции, который мог бы раскладывать выбранные решения на компоненты и этапы.

пользователь уточнил:

```text
мы сейчас не беремся декомпозировать для теха.
пусть пока они сами это делают.
```

принято:

```text
decomposition пока не tech decomposition.
```

если понадобится позже, он может помогать только в продуктово-планировочном смысле:

```text
компоненты решения;
этапы работы;
зависимости;
последовательность;
параллельность;
critical path в продуктовой логике;
что можно порезать;
какие maturity milestones.
```

---

## 15. документы как representation of entity state

одна из центральных идей:

```text
документ — это правда просто представление состояния сущности.
```

следствия:

```text
пользователь может прийти не с документом, а с сигналом / идеей / куском текста / backlog item.
система должна понять entity state и только потом отрендерить документ.
```

то есть нужны два направления:

```text
entity state → artifact rendering
artifact draft → entity state extraction
```

пример:

```text
существующий слабый opp doc → parser/extractor → opportunity item state → maturity assessment → gaps → improved doc.
```

---

## 16. зрелость и блоки

пользователь предложил идею:

```text
в идеальном мире док пишется последовательно, не переписывая старые части.
если старые части нужно переписывать, возможно, проблема в структуре.
```

принято как принцип, но без тяжелого revision engine.

важное уточнение:

```text
зрелость не равна заполненный блок.
```

зрелость = готовность к следующему meaningful decision.

пример:

```text
блок “сегмент” заполнен как “все пользователи”.
формально заполнен, но по смыслу слабый.
```

рабочий подход:

```text
у сущности есть maturity level;
у документа есть важные смысловые блоки;
плагин может сказать missing / weak / unclear;
но не надо ставить детальные статусы каждому абзацу.
```

---

## 17. важная отмена: не делаем downstream invalidation

раньше была предложена идея:

```text
если переписали старый блок, нужно инвалидировать downstream-блоки и оставлять revision log.
```

пользователь отклонил:

```text
не, это не надо.
```

итог:

```text
не строим тяжелую систему invalidation / revision log.
```

можно оставить легкий trace, но не более.

---

## 18. контрактная логика

контракты понравились как идея, но не как бюрократия.

контракт — это рамка поведения системы:

```text
когда можно перейти из состояния a в состояние b?
что должно быть известно?
какой output должен появиться?
какие ошибки надо поймать?
где нужен human approval?
```

примеры переходов:

```text
raw input → classified entry
signal → opp-r1
opp-r1 → opp-r2
opp-r2 → opp-r3
opp-r3 → solution candidate
solution candidate → prd-ready solution
prd-r1 → prd-r2
prd-r2 → prd-r3
backlog item → quarter candidate bet
selected bets → weekly/sprint maturity plan
```

важная поправка:

```text
контракты не обязательно описывать в stash.
они нужны сейчас, чтобы определить фрейм для каждого модуля, движений внутри него и взаимодействий между модулями.
```

еще важнее:

```text
контракты не должны травмировать работу сильных моделей микроменеджментом.
```

---

## 19. workflow registry

идея была непонятной и сложной, но признана потенциально полезной.

простое объяснение:

```text
workflow registry — это machine-readable каталог разрешенных движений системы.
```

не команды и не промпты, а движения:

```text
из какого состояния;
в какое состояние;
какой input;
какой context нужен;
какие контракты проверить;
какой output создать;
что должен подтвердить человек.
```

пример:

```yaml
workflow_id: opp.solution_idea_detox
input: solution_idea
from_state: unknown
to_state: opp-r1
purpose: не дать фиче притвориться проблемой
outputs:
  - problem_hypotheses
  - opp_r1_draft
  - original_solution_as_candidate
human_gates:
  - confirm_parent_or_new_opportunity
  - confirm_problem_hypothesis
```

не приоритет прямо сейчас. сначала нужно понять flow.

---

## 20. core system layers

текущие внутренние слои:

```text
mock context layer → later real context layer
entity graph
state / maturity engine
contract engine
workflow registry
backlog state store
artifact renderer / parser
quality / eval layer
```

ранее обсуждался decision / revision log, но тяжелый log отложен/не берем.

---

## 21. фазы разработки

пользователь согласился с фазами.

### phase 0. mock context

не строим real context module.
делаем простой context pack.

### phase 1. opp doc module

первый настоящий инкремент:

```text
mock context;
entry/router lite;
opportunity entity;
opp maturity r0/r1/r2/r3;
canonical flow для opp doc;
solution idea detox;
weak opp doc review;
solution candidate generation;
mock opp backlog;
mock solution backlog;
duplicate detection lite.
```

цель:

```text
signal / weak opp / solution idea
→ opp-r3
→ 1–3 solution candidates
→ mock solution backlog.
```

### phase 2. solution / prd module

```text
solution candidate
→ prd readiness
→ prd-r1/r2/r3.
```

### phase 3. backlog modules

```text
opp backlog module;
solution / prd backlog module.
```

функции:

```text
управление очередями;
поиск дублей;
prioritization;
stale items;
park / kill / continue;
readiness views.
```

### phase 4. planning module

```text
intent / goal
→ candidate bets
→ discovery / delivery classification
→ shortlist
→ rough fit
→ weekly / sprint maturity plan.
```

### phase 5. real context module

возвращаемся к context module после того, как понятно, какие поля реально нужны workflow.

---

## 22. open backlog / будущие сессии

не надо пытаться решить всё в одном заходе.

темы для отдельных сессий:

```text
1. entity & state model
2. canonical flows
3. maturity model
4. contract map
5. entry / router / onboarding
6. opp doc module deep dive
7. solution / prd module deep dive
8. backlog modules
9. planning module
10. simulations / evals
11. workflow registry format
12. real context module
```

---

## 23. simulations / evals — отложено в backlog

пользователь предложил:

```text
взять примеры доков и пройти flow с нуля до конца.
```

это нужно положить в backlog.

кейсы для симуляции:

```text
сырой сигнал;
идея решения без доказанной проблемы;
слабый opportunity doc;
новый сигнал похож на существующую opportunity;
solution candidate → prd;
куча инициатив → квартальный shortlist.
```

цель:

```text
проверить, где ломается flow;
уточнить maturity;
уточнить контракты;
понять реальные workflow;
получить examples для prompts/evals.
```

---

## 24. что важно помнить про стиль ai

плагин должен возвращать к дисциплине, но не быть душнилой.

правильный UX:

```text
pm: напиши prd по этой идее.

plugin:
я могу помочь, но сейчас это похоже на solution idea, а не prd-ready solution.
не хватает parent opportunity, target behavior и success metric.

варианты:
a. пройти solution detox;
b. оформить fast-track с явными рисками;
c. создать prd-r1 с low-readiness warning.
```

важно:

```text
не блокировать без необходимости;
не делать вид, что хаос зрелый;
давать pm понятный выбор.
```

---

## 25. итоговая формула проекта

```text
мы проектируем ai-плагин для pm, который помогает не писать документы ради документов,
а двигать продуктовую работу по зрелости.

пользователь может прийти с сигналом, идеей решения, слабым доком, prd, backlog item или квартальной целью.

система диагностирует вход, ищет похожие сущности в backlog, определяет maturity,
подгружает нужный workflow, помогает добрать недостающее,
генерирует / ревьюит артефакты и двигает item дальше.

главные пользовательские зоны:
context/onboarding, router, opp doc, opp backlog, solution/prd, solution/prd backlog, planning.

первый инкремент:
mock context + router lite + opp doc module + mock backlogs.

главный принцип:
не ускорять хаос, а возвращать продакта к дисциплине.
```
