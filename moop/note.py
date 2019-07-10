import re
import constants as Constants

# TODO: add calculation of a pitch of the note
# https://en.wikipedia.org/wiki/Scientific_pitch_notation
# TODO: replace asserts with exceptions
# (asserts can be turned off with __debug__==false)


class Note(object):
    """Class Note

    Note characteristics:
        - Note name / octave tuple
    """

    def __init__(self, note=0):
        """__init__ method:

        Args:
        Note name in {0: 'C', 1: 'CD', 2: 'D', 3: 'DE', 4: 'E', 5: 'F',
        6: 'FG', 7: 'G', 8: 'GA', 9: 'A', 10: 'AB', 11: 'B'}
       """

        self.note = note

    @property
    def note(self):
        """A note getter, returns the note number"""
        return self._note_number

    @property
    def is_black_key(self):
        """Returns true if note is a black key"""
        return (Constants.NOTES_DIC[self._note_number % 12]
                in Constants.BLACK_KEYS)

    @property
    def is_white_key(self):
        """Returns true if note is a white key"""
        return not self.is_black_key(self)

    @property
    def note_octave(self):
        """Returns the octave of the note"""
        return self._note_number // 12

    @property
    def note_name(self):
        """Returns the name of the note"""
        return Constants.NOTES_DIC[self._note_number % 12]

    @property
    def note_base_name(self):
        """Returns base name <note_name><note_octave>"""
        return self.note_name + str(self.note_octave)

    @property
    def octave_name(self):
        """Returns ocatve name"""
        return Constants.OCTAVES_DIC[self.note_octave]

    @property
    def note_sci_name(self):
        """Returns scientific name of the note:
           A4 A440
           G♯4/A♭4
        """
        if self.is_black_key:
            return "{note_1}#{octave}/{note_2}♭{octave}".format(
                note_1=Constants.NOTES_DIC[self._note_number % 12][0],
                note_2=Constants.NOTES_DIC[self._note_number % 12][1],
                octave=self.note_octave)

        return "{}{}".format(
            Constants.NOTES_DIC[self._note_number % 12],
            self.note_octave)
    # Constants.NOTES_SPECIAL_NAMES[self._note_number]
    # if self._note_number in Constants.NOTES_SPECIAL_NAMES else "")

    @note.setter
    def note(self, value):
        """Note setter

        Args: expect one of the following:
            note_tuple (tuple): ("Note str", octave)
            int: note_number
            str: note_basic_notation A0, A-1, A1
        """

        assert isinstance(value, (str, tuple, int)), "Str, tuple or int expected, not a {}!".format(type(value))

        if isinstance(value, str):    # string
            self._note_number = self._str_note_to_number(value)
            assert (self._note_number is not None), "{} is not a valid note".format(value)

        elif isinstance(value, tuple):    # tuple. accept tuples like ("A1","2") - converts it in A12 - probably fix later
            self._note_number = self._str_note_to_number(str(str(value[0])+str(value[1])))
            assert (self._note_number is not None), "{} is not a valid note tuple".format(value)

        else:    # integer
            self._note_number = value

    def _str_note_to_number(self, value):
        """returns a number of the note
           returns None if it is not a note

           note formats:
           <name><octave> where
               name in ['C', 'CD', 'D', 'DE', 'E', 'F', 'FG',
                        'G', 'GA', 'A', 'AB', 'B']
               octave is int, can be negative
           examples: A1, A-1, AB1, AB-1, CD-10, DE100
        """
        regex = (r'^(' +
                 ''.join([x+'|' if not x == Constants.NOTES[-1]
                          else x for x in Constants.NOTES]) +
                 ')(\-*)(\d+)$')
        # '^(C|CD|D|DE|E|F|FG|G|GA|A|AB|B)(\-*)(\d+)$'

        res = re.search(regex, value)
        # print("regex: {}, value: {}".format(regex,value))
        if not res:
            return None    # does not seem like a note

        if not res.group(2):    # positive note
            return (Constants.NOTES_NUM_DIC[res.group(1)] +
                    (12 * int(res.group(3))))
        else:    # negative note
            return (Constants.NOTES_NUM_DIC[res.group(1)]
                    - (12 * int(res.group(3))))

    def __add__(self, other):
        print(type(other))
        if isinstance(other, Note):
            return Note(self._note_number + other._note_number)
        elif isinstance(other, int):
            return Note(self._note_number + other)
        else:
            raise ValueError('{} is instance of {}, not {} or Note'
                             .format(other, type(other), type(1)))

    def __sub__(self, other):
        return Note(self._note_number - other._note_number)

    def __mul__(self, value):
        return self._note_number * value

    def __div__(self, value):
        return self._note_number // value

    def __gt__(self, other):
        return self._note_number > other._note_number

    def __ge__(self, other):
        return self._note_number >= other._note_number

    def __lt__(self, other):
        return self._note_number < other._note_number

    def __le__(self, other):
        return self._note_number <= other._note_number

    def __eq__(self, other):
        return self._note_number == other._note_number

    def __repr__(self):
        return "{}".format(self._note_number)
