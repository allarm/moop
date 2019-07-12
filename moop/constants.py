"""Misc constants"""

from math import ceil as ceil

# Physical contants
HEARING_RANGE = (20, 20000)    # 20 Hz to 20 kHz

# Notes
# https://en.wikipedia.org/wiki/Musical_note

NOTES = "C CD D DE E F FG G GA A AB B".split()
# I keep it as black keys as I am not sure about a better name
BLACK_KEYS = "CD DE FG GA AB".split()

NOTES_DIC = dict(zip(range(1, 13), NOTES))
# {1: 'C',
#  2: 'CD',
#  3: 'D',
#  4: 'DE',
#  5: 'E',
#  6: 'F',
#  7: 'FG',
#  8: 'G',
#  9: 'GA',
#  10: 'A',
#  11: 'AB',
#  12: 'B'}

NOTES_NUM_DIC = dict(zip(NOTES, range(1, 13)))
# {'C': 1,
#  'CD': 2,
#  'D': 3,
#  'DE': 4,
#  'E': 5,
#  'F': 6,
#  'FG': 7,
#  'G': 8,
#  'GA': 9,
#  'A': 10,
#  'AB': 11,
#  'B': 12}

# Octaves

# https://en.wikipedia.org/wiki/Octave
# 11 octaves



# Instruments
# Piano
# TODO: make separate classes for instruments

# Keys
K_RANGE = (1, 88)

OCTAVES_NUM = ceil(K_RANGE[1]/12)

# Does not work, fix later
# KEYS_DIC = {x: NOTES_DIC[(x-4) % 12]
#             for x in range(K_RANGE[0], K_RANGE[1]+1)}
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
