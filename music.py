def scale_test():
    import random
    global scales
    scales = {"C Major": ["C", "D", "E", "F", "G", "A", "B"],
              "D Major": ["D", "E", "F#", "G", "A", "B", "C#",],
              "E Major": ["E", "F#", "G#", "A", "B", "C#", "D#"],
              "F Major": ["F", "G", "A", "Bb", "C", "D", "E"],
              "G Major": ["G", "A", "B", "C", "D", "E", "F#"],
              "A Major": ["A", "B", "C#", "D", "E", "F#", "G#"],
              "B Major": ["B", "C#", "D#", "E", "F#", "G#", "A#"],
              "Db Major": ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"],
              "Eb Major": ["Eb", "F", "G", "Ab", "Bb", "C", "D"],
              "F# Major": ["F#", "G#", "A#", "B", "C#", "D#", "E#"],
              "Gb Major": ["Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F"],
              "Ab Major": ["Ab", "Bb", "C", "Db", "Eb", "F", "G"],
              "Bb Major": ["Bb", "C", "D", "Eb", "F", "G", "A"], 
              "Cb Major": ["Cb", "Db", "Eb", "Fb", "Gb", "Ab", "Bb"],
              "C# Major": ["C#", "D#", "E#", "F#", "G#", "A#", "B#"],
              "A natural minor": ["A", "B", "C", "D", "E", "F", "G"],
              "B natural minor": ["B", "C#", "D", "E", "F#", "G", "A"],
              "C natural minor": ["C", "D", "Eb", "F", "G", "Ab", "Bb"],
              "D natural minor": ["D", "E", "F", "G", "A", "Bb", "C"],
              "E natural minor": ["E", "F#", "G", "A", "B", "C", "D"],
              "F natural minor": ["F", "G", "Ab", "Bb", "C", "Db", "Eb"],
              "G natural minor": ["G", "A", "Bb", "C", "D", "Eb", "F"],
              "A natural minor": ["A", "B", "C", "D", "E", "F", "G"],
              "B natural minor": ["B", "C#", "D", "E", "F#", "G", "A"], 
              "Bb natural minor": ["Bb", "C", "Db", "Eb", "F", "Gb", "Ab"],
              "C# natural minor": ["C#", "D#", "E", "F#", "G#", "A", "B"],
              "D# natural minor": ["D#", "E#", "F#", "G#", "A#", "B", "C#"],
              "Eb natural minor": ["Eb", "F", "Gb", "Ab", "Bb", "Cb", "Db"],
              "F# natural minor": ["F#", "G#", "A", "B", "C#", "D", "E",], 
              "G# natural minor": ["G#", "A#", "B", "C#", "D#", "E", "F#"],
              "Ab natural minor": ["Ab", "Bb", "Cb", "Db", "Eb", "Fb", "Gb",],
              "A# natural minor": ["A#", "B#", "C#", "D#", "E#", "F#", "G#"],
              "C harmonic minor": ["C", "D", "Eb", "F", "G", "Ab", "B"],
                "D harmonic minor": ["D", "E", "F", "G", "A", "Bb", "C#"],
                "E harmonic minor": ["E", "F#", "G", "A", "B", "C", "D#"],
                "F harmonic minor": ["F", "G", "Ab", "Bb", "C", "Db", "E"],
                "G harmonic minor": ["G", "A", "Bb", "C", "D", "Eb", "F#"],
                "A harmonic minor": ["A", "B", "C", "D", "E", "F", "G#"],
                "B harmonic minor": ["B", "C#", "D", "E", "F#", "G", "A#"],
                "C# harmonic minor": ["C#", "D#", "E", "F#", "G#", "A", "B#"],
                "D# harmonic minor": ["D#", "E#", "F#", "G#", "A#", "B", "C#"],
                "Eb harmonic minor": ["Eb", "F", "Gb", "Ab", "Bb", "Cb", "Db", "E"],
                "F# harmonic minor": ["F#", "G#", "A", "B", "C#", "D", "E#"],
                "G# harmonic minor": ["G#", "A#", "B", "C#", "D#", "E", "F#"],
                "Ab harmonic minor": ["Ab", "Bb", "Cb", "Db", "Eb", "Fb", "Gb"],
                "A# harmonic minor": ["A#", "B#", "C#", "D#", "E#", "F#", "G#"],

              }
    while True: 
        scale = random.choice(list(scales.keys()))
        notes = scales[scale]
        answer = input(f"What are the notes in the {scale} scale? ")
        if answer.strip().split(",") == notes:
            print("Correct!")
        else:
            print(f"Incorrect. The notes in the {scale} scale are: {', '.join(notes)}")
        continue_test = input("Do you want to try another scale? (yes/no) ")
        if continue_test.strip().lower() != "yes":
            break
        
def interval_test():
    import random
    intervals = {
        "Unison": [["C", "C"], ["C#", "C#"], ["D", "D"], ["Eb", "Eb"], ["E", "E"], ["F", "F"], ["F#", "F#"], ["G", "G"], ["Ab", "Ab"], ["A", "A"], ["Bb", "Bb"], ["B", "B"]],
        "Minor Second": [["C", "C#"], ["C#", "D"], ["D", "Eb"], ["Eb", "E"], ["E", "F"], ["F", "Gb"], ["F#", "G"], ["G", "Ab"], ["Ab", "A"], ["A", "Bb"], ["Bb", "B"], ["B", "C"]],
        "Major Second": [["C", "D"], ["C#", "D#"], ["D", "E"], ["Eb", "F"], ["E", "F#"], ["F", "G"], ["F#", "G#"], ["G", "A"], ["Ab", "Bb"], ["A", "B"], ["Bb", "C"], ["B", "C#"]],
        "Minor Third": [["C", "Eb"], ["C#", "E"], ["D", "F"], ["Eb", "Gb"], ["E", "G"], ["F", "Ab"], ["F#", "A"], ["G", "Bb"], ["Ab", "B"], ["A", "C"], ["Bb", "Db"], ["B", "D"]],
        "Major Third": [["C", "E"], ["C#", "E#"], ["D", "F#"], ["Eb", "G"], ["E", "G#"], ["F", "A"], ["F#", "A#"], ["G", "B"], ["Ab", "C"], ["A", "C#"], ["Bb", "D"], ["B", "D#"]],
        "Perfect Fourth": [["C", "F"], ["C#", "F#"], ["D", "G"], ["Eb", "Ab"], ["E", "A"], ["F", "Bb"], ["F#", "B"], ["G", "C"], ["Ab", "Db"], ["A", "D"], ["Bb", "Eb"], ["B", "E"]],
        "Tritone": [["C", "F#"], ["C#", "G"], ["D", "G#"], ["Eb", "A"], ["E", "Bb"], ["F", "B"], ["F#", "C"], ["G", "Db"], ["Ab", "D"], ["A", "Eb"], ["Bb", "E"], ["B", "F"]],
        "Perfect Fifth": [["C", "G"], ["C#", "G#"], ["D", "A"], ["Eb", "Bb"], ["E", "B"], ["F", "C"], ["F#", "C#"], ["G", "D"], ["Ab", "Eb"], ["A", "E"], ["Bb", "F"], ["B", "F#"]],
        "Minor Sixth": [["C", "Ab"], ["C#", "A"], ["D", "Bb"], ["Eb", "B"], ["E", "C"], ["F", "Db"], ["F#", "D"], ["G", "Eb"], ["Ab", "F"], ["A", "Gb"], ["Bb", "G"], ["B", "A"]],
        "Major Sixth": [["C", "A"], ["C#", "A#"], ["D", "B"], ["Eb", "C"], ["E", "C#"], ["F", "D"], ["F#", "D#"], ["G", "E"], ["Ab", "F"], ["A", "F#"], ["Bb", "G"], ["B", "G#"]],
        "Minor Seventh": [["C", "Bb"], ["C#", "B"], ["D", "C"], ["Eb", "Db"], ["E", "D"], ["F", "Eb"], ["F#", "E"], ["G", "F"], ["Ab", "Gb"], ["A", "G"], ["Bb", "Ab"], ["B", "A"]],
        "Major Seventh": [["C", "B"], ["C#", "B#"], ["D", "C#"], ["Eb", "D"], ["E", "F"], ["F", "E#"], ["F#", "G"], ["G", "F#"], ["Ab", "G#"], ["A", "B"], ["Bb", "A#"], ["B", "C#"]],
    }
    while True:
        interval = random.choice(list(intervals.keys()))
        note_pair = random.choice(intervals[interval])
        answer = input(f"What is the interval between {note_pair[0]} and {note_pair[1]}? ")
        if answer.strip().lower() == interval.lower():
            print("Correct!")
        else:
            (f"Incorrect. The interval between {note_pair[0]} and {note_pair[1]} is a {interval}.")
        continue_test = input("Do you want to try another interval? (yes/no) ")
        if continue_test.strip().lower() != "yes":
            break

def scale_degrees():
    import random
    scale = random.choice(list(scales.keys()))
    notes = scales[scale]
    degrees = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th"]
    note_degrees = {note: degree for note, degree in zip(notes, degrees)}
    while True:
        note = random.choice(notes)
        answer = input(f"What is the degree of the note {note} in the {scale} scale? ")
        if answer.strip().lower() == note_degrees[note].lower():
            print("Correct!")
        else:
            print(f"Incorrect. The {note} is the {note_degrees[note]}.")
        continue_test = input("Do you want to try another note? (yes/no) ")
        if continue_test.strip().lower() != "yes":
            break

def chord_recognition():
    chords = {
        "C Major": ["C", "E", "G"],
        "D Major": ["D", "F#", "A"],
        "E Major": ["E", "G#", "B"],
        "F Major": ["F", "A", "C"],
        "G Major": ["G", "B", "D"],
        "A Major": ["A", "C#", "E"],
        "B Major": ["B", "D#", "F#"],
        "Db Major": ["Db", "F", "Ab"], 
        "Eb Major": ["Eb", "G", "Bb"],
        "F# Major": ["F#", "A#", "C#"],
        "Gb Major": ["Gb", "Bb", "Db"],
        "Ab Major": ["Ab", "C", "Eb"],
        "Bb Major": ["Bb", "D", "F"],
        "C Minor": ["C", "Eb", "G"],
        "D Minor": ["D", "F", "A"],
        "E Minor": ["E", "G", "B"],
        "F Minor": ["F", "Ab", "C"],
        "G Minor": ["G", "Bb", "D"],
        "A Minor": ["A", "C", "E"],
        "B Minor": ["B", "D", "F#"],
        "C# Minor": ["C#", "E", "G#"],
        "D# Minor": ["D#", "F#", "A#"],
        "Eb Minor": ["Eb", "Gb", "Bb"],
        "F# Minor": ["F#", "A", "C#"],
        "G# Minor": ["G#", "B", "D#"],
        "Bb Minor": ["Bb", "Db", "F"],
        "C7": ["C", "E", "G", "Bb"],
        "D7": ["D", "F#", "A", "C"],
        "E7": ["E", "G#", "B", "D"],
        "F7": ["F", "A", "C", "Eb"],
        "G7": ["G", "B", "D", "F"],
        "A7": ["A", "C#", "E", "G"],
        "B7": ["B", "D#", "F#", "A"],
        "Db7": ["Db", "F", "Ab", "Cb"], 
        "Eb7": ["Eb", "Gb", "Bb", "Db"], 
        "F#7": ["F#", "A#", "C#", "E"], 
        "Gb7": ["Gb", "Bb", "Db", "Fb"],
        "Ab7": ["Ab", "C", "Eb", "Gb"], 
        "Bb7": ["Bb", "D", "F", "Ab"], 
        "C Major 7": ["C", "E", "G", "B"],
        "D Major 7": ["D", "F#", "A", "C#"],
        "E Major 7": ["E", "G#", "B", "D#"],
        "F Major 7": ["F", "A", "C", "E"],
        "G Major 7": ["G", "B", "D", "F#"],
        "A Major 7": ["A", "C#", "E", "G#"],
        "B Major 7": ["B", "D#", "F#", "A#"],
        "Db Major 7": ["Db", "F", "Ab", "C"], 
        "Eb Major 7": ["Eb", "G", "Bb", "D"], 
        "F# Major 7": ["F#", "A#", "C#", "E#"],
        "Gb Major 7": ["Gb", "Bb", "Db", "F"],
        "Ab Major 7": ["Ab", "C", "Eb", "G"], 
        "Bb Major 7": ["Bb", "D", "F", "A"],
        "C Minor 7": ["C", "Eb", "G", "Bb"],
        "D Minor 7": ["D", "F", "A", "C"],
        "E Minor 7": ["E", "G", "B", "D"],
        "F Minor 7": ["F", "Ab", "C", "Eb"],
        "G Minor 7": ["G", "Bb", "D", "F"],
        "A Minor 7": ["A", "C", "E", "G"],
        "B Minor 7": ["B", "D", "F#", "A"],
        "C# Minor 7": ["C#", "E", "G#", "B"],
        "D# Minor 7": ["D#", "F#", "A#", "C#"], 
        "Eb Minor 7": ["Eb", "Gb", "Bb", "Db"], 
        "F# Minor 7": ["F#", "A", "C#", "E"],
        "G# Minor 7": ["G#", "B", "D#", "F#"], 
        "Bb Minor 7": ["Bb", "Db", "F", "Ab"],
        "C Diminished Triad": ["C", "Eb", "Gb"],
        "D Diminished Triad": ["D", "F", "Ab"],
        "E Diminished Triad": ["E", "G", "Bb"],
        "F Diminished Triad": ["F", "Ab", "B"],
        "G Diminished Triad": ["G", "Bb", "Db"],
        "A Diminished Triad": ["A", "C", "Eb"],
        "B Diminished Triad": ["B", "D", "F"],
        "C# Diminished Triad": ["C#", "E", "G"], 
        "D# Diminished Triad": ["D#", "F#", "A"],
        "Eb Diminished Triad": ["Eb", "Gb", "Bbb"],
        "F# Diminished Triad": ["F#", "A", "C"],
        "G# Diminished Triad": ["G#", "B", "D"],
        "Bb Diminished Triad": ["Bb", "Db", "Fb"], 
        "C Augmented": ["C", "E", "G#"],
        "D Augmented": ["D", "F#", "A#"],
        "E Augmented": ["E", "G#", "B#"],
        "F Augmented": ["F", "A", "C#"],
        "G Augmented": ["G", "B", "D#"],
        "A Augmented": ["A", "C#", "E#"],
        "B Augmented": ["B", "D#", "F##"],
        "Db Augmented": ["Db", "F", "A"],
        "Eb Augmented": ["Eb", "G", "B"],
        "F# Augmented": ["F#", "A#", "C##"],
        "Gb Augmented": ["Gb", "Bb", "D"],
        "Ab Augmented": ["Ab", "C", "E"],
        "Bb Augmented": ["Bb", "D", "F#"],
        "C Minor-Major": ["C", "Eb", "G", "B"],
        "D Minor-Major": ["D", "F", "A", "C#"],
        "E Minor-Major": ["E", "G", "B", "D#"],
        "F Minor-Major": ["F", "Ab", "C", "E"],
        "G Minor-Major": ["G", "Bb", "D", "F#"],
        "A Minor-Major": ["A", "C", "E", "G#"],
        "B Minor-Major": ["B", "D", "F#", "A#"],
        "C# Minor-Major": ["C#", "E", "G#", "B#"],
        "D# Minor-Major": ["D#", "F#", "A#", "C#"],
        "Eb Minor-Major": ["Eb", "Gb", "Bb", "Db"],
        "F# Minor-Major": ["F#", "A", "C#", "E#"],
        "G# Minor-Major": ["G#", "B", "D#", "F#"],
        "Bb Minor-Major": ["Bb", "Db", "F", "Ab"],
        "C Half-Diminished": ["C", "Eb", "Gb", "Bb"],
        "D Half-Diminished": ["D", "F", "Ab", "C"],
        "E Half-Diminished": ["E", "G", "Bb", "D"],
        "F Half-Diminished": ["F", "Ab", "B", "Eb"],
        "G Half-Diminished": ["G", "Bb", "Db", "F"],
        "A Half-Diminished": ["A", "C", "Eb", "G"],
        "B Half-Diminished": ["B", "D", "F", "A"],
        "C# Half-Diminished": ["C#", "E", "G", "B"],
        "D# Half-Diminished": ["D#", "F#", "A", "C#"],
        "Eb Half-Diminished": ["Eb", "Gb", "Bbb", "Db"],
        "F# Half-Diminished": ["F#", "A", "C", "E"],
        "G# Half-Diminished": ["G#", "B", "D", "F#"],
        "Bb Half-Diminished": ["Bb", "Db", "Fb", "Ab"],
        "C Full-Diminished": ["C", "Eb", "Gb", "Bbb"],
        "D Full-Dimished": ["D", "F", "Ab", "Cb"],
        "E Full-Diminished": ["E", "G", "Bb", "D"],
        "F Full-Diminished": ["F", "Ab", "B", "D"],
        "G Full-Diminished": ["G", "Bb", "Db", "F"],
        "A Full-Diminished": ["A", "C", "Eb", "G"],
        "B Full-Diminished": ["B", "D", "F", "A"],
        "C# Full-Diminished": ["C#", "E", "G", "B"],
        "D# Full-Diminished": ["D#", "F#", "A", "C#"],
        "Eb Full-Diminished": ["Eb", "Gb", "Bbb", "Db"],
        "F# Full-Diminished": ["F#", "A", "C", "E"],
        "G# Full-Diminished": ["G#", "B", "D", "F#"],
        "Bb Full-Diminished": ["Bb", "Db", "Fb", "Ab"],
    }