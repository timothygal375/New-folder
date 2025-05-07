# 1. Name:
#    Timothy Galbraith
# 2. Assignment Name:
#    Lab 02: Authentication
# 3. Assignment Description:
#    This program is designed to check if a user has entered valiid login credentials, to authinticate them if they
#    have, and to deny them access if they have not.
# 4. What was the hardest part? Be as specific as possible.
#    This time around, the hardest part was figuring out how to get the program to convert the JSON file to a 
#    dictionary, and then to get the username and password values to match each other. Eventually, I decided to
#    use the index numbers of the username and password lists to get the program to associate them with each other.
# 5. How long did it take you to complete this assignment?
#    This assignment took about an hour to complete. 

import json 

with open('user.json', 'r') as f:
    data = json.load(f)

usernames = data['username']
passwords = data['password']

input_username = input("Username: ")
input_password = input("Password: ")

if input_username in usernames:
    index = usernames.index(input_username)
    if passwords[index] == input_password:
        print("You are authenticated!")
    else: 
        print("You are not authorized to use the system.")
else: 
    print("You are not authorized to use the system.")