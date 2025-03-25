import unittest
import os
import shutil
from unittest.mock import patch
from abc import ABC
from CardGenerator import *

class TestCardGenerator(unittest.TestCase):
    def setUp(self):
        # Создаем временные директории для тестов
        self.test_dirs = [
            "results/bestiary",
            "results/bestiary_sets",
            "results/bestiary_parts",
            "results/bestiary_shine",
            "results/chimera_techniques",
            "results/chimeras",
            "results/chimera_eggs",
            "results/chimera_items",
            "results/for_chimeras",
            "results/eidolons",
            "results/eidolon_items",
            "results/eidolon_diarys"
        ]
        
        for dir_path in self.test_dirs:
            os.makedirs(dir_path, exist_ok=True)

    def tearDown(self):
        # Удаляем временные директории после тестов
        for dir_path in self.test_dirs:
            if os.path.exists(dir_path):
                shutil.rmtree(dir_path)
        if os.path.exists("results"):
            shutil.rmtree("results")

    def test_card_generator_is_abstract(self):
        self.assertTrue(issubclass(CardGenerator, ABC))
        with self.assertRaises(TypeError):
            CardGenerator()  # Нельзя создать экземпляр абстрактного класса

    @patch.object(FileWriter, 'write')
    def test_bestiary_card_generator(self, mock_write):
        generator = BestiaryCardGenerator()
        names = ["Test Beast"]
        sources = ["Test Source"]
        descriptions = ["Test Description"]
        
        generator.generate(names, sources, descriptions)
        
        # Проверяем, что файл был создан с правильным содержимым
        expected_content = (
            f"{START_END_STR}\n"
            f"{STATS_STR}\n"
            f"{TIER_STR}\n"
            f"{SOURCE_STR}Test Source\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['BESTIARY']}\n"
            f"{STR_PLACEHOLDERS['SKILL_NAME']}\n"
            f"Test Description\n"
        )
        mock_write.assert_called_once_with(expected_content)

    @patch.object(FileWriter, 'write')
    def test_bestiary_sets_card_generator(self, mock_write):
        generator = BestiarySetsCardGenerator()
        names = ["Test Set"]
        bonuses = ["ATK"]
        bonus_values = ["10"]
        
        generator.generate(names, bonuses, bonus_values)
        
        expected_content = (
            f"{START_END_STR}\n"
            f"{BONUS_STAT_STR}ATK\n"
            f"{VALUE_STR}10\n"
            f"{START_END_STR}\n"
            f"Test Setв отряде:ATK+10\n"
        )
        mock_write.assert_called_once_with(expected_content)

    @patch.object(FileWriter, 'write')
    def test_glyphs_card_generator(self, mock_write):
        generator = GlyphsCardGenerator()
        names = ["Test Glyph"]
        descriptions = ["Test Description"]
        stats = ["ATK"]
        stat_values = ["15"]
        
        generator.generate(names, descriptions, stats, stat_values)
        
        expected_content = (
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}Глиф\n"
            f"{STAT_STR}ATK\n"
            f"{VALUE_STR}15\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['GLYPH']}\n"
            f"Test Description\n"
        )
        mock_write.assert_called_once_with(expected_content)

    @patch.object(FileWriter, 'write')
    def test_bestiary_part_card_generator(self, mock_write):
        generator = BestiaryPartCardGenerator()
        names = ["Test Part"]
        descriptions = ["Test Description"]
        
        generator.generate(names, descriptions)
        
        expected_content = (
            f"{START_END_STR}\n"
            f"{ITEM_TYPE_STR}Часть духа\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['BESTIARY_PART']}\n"
            f"Test Description\n"
        )
        mock_write.assert_called_once_with(expected_content)

    @patch.object(FileWriter, 'write')
    def test_chimera_card_generator(self, mock_write):
        generator = ChimeraCardGenerator()
        names = ["Test Chimera"]
        descriptions = ["Test Description"]
        spectypes = ["Fire"]
        sources = ["Test Source"]
        
        generator.generate(names, descriptions, spectypes, sources)
        
        expected_content = (
            f"{START_END_STR}\n"
            f"{SPEC_TYPE_STR}Fire\n"
            f"{SOURCE_STR}Test Source\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['CHIMERA']}\n"
            f"Test Description\n"
        )
        mock_write.assert_called_once_with(expected_content)

    @patch.object(FileWriter, 'write')
    def test_eidolon_card_generator(self, mock_write):
        generator = EidolonCardGenerator()
        names = ["Test Eidolon"]
        eidolontypes = ["Attack"]
        raritys = ["Rare"]
        evolvecounts = ["3"]
        
        generator.generate(names, eidolontypes, raritys, evolvecounts)
        
        expected_content = (
            f"{START_END_STR}\n"
            f"{RARITY_STR}Rare\n"
            f"{EVOLVE_COUNT_STR}3\n"
            f"{EIDOLON_TYPE_STR}Attack\n"
            f"{START_END_STR}\n"
            f"{IMAGE_PLACEHOLDERS['EIDOLON']}\n"
            f"{STR_PLACEHOLDERS['DESCRIPTION']}\n"
            f"{STR_PLACEHOLDERS['EIDOLON_SKILL_NAME']}\n"
        )
        mock_write.assert_called_once_with(expected_content)

    def test_all_generators_have_generate_method(self):
        # Проверяем, что все конкретные генераторы реализуют метод generate
        generators = [
            BestiaryCardGenerator,
            BestiarySetsCardGenerator,
            GlyphsCardGenerator,
            BestiaryPartCardGenerator,
            BestiaryShineCardGenerator,
            ChimeraTechniquesCardGenerator,
            ChimeraCardGenerator,
            ChimeraEggCardGenerator,
            ChimeraItemCardGenerator,
            ForChimeraCardGenerator,
            EidolonCardGenerator,
            EidolonItemCardGenerator,
            EidolonDiaryCardGenerator
        ]
        
        for generator_class in generators:
            generator = generator_class()
            self.assertTrue(hasattr(generator, 'generate'))
            self.assertTrue(callable(generator.generate))

if __name__ == '__main__':
    unittest.main()