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
- [ ] Предметы + части
- [ ] В идеале предметы связанные с механикой (может быть сложно)
- [x] Я ЗАБЫЛ ПРО ГРАВИРОВКУ


# Main
- [ ] Артефакты
	- [ ] Наименование
	- [ ] Свойства
		- [ ] source
		- [ ] activation_stat
		- [ ] engrave_stats
		- [ ] engrave_stage_bonus
	- [ ] ImagePlaceholder
	- [ ] Активный скилл
		- [ ] Описание
	- [ ] Скиллы (пассивные)
		- [ ] 1
		- [ ] 2
		- [ ] 3
- [ ] Предметы/части
	- [ ] Наименование
	- [ ] Свойства
		- [ ] itemtype
	- [ ] ImagePlaceholder
	- [ ] Описание
# Заметки


