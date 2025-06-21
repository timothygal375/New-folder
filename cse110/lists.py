numbers = []

number = None
smallest = None

while number != 0:
    number = int(input("Enter a number: "))
    if number != 0:
        numbers.append(number)

for number in numbers:
    if number > 0:
        if smallest is None or number < smallest:
            smallest = number

sorted_numbers = sorted(numbers)
    
print(f"The sum of the numbers is {sum(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The smallest positive number is {smallest}")
print(f"The numbers in ascending order are {sorted_numbers}")