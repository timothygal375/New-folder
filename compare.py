integer_1 = int(input("Enter an integer: "))
integer_2 = int(input("Enter another integer: "))

if integer_1 > integer_2:
    print("The first integer is greater than the second.")

if integer_1 < integer_2:
    print("The first integer is less than the second.")

if integer_1 == integer_2:
    print("The integers are equal.")

animal = input("What is your favorite animal? ").lower()

if animal == "octopus":
    print("That's my favorite animal too!")
else:
    print("That's not my favorite animal.")
