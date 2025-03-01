import random

print("Welcome to the word guessing game! ")
def start():
    difficulty = input("Select a difficulty (Easy, Medium, Hard, Expert) ").lower()

    word_list = ["apple", "blue", "star", "fish", "rock", "book", "tree", "frog", "gold", "moon", "sand", "kite", "rain", "snow", "fire"]
    word_list2 = ["rocket", "planet", "paper", "puzzle", "music", "dance", "green", "brown", "cloud", "chair", "house", "smile", "beach", "ocean", "train"]
    word_list3 = ["butterfly", "universe", "computer", "picture", "adventure", "sunflower", "journey", "mystery", "blanket", "rhythm", "candle", "library", "horizon", "bicycle", "travel"]
    word_list4 = ["encyclopedia", "extraordinary", "kindergarten", "laboratory", "waterfall", "astronaut", "skyscraper", "photography", "hologram", "discovery", "observation", "celebration", "generation", "championship", "elephant"]

    if difficulty == "easy":
        word = random.choice(word_list)

    elif difficulty == "medium":
        word = random.choice(word_list2)
    
    elif difficulty == "hard":
        word = random.choice(word_list3)
    
    elif difficulty == "expert":
        word = random.choice(word_list4)
    
    else:
        print("Invalid input. Please try again. ")
        start()

    guesses = ['_'] * len(word)
    count = 0
    print(f"Your hint is {' '.join(guesses)}")

    while True:
        guess = (input("What is your guess? "))
        count += 1
    
        if len(guess) != len(word):
            print(f"Your guess must be {len(word)} letters long. Try again. ")
            continue
        
        new_guesses = ["_"] * len(word)
        
        for i in range(len(word)):
            if guess[i] == word[i]:
                new_guesses[i] = guess[i].upper()
        
        for i in range(len(word)):
            if new_guesses[i] == "_":
                if guess[i] in word:
                    new_guesses[i] = guess[i]
        
        if new_guesses == guesses:
            print("No new letters were correct. Try again. ")
        else:
            guesses = new_guesses
            print(f"{" ".join(guesses)}")

        if "".join(guesses).lower() == word.lower():
             print(f"Nice! You got it. It took you {count} guesses. ")
             break

    restart = input("Do you want to play again? (yes/no) ")
    if restart == "yes":
        start()
    else:
        print("Thanks for playing! ")

start()