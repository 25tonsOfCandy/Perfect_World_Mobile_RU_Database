
# Генерация карточек бестиария
Что у меня есть?
Данные в табличках вида Excel.
	- Список всех **(проверить)** карточек бестиария 
	- Источники этих карточек **(проверить)**
	- Есть описания скиллов этих карточек
		- Вероятно в перемешку с категорией сборов
	- Есть список связей, которые надо обработать, в том числе их бонусы

Есть шаблон того как должна выглядеть страничка карточки.
	- Свойства вида
		- Тир карточки
		- Статы
		- Источник
	- Картинка из игры
	- Название скилла
	- Описание скилла
	- Эффект сбора (вероятно, нет необходимости сразу добавлять)
	- Связи (бонусы строя)


Что я хочу?
Автоматически сгенерировать все возможные карточки согласно шаблону выше.

Как я хочу?
У меня есть таблица данных, поэтому эти данные мне нужно получить в удобный для работы вид. Для этого надо использовать библиотеку, которая умеет работать с таблицами. Так как формат таблиц может быть разным, необходимо сделать гибкую функцию получения информации из таблицы. 
- Варианты: Использовать пресеты (допустим одна функция будет в зависимости от установленного пресета выполнять разные функции)
- Написать максимально простые функции, которые выполняют типичную задачу, различаться будет только генерация страниц **(ПРИОРИТЕТ)**

Пока вот так, в зависимости от библиотеки поменяю  
```python
def get_content_from_table(filename: str, column0: str or int, column1: str or int)
```

Получив данные, необходимо сгенерировать MD файлы. Задачи:
	- Генерировать данные в виде списка
		- Согласно шаблону
			- Шапка, в виде свойств с пустыми значениями
				- Может быть если в названии карточки есть обозначение S, A заполнять тир (не сильно важная проблема)
			- Если есть желание можно сделать заранее картинки и добавлять ссылки на них, либо заглушка, либо ничего
			- Заглушка названия скилла (информация об этом в CMS отсутствует, где она хранится, выяснить не удалось)
			- Связи (надо найти их названия и описания бонусов)
	- Этот список записывать в файл
		- файлу давать название карточки 
		- удалить из него ненужную информацию (дух S, A)


Какие проблемы я вижу?
	- Таблицы разные и их несколько, метод для чтения таблиц должен быть максимально гибким
		 Решение:
		- Он должен получать список столбцов которые нужно считать
	- Тяжело определить последовательность считывания данных из столбцов
		Решение:
		- Прописывать решение генерации для каждого отдельного случая
		- Расписывать псевдокодом все необходимое, иначе я умру
		- Тут пригодятся пресеты, если придется прописывать всю генерацию в рамках одной функции
	- Запись
		При большом количестве данных может вызывать проблемы
			Решение
				- Заранее подготавливать таблицы с необходимыми данными, не нужно подсовывать программе то что ей не нужно


Итоговый список задач
- [x] Метод получения данных из таблиц
	- [x] Найти библиотеку которая умеет это делать
		- [ ] xlsxwriter
		- [x] openpyxl - на первый взгляд подходит лучше всего
		- [ ] pandas
		- [ ] faker
	- [x] возникла проблема как можно вернуть несколько значений
		- [x] решение yield
	- [x] нужна тестовая таблица 
	- [x] решение готово
		
- [ ] Метод формирования записей
	- [ ] нужны данные и шаблон
- [x] Метод записи сформированных данных в файл
	- [x] тут вообще все должно быть просто, лист записываем в файл в папку
		- [x] вероятно нужно проверять наличие папки или ловить исключение, создавать папку и делать еще разочек запись
			- [x] принято решение перед запуском программы проверять наличие всех необходимых директорий
- [x] Запись в файл list не очень подходит под задачу, поэтому запись в файл была реализована внутри модуля генерации карточек
- [x] Добавить замену пустых значений в Source на "Информация отсутствует"



Итоговые решения:
Получение данных из таблицы по столбцам, необходимо лишь расписывать данные по разным переменным или выбрасывать их через next по необходимости. 

```python
def get_data_from_xlsx_file(filename: str, column_list :list):
    """Return data in columns from column_list throught the yield.

    Args:
        filename (str): filename (Exapmle: imgay.xlsx)
        column_list (list): list of colums (Example: [1, 2, 4, 6])

    yeild: 
        result (list): rows from each column in column_list
    """
    workbook = openpyxl.load_workbook(filename=filename)
    sheet = workbook.active

    for column in column_list:
        result = []
        for row in range(1, sheet.max_row):
            result.append(sheet.cell(row, column).value)
        yield result
```

Запись в файл
```python
def write_list_to_file(data_list: list, path_to_file_with_filename: str):
    with open(path_to_file_with_filename, "w", encoding="UTF-8")  as file:
        for line in data_list:
            file.write(str(line) + "\n")
        print("File created: " + path_to_file_with_filename)
```

Проверка всех директорий (моя не дружить с английским)
```python
def check_exists_all_important_directories():
    for directory in DIRECTORIES:
        if not os.path.exists(directory):
            os.makedirs(directory)
```

Генерация карточек
```python
def generate_bestiary_cards(names_list: list, source_list: list, description_list: list):
    property_start_end_str = "---"
    property_stats_str = "stats: "
    property_tier_str = "tier: "
    property_source_str = "source: "
    placeholder_str = "![[Temp/Placeholder_Bestiary.png]]"
    placeholder_skill_name_str = "SkillNamePlaceholder"
    set_str = "# Связи"

    element_number = 0

    for name in names_list:
        with open('bestiary/' + str(name) + '.md', 'w', encoding='UTF-8') as bestiary_file:
            bestiary_file.write(property_start_end_str + '\n')
            bestiary_file.write(property_stats_str + '\n')
            bestiary_file.write(property_tier_str + '\n')
            if source_list[element_number]  != None:
                bestiary_file.write(property_source_str + str(source_list[element_number]) + '\n')
            else: 
                bestiary_file.write(property_source_str + "Информация отсутствует" + '\n')
            bestiary_file.write(property_start_end_str + '\n')
            bestiary_file.write(placeholder_str + '\n')
            bestiary_file.write(placeholder_skill_name_str + '\n')
            bestiary_file.write(description_list[element_number] + '\n')
            
            element_number += 1
```

# Генерация карточек связей

Что я хочу?
- Вынести все связи в отдельные карточки
- Иметь ссылки на карточки внутри этих связей
- Названия этих связей
- Оно должно выглядеть примерно так:
	- Свойства
		- Что за стат дает
		- Значение этого стата
	- Что за карточки нужны для этой связи

Что нужно сделать?
- Написать скрипт, который будет автоматически генерировать эти карточки
	- По аналогии с прошлой генерицией
- Подготовить все необходимые данные
	- Наименование связи
		- Буду использовать имена карточек, которые участвуют в связи
		- Их же буду писать со ссылками внутрь файла
	- Что за стат дает связь
	- Сколько стата дает связь
- Добавить ссылки в эти карточки
	- Думаю надо сделать это на этапе подготовки данных

Процесс
- [ ] Написать модуль генерации
	- [ ] Протестить
- [x] Подготовить данные
	- [x] Данные готовы, но надо добавить ссылки на все карточки сразу
		- [x] Думаю что хороший вариант вытаскивать необходимые ссылки из обсидиана и вставлять их куда надо
			- [x] Нет, все равно много косяков будет, хз даже че делать, надо либо подумать либо руками уже делать и не париться
				- [x] очень хочу уже так сделать сил нет

Генерация карточек (не тестил)
```python
def generate_bestiary_sets(sets_list: list, sets_bonus_list: list, sets_bonus_value_list: list):
    property_start_end_str = "---"
    property_set_bonus_str = "bonus: "
    property_set_bonus_value_str = "value: "
    element_number = 0
    
    for set in sets_list:
        with open('bestiary_sets/' + str(set) + '.md', 'w', encoding='UTF-8') as bestiary_set_file:
            bestiary_set_file.write(property_start_end_str + '\n')
            bestiary_set_file.write(property_set_bonus_str + sets_bonus_list[element_number] + '\n')
            bestiary_set_file.write(property_set_bonus_value_str + str(sets_bonus_value_list[element_number]) + '\n')
            bestiary_set_file.write(property_start_end_str + '\n')
            bestiary_set_file.write(set + 'в отряде:' + sets_bonus_list[element_number] + '+' + str(sets_bonus_value_list[element_number]) + '\n')

            element_number += 1
```

# Генерация карточек глифов

Что я хочу?
Автоматически создать все карточки для глифов. Верификация - руками.

Что мне нужно сделать?
Написать скрипт, который будет генерировать странички следующего вида:
	Свойства:
		itemtype
		stat
		value
	Картинка
	Описание предмета
Как я хочу это сделать?
Во-первых, хочется вынести все генераторы в отдельный файл/класс
Во-вторых, некоторые вещи хочется вынести из всех генераторов. 
В остальном все так же как и было.

```python
    def generate_glyph_cards(self, glyph_list: list, glyph_description_list: list, glyph_stats_list: list, glyph_stat_values_list: list):
        element_number = 0
        
        for glyph_name in glyph_list:
            with open('glyphs/' + str(glyph_name) + '.md', 'w', encoding='UTF-8') as glyph_file:
                glyph_file.write(self.property_start_end_str + '\n')
                glyph_file.write(self.property_item_type_str + 'Глиф' + '\n')
                glyph_file.write(self.property_stat_str + str(glyph_stats_list[element_number]) + '\n')
                glyph_file.write(self.property_value_str + str(glyph_stat_values_list[element_number]) + '\n')
                glyph_file.write(self.property_start_end_str + '\n')
                glyph_file.write(self.glyph_placeholder_str + '\n')
                glyph_file.write(str(glyph_description_list[element_number]) + '\n')

                element_number += 1
```

# Генерация частей Бестиария
Что я хочу?
Автоматически создать все карточки для частей карт бестиария. Верификация - руками.

Что мне нужно сделать?
Написать скрипт, который будет генерировать странички следующего вида:
	Свойства:
		itemtype
	Картинка
	Описание предмета

