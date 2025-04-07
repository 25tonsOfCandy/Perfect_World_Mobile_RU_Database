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


- [x] Вытащить все необходимые данные
	- [x] Кодексы
	- [x] Поменять АТК, на Атаку или наоборот
	- [x] 
	- [x] убрать все лишнее
		- [x] Имя
		- [x] уровни
		- [x] описание
			- [x] Желательно скиллов
		- [x] Статы надето
		- [x] Статы имеется
		- [x] itemtype = Кодекс
		- [x] codextype
	- [x] Предметы для кодексов
		- [x] Убрать все лишнее
		- [x] Имя
		- [x] Описание
		- [x] Тип предмета
	- [x] Фолианты
	- [x] СТК? что это?
		- [x] убрать все лишнее
		- [x] Имя
		- [x] Описание
			- [x] Статы
		- [x] Кодексы необходимые для активации
			- [x] Если нет = Информация отсутствует
- [x] Свитки
	- [x] ????????????????
	- [x] Сомнения в необходимости делать это сейчас, думаю что можно попробовать сделать это позже если не получится найти все данные по статам
		- [x] Скип

- [x] Классы
	- [x] Кодексы
	- [x] Фолианты
	- [x] Предметы Кодексов
# Main
- [x] Добавить все Кодексы
	- [x] Наименование
		- [x] Свойства
			- [x] level
			- [x] stats_own
			- [x] stats_on
			- [x] itemtype
			- [x] codex_type
		- [x] Placeholder
		- [x] Skill
			- [x] SkillDescription
- [x] Добавить все Сутры (Фолианты)
	- [x] Наменование
	- [x] Свойства
		- [x] itemtype
		- [x] stats
	- [x] description
	- [x] codex needed
		- [x] codex list - how much if null "Информация отсутствует"
- [x] Предметы для Кодексов
	- [x] Наименование
		- [x] itemtype
	- [x] description


# Заметки


