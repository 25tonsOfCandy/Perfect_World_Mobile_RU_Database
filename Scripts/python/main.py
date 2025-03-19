"""
"""
import os
from CardGenerator import BestiaryCardGenerator, BestiarySetsCardGenerator, BestiaryPartCardGenerator, BestiaryShineCardGenerator, GlyphsCardGenerator
from Utils import Utils
from config import DIRECTORIES, FILES, TRIGGERS

bestiary_generator = BestiaryCardGenerator()
bestiarypart_generator = BestiaryPartCardGenerator()
bestiaryset_generator = BestiarySetsCardGenerator()
bestiaryshine_generator = BestiaryShineCardGenerator()
glyph_generator = GlyphsCardGenerator()
utils = Utils()


def process_bestiary():
    raw_data = utils.get_data_from_xlsx_file(filename = FILES['BESTIARY'], column_list = [3, 4, 5])
    names_list, description_list, source_list = raw_data
    bestiary_generator.generate(names_list, source_list, description_list)


def process_bestiary_sets():
    raw_data = utils.get_data_from_xlsx_file(filename = FILES['BESTIARY_SETS'], column_list = [1, 2, 3])
    sets_list, sets_bonus_list, sets_bonus_value_list = raw_data
    bestiaryset_generator.generate(sets_list, sets_bonus_list, sets_bonus_value_list)


def process_glyphs():
    raw_data = utils.get_data_from_xlsx_file(filename = FILES['GLYPHS'], column_list = [2, 3, 4, 5])
    glyph_names_list, glyph_description_list, glyph_stats_list, glyph_stat_values_list = raw_data
    glyph_generator.generate(glyph_names_list, glyph_description_list, glyph_stats_list, glyph_stat_values_list)


def process_bestiary_parts():
    raw_data = utils.get_data_from_xlsx_file(filename=FILES['BESTIARY_PARTS'], column_list=[2, 3])
    bestiary_part_names_list, bestiary_part_descriptions_list = raw_data
    bestiarypart_generator.generate(bestiary_part_names_list, bestiary_part_descriptions_list)


def process_bestiary_shines():
    raw_data = utils.get_data_from_xlsx_file(filename=FILES['BESTIARY_SHINE'], column_list=[2, 3])
    bestiary_shine_names_list, bestiary_shine_descriptions_list = raw_data
    bestiaryshine_generator.generate(bestiary_shine_names_list, bestiary_shine_descriptions_list)


def check_exists_all_important_directories():
    for directory in DIRECTORIES:
        if not os.path.exists(directory):
            os.makedirs(directory)


def main():
    check_exists_all_important_directories()

    if TRIGGERS["BESTIARY"]:
        process_bestiary()

    if TRIGGERS['BESTIARY_SETS']:
        process_bestiary_sets()

    if TRIGGERS['GLYPHS']:
        process_glyphs()

    if TRIGGERS['BESTIARY_PARTS']:
        process_bestiary_parts()

    if TRIGGERS['BESTIARY_SHINE']:
        process_bestiary_shines()

    return 0


if __name__ == '__main__':
    main()
    print("Complete!")
