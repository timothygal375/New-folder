def start():
    print("Welcome to the word guessing game! ")
    word = "jarom"
    guesses = ['_'] * len(word)
    count = 0
    print(f"Your hint is {' '.join(guesses)}")
    while "_" in guesses:
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
    
    print(f"Nice! You got it. It took you {count} guesses. ")
    restart = input("Do you want to play again? (yes/no) ")
    if restart == "yes":
        start()
    else:
        print("Thanks for playing! ")

start()