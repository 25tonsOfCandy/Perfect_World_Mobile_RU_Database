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
- [x] Подготовить файлы
	- [x] Талисманы
	- [x] Яшмы
		- [x] сундук яшм
	- [x] Куски талисманов
	- [x] Тайны разума
		- [x] Скрижали
			- [x] Статы?
		- [x] Бумажки (откровения)
			- [x] Статы
			- [x] Откровения содержат статы, описаний у них нет, на каждую скрижаль необходимо создавать наверное файлы по типу TabletName+(Малый/Большой/Совершенный)
			- [x] Либо прописывать их в каждой скрижали с возможными статами?
				- [x] То есть в виде
				- [x] base_stats
				- [x] small_tablet_stats_random
				- [x] big_tablet_stats_random
				- [x] perfect_tablet_stats_random
- [x] Placeholders
	- [x] Talismans
	- [x] TalismanParts
	- [x] TabletItems
	- [x] Tablets
- [x] Генераторы
	- [x] Талисманы
	- [x] Части талисманов
	- [x] Скрижали
	- [x] Предметы скрижалей
- [x] Переместить все скрижали в механики


# Main

- [x] Талисманы
	- [x] Наименование
	- [x] Свойства
		- [x] source
		- [x] activate_silver_num
		- [x] parts_needed
		- [x] jasper_slots
	- [x] ImagePlaceholder
	- [x] Описание
- [x] Яшма
	- [x] Наименование
	- [x] Свойства
		- [x] itemtype
		- [x] stats
	- [x] ImagePlaceholder
	- [x] Описание

- [x] Сундук Яшм/Кусок сундука
	- [x] Наименование
	- [x] Свойства
		- [x] ItemType
	- [x] ImagePlaceholder
	- [x] Описание
- [x] Куски талисманов
	- [x] Наименование
	- [x] Свойства
		- [x] ItemType
	- [x] ImagePlaceholder
	- [x] Описание

- [x] Скрижали
	- [x] Наименование
	- [x] Свойства
		- [x] base_stats
		- [x] small_tablet_stats_random
		- [x] big_tablet_stats_random
		- [x] perfect_tablet_stats_random
		- [x] rarity
		- [x] number_slots
		- [x] source
- [x] Предметы скрижалей
	- [x] Наименование
	- [x] Свойства
		- [x] itemtype
	- [x] ImagePlaceholder
	- [x] Описание
# Заметки


