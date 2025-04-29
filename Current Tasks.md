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
- [x] Так, надо найти все эффекты рун и в идеале руны
	- [x] Какие проблемсы? 
		- [x] Большую часть придется делать руками, наверное, это самая сложная история из всех
		- [x] В теории я могу вытащить хотя бы часть данных из таблиц, насколько это будет хорошо надо оценить
	- [x] Скорее всего придется делать отдельные папки под каждый класс, потому что названия то одинаковые
	- [x] Предметы не нужны, я думаю, просто ненужная тупость на текущий момент, лучше сосредоточиться именно на самих рунах, потом можно будет все это доделать
- [x] Вытащить описание эффектов обнаруженных в баффах
- [x] Сделать список всех рун
- [x] Сделать список всех рун с навыками
- [ ] Сеты
	- [ ] Страничка со статами (можно попробовать циферки, но мне кажется они разнятся(чекнуть на разных персах?))
- [x] Генераторы
	- [x] Руны с навыками
		- [x] Разделить по классам (13 папок получается)
	- [x] Руны сами по себе

# Main
- [ ] Структура
	- [ ] Руны с навыками
		- [ ] Папка на каждый класс
		- [ ] Либо в названии пишем класс и базу руны
	- [ ] Руны со статами
		- [ ] Папка для рун сетовых
		- [ ] Папка для обычных рун
		- [ ] Либо общая папка и просто по редкости делить через свойство
	- [ ] Сеты
		- [ ] Оборона
		- [ ] Атака
		- [ ] Духи
# Заметки


