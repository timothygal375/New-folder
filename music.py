import random
def scale_recognition():
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
    global chords
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
        "E Full-Diminished": ["E", "G", "Bb", "Db"],
        "F Full-Diminished": ["F", "Ab", "B", "D"],
        "G Full-Diminished": ["G", "Bb", "Db", "Fb"],
        "A Full-Diminished": ["A", "C", "Eb", "Gb"],
        "B Full-Diminished": ["B", "D", "F", "Ab"],
        "C# Full-Diminished": ["C#", "E", "G", "A#"],
        "D# Full-Diminished": ["D#", "F#", "A", "C"],
        "Eb Full-Diminished": ["Eb", "Gb", "Bbb", "C"],
        "F# Full-Diminished": ["F#", "A", "C", "D#"],
        "G# Full-Diminished": ["G#", "B", "D", "F"],
        "Bb Full-Diminished": ["Bb", "Db", "Fb", "Abb"],
    }
    while True:
        chord_name = random.choice(list(chords.keys()))
        notes = chords[chord_name]
        answer = input(f"What are the notes in the {chord_name} chord? ")
        if answer.strip().split(",") == notes:
            print("Correct!")
        else:
            print(f"Incorrect. The notes in the {chord_name} chord are: {', '.join(notes)}")
        continue_test = input("Do you want to try another chord? (yes/no) ")
        if continue_test.strip().lower() != "yes":
            break
def chord_composition():
    while True:
        chord_name = random.choice(list(chords.keys()))
        notes = chords[chord_name]
        answer = input(f"Compose a {chord_name} chord using the notes {', '.join(notes)}: ")
        if set(answer.strip().split(",")) == set(notes):
            print("Correct! You composed the chord correctly.")
        else:
            print(f"Incorrect. The correct notes for the {chord_name} chord are: {', '.join(notes)}")
        continue_test = input("Do you want to try composing another chord? (yes/no) ")
        if continue_test.strip().lower() != "yes":
            break
def relative_major_minor():
    relative_pairs = {
        "C Major": "A Minor",
        "D Major": "B Minor",
        "E Major": "C# Minor",
        "F Major": "D Minor",
        "G Major": "E Minor",
        "A Major": "F# Minor",
        "B Major": "G# Minor",
        "C# Major": "A# Minor",
        "D# Major": "B# Minor",
        "Eb Major": "C Minor",
        "F# Major": "D# Minor",
        "Gb Major": "Eb Minor",
        "Ab Major": "F Minor",
        "Bb Major": "G Minor",
    }
    while True:
        major_key = random.choice(list(relative_pairs.keys()))
        minor_key = relative_pairs[major_key]
        answer = input(f"What is the relative minor of {major_key}? ")
        if answer.strip().lower() == minor_key.lower():
            print("Correct!")
        else:
            print(f"Incorrect. The relative minor of {major_key} is {minor_key}.")
        continue_test = input("Do you want to try another relative key? (yes/no) ")
        if continue_test.strip().lower() != "yes":
            break
def key_signature_identification():
    key_signatures = {
        "C Major": 0,
        "G Major": 1,
        "D Major": 2,
        "A Major": 3,
        "E Major": 4,
        "B Major": 5,
        "F# Major": 6,
        "C# Major": 7,
        "F Major": 1,
        "Bb Major": 2,
        "Eb Major": 3,
        "Ab Major": 4,
        "Db Major": 5,
        "Gb Major": 6,
        "Cb Major": 7,
        "A Minor": 0,
        "E Minor": 1,
        "B Minor": 2,
        "F# Minor": 3,
        "C# Minor": 4,
        "G# Minor": 5,
        "D# Minor": 6,
        "B# Minor": 7,
        "D Minor": 1,
        "G Minor": 2,
        "C Minor": 3,
        "F Minor": 4,
        "Bb Minor": 5,
        "Eb Minor": 6,
        "Ab Minor": 7,
    }
    while True:
        key = random.choice(list(key_signatures.keys()))
        answer = input(f"What is the key signature for {key}? (Enter the number of sharps/flats) ")
        if answer.strip() == str(key_signatures[key]):
            print("Correct!")
        else:
            print(f"Incorrect. The key signature for {key} has {key_signatures[key]} sharps/flats.")
        continue_test = input("Do you want to try another key signature? (yes/no) ")
        if continue_test.strip().lower() != "yes":
            break
def mode_recognition():
    modes = {
        "C Ionian": ["C", "D", "E", "F", "G", "A", "B"],
        "C Dorian": ["C", "D", "Eb", "F", "G", "A", "Bb"],
        "C Phrygian": ["C", "Db", "Eb", "F", "G", "Ab", "Bb"],
        "C Lydian": ["C", "D", "E", "F#", "G", "A", "B"],
        "C Mixolydian": ["C", "D", "E", "F", "G", "A", "Bb"],
        "C Aeolian": ["C", "D", "Eb", "F", "G", "Ab", "Bb"],
        "C Locrian": ["C", "Db", "Eb", "F", "Gb", "Ab", "Bb"],
        "D Ionian": ["D", "E", "F#", "G", "A", "B", "C#"],
        "D Dorian": ["D", "E", "F", "G", "A", "B", "C"],
        "D Phrygian": ["D", "Eb", "F", "G", "A", "Bb", "C"],
        "D Lydian": ["D", "E", "F#", "G#", "A", "B", "C#"],
        "D Mixolydian": ["D", "E", "F#", "G", "A", "B", "C"],
        "D Aeolian": ["D", "E", "F", "G", "A", "Bb", "C"],
        "D Locrian": ["D", "Eb", "F", "G", "Ab", "Bb", "C"],
        "E Ionian": ["E", "F#", "G#", "A", "B", "C#", "D#"],
        "E Dorian": ["E", "F#", "G", "A", "B", "C#", "D"],
        "E Phrygian": ["E", "F", "G", "A", "B", "C", "D"],
        "E Lydian": ["E", "F#", "G#", "A#", "B", "C#", "D#"],
        "E Mixolydian": ["E", "F#", "G#", "A", "B", "C#", "D"],
        "E Aeolian": ["E", "F#", "G", "A", "B", "C", "D"],
        "E Locrian": ["E", "F", "G", "A", "Bb", "C", "D"],
        "F Ionian": ["F", "G", "A", "Bb", "C", "D", "E"],
        "F Dorian": ["F", "G", "Ab", "Bb", "C", "D", "Eb"],
        "F Phrygian": ["F", "Gb", "Ab", "Bb", "C", "Db", "Eb"],
        "F Lydian": ["F", "G", "A", "B", "C", "D", "E"],
        "F Mixolydian": ["F", "G", "A", "Bb", "C", "D", "Eb"],
        "F Aeolian": ["F", "G", "Ab", "Bb", "C", "Db", "Eb"],
        "F Locrian": ["F", "Gb", "Ab", "Bb", "Cb", "Db", "Eb"],
        "G Ionian": ["G", "A", "B", "C", "D", "E", "F#"],
        "G Dorian": ["G", "A", "Bb", "C", "D", "E", "F"],
        "G Phrygian": ["G", "Ab", "Bb", "C", "D", "Eb", "F"],
        "G Lydian": ["G", "A", "B", "C#", "D", "E", "F#"],
        "G Mixolydian": ["G", "A", "B", "C", "D", "E", "F"],
        "G Aeolian": ["G", "A", "Bb", "C", "D", "Eb", "F"],
        "G Locrian": ["G", "Ab", "Bb", "C", "Db", "Eb", "F"],
        "A Ionian": ["A", "B", "C#", "D", "E", "F#", "G#"],
        "A Dorian": ["A", "B", "C", "D", "E", "F#", "G"],
        "A Phrygian": ["A", "Bb", "C", "D", "E", "F", "G"],
        "A Lydian": ["A", "B", "C#", "D#", "E", "F#", "G#"],
        "A Mixolydian": ["A", "B", "C#", "D", "E", "F#", "G"],
        "A Aeolian": ["A", "B", "C", "D", "E", "F", "G"],
        "A Locrian": ["A", "Bb", "C", "D", "Eb", "F", "G"],
        "B Ionian": ["B", "C#", "D#", "E", "F#", "G#", "A#"],
        "B Dorian": ["B", "C#", "D", "E", "F#", "G#", "A"],
        "B Phrygian": ["B", "C", "D", "E", "F#", "G", "A"],
        "B Lydian": ["B", "C#", "D#", "E#", "F#", "G#", "A#"],
        "B Mixolydian": ["B", "C#", "D#", "E", "F#", "G#", "A"],
        "B Aeolian": ["B", "C#", "D", "E", "F#", "G", "A"],
        "B Locrian": ["B", "C", "D", "E", "F", "G", "A"],
        "Db Ionian": ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"],
        "C# Dorian": ["C#", "D#", "E", "F#", "G#", "A", "B"],
        "C# Phrygian": ["C#", "D", "E", "F#", "G#", "A", "B"],
        "Db Lydian": ["Db", "Eb", "F", "G", "Ab", "Bb", "C"],
        "Db Mixolydian": ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"],
        "C# Aeolian": ["C#", "D#", "E", "F#", "G#", "A", "B"],
        "C# Locrian": ["C#", "D", "E", "F#", "G", "A", "B"],
        "Eb Ionian": ["Eb", "F", "G", "Ab", "Bb", "C", "D"],
        "Eb Dorian": ["Eb", "F", "Gb", "Ab", "Bb", "C", "Db"],
        "Eb Phrygian": ["Eb", "F", "Gb", "Ab", "Bb", "C", "Db"],
        "Eb Lydian": ["Eb", "F", "G", "A", "Bb", "C", "D"],
        "Eb Mixolydian": ["Eb", "F", "G", "Ab", "Bb", "C", "Db"],
        "Eb Aeolian": ["Eb", "F", "Gb", "Ab", "Bb", "C", "Db"],
        "Eb Locrian": ["Eb", "F", "Gb", "Ab", "Bb", "Cb", "Db"],
        "F# Ionian": ["F#", "G#", "A#", "B", "C#", "D#", "E#"],
        "F# Dorian": ["F#", "G#", "A", "B", "C#", "D#", "E"],
        "F# Phrygian": ["F#", "G", "A", "B", "C#", "D", "E"],
        "F# Lydian": ["F#", "G#", "A#", "B#", "C#", "D#", "E#"],
        "F# Mixolydian": ["F#", "G#", "A#", "B", "C#", "D#", "E"],
        "F# Aeolian": ["F#", "G#", "A", "B", "C#", "D", "E"],
        "F# Locrian": ["F#", "G", "A", "B", "C", "D", "E"],
        "Gb Ionian": ["Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F"],
        "Gb Mixolydian": ["Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F"],
        "Gb Lydian": ["Gb", "Ab", "Bb", "C", "Db", "Eb", "F"],
        "Ab Ionian": ["Ab", "Bb", "C", "Db", "Eb", "F", "G"],
        "Ab Dorian": ["Ab", "Bb", "Cb", "Db", "Eb", "F", "Gb"],
        "Ab Phrygian": ["Ab", "A", "Cb", "Db", "Eb", "F", "Gb"],
        "Ab Lydian": ["Ab", "Bb", "C", "D", "Eb", "F", "G"],
        "Ab Mixolydian": ["Ab", "Bb", "C", "Db", "Eb", "F", "Gb"],
        "Ab Aeolian": ["Ab", "Bb", "Cb", "Db", "Eb", "F", "Gb"],
        "Ab Locrian": ["Ab", "A", "Cb", "Db", "Eb", "Fb", "Gb"],
        "Bb Ionian": ["Bb", "C", "D", "Eb", "F", "G", "A"],
        "Bb Dorian": ["Bb", "C", "Db", "Eb", "F", "G", "Ab"],
        "Bb Phrygian": ["Bb", "B", "Db", "Eb", "F", "G", "Ab"],
        "Bb Lydian": ["Bb", "C", "D", "E", "F", "G", "A"],
        "Bb Mixolydian": ["Bb", "C", "D", "Eb", "F", "G", "Ab"],
        "Bb Aeolian": ["Bb", "C", "Db", "Eb", "F", "G", "Ab"],
        "Bb Locrian": ["Bb", "B", "Db", "Eb", "F", "Gb", "Ab"],
    }
    while True:
        mode = random.choice(list(modes.keys()))
        notes = modes[mode]
        answer = input(f"What are the notes in the {mode} mode? ")
        if answer.strip().split(",") == notes:
            print("Correct!")
        else:
            print(f"Incorrect. The notes in the {mode} mode are: {', '.join(notes)}")
        continue_test = input("Do you want to try another mode? (yes/no) ")
        if continue_test.strip().lower() != "yes":
            break
def main():
    print("Welcome to the Music Theory Quiz!")
    while True:
        print("\nChoose a test:")
        print("1. Scale Recognition")
        print("2. Interval Recognition")
        print("3. Scale Degrees")
        print("4. Chord Recognition")
        print("5. Chord Composition")
        print("6. Relative Major/Minor")
        print("7. Key Signature Identification")
        print("8. Mode Recognition")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")
                
        if choice == "1":
            scale_recognition()
        elif choice == "2":
            interval_test()
        elif choice == "3":
            scale_degrees()
        elif choice == "4":
            chord_recognition()
        elif choice == "5":
            chord_composition()
        elif choice == "6":
            relative_major_minor()
        elif choice == "7":
            key_signature_identification()
        elif choice == "8":
            mode_recognition()
        elif choice == "9":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice, please try again.")
main()