const noteDisplay = document.querySelector(".note-display img");
const feedback = document.getElementById("feedback");
const buttons = document.querySelectorAll(".note-options button");

const notes = ["C", "D", "E", "F", "G", "A", "B"];
let currentNote = "";

document.body.addEventListener("click", () => {
  Tone.start();
}, { once: true });

// Initialize the synth once
const synth = new Tone.Synth().toDestination();

function playNoteSound(note) {
  const noteWithOctave = note + "4"; // Middle C octave (you can adjust)
  synth.triggerAttackRelease(noteWithOctave, "8n");
}

// Load a new random note
function loadRandomNote() {
  const index = Math.floor(Math.random() * notes.length);
  currentNote = notes[index];
  noteDisplay.src = `assets/notes/note_${currentNote}.png`;
  feedback.textContent = "";
  playNoteSound(currentNote);
}

// Check user's answer
buttons.forEach(button => {
  button.addEventListener("click", () => {
    const guess = button.textContent;
    if (guess === currentNote) {
      feedback.textContent = "✅ Correct!";
      feedback.style.color = "green";
      setTimeout(loadRandomNote, 1000); // Load next note after 1 sec
    } else {
      feedback.textContent = "❌ Try again.";
      feedback.style.color = "red";
    }
  });
});

// Initialize first note
loadRandomNote();
