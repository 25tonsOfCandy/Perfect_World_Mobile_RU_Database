"""
"""

import openpyxl
import os
# PRESETS
# BESTIARY - for generating bestiary cards
# BESTIARY_SETS - for generating bestiary sets pages
# NULL ("") - do nothing
PRESET = "BESTIARY_SETS"
DIRECTORIES = ['bestiary', 'bestiary_sets'] # Important directories for checking


# UTILS
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


def write_list_to_file(data_list: list, path_to_file_with_filename: str):
    with open(path_to_file_with_filename, "w", encoding="UTF-8")  as file:
        for line in data_list:
            file.write(str(line) + "\n")
        print("File created: " + path_to_file_with_filename)


def check_exists_all_important_directories():
    for directory in DIRECTORIES:
        if not os.path.exists(directory):
            os.makedirs(directory)


# GENERATORS OF CARDS
def generate_bestiary_cards(names_list: list, source_list: list, description_list: list):
    property_start_end_str = "---"
    property_stats_str = "stats: "
    property_tier_str = "tier: "
    property_source_str = "source: "
    placeholder_str = "![[Temp/Placeholder_Bestiary.png]]"
    placeholder_skill_name_str = "SkillNamePlaceholder"
    # set_str = "# Связи"

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


def generate_bestiary_sets(sets_list: list, sets_bonus_list: list, sets_bonus_value_list: list):
    property_start_end_str = "---"
    property_set_bonus_str = "bonus: "
    property_set_bonus_value_str = "value: "
    element_number = 0
    
    for set in sets_list:
        with open('bestiary_sets/' + str(set) + '.md', 'w', encoding='UTF-8') as bestiary_set_file:
            bestiary_set_file.write(property_start_end_str + '\n')
            bestiary_set_file.write(property_set_bonus_str + sets_bonus_list[element_number] + '\n')
            bestiary_set_file.write(property_set_bonus_value_str + sets_bonus_value_list[element_number] + '\n')
            bestiary_set_file.write(property_start_end_str + '\n')
            bestiary_set_file.write(set + 'в отряде:' + sets_bonus_list[element_number] + '+' + sets_bonus_value_list[element_number] + '\n')

            element_number += 1


def main():
    check_exists_all_important_directories()

    if PRESET == "BESTIARY":
        raw_data = get_data_from_xlsx_file(filename = 'Bestiary_Skills_Source_RUCHNames.xlsx', column_list = [3, 4, 5])
        names_list = next(raw_data)
        description_list = next(raw_data)
        source_list = next(raw_data)

        generate_bestiary_cards(names_list, source_list, description_list)
        return 0


    elif PRESET == "BESTIARY_SETS":
        raw_data = get_data_from_xlsx_file(filename = 'BestiarySetBonuses.xlsx', column_list = [1, 2, 3])
        sets_list = next(raw_data)
        sets_bonus_list = next(raw_data)
        sets_bonus_value_list = next(raw_data)

        print(sets_list)
        # generate_bestiary_sets(sets_list, sets_bonus_list, sets_bonus_value_list)
        return 0

    if PRESET == "":
        return 1
    else:
        return 2


if __name__ == '__main__':
    result = main()
    if result == 1:
        print('Preset is empty')

    elif result == 2:
        print('Wrong preset')

    else: print("Complete!")
    
