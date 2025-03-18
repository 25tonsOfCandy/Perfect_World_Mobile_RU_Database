class CardGenerator:
    def __init__(self):
        # base
        self.property_start_end_str = "---"
        
        # markdown property strings 
        self.property_stats_str = "stats: "
        self.property_tier_str = "tier: "
        self.property_source_str = "source: "
        self.property_bonus_stat_str = "bonus: "
        self.property_value_str = "value: "
        self.property_item_type_str = "itemtype: "
        self.property_stat_str = "stat: "
        
        # image placeholders
        self.bestiary_placeholder_str = "![[Temp/Placeholder_Bestiary.png]]"
        self.glyph_placeholder_str = "![[Temp/Placeholder_Glyph.png]]"
        self.bestiary_part_placeholder_str = "![[Temp/Placeholder_Bestiary_Part.png]]"

        # string placeholders
        self.placeholder_skill_name_str = "SkillNamePlaceholder"

    
    def generate_bestiary_cards(self, names_list: list, source_list: list, description_list: list):
        element_number = 0

        for name in names_list:
            with open('bestiary/' + str(name) + '.md', 'w', encoding='UTF-8') as bestiary_file:
                bestiary_file.write(self.property_start_end_str + '\n')
                bestiary_file.write(self.property_stats_str + '\n')
                bestiary_file.write(self.property_tier_str + '\n')
                if source_list[element_number]  != None:
                    bestiary_file.write(self.property_source_str + str(source_list[element_number]) + '\n')
                else: 
                    bestiary_file.write(self.property_source_str + "Информация отсутствует" + '\n')
                bestiary_file.write(self.property_start_end_str + '\n')
                bestiary_file.write(self.bestiary_placeholder_str + '\n')
                bestiary_file.write(self.placeholder_skill_name_str + '\n')
                bestiary_file.write(description_list[element_number] + '\n')
                
                element_number += 1


    def generate_bestiary_sets(self, sets_list: list, sets_bonus_list: list, sets_bonus_value_list: list):
        element_number = 0
        
        for set_name in sets_list:
            with open('bestiary_sets/' + str(set_name) + '.md', 'w', encoding='UTF-8') as bestiary_set_file:
                bestiary_set_file.write(self.property_start_end_str + '\n')
                bestiary_set_file.write(self.property_bonus_stat_str + sets_bonus_list[element_number] + '\n')
                bestiary_set_file.write(self.property_value_str + str(sets_bonus_value_list[element_number]) + '\n')
                bestiary_set_file.write(self.property_start_end_str + '\n')
                bestiary_set_file.write(set_name + 'в отряде:' + sets_bonus_list[element_number] + '+' + str(sets_bonus_value_list[element_number]) + '\n')

                element_number += 1

    
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

    def generate_bestiary_part_cards(self, bestiary_part_names_list: list, bestiary_part_descriptions_list: list):
        element_number = 0
    
        for bestiary_part_name in bestiary_part_names_list:
            with open('bestiary_parts/' + str(bestiary_part_name) + '.md', 'w', encoding='UTF-8') as bestiary_part_file:
                bestiary_part_file.write(self.property_start_end_str + '\n')
                bestiary_part_file.write(self.property_item_type_str + 'Часть духа' + '\n')
                bestiary_part_file.write(self.property_start_end_str + '\n')
                bestiary_part_file.write(self.bestiary_part_placeholder_str + '\n')
                bestiary_part_file.write(str(bestiary_part_descriptions_list[element_number]) + '\n')
                print(bestiary_part_name)
                element_number += 1