from enum import Enum


class Interval(Enum):
    Major = [0, 2, 2, 1, 2, 2, 2]
    Minor = [0, 2, 1, 2, 2, 1, 2]
    Ionian = [0, 2, 2, 1, 2, 2, 2]
    Dorian = [0, 2, 1, 2, 2, 2, 1]
    Phrygian = [0, 1, 2, 2, 2, 1, 2]
    Lydian = [0, 2, 2, 2, 1, 2, 2]
    Mixolydian = [0, 2, 2, 1, 2, 2, 1]
    Aeolian = [0, 2, 1, 2, 2, 1, 2]
    Locrian = [0, 1, 2, 2, 1, 2, 2]
    DiminishedWholeHalf = [0, 2, 1, 2, 1, 2, 1, 2]
    DiminishedHalfWhole = [0, 1, 2, 1, 2, 1, 2, 1]
    MajorPentatonic = [0, 2, 2, 2, 2]
    MinorPentatonic = [0, 3, 2, 2, 3]
    MajorBlues = [0, 2, 1, 1, 3, 2]
    MinorBlues = [0, 3, 2, 1, 1, 3]
    WholeTone = [0, 2, 2, 2, 2, 2]
    Chromatic = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


class ScaleGenerator:
    def __init__(self, scale_root, scale_type):
        self.scale_root = scale_root
        self.scale_type = scale_type

    def generate_scale(self):
        chromatic_scale = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

        two_octaves = chromatic_scale + chromatic_scale

        scale = []

        root_index = two_octaves.index(self.scale_root)
        index_offset = 0

        for i in self.scale_type.value:
            index_offset += i
            scale.append(two_octaves[index_offset + root_index])

        return scale


class Fret:
    def __init__(self, note, fretted):
        self.note = note
        self.fretted = fretted

    def __str__(self):
        return "X" if self.fretted else "."


class String:
    def __init__(self, base_fret, fretted_notes):

        self.base_fret = base_fret
        self.fretted_notes = fretted_notes
        self.frets = self.generate_frets()

    def generate_frets(self):
        chromatic_scale = ScaleGenerator(self.base_fret, Interval.Chromatic).generate_scale()

        return [Fret(f, f in self.fretted_notes) for f in chromatic_scale + chromatic_scale + chromatic_scale][0:25]

    def __str__(self):
        #   E  X   |   X   X   X   |   |   X   |   X   |   |   X   |   X   X   X   |   |   X   |   X   |   |   X
        #   B  X   |   X   |   |   X   |   X   X   X   |   |   X   |   X   |   |   X   |   X   X   X   |   |   X
        #   G  X   X   |   |   X   |   X   |   |   X   |   X   X   X   |   |   X   |   X   |   |   X   |   X   X
        #   D  |   |   X   |   X   X   X   |   |   X   |   X   |   |   X   |   X   X   X   |   |   X   |   X   |
        #   A  |   |   X   |   X   |   |   X   |   X   X   X   |   |   X   |   X   |   |   X   |   X   X   X   |
        #   E  X   |   X   X   X   |   |   X   |   X   |   |   X   |   X   X   X   |   |   X   |   X   |   |   X
        #      0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24

        string = f"{self.base_fret}  "

        for i, f in enumerate(self.frets):
            string += f"{str(f)}   "

        return string

    def __len__(self):
        return len(self.frets)


class Fretboard:
    def __init__(self, strings, scale_type, scale_root):
        self.fretted_notes = ScaleGenerator(scale_root, scale_type).generate_scale()
        self.strings = [String(s, self.fretted_notes) for s in strings]
        self.length = max([len(s) for s in self.strings])

    def __str__(self):
        strings = "\n".join([str(s) for s in self.strings]) + "\n"

        for i in range(0, self.length):
            space_delimter = '   '

            if i >= 11:
                space_delimter = '  '

            strings += f"{space_delimter}{str(i)}"

        return strings
