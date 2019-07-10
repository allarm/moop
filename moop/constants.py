"""Misc constants"""

from math import ceil as ceil

K_RANGE = (1, 88)

OCTAVES_NUM = ceil(K_RANGE[1]/12)

HEARING_RANGE = (20, 20000)    # 20 Hz to 20 kHz

NOTES = "C CD D DE E F FG G GA A AB B".split()
BLACK_KEYS = "CD DE FG GA AB".split()

NOTES_DIC = dict(zip(range(0, 12), NOTES))
# NOTES_DIC : {0: 'C', 1: 'CD', 2: 'D', 3: 'DE',
# 4: 'E', 5: 'F', 6: 'FG', 7: 'G', 8: 'GA', 9: 'A', 10: 'AB', 11: 'B'}

NOTES_NUM_DIC = dict(zip(NOTES, range(0, 12)))
# NOTES_NUM_DIC : {'C': 0, 'CD': 1, 'D': 2, 'DE': 3,
# 'E': 4, 'F': 5, 'FG': 6, 'G': 7, 'GA': 8, 'A': 9, 'AB': 10, 'B': 11}

KEYS_DIC = {x: NOTES_DIC[(x-4) % 12]
            for x in range(K_RANGE[0], K_RANGE[1]+1)}
# KEYS_DIC : {1: 'A', 2: 'AB', 3: 'B' ... 87: 'B', 88: 'C'}

NOTES_SPECIAL_NAMES = {
    4:  'Pedal C',
    16: 'Deep C',
    40: 'Middle C',
    49: 'A440',
    52: 'Tenor C',
    64: 'Soprano C (High C)',
    76: 'Double high C',
    88: 'Eighth octave'
}

OCTAVES_NAMES = [
    'octocontra',
    'subsubcontra',
    'subcontra',
    'contra',
    'great',
    'small',
    'one-lined',
    'two-lined',
    'three-lined',
    'four-lined',
    'five-lined',
    'six-lined',
    'seven-lined'
]
OCTAVES_DIC = dict(zip(range(0, len(OCTAVES_NAMES)), OCTAVES_NAMES))
# OCTAVES_DIC : {0: 'octocontra', 1: 'subsubcontra' ... 12: 'seven-lined'}
