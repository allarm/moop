import re


class Constants(object):
    # Physical constants
    HEARING_RANGE = (20, 20000)  # 20 Hz to 20 kHz

    # Notes
    # https://en.wikipedia.org/wiki/Musical_note
    # Main constant
    # Piano range 21-108 (88 keys from A0 to C8)

    # Everything is tied to MIDI note number. It's fundamental.

    MIDI_NOTE_RANGE = range(0, 128)

    NOTES = "C CD D DE E F FG G GA A AB B".split()
    BLACK_KEYS = "CD DE FG GA AB".split()

    NOTES_DIC = dict(zip(range(1, 13), NOTES))
    # {1: 'C',  2: 'CD', 3: 'D',   4: 'DE',
    #  5: 'E',  6: 'F',  7: 'FG',  8: 'G',
    #  9: 'GA', 10: 'A', 11: 'AB', 12: 'B'}

    NOTES_NUM_DIC = dict(zip(NOTES, range(1, 13)))
    # {'C': 1,  'CD': 2, 'D': 3,   'DE': 4,
    #  'E': 5,  'F': 6,  'FG': 7,  'G': 8,
    #  'GA': 9, 'A': 10, 'AB': 11, 'B': 12}

    # Octaves

    # https://en.wikipedia.org/wiki/Octave
    # 11 octaves
    # Using scientific notation (-1...11)
    # MIDI notation is (-5...5)

    OCTAVES_RANGE = range(-1, 12)

    OCTAVES_DIC = {
        -1: 'Dbl Contra',
        0:  'Sub Contra',
        1:  'Contra',
        2:  'Great',
        3:  'Small',
        4:  '1 Line',
        5:  '2 Line',
        6:  '3 Line',
        7:  '4 Line',
        8:  '5 Line',
        9:  '6 Line',
        10: '7 Line',
        11: ''
        }


class Note(object):
    """Class Note """

    # def __init__(self, *args, **kwargs):
    def __init__(self, value=None):
        """__init__ method:

        Args:
        Note name in {0: 'C', 1: 'CD', 2: 'D', 3: 'DE', 4: 'E', 5: 'F',
        6: 'FG', 7: 'G', 8: 'GA', 9: 'A', 10: 'AB', 11: 'B'}
       """
        # print(args, kwargs)
        # self._midi_note_number = value
        self.note = value

    @property
    def note(self):
        """A note getter, returns the note number"""
        return self._midi_note_number

    @property
    def is_black_key(self):
        """Returns true if note is a black key"""
        return (Constants.NOTES_DIC[self._midi_note_number % 12 + 1]
                in Constants.BLACK_KEYS)

    @property
    def is_white_key(self):
        """Returns true if note is a white key"""
        # return not self.is_black_key(self)
        return not (Constants.NOTES_DIC[self._midi_note_number % 12 + 1]
                    in Constants.BLACK_KEYS)

    @property
    def note_sci_octave(self):
        """Returns the octave of the note"""
        return self._midi_note_number // 12 - 1

    @property
    def note_midi_octave(self):
        """Returns the MIDI octave of the note"""
        return self._midi_note_number // 12 - 5

    @property
    def note_name(self):
        """Returns the name of the note"""
        return Constants.NOTES_DIC[self._midi_note_number % 12 + 1]

    @property
    def note_base_name(self):
        """Returns base name <note_name><note_octave>"""
        return self.note_name + str(self.note_sci_octave)

    @property
    def octave_name(self):
        """Returns ocatve name"""
        return Constants.OCTAVES_DIC[self.note_sci_octave]

    @property
    def note_sci_name(self):
        """Returns scientific name of the note:
           A4 
           G♯4/A♭4
        """
        if self.is_black_key:
            return "{note_1}#{octave}/{note_2}♭{octave}".format(
                    note_1=Constants.NOTES_DIC[self._midi_note_number % 12 + 1][0],
                    note_2=Constants.NOTES_DIC[self._midi_note_number % 12 + 1][1],
                    octave=self.note_sci_octave)

        return "{}{}".format(
                Constants.NOTES_DIC[self._midi_note_number % 12 + 1],
                self.note_sci_octave)

    @note.setter
    def note(self, value):
        """Note setter

        Args: expect one of the following:
            note_tuple (tuple): ("Note str", octave)
            int: MIDI note number
            str: scientific notation: A0, A-1, A1

        TODO: add Helmholtz notation
        """

        if not isinstance(value, (self.__class__, str, tuple, int, type(None))):
            raise ValueError(
                    'Wrong type {}'.format(type(value)))

        if isinstance(value, str):  # string
            # print("{}: {}".format(value, self._str_note_to_number(value)))
            self._midi_note_number = self._str_note_to_number(value)
            if self._midi_note_number is None:
                raise ValueError(
                        '{} is not a valid note.'.format(value))

        # tuple. expect ("A", 1) - (note, octave)
        elif isinstance(value, tuple):
            if not isinstance(value[1], int):
                # Expected the octave number in integer
                raise ValueError(
                        'Expected int got {}'.format(type(value[1])))
            self._midi_note_number = self._str_note_to_number(
                    ''.join(map(str, value))
                    )
        else:  # integer or None
            self._midi_note_number = value

    @note.getter
    def note(self):
        return self._midi_note_number

    def _str_note_to_number(self, value):
        """returns a MIDI number of the note
           returns None if it is not a note

           Input: value - str, note in a scientific format

           note formats:
           <name><octave> where
               name in ['C', 'CD', 'D', 'DE', 'E', 'F', 'FG',
                        'G', 'GA', 'A', 'AB', 'B']
               octave is int, can be negative
           examples: A1, A-1, AB1, AB-1, CD-4, DE3
        """
        value = value.upper()

        regex = (r'^(' +
                 ''.join([x + '|' if not x == Constants.NOTES[-1]
                          else x for x in Constants.NOTES]) +
                 ')(\-*)(\d+)$')
        # '^(C|CD|D|DE|E|F|FG|G|GA|A|AB|B)(\-*)(\d+)$'

        res = re.search(regex, value)
        # print("regex: {}, value: {}".format(regex,value))
        if not res:
            raise ValueError('Wrong note: {}'.format(value))

        # A-1 -> A
        _input_note = res.group(1)

        # A-1 -> -1
        _input_octave = int(res.group(2) + res.group(3))

        # return the MIDI number
        return (12 * (_input_octave + 1) +
                Constants.NOTES_NUM_DIC[_input_note] - 1)

    def __add__(self, other):
        """
        Addition

        :param other: Note or int
        :return: Note

        DONE: add range check
        """
        if isinstance(other, self.__class__):
            # both arguments are Note
            result = Note(self.note + other.note)
        elif isinstance(other, int):
            result = Note(self.note + other)
        else:
            raise ValueError('{} is instance of {}, not {} or Note'
                             .format(other, type(other), type(1)))
        if result.note in Constants.MIDI_NOTE_RANGE:
            return result
        else:
            raise ValueError('Result {} out of range {}.'
                             .format(result.note, Constants.MIDI_NOTE_RANGE))

    def __sub__(self, other):
        """
        Subtraction

        :param other: Note or int
        :return: Note
        """
        if isinstance(other, self.__class__):
            # both arguments are Note
            result = Note(self.note - other.note)
        elif isinstance(other, int):
            result = Note(self.note - other)
        else:
            raise ValueError('{} is instance of {}, not {} or Note'
                             .format(other, type(other), type(1)))
        if result.note in Constants.MIDI_NOTE_RANGE:
            return result
        else:
            raise ValueError('Result {} out of range {}.'
                             .format(result.note, Constants.MIDI_NOTE_RANGE))

    def __mul__(self, other):
        """
        Multiplication

        :param other: Note or int
        :return: Note
        """

        if isinstance(other, self.__class__):
            # both arguments are Note
            result = Note(self.note * other.note)
        elif isinstance(other, int):
            result = Note(self.note * other)
        else:
            raise ValueError('{} is instance of {}, not {} or Note'
                             .format(other, type(other), type(1)))
        if result.note in Constants.MIDI_NOTE_RANGE:
            return result
        else:
            raise ValueError('Result {} out of range {}.'
                             .format(result.note, Constants.MIDI_NOTE_RANGE))

    def __truediv__(self, other):
        """
        Division

        :param other: Note or int
        :return: Note
        """

        if isinstance(other, self.__class__):
            # both arguments are Note
            result = Note(self.note // other.note)
        elif isinstance(other, int):
            result = Note(self.note // other)
        else:
            raise ValueError('{} is instance of {}, not {} or Note'
                             .format(other, type(other), type(1)))
        if result.note in Constants.MIDI_NOTE_RANGE:
            return result
        else:
            raise ValueError('Result {} out of range {}.'
                             .format(result.note, Constants.MIDI_NOTE_RANGE))

    def __gt__(self, other):
        """
        Greater than

        :param other: Note or int
        :return: boolean
        """
        if isinstance(other, self.__class__):
            # both arguments are Note
            return self.note > other.note
        elif isinstance(other, int):
            return self.note > other
        else:
            raise ValueError('{} is instance of {}, not {} or Note'
                             .format(other, type(other), type(1)))

    def __ge__(self, other):
        """
        Greater or equal

        :param other: Note or int
        :return: boolean
        """

        if isinstance(other, self.__class__):
            # both arguments are Note
            return self.note >= other.note
        elif isinstance(other, int):
            return self.note >= other
        else:
            raise ValueError('{} is instance of {}, not {} or Note'
                             .format(other, type(other), type(1)))

    def __lt__(self, other):
        """
        Less than

        :param other: Note or int
        :return: boolean
        """

        if isinstance(other, self.__class__):
            # both arguments are Note
            return self.note < other.note
        elif isinstance(other, int):
            return self.note < other
        else:
            raise ValueError('{} is instance of {}, not {} or Note'
                             .format(other, type(other), type(1)))

    def __le__(self, other):
        """
        Less or equal

        :param other: Note or int
        :return: boolean
        """

        if isinstance(other, self.__class__):
            # both arguments are Note
            return self.note <= other.note
        elif isinstance(other, int):
            return self.note <= other
        else:
            raise ValueError('{} is instance of {}, not {} or Note'
                             .format(other, type(other), type(1)))

    def __eq__(self, other):
        """
        Equal

        :param other: Note or int
        :return: boolean
        """
        if isinstance(other, self.__class__):
            # both arguments are Note
            return self.note == other.note
        elif isinstance(other, int):
            return self.note == other
        else:
            raise ValueError('{} is instance of {}, not {} or Note'
                             .format(other, type(other), type(1)))

    def __repr__(self):
        # return "{}".format(self._midi_note_number)
        return "{}: {} / {}"\
            .format(self.note, self.note_base_name, self.note_sci_name)
