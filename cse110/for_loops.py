quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

def go():
    count = 0
    x = int(input("Please enter a number: "))
    for letter in quote:
        if letter != " ":
            count += 1
            if count % x == 0:
                print(letter.upper(), end = "")
            else:
                print(letter, end = "")
        else:
            print(letter, end = "")

go()