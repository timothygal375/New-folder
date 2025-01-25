child_price = float(input("What is the price of a child's meal? "))
adult_price = float(input("What is the price of an adult's meal? "))
child_number = int(input('How many kids are there? '))
adult_number = int(input('How many adults are there? '))
sales_tax = float(input('What is the sales tax rate? (in %) '))
tip = float(input('How much would you like to tip? (in %) '))

subtotal = (child_price * child_number) + (adult_price * adult_number)
tax = subtotal * (sales_tax / 100) * (tip / 100)
round_tax = round(tax, 2)
total = subtotal + round_tax 

final_subtotal = f"{subtotal:.2f}" 
final_tax = f"{round_tax:.2f}" 
final_total = f"{total:.2f}"

print()
print(f'Subtotal: ${final_subtotal}')
print(f'Tax: ${final_tax}')
print (f'Total: ${final_total} ')

print()
payment = float(input('How much is the payment? '))
change = payment - total 
round_change = round(change, 2)
final_change = f"{round_change:.2f}" 
print(f'Your change is ${final_change}.')