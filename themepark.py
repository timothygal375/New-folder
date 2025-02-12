number = input("Are there going to be 1 or 2 people riding? ")

def welcome():
    print("Welcome to the ride! Be safe and have fun!")

def one_rider():
    height = int(input("How tall are you? (in inches) "))
    age = int(input("How old are you? "))
    if height < 62:
        print("Sorry. You may not ride. You are shorter than 62 inches.")
    elif age < 18:
        if age >= 12:
            passport = input("Do you have a Golden Passport? (yes/no) ").lower()
            if passport == "yes":
                welcome()
            else: 
                print("Sorry, you may not ride. You are under 18 and do not have a passport. ")
        else: 
            print("Sorry, you may not ride. You are under 18. ")
    else: 
        welcome()

def two_riders():
    height1 = int(input("How tall is the first rider? (in inches) "))
    age1 = int(input("How old is the first rider? "))
    height2 = int(input("How tall is the second rider? (in inches) "))
    age2 = int(input("How old is the second rider? "))
    if height1 < 36 or height2 < 36:
        print("Sorry. You may not ride. One of you is under 36 inches. ")
    elif age1 < 18 and age2 < 18:
        if age1 >= 12 and age2 >= 12 and height1 >= 52 and height2 >= 52:
            welcome()
        elif age1 < 12 or age2 < 12:
            print("Sorry, you may not ride. One or both of you are under 12. ")
        elif height1 < 52 or height2 < 52:
            passport = input("Do both of you have a Golden Passport? (yes/no)")
            if passport == "yes":
                welcome()
            else:
                print("Sorry, you may not ride. One or both of you are under 52 inches and doesn't have a Golden Passport. ")
        elif age1 >= 14 and age2 >= 16 or age1 >=16 and age2 >= 14:
            welcome()
        else: 
            print("Sorry, you may not ride. You are both too young. ")
    else: 
        welcome()

if number == "1":
    one_rider()
elif number == "2":
    two_riders()
else: 
    print("Sorry. Only one or two people may ride. ")



