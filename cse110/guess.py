# 1. Name:
#    Timothy Galbraith
# 2. Assignment Name: 
#    Lab 01: Guessing Game
# 3. Assignment Description:
#    Design a program that allows a user to guess a number within a range from one to any number the user chooses.
# 4. What was the hardest part? Be as specific as possible. 
#    The hardest part of this assingment for me was trying to decide how I wanted to strcture the while loop. I knew
#    that it needed to iterate every time the user guessed too high or too low and that it needed to break when the 
#    user correctly gussed the number. However, it was juggling all of the things that the loop needed to do that was
#    challenging. 
#5. How long did it take you to complete the assignment?
#   This assingment took about an hour and a half to complete. 

import random
guesses = []

print("This is the 'guess a number' game.")
print("You try to guess a number in the smallest number of attempts.")

def start():
    number_range = int(input("Pick a positive integer: "))
    number = random.randint(1,number_range)
    count = 0

    while True:
        guess = int(input(f"Guess a number between 1 and {number_range}: "))
        guesses.append(guess)
        count += 1
        
        if guess > number:
            print("\tToo High!")
        elif guess < number:
            print("\tToo Low!")
        else:
            print(f"You got it! It took you {count} guesses. ")
            print(f"The numbers you guessed were: {guesses}")
            break
    
    restart = input("Do you want to play again? (yes/no) ")
    if restart == "yes":
        start()
    else:
        print("Thanks for playing! ")

start()