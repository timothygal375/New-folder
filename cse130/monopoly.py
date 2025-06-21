# 1. Name:
#      timothy Galbraith
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      this program is designed to help someone playing the board game "Monopoly" to determine if they can place a hotel on Pennsylvania Avenue.
# 4. What was the hardest part? Be as specific as possible.
#    The hardest part of this program was accounting for every possible case and designing the functions to flow into one
#    another in a natural way. I also wanted to minimize the number of prompts for the use to input. 
# 5. How long did it take for you to complete the assignment?
#      2 hours

def start():
    global money_owned
    owned_properties = input("Do you own all three green properties? (yes/no): ").strip().lower()
    if owned_properties == "yes":
        pennsylvania_check_hotel()
    else:
        print("You cannot purchase a hotel if you do not own all three properties.")
        restart()

def pennsylvania_check_hotel():
    global items_on_pennsylvania
    items_on_pennsylvania = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))

    if items_on_pennsylvania == 5:
        print("You cannot purchase a hotel if the property already has one.")
        restart()
    else:
        north_carolina_check_houses()

def north_carolina_check_houses():
    global items_on_north_carolina
    items_on_north_carolina = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))
    if items_on_north_carolina == 5:
        swap_hotel()
    else:
        pacific_check_houses()

def pacific_check_houses(): 
    global items_on_pacific
    items_on_pacific = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))
    if items_on_pacific == 5:
        swap_hotel()
    else:
        enough_money()

def swap_hotel():
    if items_on_pennsylvania == 4:
        swap_hotel_2()
    else: 
        print("You cannot swap a hotel if Pennsylvania Avenue does not have four houses.")
        restart()

def swap_hotel_2():
    move_from_where = input("Where do you want to move the hotel from? (Pacific Avenue/North Carolina Avenue): ").strip().lower()

    if move_from_where == "pacific":
        print("Swap Pacific's hotel with Pennsylvania's four houses.")
        restart()
    elif move_from_where == "north carolina":
        print("Swap North Carolina's hotel with Pennsylvania's four houses.")
        restart()
    else:
        print("Invalid input. Please enter either 'Pacific Avenue' or 'North Carolina Avenue'.")
        swap_hotel_2()

def enough_money():
    global house_amount, pay_amount
    house_amount = int(input("How many houses do you want to purchase?"))
    pay_amount = (house_amount + 1) * 200
    money_owned = int(input("How much money do you have on hand? "))
    if money_owned >= pay_amount:
        bank_house_check()
    else: 
        print("You do not have enough money to purchase a hotel.")
        restart()

def bank_house_check():
    if house_amount > 0:
        find_price()
    else: 
        bank_hotel_check()

def find_price():
    bank_houses = int(input("How many houses are in the bank?"))
    if bank_houses >= house_amount:
        bank_hotel_check()
    else: 
        print("There are not enough houses available for purchase at this time.")
        restart()

def bank_hotel_check():
    bank_hotels = int(input("How many hotels are in the bank?"))
    if bank_hotels > 0:
        transaction_1()
    else:
        print("There are no hotels available for purchase at this time.")
        restart()

def transaction_1():
    print(f"This will cost you ${pay_amount}. Purchase one hotel and {house_amount} house(s). Put one hotel on Pennsylvania Avenue and return any houses to the bank.")
    pacific_houses = int(input("How many houses will you be putting on Pacific Avenue?"))
    if pacific_houses > 0:
        print(f"Put {pacific_houses} house(s) on Pacific Avenue.")
        transaction_2()
    else: 
        transaction_2()

def transaction_2():
    north_carolina_houses = int(input("How many houses will you be putting on North Carolina Avenue?"))
    if north_carolina_houses > 0:
        print(f"Put {north_carolina_houses} house(s) on North Carolina Avenue.")
        restart()
    else:
        restart()

def restart():
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        start()
    else:
        print("Thank you for playing!")

start()

