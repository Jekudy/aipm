# Каталог критериев D1/D2/D5 v1

**Версия:** 1.0.0  
**Источник:** сокращённая исполняемая проекция `signal-problem-audit-criteria-catalog.md` v0.3.1 от 2026-09-03.  
**Scope:** безусловные CORE-атомы D1/D2/D5 и закрыто-предикатные обязательные проверки, которые v0.3.1 включает при срабатывании runtime predicate.

В v1 намеренно не входят диагностические, будущие, отброшенные и доменные проверки, общий балл и критерии D3/D4. Проверки ниже не являются расширением scope: это исполняемая часть v0.3.1, без которой аудит теряет опровержимость, допустимость метода, границы выборки и Park-trigger.

## Контракт атома

```yaml
criterion_instance:
  id: <criterion_id:claim_or_relation_id>
  applicability: APPLICABLE | NOT_APPLICABLE
  applicability_rule_id: <rule id>
  assessability: ASSESSABLE | BLOCKED
  result: MET | NOT_MET | null
  primary_reason: <reason-action-map enum>
  anchor:
    quote: <дословная цитата или null только для ABSENT/BLOCKED>
    location: <страница/файл и секция/строки>
    claim_id: <id или null>
    evidence_id: <id или null>
```

`NOT_APPLICABLE` и `BLOCKED` всегда имеют `result: null`. `MET` требует наблюдаемый anchor; доказательный атом дополнительно требует прочитанный внешний источник. Для `ABSENT` не выдумывай цитату: `quote: null`, а в `location` перечисли точную границу поиска по manifest.

## CORE-каталог

| ID | Переход | Проверка и минимальный MET anchor |
|---|---|---|
| DB-PURPOSE-01 | D1/D2/D5 | Названы причина рассмотрения проблемы и decision consumer; нужны две цитаты. |
| DB-04 | D1/D2/D5 | Назван человек или роль с правом принять заявленное решение. |
| DB-06 | Если `previous_decision_exists=true` | Процитированы последнее решение и его дата. |
| S-01 | D1/D2 | Процитировано наблюдаемое событие, паттерн или изменение, а не только интерпретация. |
| S-02 | D1/D2 | Назван origin channel или первичный артефакт сигнала; «по данным» без источника не проходит. |
| S-04 | D1/D2 | Указаны дата или период наблюдения; дата документа не подменяет дату сигнала. |
| S-05 | D1/D2 | Указана граница наблюдения: поток, категория, платформа, процесс или эквивалент. |
| S-06 | D1/D2 | Назван наблюдаемый субъект: роль, когорта, операция, сервис или процесс. |
| S-07 | Если `has_numeric_claim=true` | У числового claim есть знаменатель или явно определённая популяция. |
| S-09 | Если `conditional_probability_claim=true` | Направление условной вероятности записано явно и не инвертировано. |
| P-02 | D2 | Назван конкретный affected subject; общего «пользователи» недостаточно. |
| P-03 | D2 | Назван момент, событие или условие возникновения проблемы. |
| P-JOB-01 | Если `subject_type=internal_team|process_or_system` | Названо ожидаемое состояние, обязательство или SLO. |
| P-04 | D2 | Записано наблюдаемое отклонение; оценка «плохо работает» без наблюдаемой формы не проходит. |
| P-05 | D2 | Записано последствие для affected subject или обязательства. |
| P-WORK-01 | Если `existing_control_mentioned=true` или сработал `context_pack.control_trigger` | Назван результат существующего контроля на проблеме либо честное «не знаем». |
| P-HYP-01 | D2 | Есть decision-relevant problem hypothesis; одна становится central автоматически, из нескольких central объявляет автор. |
| P-MECH-01 | Если `mechanism_claim_present=true` | Механизм помечен как факт или предположение и связан с проверяемой опорой. |
| P-PREV-01 | D2, если `previous_research_exists=true` | Процитировано предыдущее исследование и его decision-relevant результат. |
| P-TEST-02 | D2 | Процитирован фактически полученный результат проверки, а не только «проверили, подтвердилось». |
| V-REACH-02 | D2 | Есть active reach claim о частоте, охвате или повторяемом qualitative pattern с population. |
| V-01 | D2, если `reach_route=prevalence` | Популяция scale claim совпадает с affected subject либо связь объяснена. |
| V-02 | D2, если `reach_route=prevalence` | Scale claim содержит число и единицу. |
| V-04 | D2, если `reach_route=prevalence` | Scale claim содержит дату или период. |
| V-05 | D2, если `reach_route=prevalence` | Claim помечен measured/estimated/assumed либо значение найдено в источнике. |
| V-SEVERITY-01 | D2 | Есть active harm claim с affected subject и наблюдаемым вредом. |
| P-OUTCOME-01 | D2 | Назван независимый от решения наблюдаемый индикатор и желаемое направление изменения. |
| V-HARM-REL-01 | D2 | Outcome является direct measure harm либо indirect bridge оформлен отдельным evidence-required claim. |
| REL-ESS-01 | D2, 2 instances | Central problem связан отдельно с reach и harm: тот же phenomenon или evidence-required bridge. |
| REL-01 | Если `count(left)>1` или `count(right)>1` | Явно связаны нужные signal, hypothesis, problem, reach и outcome claims без неоднозначного co-reference. |
| ER-01 | D2 evidence-required essentials; D5 evidence reason | Для claim есть конкретный source reference; «по данным» без ссылки не проходит. |
| ER-03 | D2 evidence-required essentials; D5 evidence reason | В источнике есть цитируемое наблюдение с совпадающими scope, period, grain и value, включая direction. |
| INF-DISC-01 | Если `D2 AND decision_role=ESSENTIAL AND inference_required=true` | Для claim задан наблюдаемый результат, при котором claim не поддерживается. |
| INF-METHOD-01 | D2 evidence-required essentials | Versioned method profile допускает claim type и содержит все required fields. |
| INF-CONC-01 | D2 evidence-required essentials | Авторский conclusion совпадает с вычисленным `SUPPORTS/REFUTES/MIXED/DOES_NOT_BEAR`. |
| INF-SEL-01 | Если `selection_required=true` | Зафиксированы observation universe, inclusion/exclusion rule и period. |
| INF-SCOPE-01 | Если claim обобщается за наблюдённые единицы | Claim ограничен наблюдёнными единицами либо generalization route допустим. |
| INF-RIVAL-01 | Essential causal/mechanism/explanatory claim | Назван rival claim, способный породить то же исходное наблюдение. |
| INF-RIVAL-02 | Если `INF-RIVAL-01=MET` | Для central и rival записаны разные наблюдаемые predictions. |
| INF-RIVAL-03 | Если `INF-RIVAL-02=MET` | Проведён различающий contrast, записаны actual result и rival status. |
| INF-UNC-01 | Если открыт decision-flipping unknown | Для каждого исхода unknown задано решение `OPEN/CONTINUE/STOP/PARK`. |
| INF-UNC-02 | Если `INF-UNC-01=MET` и unknown открыт | Записан следующий наблюдаемый discriminating test. |
| CONF-02 | Если есть essential conflict | Конфликт разрешён versioned rule либо явно оставлен `UNRESOLVED/MIXED` и отражён в conclusion/candidate. |
| Q-01 | Если `reach_route=qualitative_pattern` | У цитируемого наблюдения есть case ID и verbatim/разметка. |
| Q-03 | Если `reach_route=qualitative_pattern` | Pattern опирается более чем на один origin; single case явно назван single case. |
| R-REGISTRY-01 | Если `transition=D1 AND registry_configured=true` | Зафиксированы version, query/filter, дата и matches/0. |
| INF-FRESH-01 | Если pack задаёт `max_age_days` или есть material-change date | Evidence после material change и не старше активного порога. |
| INF-PROXY-01 | Если evidence variable отличается от target variable | Bridge evidence→target является evidence-required claim либо conclusion явно ограничен промежуточной метрикой. |
| INF-LINEAGE-01 | Если proof создан проверяемым selector/score/intervention или downstream от него | Data lineage не circular либо есть independent validation. |
| ST-00 | D5 | Decision type явно `STOP` или `PARK`. |
| ST-01 | D5 | Причина имеет тип `NOT_CONFIRMED`, `BELOW_ATTENTION`, `PRIORITY_DECISION` или `AUTHORITY`. |
| ST-02 | D5 | Записана дата решения; дата страницы её не заменяет. |
| ST-03P | D5, если `decision_type=PARK` | Указан наблюдаемый триггер возврата: порог, дата, событие или изменение ограничения. |

На D2 active `ESSENTIAL`: occurrence, central hypothesis, reach, harm и reverse dependency closure всех bridge claims. `ER-01/02/03`, `INF-DISC-01`, `INF-METHOD-01` и `INF-CONC-01` создаются отдельно для каждого evidence-required essential claim; selection/scope/rival/unknown/freshness/lineage включаются только закрытыми predicates. `REL-ESS-01` всегда создаёт ровно два relation instances: `problem→reach` и `problem→harm`.

## Минимальные runtime-правила

1. **Preflight.** `DB-01`: transition явно `D1|D2|D5`; `DB-02`: track явно `discovery`; `DB-03`: ровно один независимый decision thread; `DB-09`: следующий commitment не дороже перехода, а D2 разрешает только bounded Solution Discovery. Нарушение блокирует оценку, но не создаёт content `NOT_MET`.
2. **Central claim.** Единственная problem hypothesis становится central автоматически. При нескольких без явного focus — `BLOCKED(CENTRAL_CLAIM_UNRESOLVED)`.
3. **Manifest.** Корневой locator, явно переданный пользователем, получает `IN_SCOPE`. Для каждого дополнительного ресурса обязательны `resource_id`, locator и `scope_state: IN_SCOPE|OUT_OF_SCOPE|UNRESOLVED`; runtime заполняет `required_by`. Не обходить ссылки рекурсивно. Ref вне manifest получает synthetic `{scope_state: UNRESOLVED, review_state: UNAVAILABLE}`.
4. **ER-02 assessability.** Evidence relation проверяема только при `scope_state=IN_SCOPE` и `review_state=READ`; иначе `BLOCKED(BLOCKED_SOURCE)`. Missing/invalid scope state даёт также preflight `BLOCKED(INVALID_INPUT)`.
5. **Tie-break.** При сомнении `MET` против `NOT_MET` выбирать `NOT_MET`; конфликтующие источники не разрешать выбором удобного.
6. **Faithful refutation.** Если источник совпадает по scope/period/grain/value и честно даёт `REFUTES` или `MIXED`, `ER-03=MET`. Несовпадение авторского вывода ловит `INF-CONC-01`.
7. **Claim inventory.** Active claims получают стабильные ID, цитаты, локации, source refs и классы. `MULTIPLIER_RHETORICAL` или `INTENSIFIER`, используемый как essential factual premise, без source anchor и наблюдаемой границы или операционализации даёт `ER-03=NOT_MET(INVALID_FORM)`.

## Допустимость метода

```yaml
OBSERVED_OCCURRENCE: [DIRECT_RECORD, EVENT_TRACE, VERBATIM_REPORT]
OBSERVED_HARM: [DIRECT_OUTCOME_RECORD, EVENT_TRACE, VERBATIM_REPORT]
QUANTIFIED_HARM: [CENSUS_QUERY, DENOMINATOR_SAMPLE]
PREVALENCE: [CENSUS_QUERY, DENOMINATOR_SAMPLE]
QUALITATIVE_PATTERN: [SYSTEMATIC_CASE_REVIEW]
DESCRIPTIVE_COMPARISON: [COMMON_FRAME_COMPARISON, RANDOMIZED_COMPARISON, QUASI_EXPERIMENT]
DESCRIPTIVE_TREND: [REPEATED_MEASURE_SAME_DEFINITION]
CAUSAL_EFFECT: [RANDOMIZED_EXPERIMENT, QUASI_EXPERIMENT_WITH_IDENTIFICATION]
MECHANISM: [INTERVENTION_TEST, DISCRIMINATING_PROCESS_TRACE]
EXPLANATORY_INTERPRETATION: [DISCRIMINATING_COMPARISON, DISCRIMINATING_PROCESS_TRACE]
```

Одного label недостаточно: method profile обязан иметь version, `allowed_claim_types`, `required_fields`, `uses_subset` и `generalization_routes`. Before/after без контрольного контраста не допускается для `CAUSAL_EFFECT`; `VERBATIM_REPORT` не доказывает prevalence; `SYSTEMATIC_CASE_REVIEW` доказывает pattern только в описанной выборке.

## Агрегация без баллов

`dossier_status=BLOCKED`, если preflight или обязательный ER-02 заблокирован. Иначе `DECISION_READY_DOSSIER`, только если все применимые CORE и закрыто-предикатные instances имеют `MET`; в остальных случаях `NOT_READY`.

Canonical candidate вычисляется первым сработавшим правилом и затем нормализуется в exposed contract; `candidate_available` не даёт спутать «продолжить discovery» с «candidate пока нельзя вывести»:

1. Assessable `ST-00=MET` со значением `PARK` → canonical `D5_PARK_CANDIDATE`, exposed `STOP_CANDIDATE`, `d5_mode=PARK`, `candidate_available=true`; это сохраняется, даже если owner, дата или триггер возврата дают `NOT_READY`.
2. Иначе assessment blocker → canonical `NO_CANDIDATE`, exposed `BLOCKED`, `d5_mode=null`, `candidate_available=false`.
3. Assessable D5 Stop даёт canonical `D5_STOP_CANDIDATE`, exposed `STOP_CANDIDATE`, `d5_mode=STOP`, `candidate_available=true`, если `ST-01` равен `PRIORITY_DECISION/AUTHORITY` либо причина `NOT_CONFIRMED/BELOW_ATTENTION` подтверждена обязательной evidence relation.
4. Для D2 essential occurrence/harm=`REFUTES` или сработал versioned below-attention rule → тот же Stop candidate.
5. Non-supporting essential, surviving rival, mapped open unknown или unresolved conflict → canonical/exposed `CONTINUE_CANDIDATE`, `candidate_available=true`.
6. Для D2 ready dossier и каждый active essential=`SUPPORTS` → canonical/exposed `D2_CANDIDATE`, `d5_mode=null`, `candidate_available=true`.
7. Для D1 ready dossier → canonical/exposed `CONTINUE_CANDIDATE`, `candidate_available=true`, outcome `TAKE_SIGNAL_INTO_DISCOVERY`.
8. Иной `NOT_READY` → canonical `NO_CANDIDATE`, exposed `CONTINUE_CANDIDATE` только как транспортное значение, `candidate_available=false`, outcome `NOT_DECIDED`.

Все `MET` означают только достаточное decision-ready dossier для запрошенного перехода. Они не доказывают истинность проблемы, качество фичи, автоматический GO или качество будущего решения.
