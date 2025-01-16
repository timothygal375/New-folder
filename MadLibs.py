print('Please enter the following: ')
print()

def a_or_an(word):
    vowels = 'aeiouAEIOU'
    if word[0] in vowels:
        return 'an'
    else:
        return 'a'
    
adjective = input('adjective: ')
animal = input('animal: ')
verb1 = input('verb (with "ing"): ')
exclamation = input('exclamation: ').capitalize()
verb2 = input('verb: ')
verb3 = input('verb: ')
celebrity = input('celebrity: ').title()
weapon = input('weapon: ')
yell = input('synonymn for yell: ')
verb4 = input('verb: ')
item = input('handy item: ')
adjective2 = input('adjective: ')

correct_article = a_or_an(adjective2)

print('\nYour story is: ')
story=f"The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb1} down the hallway. \"{exclamation}!\" I yelled. But all I could think to do was to {verb2} over and over. Miraculously,that caused it to stop, but not before it tried to {verb3} right in front of my family. However, this {animal} would soon prove to be the least of my issues. At that very instant, a portal opened and who should appear but {celebrity}, toting an extremely deadly {weapon}. With a loud {yell} they used their {weapon} to {verb4} my family. Luckily, I had my {item} handy and threw it at {celebrity}, incapacitating them. What {correct_article} {adjective2} day! "
print(story)