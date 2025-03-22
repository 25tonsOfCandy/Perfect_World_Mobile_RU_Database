from abc import ABC, abstractmethod
from FileWriter import FileWriter
from cardgeneratorconfig import *


class CardGenerator(ABC):
    def _create_file(self, file_path, content):
        file_writer = FileWriter(file_path)
        file_writer.write(content)

    @abstractmethod
    def generate(self, *args):
        pass


class BestiaryCardGenerator(CardGenerator):
    def generate(self, names_list: list, source_list: list, description_list: list):
        for index, name in enumerate(names_list):
            file_path = f"results/bestiary/{name}.md"
            content =(
            f"{START_END_STR}\n"
            f"{STATS_STR}\n"
            f"{TIER_STR}\n"
            f"{SOURCE_STR}{source_list[index] if source_list[index] is not None else 'Информация отсутствует'}\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['BESTIARY']}\n"
            f"{STR_PLACEHOLDERS['SKILL_NAME']}\n"
            f"{description_list[index]}\n"
            )
            self._create_file(file_path, content)


class BestiarySetsCardGenerator(CardGenerator):
    def generate(self, names_list: list, bonus_list: list, bonus_value_list: list):
        for index, set_name in enumerate(names_list):
            file_path = f"results/bestiary_sets/{set_name}.md"
            content =(
            f"{START_END_STR}\n"
            f"{BONUS_STAT_STR}{bonus_list[index]}\n"
            f"{VALUE_STR}{bonus_value_list[index]}\n"
            f"{START_END_STR}\n"
            f"{set_name}в отряде:{bonus_list[index]}+{bonus_value_list[index]}\n"
            )
            self._create_file(file_path, content)


class GlyphsCardGenerator(CardGenerator):
    def generate(self, names_list: list, descriptions_list: list, stats_list: list, stat_values_list: list):
        for index, bestiary_part_name in enumerate(names_list):
            file_path = f"results/bestiary_parts/{bestiary_part_name}.md"
            content =(
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}Глиф\n"
            f"{STAT_STR}{stats_list[index]}\n"
            f"{VALUE_STR}{stat_values_list[index]}\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['GLYPH']}\n"
            f"{descriptions_list[index]}\n"
            )
            self._create_file(file_path, content)


class BestiaryPartCardGenerator(CardGenerator):
    def generate(self, names_list: list, descriptions_list: list):
        for index, bestiary_part_name in enumerate(names_list):
            file_path = f"results/bestiary_parts/{bestiary_part_name}.md"
            content =(
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}Часть духа\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['BESTIARY_PART']}\n"
            f"{descriptions_list[index]}\n"
            )
            self._create_file(file_path, content)


class BestiaryShineCardGenerator(CardGenerator):
    def generate(self, names_list: list, descriptions_list: list):
        for index, bestiary_shine_name in enumerate(names_list):
            file_path = f"results/bestiary_shine/{bestiary_shine_name}.md"
            content =( 
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}Дух Блеск\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['BESTIARY_SHINE']}\n"
            f"{descriptions_list[index]}\n"
            )
            self._create_file(file_path, content)


class ChimeraTechniquesCardGenerator(CardGenerator):
    def generate(self, names_list: list, descriptions_list: list, itemtypes_list: list):
        for index, chimera_techniques_name in enumerate(names_list):
            file_path = f"results/chimera_techniques/{chimera_techniques_name}.md"
            content =(
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}{itemtypes_list[index]}\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['CHIMERA_TECHNIQUES']}\n"
            f"{descriptions_list[index]}\n"
            )
            self._create_file(file_path, content)


class ChimeraCardGenerator(CardGenerator):
    def generate(self, names_list: list, descriptions_list: list, spectypes_list: list, source_list: list):
        for index, chimera_name in enumerate(names_list):
            file_path = f"results/chimeras/{chimera_name}.md"
            content =(
            f"{START_END_STR}\n"
            f"{SPEC_TYPE_STR}{spectypes_list[index]}\n"
            f"{SOURCE_STR}{source_list[index]}"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['CHIMERA']}\n"
            f"{descriptions_list[index]}\n"
            )
            self._create_file(file_path, content)


class ChimeraEggCardGenerator(CardGenerator):
    def generate(self, names_list: list, descriptions_list: list):
        for index, chimera_egg_name in enumerate(names_list):
            file_path = f"results/chimera_eggs/{chimera_egg_name}.md"
            content =(
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}Яйцо Химеры\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['CHIMERA_EGG']}\n"
            f"{descriptions_list[index]}\n"
            )
            self._create_file(file_path, content)


class ChimeraItemCardGenerator(CardGenerator):
    def generate(self, names_list: list, descriptions_list: list):
        for index, chimera_item_name in enumerate(names_list):
            file_path = f"results/chimera_items/{chimera_item_name}.md"
            content =( 
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}Химера\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['CHIMERA_ITEM']}\n"
            f"{descriptions_list[index]}\n"
            )
            self._create_file(file_path, content)


class ForChimeraCardGenerator(CardGenerator):
    def generate(self, names_list: list, descriptions_list: list):
        for index, chimera_item_name in enumerate(names_list):
            file_path = f"results/for_chimeras/{chimera_item_name}.md"
            content =( 
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}Для Химеры\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['FOR_CHIMERA']}\n"
            f"{descriptions_list[index]}\n"
            )
            self._create_file(file_path, content)