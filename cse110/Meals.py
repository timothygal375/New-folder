import re

hamburger = 5
fries = 2.5
small_drink = 0.5 
drink = 1
large_drink = 1.5 
shake = 2
sales_tax = 0.05

print("A hamburger is $5")
print("Fries are $2.50")
print("A small drink is $0.50")
print("A medium drink is $1")
print("A large drink is $1.50")
print("A shake is $2")

order = input("Enter your order (e.g. 1 hamburger, 2 fries, 2 small drinks): ")

pattern = r"(\d+)\s*(hamburger|fries|small drink|medium drink|large drink|shake)"

total_hamburger = 0
total_fries = 0
total_small_drink = 0
total_drink = 0 
total_large_drink = 0 
total_shake = 0

matches = re.findall(pattern, order.lower())

for match in matches:
    quantity = int(match[0])
    item = match[1]
    if item == "hamburger":
        total_hamburger += quantity * hamburger
    elif item == "fries":
        total_fries += quantity * fries
    elif item == "small drink":
        total_small_drink += quantity * small_drink
    elif item == "medium drink":
        total_drink += quantity * drink
    elif item == "large drink":
        total_large_drink += quantity * large_drink
    elif item == "shake":
        total_shake += quantity * shake

tip = float(input('How much would you like to tip? (in %) '))

subtotal = (total_hamburger + total_fries + total_small_drink + total_drink + total_large_drink + total_shake + (tip/100))

tax = subtotal * sales_tax

total = subtotal + tax


print()
print(f'Subtotal: ${subtotal: .2f}')
print(f'Tax: ${tax: .2f}')
print (f'Total: ${total: .2f} ')

print()
payment = float(input('How much is the payment? '))
change = payment - total 
round_change = round(change, 2)
print(f'Your change is ${round_change: .2f}.')