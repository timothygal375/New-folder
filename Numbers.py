age = input('Please enter your current age: ')
age = int(age)
new_age = (age) + 1 
print (f'You will be {new_age} on your next birthday') 

print()
egg = input('Please enter the number of egg cartons currently in your possesion: ')
egg = int(egg)
answer = input('Do all of your cartons hold one dozen eggs? ').lower()
if answer == ('yes'):
    total_eggs = egg * 12
else: 
    carton_size = input('How many of your cartons contain 12 eggs? ')
    carton_size = int(carton_size)
    special_cartons = (egg) - (carton_size)
    carton_number = ('Do the remainder of your cartons each contain the same number of eggs? ').lower()
    if carton_number == 'yes' : 
        egg_number = input('How many eggs do the remainder of your cartons contain each? ')
        egg_number = int(egg_number)
        subtotal = special_cartons * egg_number
        subtotal2 = carton_size * 12
        total_eggs = subtotal + subtotal2 
    else: 
        eggs = 0
        cartons_entered = 0
        first_carton = True 
        while cartons_entered < special_cartons:
            if first_carton: 
                egg_number = input("Great! Now, let's talk about the cartons that don't contain 12 eggs. How many eggs does one of those cartons have? ")
                first_carton = False
            else:
                egg_number = input('How many eggs does another one of those cartons have? ')
            cartons = input('How many cartons do you have with that many eggs? ')
            egg_number = int(egg_number)
            cartons = int(cartons)
            eggs = egg_number * cartons
            cartons_entered += cartons
            if cartons_entered >= special_cartons:
                break 
        eggs2 = carton_size * 12
        eggs2 = int(eggs2)
        total_eggs = eggs + eggs2 
print(f'You have a total of {total_eggs} eggs')

print()
cookies = input('How many cookies do you have? ')
people = input('How many people are there? ')
cookies = float(cookies)
people = float(people)
divide = cookies / people
print(f'Each person may have {divide} cookies')