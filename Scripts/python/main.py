"""
"""
import os
from CardGenerator import *
from XLSXDataExtractor import XLSXDataExtractor
from config import DIRECTORIES, FILES, TRIGGERS, COLUMNS


generators = {
    "BESTIARY": BestiaryCardGenerator(),
    "BESTIARY_PARTS": BestiaryPartCardGenerator(),
    "BESTIARY_SETS": BestiarySetsCardGenerator(),
    "BESTIARY_SHINES": BestiaryShineCardGenerator(),
    "GLYPHS": GlyphsCardGenerator(),
    "CHIMERA_TECHNIQUES": ChimeraTechniquesCardGenerator(),
    "CHIMERAS": ChimeraCardGenerator(),
    "CHIMERA_EGGS": ChimeraEggCardGenerator(),
    "CHIMERA_ITEMS": ChimeraItemCardGenerator(),
    "FOR_CHIMERAS": ForChimeraCardGenerator(),
    "EIDOLONS": EidolonCardGenerator(),
    "EIDOLON_ITEMS": EidolonItemCardGenerator(),
    "EIDOLON_DIARYS": EidolonDiaryCardGenerator(),
    "EIDOLON_PILLS": EidolonPillCardGenerator(),
    "CODEXES": CodexCardGenerator(),
    "CODEX_ITEMS": CodexItemCardGenerator(),
    "FOLIOS": FolioCardGenerator(),
    "TALISMANS": TalismanCardGenerator(),
    "TALISMAN_PARTS": TalismanPartCardGenerator(),
    "TABLETS": TabletCardGenerator(),
    "TABLET_ITEMS": TabletItemCardGenerator(),
    "JASPERS": JasperCardGenerator(),
    "ARTIFACTS": ArtifactCardGenerator(),
    "ARTIFACT_ITEMS": ArtifactItemCardGenerator(),
    "RUNES": RuneCardGenerator(),
    "RUNE_BUFFS": RuneBuffCardGenerator(),
}
xlsx_data_extractor = XLSXDataExtractor()


def generate_cards(generator: CardGenerator, source_file: str, columns: str):
    generator.generate(*xlsx_data_extractor.extract_data(source_file, columns))


def ensure_directories_exist():
    for directory in DIRECTORIES:
        if not os.path.exists(directory):
            os.makedirs(directory)


def main():
    ensure_directories_exist()

    for key, value in TRIGGERS.items():
        if value:
            print(f"{key} generating...")
            generate_cards(generators[key], FILES[key], COLUMNS[key])

    return 0


if __name__ == '__main__':
    main()
    print("Complete!")
