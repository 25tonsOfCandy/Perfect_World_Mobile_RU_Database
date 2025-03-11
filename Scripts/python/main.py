"""
"""

import openpyxl
import os
# PRESETS
# BESTIARY - for generating bestiary cards
# NULL ("") - do nothing
PRESET = "BESTIARY"
DIRECTORIES = ['bestiary'] # Important directories for checking


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
    set_str = "# Связи"

    element_number = 0

    for name in names_list:
        with open('bestiary/' + str(name) + '.md', 'w', encoding='UTF-8') as bestiary_file:
            bestiary_file.write(property_start_end_str + '\n')
            bestiary_file.write(property_stats_str + '\n')
            bestiary_file.write(property_tier_str + '\n')
            bestiary_file.write(property_source_str + str(source_list[element_number]) + '\n')
            bestiary_file.write(property_start_end_str + '\n')
            bestiary_file.write(placeholder_str + '\n')
            bestiary_file.write(placeholder_skill_name_str + '\n')
            bestiary_file.write(description_list[element_number] + '\n')
            
            element_number += 1



def main():
    check_exists_all_important_directories()

    if PRESET == "BESTIARY":
        raw_data = get_data_from_xlsx_file(filename = 'test.xlsx', column_list = [1, 2, 4])
        column1 = next(raw_data)
        column2 = next(raw_data)
        column3 = next(raw_data)
        write_list_to_file(column1, 'bestiary/test.md')

        # print(column1, column2, column3, sep="   ")

    if PRESET == "":
        return 0



if __name__ == '__main__':
    main()
