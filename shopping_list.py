item = 0 
accounts = []
amounts = []

print("Please enter the names of bank accounts and balances. Type 'quit' when finished.")

while True:
    item = input("Enter the name of the account: ")
    if item == "quit":
        break
    balance = float(input("Enter the balance of the account: "))
    accounts.append(item)
    amounts.append(balance)
    
   
print("Account information: ")
for i in range(len(accounts)):
    print(f"{accounts[i]} - ${amounts[i]:.2f}")

def display():
    total = sum(amounts)
    average = total/len(amounts)
    highest = max(amounts)
    
    print(f"Total: ${total:.2f}")
    print(f"Average: ${average:.2f}")
    print(f"Highest balance: ${highest:.2f}")
display()

update = input("Would you like to update an account? " ).lower()

while True:
    if update == "yes":
        target = input("What is the index of the account you would like to update? ")
        target = int(target)
        new_balance = float(input("What is the new balance? "))
        amounts[target] = new_balance
        print("Account information: ")
        for i in range(len(accounts)):
            print(f"{accounts[i]} - ${amounts[i]:.2f}")
        display()
    else:
        print("Thank you. Goodbye. ")
