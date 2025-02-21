import random

def start():
    number = random.randint(1,100)
    count = 0
    while True:
        guess = int(input("What is your guess? "))
        count += 1
        if guess > number:
            print("Lower")
        elif guess < number:
            print("Higher")
        else:
            print(f"You got it! It took you {count} guesses. ")
            break
    restart = input("Do you want to play again? (yes/no) ")
    if restart == "yes":
        start()
    else:
        print("Thanks for playing! ")

start()









