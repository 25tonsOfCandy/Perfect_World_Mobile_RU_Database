from Utils import Utils
Utils = Utils()

class CardGenerator:
    def __init__(self):
        # base
        self.start_end_str = "---"
        
        # markdown property strings 
        self.stats_str = "stats: "
        self.tier_str = "tier: "
        self.source_str = "source: "
        self.bonus_stat_str = "bonus: "
        self.value_str = "value: "
        self.item_type_str = "itemtype: "
        self.stat_str = "stat: "
        
        # image placeholders
        self.placeholder_bestiary = "![[Temp/Placeholder_Bestiary.png]]"
        self.placeholder_glyph = "![[Temp/Placeholder_Glyph.png]]"
        self.placeholder_bestiary_part = "![[Temp/Placeholder_Bestiary_Part.png]]"
        self.placeholder_bestiary_shine = "![[Temp/Placeholder_Bestiary_Shine.png]]"
        
        # string placeholders
        self.placeholder_skill_name = "SkillNamePlaceholder"

    
    def generate_bestiary_cards(self, names_list: list, source_list: list, description_list: list):
        index = 0
        for index, name in enumerate(names_list):
            file_path = f"bestiary/{name}.md"
            content =(
            f"{self.start_end_str}\n"
            f"{self.stats_str}\n"
            f"{self.tier_str}\n"
            f"{self.source_str}{source_list[index] if source_list[index] is not None else 'Информация отсутствует'}\n"
            f"{self.start_end_str}\n"
            f"{self.placeholder_bestiary}\n"
            f"{description_list[index]}\n"
            )
            print(content)
            Utils.write_content_to_file(file_path, content)


    def generate_bestiary_sets(self, sets_list: list, sets_bonus_list: list, sets_bonus_value_list: list):
        index = 0
        for index, set_name in enumerate(sets_list):
            file_path = f"bestiary_sets/{set_name}.md"
            content =(
            f"{self.start_end_str}\n"
            f"{self.bonus_stat_str}{sets_bonus_list[index]}\n"
            f"{self.value_str}{sets_bonus_value_list[index]}\n"
            f"{self.start_end_str}\n"
            f"{set_name}в отряде:{sets_bonus_list[index]}+{sets_bonus_value_list[index]}\n"
            )

            Utils.write_content_to_file(file_path, content)


    def generate_glyph_cards(self, glyph_list: list, glyph_description_list: list, glyph_stats_list: list, glyph_stat_values_list: list):
        index = 0

        for index, bestiary_part_name in enumerate(glyph_list):
            file_path = f"bestiary_parts/{bestiary_part_name}.md"
            content =(
            f"{self.start_end_str}\n"
            f"{self.item_type_str}Глиф\n"
            f"{self.stat_str}{glyph_stats_list[index]}\n"
            f"{self.value_str}{glyph_stat_values_list[index]}\n"
            f"{self.start_end_str}\n"
            f"{self.placeholder_glyph}\n"
            f"{glyph_description_list[index]}\n"
            )

            Utils.write_content_to_file(file_path, content)


    def generate_bestiary_part_cards(self, bestiary_part_names_list: list, bestiary_part_descriptions_list: list):
        index = 0

        for index, bestiary_part_name in enumerate(bestiary_part_names_list):
            file_path = f"bestiary_parts/{bestiary_part_name}.md"
            content =(
            f"{self.start_end_str}\n"
            f"{self.item_type_str}Часть духа\n"
            f"{self.start_end_str}\n"
            f"{self.placeholder_bestiary_part}\n"
            f"{bestiary_part_descriptions_list[index]}\n"
            )

            Utils.write_content_to_file(file_path, content)


    def generate_bestiary_shine_cards(self, bestiary_shine_names_list: list, bestiary_shine_descriptions_list: list):
        index = 0

        for index, bestiary_shine_name in enumerate(bestiary_shine_names_list):
            file_path = f"bestiary_shine/{bestiary_shine_name}.md"
            content =( 
            f"{self.start_end_str}\n"
            f"{self.item_type_str}Дух Блеск\n"
            f"{self.start_end_str}\n"
            f"{self.placeholder_bestiary_shine}\n"
            f"{bestiary_shine_descriptions_list[index]}\n"
            )

            Utils.write_content_to_file(file_path, content)
