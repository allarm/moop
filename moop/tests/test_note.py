from unittest import TestCase
from moop.base import note as NoteClass


class TestNote(TestCase):
    note_1 = NoteClass.Note()
    note_1.note = 'a1'  # first octave A
    note_2 = NoteClass.Note('a2')  # second octave A
    note_3 = NoteClass.Note('CD1')  # 'C#1/D♭1'
    note_4 = NoteClass.Note('C1')
    note_5 = NoteClass.Note(0) # C-1

    all_notes = "C-1 CD-1 D-1 DE-1 E-1 F-1 FG-1 G-1 GA-1 A-1 AB-1 B-1 C0 CD0 D0 " \
                "DE0 E0 F0 FG0 G0 GA0 A0 AB0 B0 C1 CD1 D1 DE1 E1 F1 FG1 G1 GA1 " \
                "A1 AB1 B1 C2 CD2 D2 DE2 E2 F2 FG2 G2 GA2 A2 AB2 B2 C3 CD3 D3 " \
                "DE3 E3 F3 FG3 G3 GA3 A3 AB3 B3 C4 CD4 D4 DE4 E4 F4 FG4 G4 GA4 " \
                "A4 AB4 B4 C5 CD5 D5 DE5 E5 F5 FG5 G5 GA5 A5 AB5 B5 C6 CD6 D6 " \
                "DE6 E6 F6 FG6 G6 GA6 A6 AB6 B6 C7 CD7 D7 DE7 E7 F7 FG7 G7 GA7 " \
                "A7 AB7 B7 C8 CD8 D8 DE8 E8 F8 FG8 G8 GA8 A8 AB8 B8 C9 CD9 D9 " \
                "DE9 E9 F9 FG9 G9".split()

    notes = [NoteClass.Note(x) for x in range(0,128)]

    # def test_note(self):
    #     self.fail()

    def test_notes(self):
        for x, y in zip(self.all_notes, self.notes):
            self.assertEqual(x, y.note_base_name)

    def test_is_black_key(self):
        self.assertEqual(self.note_3.is_black_key, True)
        self.assertEqual(self.note_4.is_black_key, False)
        self.assertEqual(self.note_5.is_black_key, False)

    def test_is_white_key(self):
        self.assertEqual(self.note_1.is_white_key, True)
        self.assertEqual(self.note_4.is_white_key, True)
        self.assertEqual(self.note_3.is_white_key, False)

    def test_note_sci_octave(self):
        self.assertEqual(self.note_4.note_sci_octave, 1)
        self.assertEqual(self.note_5.note_sci_octave, -1)

    def test_note_midi_octave(self):
        self.assertEqual(self.note_4.note_midi_octave, -3)
        self.assertEqual(self.note_5.note_midi_octave, -5)

    def test_note_name(self):
        self.assertEqual(self.note_4.note_name, 'C')
        self.assertEqual(self.note_5.note_name, 'C')

    def test_note_base_name(self):
        self.assertEqual(self.note_4.note_base_name, 'C1')
        self.assertEqual(self.note_5.note_base_name, 'C-1')

    def test_octave_name(self):
        self.assertEqual(self.note_4.octave_name, 'Contra')
        self.assertEqual(self.note_5.octave_name, 'Dbl Contra')

    def test_note_sci_name(self):
        self.assertEqual(self.note_3.note_sci_name, 'C#1/D♭1')
        self.assertEqual(self.note_5.note_sci_name, 'C-1')

    def test___add__(self):
        self.assertEqual((self.note_4+1).note, 25)

        raised_exc = None

        try:
            self.note_5 + 130
        except ValueError as e:
            raised_exc = e
        if not raised_exc:
            self.fail("{} was not raised".format(ValueError))

    def test___sub__(self):
        self.assertEqual((self.note_4-1).note, 23)

        raised_exc = None

        try:
            self.note_5 - 1
        except ValueError as e:
            raised_exc = e
        if not raised_exc:
            self.fail("{} was not raised".format(ValueError))

    # def test__str_note_to_number(self):
    #     self.fail()
