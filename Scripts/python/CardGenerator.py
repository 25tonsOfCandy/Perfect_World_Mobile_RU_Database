from abc import ABC, abstractmethod
from FileWriter import FileWriter
from cardgeneratorconfig import *

# TODO: посмотреть можно ли переписать генерацию чтобы не делить на несколько классов

class CardGenerator(ABC):
    def _create_file(self, file_path, content):
        FileWriter(file_path).write(content)

    @abstractmethod
    def generate(self, *args):
        pass


class BestiaryCardGenerator(CardGenerator):
    def generate(self, names_list: list, description_list: list, source_list: list ):
        for index, name in enumerate(names_list):
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
            self._create_file(f"results/bestiary/{name}.md", content)


class BestiarySetsCardGenerator(CardGenerator):
    def generate(self, names_list: list, bonus_list: list, bonus_value_list: list):
        for index, set_name in enumerate(names_list):
            content =(
            f"{START_END_STR}\n"
            f"{BONUS_STAT_STR}{bonus_list[index]}\n"
            f"{VALUE_STR}{bonus_value_list[index]}\n"
            f"{START_END_STR}\n"
            f"{set_name}в отряде:{bonus_list[index]}+{bonus_value_list[index]}\n"
            )
            self._create_file(f"results/bestiary_sets/{set_name}.md", content)


class GlyphsCardGenerator(CardGenerator):
    def generate(self, names_list: list, descriptions_list: list, stats_list: list, stat_values_list: list):
        for index, bestiary_part_name in enumerate(names_list):
            content =(
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}Глиф\n"
            f"{STAT_STR}{stats_list[index]}\n"
            f"{VALUE_STR}{stat_values_list[index]}\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['GLYPH']}\n"
            f"{descriptions_list[index]}\n"
            )
            self._create_file(f"results/bestiary_parts/{bestiary_part_name}.md", content)


class BestiaryPartCardGenerator(CardGenerator):
    def generate(self, names_list: list, descriptions_list: list):
        for index, bestiary_part_name in enumerate(names_list):
            content =(
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}Часть духа\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['BESTIARY_PART']}\n"
            f"{descriptions_list[index]}\n"
            )
            self._create_file(f"results/bestiary_parts/{bestiary_part_name}.md", content)


class BestiaryShineCardGenerator(CardGenerator):
    def generate(self, names_list: list, descriptions_list: list):
        for index, bestiary_shine_name in enumerate(names_list):
            content =( 
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}Дух Блеск\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['BESTIARY_SHINE']}\n"
            f"{descriptions_list[index]}\n"
            )
            self._create_file(f"results/bestiary_shine/{bestiary_shine_name}.md", content)


class ChimeraTechniquesCardGenerator(CardGenerator):
    def generate(self, names_list: list, descriptions_list: list, itemtypes_list: list):
        for index, chimera_techniques_name in enumerate(names_list):
            content =(
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}{itemtypes_list[index]}\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['CHIMERA_TECHNIQUES']}\n"
            f"{descriptions_list[index]}\n"
            )
            self._create_file(f"results/chimera_techniques/{chimera_techniques_name}.md", content)


class ChimeraCardGenerator(CardGenerator):
    def generate(self, names_list: list, descriptions_list: list, spectypes_list: list, source_list: list):
        for index, chimera_name in enumerate(names_list):
            content =(
            f"{START_END_STR}\n"
            f"{SPEC_TYPE_STR}{spectypes_list[index]}\n"
            f"{SOURCE_STR}{source_list[index]}\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['CHIMERA']}\n"
            f"{descriptions_list[index]}\n"
            )
            self._create_file(f"results/chimeras/{chimera_name}.md", content)


class ChimeraEggCardGenerator(CardGenerator):
    def generate(self, names_list: list, descriptions_list: list):
        for index, chimera_egg_name in enumerate(names_list):
            content =(
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}Яйцо Химеры\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['CHIMERA_EGG']}\n"
            f"{descriptions_list[index]}\n"
            )
            self._create_file(f"results/chimera_eggs/{chimera_egg_name}.md", content)


class ChimeraItemCardGenerator(CardGenerator):
    def generate(self, names_list: list, descriptions_list: list):
        for index, chimera_item_name in enumerate(names_list):
            content =( 
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}Химера\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['CHIMERA_ITEM']}\n"
            f"{descriptions_list[index]}\n"
            )
            self._create_file(f"results/chimera_items/{chimera_item_name}.md", content)


class ForChimeraCardGenerator(CardGenerator):
    def generate(self, names_list: list, descriptions_list: list):
        for index, chimera_item_name in enumerate(names_list):
            content =( 
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}Для Химеры\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['FOR_CHIMERA']}\n"
            f"{descriptions_list[index]}\n"
            )
            self._create_file(f"results/for_chimeras/{chimera_item_name}.md", content)


class EidolonCardGenerator(CardGenerator):
    def generate(self, names_list: list, eidolontypes_list: list, raritys_list: list, evolvecounts_list: list):
        for index, eidolon_name in enumerate(names_list):
            content =( 
            f"{START_END_STR}\n"
            f"{RARITY_STR}{raritys_list[index]}\n"
            f"{EVOLVE_COUNT_STR}{evolvecounts_list[index]}\n"
            f"{EIDOLON_TYPE_STR}{eidolontypes_list[index]}\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['EIDOLON']}\n"
            f"{STR_PLACEHOLDERS['DESCRIPTION']}\n"
            f"{STR_PLACEHOLDERS['EIDOLON_SKILL_NAME']}\n"
            )
            self._create_file(f"results/eidolons/{eidolon_name}.md", content)


class EidolonItemCardGenerator(CardGenerator):
    def generate(self, names_list: list, descriptions_list: list, itemtypes_list: list):
        for index, eidolon_item_name in enumerate(names_list):
            content =( 
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}{itemtypes_list[index]}\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['EIDOLON_ITEM']}\n"
            f"{descriptions_list[index]}\n"
            )
            self._create_file(f"results/eidolon_items/{eidolon_item_name}.md", content)


class EidolonDiaryCardGenerator(CardGenerator):
    def generate(self, names_list: list, descriptions_list: list, itemtypes_list: list):
        for index, eidolon_diary_name in enumerate(names_list):
            content =( 
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}{itemtypes_list[index]}\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['EIDOLON_DIARY']}\n"
            f"{descriptions_list[index]}\n"
            )
            self._create_file(f"results/eidolon_diarys/{eidolon_diary_name}.md", content)


class EidolonPillCardGenerator(CardGenerator):
    def generate(self, names_list: list, descriptions_list: list, itemtypes_list: list):
        for index, eidolon_pill_name in enumerate(names_list):
            content =( 
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}{itemtypes_list[index]}\n"
            f"{STAT_STR}\n"
            f"{VALUE_STR}\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['EIDOLON_PILL']}\n"
            f"{descriptions_list[index]}\n"
            )
            self._create_file(f"results/eidolon_pills/{eidolon_pill_name}.md", content)


class CodexCardGenerator(CardGenerator): # name, desc, itemtype, codexlvl, stats_own, stats_on, codextype
    def generate(self, names_list: list, descriptions_list: list, itemtypes_list: list, codexlvls_list: list, codex_stats_own_list: list, codex_stats_on_list: list, codextypes_list: list):
        for index, codex_name in enumerate(names_list):
            content =( 
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}{itemtypes_list[index]}\n"
            f"{CODEX_LVL_STR}{codexlvls_list[index]}\n"
            f"{STATS_OWN_STR}{codex_stats_own_list[index]}\n"
            f"{STATS_ON_STR}{codex_stats_on_list[index]}\n"
            f"{CODEX_TYPE_STR}{codextypes_list[index]}\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['CODEX']}\n"
            f"{str(descriptions_list[index])}\n"
            )
            self._create_file(f"results/codexes/{codex_name}.md", content)


class CodexItemCardGenerator(CardGenerator):
    def generate(self, names_list: list, descriptions_list: list, item_types_list: list):
        for index, codex_item_name in enumerate(names_list):
            content =( 
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}{item_types_list[index]}\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['CODEX_ITEM']}\n"
            f"{str(descriptions_list[index])}\n"
            )
            self._create_file(f"results/codex_items/{codex_item_name}.md", content)


class FolioCardGenerator(CardGenerator):
    def generate(self, names_list: list, descriptions_list: list, itemtypes_list: list, codex_needed_list: list, stats_list: list):
        for index, folio_name in enumerate(names_list):
            content =( 
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}{itemtypes_list[index]}\n"
            f"{STATS_STR}{stats_list[index]}\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['FOLIO']}\n"
            f"{descriptions_list[index]}\n\n"
            f"Для активации необходимы кодексы: "
            f"\n{codex_needed_list[index]}\n"
            )
            self._create_file(f"results/folios/{folio_name}.md", content)