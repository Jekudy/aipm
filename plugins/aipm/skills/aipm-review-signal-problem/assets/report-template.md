# Шаблон отчёта

Первая строка ответа всегда имеет формат:

```text
{DECISION_READY_DOSSIER | NOT_READY | BLOCKED} / {D2_CANDIDATE | CONTINUE_CANDIDATE | STOP_CANDIDATE | BLOCKED} / {достаточно | недостаточно | проверка заблокирована}
```

## Внешний слой: только расхождения

```markdown
Переход: {D1 | D2 | D5}; d5_mode: {STOP | PARK | null}

1. [{issue_id}] {что расходится с критерием — одна фраза}
   - Опора: «{дословная цитата}» — {location}; для ABSENT/BLOCKED: {граница поиска или источник, который не удалось прочитать}
   - Причина: {primary_reason}
   - Минимальное действие: {action} — {конкретное действие}
   - Проверка: {acceptance_test того же instance}

Показано: {0..3}; скрыто: {omitted_count}.
Границы: coverage={COMPLETE | INCOMPLETE | NOT_ASSESSABLE}; прочитано={resource ids}; не прочитано={ids}; недоступно={ids}; вне scope={ids}.
Проход-опровержение: {NO_FINDING | FINDING_RAISED | CANNOT_ASSESS} — {самое дешёвое наблюдение, меняющее вывод, и есть ли оно в supplied scope}.
```

Сортируй issues по `BLOCKS_ASSESSMENT → BLOCKS_DOSSIER → CHANGES_CANDIDATE → NO_CURRENT_EFFECT`, затем по стабильному `issue_id`; показывай максимум три. При `достаточно` список пуст: не придумывай улучшения и не добавляй общую похвалу.

## Structured layer

```yaml
audit:
  rubric_version: "criteria-d1-d2-d5@1.0.0"
  model_version: <exact id>
  transition: D1 | D2 | D5
  track: discovery
  thread_id: <stable id>
  dossier_status: DECISION_READY_DOSSIER | NOT_READY | BLOCKED
  transition_candidate: D2_CANDIDATE | CONTINUE_CANDIDATE | STOP_CANDIDATE | BLOCKED
  canonical_transition_candidate: D2_CANDIDATE | CONTINUE_CANDIDATE | D5_STOP_CANDIDATE | D5_PARK_CANDIDATE | NO_CANDIDATE
  d5_mode: STOP | PARK | null
  decision_outcome: OPEN_SOLUTION_DISCOVERY | CONTINUE_PROBLEM_DISCOVERY | STOP | PARK | NOT_DECIDED
  source_coverage:
    status: COMPLETE | INCOMPLETE | NOT_ASSESSABLE
    resources: [{resource_id, locator, scope_state, review_state, required_by}]
  criteria:
    - {id, applicability, applicability_rule_id, assessability, result, primary_reason, anchor}
  issues:
    - {issue_id, kind, criterion_id, primary_reason, anchors, candidate_impact, action, target_ids, acceptance_test}
  falsification:
    status: NO_FINDING | FINDING_RAISED | CANNOT_ASSESS
    claim_ids: [<ids>]
    resource_ids: [<supplied ids>]
    decision_flipping_observation: <bounded statement or null>
    finding: <bounded statement or null>
  omitted_count: <integer >= 0>
```

Все machine issues сохраняются в structured layer. Finding не меняет result или candidate, пока владелец не примет его как новый claim/unknown и не запустит аудит заново.

## Append-only audit layer

Записывай этот блок в конец исходного документа только при явной просьбе изменить источник. Иначе верни его готовым для вставки. Здесь хранятся подтверждённые атомы; во внешнем feedback их не повторяют.

```markdown
## Аудит сигнала и проблемы

### {YYYY-MM-DD HH:MM} — {transition}, rubric v1.0.0

- Вердикт: {dossier_status} / {transition_candidate}; d5_mode={value}; решение владельца={не принято | значение}
- Границы: {source coverage summary}
- Подтверждено:
  - [{criterion_instance_id}] «{дословная цитата}» — {location}; evidence={evidence_id | не требуется}
- Открытые расхождения: {issue_ids или «нет»}
- Проход-опровержение: {status}; «{bounded finding или наблюдение}»; опоры={claim/resource ids}
```

Новый прогон добавляет запись, а не переписывает предыдущую.
