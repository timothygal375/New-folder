grade = int(input("Enter your grade percentage: "))
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

second_digit = grade % 10
if second_digit >= 7:
    symbol = "+"
elif second_digit <= 3:
    symbol = "-"
else:
    symbol = ""

if grade >= 97:
    symbol = ""
if grade <= 59:
    symbol = ""

print(f"Your grade is {letter}{symbol}. ")

if grade >= 70:
    print("You passed!")
else:
    print("You failed.")