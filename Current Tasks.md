Общий прогресс базы:
```dataviewjs
const tasks = dv.pages('"Future Updates"').file.tasks;
const total = tasks.length;
const done = tasks.where(t => t.checked).length;
const percent = Math.round((done / total) * 100) || 0;

dv.el("div", `
  <div style="width: 100%; background: #eee; border-radius: 5px;">
    <div style="width: ${percent}%; background: var(--color-accent); height: 20px; border-radius: 5px; text-align: center; color: white; line-height: 20px;">
      ${percent}%
    </div>
  </div>
`);
```

Прогресс текущей итерации:
```dataviewjs
const tasks = dv.pages('"Current Tasks"').file.tasks;
const total = tasks.length;
const done = tasks.where(t => t.checked).length;
const percent = Math.round((done / total) * 100) || 0;

dv.el("div", `
  <div style="width: 100%; background: #eee; border-radius: 5px;">
    <div style="width: ${percent}%; background: var(--color-accent); height: 20px; border-radius: 5px; text-align: center; color: white; line-height: 20px;">
      ${percent}%
    </div>
  </div>
`);
```
# In progress
- [x] Найти список всех артефактов
- [x] Активные навыки
- [x] Пассивные навыки
- [x] Статы приемки
- [x] Наименования пассивных навыков
- [x] Предметы + части
- [x] В идеале предметы связанные с механикой (может быть сложно)
- [x] Я ЗАБЫЛ ПРО ГРАВИРОВКУ
- [x] Генераторы
	- [x] Артефакты
	- [x] Предметы

- [x] Добавить все необходимые ссылки для артефактов
- [x] Переместить их в базу
	- [x] В механики

- [x] Добавить все необходимые ссылки для предметов артефактов
- [x] Переместить их в базу
	- [x] В предметы

Артефакт
Орден артефакта
Предмет артефакта
Часть артефакта
# Main
- [x] Артефакты
	- [x] Наименование
	- [x] Свойства
		- [x] source
		- [x] activation_stat
		- [x] engrave_stats
		- [x] engrave_stage_bonus
	- [x] ImagePlaceholder
	- [x] Активный скилл
		- [x] Описание
	- [x] Скиллы (пассивные)
		- [x] 1
		- [x] 2
		- [x] 3
- [x] Предметы/части
	- [x] Наименование
	- [x] Свойства
		- [x] itemtype
	- [x] ImagePlaceholder
	- [x] Описание
# Заметки


