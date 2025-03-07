actions = ['1. Add item','2. View Cart', '3. Remove item', '4. Compute total', '5. Quit']

print("Welcome to the Shopping Cart Program!")
print("Please select one of the following:")

for action in actions:
    print(action)

cart = {}

def add_item():
    item = input("What item would you like to add? ")
    price = float(input("What is the price of the item? "))
    cart[item] = price
    print(f"{item} has been added to your cart. ")

def view_cart():
    for item, price in cart.items():
        print(f"{item}: ${price}")

def remove_item():
    remove = input("What item would you like to remove? ")
    if remove in cart:
        del cart[remove]
        print(f"{remove} has been removed from your cart. ")
    else:
        print(f"{remove} is not in your cart. ")

def compute_total():
    total = sum(cart.values())
    print(f"Your total is ${total}")

def quit():
    print("Thank you. Goodbye. ")

while True:
    act_num = input("Please enter the number of the action you would like to take: ")

    if act_num == "1":
        add_item()
    elif act_num == "2":
        view_cart()
    elif act_num == "3":
        remove_item()
    elif act_num == "4":
        compute_total()
    elif act_num == "5":
        quit()
        break
    else:
        print("Invalid input. Please try again. ")

