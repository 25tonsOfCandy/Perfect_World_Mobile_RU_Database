"""
"""
import os
from CardGenerator import CardGenerator
from Utils import Utils

# Triggers
# BESTIARY - for generating bestiary cards
# BESTIARY_SETS - for generating bestiary sets pages
# GLYPHS - for generating glyph cards
# BESTIARY_PARTS - for generating bestiary parts
# BESTIARY_SHINE - for generating bestiary shine cards
# NULL ("") - do nothing
ISBESTIARY = False
ISBESTIARY_PART = False
ISGLYPH = False
ISBESTIARY_SETS = False
ISBESTIARY_SHINE = False

DIRECTORIES = ['bestiary', 'bestiary_sets', 'glyphs', 'bestiary_parts', 'bestiary_shine'] # Important directories for checking
Utils = Utils()

# UTILS
def check_exists_all_important_directories():
    for directory in DIRECTORIES:
        if not os.path.exists(directory):
            os.makedirs(directory)


def main():
    check_exists_all_important_directories()
    generator = CardGenerator()

    if ISBESTIARY:
        raw_data = Utils.get_data_from_xlsx_file(filename = 'Bestiary_Skills_Source_RUCHNames.xlsx', column_list = [3, 4, 5])
        names_list = next(raw_data)
        description_list = next(raw_data)
        source_list = next(raw_data)
        generator.generate_bestiary_cards(names_list, source_list, description_list)

    if ISBESTIARY_SETS:
        raw_data = Utils.get_data_from_xlsx_file(filename = 'BestiarySetBonuses.xlsx', column_list = [1, 2, 3])
        sets_list = next(raw_data)
        sets_bonus_list = next(raw_data)
        sets_bonus_value_list = next(raw_data)
        generator.generate_bestiary_sets(sets_list, sets_bonus_list, sets_bonus_value_list)

    if ISGLYPH:
        raw_data = Utils.get_data_from_xlsx_file(filename = 'Glyphs.xlsx', column_list = [2, 3, 4, 5])
        glyph_names_list = next(raw_data)
        glyph_description_list = next(raw_data)
        glyph_stats_list = next(raw_data)
        glyph_stat_values_list = next(raw_data)
        generator.generate_glyph_cards(glyph_names_list, glyph_description_list, glyph_stats_list, glyph_stat_values_list)

    if ISBESTIARY_PART:
        raw_data = Utils.get_data_from_xlsx_file(filename='BestiaryParts.xlsx', column_list=[2, 3])
        bestiary_part_names_list = next(raw_data)
        bestiary_part_descriptions_list = next(raw_data)
        generator.generate_bestiary_part_cards(bestiary_part_names_list, bestiary_part_descriptions_list)

    if ISBESTIARY_SHINE:
        raw_data = Utils.get_data_from_xlsx_file(filename='BestiaryShine.xlsx', column_list=[2, 3])
        bestiary_shine_names_list = next(raw_data)
        bestiary_shine_descriptions_list = next(raw_data)
        generator.generate_bestiary_shine_cards(bestiary_shine_names_list, bestiary_shine_descriptions_list)

    return 0


if __name__ == '__main__':
    main()
    print("Complete!")
