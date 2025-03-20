"""
"""
import os
from CardGenerator import BestiaryCardGenerator, BestiarySetsCardGenerator, BestiaryPartCardGenerator
from CardGenerator import ChimeraTechniquesCardGenerator, BestiaryShineCardGenerator, GlyphsCardGenerator
from XLSXDataExtractor import XLSXDataExtractor
from config import DIRECTORIES, FILES, TRIGGERS, COLUMNS

bestiary_generator = BestiaryCardGenerator()
bestiarypart_generator = BestiaryPartCardGenerator()
bestiaryset_generator = BestiarySetsCardGenerator()
bestiaryshine_generator = BestiaryShineCardGenerator()
glyph_generator = GlyphsCardGenerator()
chimera_technique_generator = ChimeraTechniquesCardGenerator()
xlsx_data_extractor = XLSXDataExtractor()


def process_bestiary():
    raw_data = xlsx_data_extractor.get_columns_data(filename = FILES['BESTIARY'], column_list = COLUMNS['BESTIARY'])
    names_list, description_list, source_list = raw_data
    bestiary_generator.generate(names_list, source_list, description_list)


def process_bestiary_sets():
    raw_data = xlsx_data_extractor.get_columns_data(filename = FILES['BESTIARY_SETS'], column_list = COLUMNS['BESTIARY_SETS'])
    names_list, bonus_list, bonus_value_list = raw_data
    bestiaryset_generator.generate(names_list, bonus_list, bonus_value_list)


def process_glyphs():
    raw_data = xlsx_data_extractor.get_columns_data(filename = FILES['GLYPHS'], column_list = COLUMNS["GLYPHS"])
    names_list, description_list, stats_list, stat_values_list = raw_data
    glyph_generator.generate(names_list, description_list, stats_list, stat_values_list)


def process_bestiary_parts():
    raw_data = xlsx_data_extractor.get_columns_data(filename=FILES['BESTIARY_PARTS'], column_list=COLUMNS['BESTIARY_PARTS'])
    names_list, descriptions_list = raw_data
    bestiarypart_generator.generate(names_list, descriptions_list)


def process_bestiary_shines():
    raw_data = xlsx_data_extractor.get_columns_data(filename=FILES['BESTIARY_SHINE'], column_list=COLUMNS['BESTIARY_SHINES'])
    names_list, descriptions_list = raw_data
    bestiaryshine_generator.generate(names_list, descriptions_list)


def process_chimera_techniques():
    raw_data = xlsx_data_extractor.get_columns_data(filename=FILES['CHIMERA_TECHNIQUES'], column_list=COLUMNS['CHIMERA_TECHNIQUES'])
    names_list, description_list, itemtypes_list= raw_data
    chimera_technique_generator.generate(names_list, description_list, itemtypes_list)


def ensure_directories_exist():
    for directory in DIRECTORIES:
        if not os.path.exists(directory):
            os.makedirs(directory)


def main():
    ensure_directories_exist()

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

    if TRIGGERS["CHIMERA_TECHNIQUES"]:
        process_chimera_techniques()
        
    return 0


if __name__ == '__main__':
    main()
    print("Complete!")
