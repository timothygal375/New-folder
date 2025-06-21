import re 

def palindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s)
    return s == s[::-1]

word = input("Please enter a word, phrase, or number: ").title()
if palindrome(word):
    print(f"{word} is a palindrome")
else: 
    print(f"{word} is not a palindrome")