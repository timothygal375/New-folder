# 1. Name:
#     Timothy Galbraith
# 2. Assignment Name:
#      Lab 13: Power
# 3. Assignment Description:
#      This program is designed to import an array of integers from a json file and find the highest average among 
#      a set of subarrays within the original array, with each subarray being of a size specified by the user. 
# 4. What was the hardest part? Be as specific as possible.
#      This assignment was relatively simple. As usual, I was easily able to convert my pseudocode to Python without
#      any real issues. The hardest part of this assignment was designing the logic for importing the json file
#      and getting the program to recognize all of the specified asserts in the assingment description. I spent
#      quite some time thinking about how I wanted to handle asserts, and I ended using a lot of try/except and 
#      if/then blocks to handle logic for asserts. 
# 5. How long did it take for you to complete the assignment?
#      This assignment took about an hour to complete. 

import json
import os
import sys

file_name = input("Please enter the file name: ")

if not os.path.isfile(file_name):
    print("Error. File does not exist. ")
    sys.exit(1)

try:
    with open(file_name, "r") as data_file:
        data = json.load(data_file)
except json.JSONDecodeError:
    print("Error. File is not a valid json file. ")
    sys.exit(1)

if "array" not in data:
    print("Error. The json must contain a top-level key called 'array'. ")
    sys.exit(1)

array = data["array"]
if not isinstance(array, list) or not all(isinstance(i, int) for i in array):
    print("Error. The key 'array' must contain integer values. ")
    sys.exit(1)

try:
    size = int(input("Enter the size of the subarray: "))
    if size <= 0 or size > len(array):
        print(f"Error. Subarray size must be a positive integer that is less than the size of the array. ")
        sys.exit(1)
except ValueError:
    print("Error. Please enter a valid integer for the subarray size. ")
    sys.exit(1)


def find_highest_average(list, subarray_size):
    averages = []
    loop_amount = len(list) - subarray_size + 1

    for i in range(0, loop_amount):
        average_count = 0
        for j in range(i, i + subarray_size - 1):
            average_count += list[j]
        average = average_count / subarray_size
        averages.append(average)
    
    highest_average = 0 
    for i in averages: 
        if i > highest_average:
            highest_average = i
    
    print(f"The highest average value was {highest_average}")

find_highest_average(array, size)
