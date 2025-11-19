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
        counter = 1

        for i in self.scale_type.value:
            index_offset += i
            scale.append((two_octaves[index_offset + root_index], counter))
            counter += 1

        return scale


class Fret:
    def __init__(self, note, fretted, show_scale_degrees, scale_number=None):
        self.show_scale_degrees = show_scale_degrees
        self.note = note
        self.fretted = fretted
        self.scale_number = scale_number

    def __str__(self):
        if self.fretted:
            if self.show_scale_degrees:
                return str(self.scale_number)
            else:
                return "X"

        return "."


class String:
    def __init__(self, base_fret, fretted_notes, show_scale_degrees):

        self.base_fret = base_fret
        self.fretted_notes = fretted_notes
        self.show_scale_degrees = show_scale_degrees
        self.frets = self.generate_string_frets()

    def generate_string_frets(self):
        chromatic_scale = [f for f in ScaleGenerator(self.base_fret, Interval.Chromatic).generate_scale()]

        string_frets = chromatic_scale[0:12] + chromatic_scale[0:12] + [chromatic_scale[0]]

        frets = []

        for sf in string_frets:
            note = sf[0]
            is_fretted = sf[0] in [fn[0] for fn in self.fretted_notes]

            scale_number = 0

            if is_fretted:
                # find the matching fretted note
                fretted_note = [fn for fn in self.fretted_notes if fn[0] == sf[0]][0]
                scale_number = fretted_note[1]

            frets.append(Fret(note, is_fretted, self.show_scale_degrees, scale_number))

        return frets

    def __str__(self):
        #   E  X   |   X   X   X   |   |   X   |   X   |   |   X   |   X   X   X   |   |   X   |   X   |   |   X
        #   B  X   |   X   |   |   X   |   X   X   X   |   |   X   |   X   |   |   X   |   X   X   X   |   |   X
        #   G  X   X   |   |   X   |   X   |   |   X   |   X   X   X   |   |   X   |   X   |   |   X   |   X   X
        #   D  |   |   X   |   X   X   X   |   |   X   |   X   |   |   X   |   X   X   X   |   |   X   |   X   |
        #   A  |   |   X   |   X   |   |   X   |   X   X   X   |   |   X   |   X   |   |   X   |   X   X   X   |
        #   E  X   |   X   X   X   |   |   X   |   X   |   |   X   |   X   X   X   |   |   X   |   X   |   |   X
        #      0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24

        string = f"{self.base_fret}"

        if len(self.base_fret) == 1:
            string += '  '
        else:
            string += ' '

        for i, f in enumerate(self.frets):
            string += f"{str(f)}"

            if len(str(f)) == 1:
                string += '   '
            else:
                string += '  '

        return string

    def __len__(self):
        return len(self.frets)


class Fretboard:
    def __init__(self, strings, scale_type, scale_root, show_scale_degrees):
        self.show_scale_degrees = show_scale_degrees
        self.fretted_notes = ScaleGenerator(scale_root, scale_type).generate_scale()
        self.strings = [String(s, self.fretted_notes, show_scale_degrees) for s in strings]
        self.length = max([len(s) for s in self.strings])

    def __str__(self):
        strings = "\n".join([str(s) for s in self.strings]) + "\n"

        for i in range(0, self.length):
            space_delimter = '   '

            if i >= 11:
                space_delimter = '  '

            strings += f"{space_delimter}{str(i)}"

        return strings


f = Fretboard(
    strings=["E", "B", "G", "D", "A", "E"],
    scale_type=Interval.Major,
    scale_root="E",
    show_scale_degrees=True
)

print(f)