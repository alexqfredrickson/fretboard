# fretboard

It's a guitar fretboard!

## usage

``` python
f = Fretboard(
    strings=["D#", "A#", "G", "C#", "G#", "D#"],
    scale_type=Interval.Mixolydian,
    scale_root="D#"
)

print(f)
```

```
D# X   .   X   .   X   X   .   X   .   X   X   .   X   .   X   .   X   X   .   X   .   X   X   .   X   
A# X   .   X   X   .   X   .   X   .   X   X   .   X   .   X   X   .   X   .   X   .   X   X   .   X   
G  X   X   .   X   .   X   X   .   X   .   X   .   X   X   .   X   .   X   X   .   X   .   X   .   X   
C# X   .   X   .   X   .   X   X   .   X   .   X   X   .   X   .   X   .   X   X   .   X   .   X   X   
G# X   .   X   .   X   X   .   X   .   X   .   X   X   .   X   .   X   X   .   X   .   X   .   X   X   
D# X   .   X   .   X   X   .   X   .   X   X   .   X   .   X   .   X   X   .   X   .   X   X   .   X   
   0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24
```