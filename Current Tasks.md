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
	- [ ] Тайны разума
		- [ ] Бумажки
			- [ ] Статы


# Main

- [ ] Талисманы
	- [ ] Наименование
	- [ ] Свойства
		- [ ] source
		- [ ] activate_silver_num
		- [ ] parts_needed
		- [ ] jasper_slots
	- [ ] ImagePlaceholder
	- [ ] Описание
- [ ] Яшма
	- [ ] Наименование
	- [ ] Свойства
		- [ ] itemtype
		- [ ] stats
	- [ ] ImagePlaceholder
	- [ ] Описание

- [ ] Сундук Яшм/Кусок сундука
	- [ ] Наименование
	- [ ] Свойства
		- [ ] ItemType
	- [ ] ImagePlaceholder
	- [ ] Описание
- [ ] Куски талисманов
	- [ ] Наименование
	- [ ] Свойства
		- [ ] ItemType
	- [ ] ImagePlaceholder
	- [ ] Описание


# Заметки


