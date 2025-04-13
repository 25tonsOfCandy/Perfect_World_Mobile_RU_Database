TRIGGERS = {
    "BESTIARY": False,
    "BESTIARY_SETS": False,
    "GLYPHS": False,
    "BESTIARY_PARTS": False,
    "BESTIARY_SHINES": False,
    "CHIMERA_TECHNIQUES": False,
    "CHIMERAS": False,
    "CHIMERA_EGGS": False,
    "CHIMERA_ITEMS": False,
    "FOR_CHIMERAS": False,
    "EIDOLONS": False,
    "EIDOLON_ITEMS": False,
    "EIDOLON_DIARYS": False,
    "EIDOLON_PILLS": False,
    "CODEXES": False,
    "CODEX_ITEMS": False,
    "FOLIOS": False,
    "TALISMANS": False,
    "TALISMAN_PARTS": False,
    "TABLETS": False,
    "TABLET_ITEMS": False,
    "JASPERS": True,
}

DIRECTORIES = ['results',
            'results/bestiary',
            'results/bestiary_sets', 
            'results/glyphs', 
            'results/bestiary_parts', 
            'results/bestiary_shines',
            'results/chimera_techniques',
            'results/chimeras',
            'results/chimera_eggs',
            'results/chimera_items',
            'results/for_chimeras',
            'results/eidolons',
            'results/eidolon_items',
            'results/eidolon_diarys',
            'results/eidolon_pills',
            "results/codexes",
            "results/codex_items",
            "results/folios",
            "results/talismans",
            "results/talisman_parts",
            "results/tablets",
            "results/tablet_items",
            "results/jaspers"] 


FILES = {
    "BESTIARY": 'SourceTables/Bestiary_Skills_Source_RUCHNames.xlsx',
    "BESTIARY_SETS": 'SourceTables/BestiarySetBonuses.xlsx',
    "GLYPHS": 'SourceTables/Glyphs.xlsx',
    "BESTIARY_PARTS": 'SourceTables/BestiaryParts.xlsx',
    "BESTIARY_SHINES": 'SourceTables/BestiaryShine.xlsx',
    "CHIMERA_TECHNIQUES": "SourceTables/ChimeraTechniques.xlsx",
    "CHIMERAS": "SourceTables/Chimeras.xlsx",
    "CHIMERA_EGGS": "SourceTables/ChimeraEggs.xlsx",
    "CHIMERA_ITEMS": "SourceTables/ChimeraItems.xlsx",
    "FOR_CHIMERAS": "SourceTables/ForChimeras.xlsx",
    "EIDOLONS": "SourceTables/Eidolons.xlsx",
    "EIDOLON_ITEMS": "SourceTables/EidolonItems.xlsx",
    "EIDOLON_DIARYS": "SourceTables/EidolonSkills.xlsx",
    "EIDOLON_PILLS": "SourceTables/EidolonPills.xlsx",
    "CODEXES": "SourceTables/Codexes.xlsx",
    "CODEX_ITEMS": "SourceTables/CodexItems.xlsx",
    "FOLIOS": "SourceTables/Folios.xlsx",
    "TALISMANS": "SourceTables/Talismans.xlsx",
    "TALISMAN_PARTS": "SourceTables/TalismanParts.xlsx",
    "TABLETS": "SourceTables/Tablets.xlsx",
    "TABLET_ITEMS": "SourceTables/TabletItems.xlsx",
    "JASPERS": "SourceTables/Jaspers.xlsx",
}

COLUMNS = {
    "BESTIARY": [3, 4, 5],
    "BESTIARY_SETS": [1, 2, 3],
    "GLYPHS": [2, 3, 4, 5],
    "BESTIARY_PARTS": [2, 3],
    "BESTIARY_SHINES": [2, 3],
    "CHIMERA_TECHNIQUES": [2, 3, 4],
    "CHIMERAS": [2, 4, 3, 5],
    "CHIMERA_EGGS": [2, 3],
    "CHIMERA_ITEMS": [2, 4],
    "FOR_CHIMERAS": [2, 3],
    "EIDOLONS": [3, 7, 4, 5],
    "EIDOLON_ITEMS": [2, 4, 3],
    "EIDOLON_DIARYS": [2, 4, 3],
    "EIDOLON_PILLS": [2, 4, 3],
    "CODEXES": [2, 5, 3, 4, 6, 7, 8],
    "CODEX_ITEMS": [2, 4, 3],
    "FOLIOS": [2, 5, 3, 4, 6],  
    "TALISMANS": [3, 7, 4, 5, 6, 8], # name, desc, parts_needed, activate_silver_cost, jasper_slot, source 
    "TALISMAN_PARTS": [2, 4, 3], 
    "TABLETS": [3, 2, 4, 5, 6, 7 , 8, 9, 10],
    "TABLET_ITEMS": [3, 5, 4],
    "JASPERS": [3, 5, 4, 6], 
}
