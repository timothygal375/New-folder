name = "Uncle Bob"
search_letter = "o"

letter_found = False

if search_letter in name:
    print(f"{search_letter} is in {name}")
else:
    print(f"{search_letter} is not in {name}")

for letter in name:
    if search_letter == letter:
        letter_found = True 
        break

if letter_found:
    print(f"{search_letter} is in {name}")
else: 
    print(f"{search_letter} is not in {name}")

found = False 
index = 0 
while not found:
    if search_letter == name[index]:
        found = True 
        index += 1 
