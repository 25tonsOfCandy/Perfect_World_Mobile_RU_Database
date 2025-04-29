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


class TalismanCardGenerator(CardGenerator):
    def generate(self, names_list: list, descriptions_list: list, parts_needed_list: list, activate_silver_cost_list: list, jasper_slots_list: list, sources_list: list):
        for index, talisman_name in enumerate(names_list):
            content =( 
            f"{START_END_STR}\n"
            f"{ACTIVATE_SILVER_COST_STR}{activate_silver_cost_list[index]}\n"
            f"{PARTS_NEEDED_STR}{parts_needed_list[index]}\n"
            f"{JASPER_SLOTS_STR}{jasper_slots_list[index]}\n"
            f"{SOURCE_STR}{sources_list[index]}\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['TALISMAN']}\n"
            f"{descriptions_list[index]}\n"
            )
            self._create_file(f"results/talismans/{talisman_name}.md", content)


class TalismanPartCardGenerator(CardGenerator):
    def generate(self, names_list: list, descriptions_list: list, itemtypes_list: list):
        for index, talisman_part_name in enumerate(names_list):
            content =( 
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}{itemtypes_list[index]}\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['TALISMAN_PART']}\n"
            f"{descriptions_list[index]}\n"
            )
            self._create_file(f"results/talisman_parts/{talisman_part_name}.md", content)


class TabletCardGenerator(CardGenerator): # name, desc, rarity, number_slots, base_stats, small_tablet_stats, big_tablet_stats, perfect_tablet_stats, source
    def generate(self, names_list: list, descriptions_list: list, rarities_list: list, 
                 number_slots_list: list, base_stats_list: list, 
                 small_tablet_stats_list: list, big_tablet_stats_list: list, 
                 perfect_tablet_stats_list: list, sources_list: list):

        for index, tablet_name in enumerate(names_list):
            content =( 
            f"{START_END_STR}\n"
            f"{RARITY_STR}{rarities_list[index]}\n"
            f"{NUMBER_SLOTS_STR}{number_slots_list[index]}\n"
            f"{STATS_STR}{base_stats_list[index]}\n"
            f"{SMALL_TABLET_STATS_STR}{small_tablet_stats_list[index]}\n"
            f"{BIG_TABLET_STATS_STR}{big_tablet_stats_list[index]}\n"
            f"{PERFECT_TABLET_STATS_STR}{perfect_tablet_stats_list[index]}\n"
            f"{SOURCE_STR}{sources_list[index]}\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['TABLET']}\n"
            f"{descriptions_list[index]}\n"
            )
            self._create_file(f"results/tablets/{tablet_name}.md", content)


class TabletItemCardGenerator(CardGenerator):# name, desc, itemtype
    def generate(self, names_list: list, descriptions_list: list, itemtypes_list: list):
        for index, tablet_item_name in enumerate(names_list):
            content =( 
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}{itemtypes_list[index]}\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['TABLET_ITEM']}\n"
            f"{descriptions_list[index]}\n"
            )
            self._create_file(f"results/tablet_items/{tablet_item_name}.md", content)


class JasperCardGenerator(CardGenerator):# name, desc, itemtype, stats
    def generate(self, names_list: list, descriptions_list: list, itemtypes_list: list, stats_list: list):
        for index, jasper_name in enumerate(names_list):
            content =( 
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}{itemtypes_list[index]}\n"
            f"{STATS_STR}{stats_list[index]}\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['JASPER']}\n"
            f"{descriptions_list[index]}\n"
            )
            self._create_file(f"results/jaspers/{jasper_name}.md", content)


class ArtifactCardGenerator(CardGenerator):
    def generate(self, names_list: list, activation_stats_list: list, 
                 engraving_stats_list: list, engraving_stage_bonus_list: list, 
                 sources_list: list, active_skills_list: list,
                 passive_skill_names1_list: list, passive_skill_names2_list: list, passive_skill_names3_list: list, 
                 passive_skills1_list: list, passive_skills2_list: list, passive_skills3_list: list):
        for index, artifact_name in enumerate(names_list):
            content =( 
            f"{START_END_STR}\n"
            f"{ACTIVATION_BONUS_STR}{activation_stats_list[index]}\n"
            f"{ENGRAVING_STATS_STR}{engraving_stats_list[index]}\n"
            f"{ENGRAVING_STAGE_BONUS_STR}{engraving_stage_bonus_list[index]}\n"
            f"{SOURCE_STR}{sources_list[index]}\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['ARTIFACT']}\n"
            f"{STR_PLACEHOLDERS['ACTIVE_SKILL']}\n"
            f"{active_skills_list[index]}\n\n"
            f"# {passive_skill_names1_list[index]}: \n{passive_skills1_list[index]}\n"
            f"# {passive_skill_names2_list[index]}: \n{passive_skills2_list[index]}\n"
            f"# {passive_skill_names3_list[index]}: \n{passive_skills3_list[index]}\n"
            )
            self._create_file(f"results/artifacts/{artifact_name}.md", content)


class ArtifactItemCardGenerator(CardGenerator):# name, desc, item_type
    def generate(self, names_list: list, descriptions_list: list, item_types_list: list):
        for index, artifact_item_name in enumerate(names_list):
            content =( 
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}{item_types_list[index]}\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['ARTIFACT_ITEM']}\n"
            f"{descriptions_list[index]}\n"
            )
            self._create_file(f"results/artifact_items/{artifact_item_name}.md", content)


class RuneCardGenerator(CardGenerator): # name, stats, rarity, rune_type
    def generate(self, names_list: list, stats_list: list, rarities_list: list, rune_types_list: list):
        for index, rune_name in enumerate(names_list):
            content =( 
            f"{START_END_STR}\n"
            f"{STATS_STR}{stats_list[index]}\n"
            f"{RARITY_STR}{rarities_list[index]}\n"
            f"{RUNE_TYPE_STR}{rune_types_list[index]}\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['RUNE']}\n"
            )
            self._create_file(f"results/runes/{rune_name}.md", content)


class RuneBuffCardGenerator(CardGenerator): # # name, rune_type, rune_skill, class
    def generate(self, names_list: list, rune_types_list: list, rune_skills_list: list, classes_list: list):
        for index, rune_buff_name in enumerate(names_list):
            if classes_list[index] == "Class": continue
            
            content =( 
            f"{START_END_STR}\n"
            f"{RUNE_TYPE_STR}{rune_types_list[index]}\n"
            f"{CLASS_STR}{classes_list[index]}\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['RUNE_BUFF']}\n"
            f"{rune_skills_list[index]}\n"
            )
            self._create_file(f"results/rune_buffs/{classes_list[index]}/{rune_buff_name}.md", content)