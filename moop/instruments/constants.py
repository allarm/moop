# Piano constants

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
