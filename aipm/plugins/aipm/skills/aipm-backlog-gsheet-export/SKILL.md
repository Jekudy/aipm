---
name: aipm-backlog-gsheet-export
description: Экспортирует и синхронизирует элементы продуктового бэклога из Confluence страниц в табличное отображение в Google Sheets.
---

# Purpose
Отобразить backlog продуктовых инициатив из Confluence в удобном для анализа продакт-менедежером табличном виде в Google Sheets.


# When to use
- Пользователь просит вывести бэклог/backlog в google sheets
- Происходит изменение элементов бэклога в Confluence, требующее синхронизации


# When not to use
Пользователь задает абстрактные вопросы по product backlog или Google Sheets для общего развития. 
Обсуждает лучшие практики ведения product backlog
Задает вопросы по работе с google sheets без привязки к бэклогу

# Workflow

1. Используй скилл $aipm-configuration для получения / создания конфигурации скилла

2. В Confluence разделе из конфига backlog-confluence-root содержится бэклог инициатив. 

### 2.1 full refresh - если пользователь просит выгрузить все данные / полную синхронизацию

2.1.1 В соответствии с колонками, перечисленными в assets/gsheet-export-template.md Собери данные из инициатив в табличную структуру, удобную для экспорта в Google sheets. 
2.1.2 Экспортируй табличные данные в Google Sheets, используя skill '$google-drive:google-sheets', включая названия колонок. Сохраняй стили и порядок существующих строк. Новые добавляй в конец.

### 2.2 incremental - если пользователь просит добавить один элемент

Добавь строки с новыми инициативами, используя skill '$google-drive:google-sheets', которых еще нет в таблице


# Constraints

1. Master-системой являтеся Confluence. Изменения данных в бэклоге меняется только в Confluence, а в Google Sheets только отображаются.
В случае рассинхрона между Confluence и Google Sheets, апдейтится только Google Sheets.

2. Если в Google docs уже применены какие-то стили, наложены фильтры, не перетирай лист занового. Просто добавь новые строки и актуализируй ячейки. Для синхронизации ориентируйся на колонку id, в которой сохранены confluence_page_id


# Definition of done
В Google Sheet
- есть все элементы бэклога из Confluence
- данные разложены по колонкам assets/gsheet-export-template.md
- данные в Google Sheet соответствуют данным в Confluence

# Output format

### Успех
```
Экспортировал все элементы продуктового бэклога в Google Sheets
{Ссылка на Google Sheets}
```

# Failure handling

Вывести причины ошибки
Порекомендовать как устранить