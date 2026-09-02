---
name: aipm-configuration
description: Кофигуратор плагина aipm
---

# Purpose
Сохранить или актуализировать конфиги для плагина aipm:
- путь к корневому разделу Confluence со списком элементов бэклога
- путь к Google Sheet для вывода элементов бэклога в табличном виде

## Расположение конфигурации

Храни конфигурацию, специфичную для текущего рабочего проекта, в файле:
`<project-root>/.codex/aipm-config.json`

# When to use
- Когда скилл вызывается внутри других скиллов плагина aipm
- Когда просит изменить корневой раздел Confluence для бэклога (backlog-confluence-root)
- Когда просит изменить путь к Google Sheet для бэклога (backlog-gsheet-link)

# When not to use
- Когда пользователь не упоминает plugin/skill aipm

# Workflow

Проверь существует ли файл конфигурации

[ЕСЛИ ЕСТЬ]
	- через MCP Avito Confluence и plugin Google Sheet проверь, что указанная в конфигурации backlog-confluence-root и backlog-gsheet-link доступны
	- если доступны продолжи выполнение
	- если недоступны, то сообщи об этом пользователю и предложи передать
	- верни конфигурацию из файла в формате JSON

[ЕСЛИ НЕТ]
	- Попроси пользователя прислать 
		- ссылку на родительскую страницу Confluence, внутри которой следует создавать единицы бэклога.
		- ссылку на страницу google sheet для вывода бэклога в табличном виде
	- Для Confluence
		- Через MCP Avito Confluence Проверь, что страница существует и доступна.
		- Определи:
		   - ключ пространства (`space_key`);
		   - ID родительской страницы (`parent_page_id`);
		   - название родительской страницы (`parent_page_title`).
   	   - Сохрани данные в файл конфигурации по шаблону assets/aipm_config_template.json в блок backlog-confluence-root
	- Для Gsheet
		- Проверь, что Gsheet существует и доступен.
   	   - Сохрани ссылку на Gsheet в файл конфигурации в параметр backlog-gsheet-link по шаблону assets/aipm_config_template.json