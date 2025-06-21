# 1. Name:
#      Timothy Galbraith
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This program read a JSON file and sorts an array of words alphabetically via a bubble sort algorithm. 
#      The program then returns the sorted list and prints it in the console. 
# 4. What was the hardest part? Be as specific as possible.
#      This assignment was relatively easy, given that I deisgned much of the logic for it last week in 
#      pseudocode. I was able to implement most of it fairly easily, with the most difficult part being designing
#      the logic that would actually swap the two words in the list that needed to be swapped according to the 
#      parameters of the assignment. The logic for loading the json file and having the program read it was fairly 
#      simple, as I've done it many times before. Overall, this assignment didn't give me a whole lot of trouble, 
#      thus, I was able to finish it fairly quickly. 
# 5. How long did it take for you to complete the assignment?
#      About an hour

import json

file_name = input("Please enter the name of a json file: ")

with open(file_name, 'r') as file:
    data = json.load(file)
    word_list = data['array']

def bubble_sort(word_list):
    if word_list is None or len(word_list) == 0:
        return []
    
    if len(word_list) == 1:
        return word_list
    
    for i in range(len(word_list) - 1):
        for j in range(len(word_list) - 1 - i):
            if word_list[j] > word_list[j + 1]:
                word_list[j], word_list[j + 1] = word_list[j + 1], word_list[j]
    return word_list

sorted_list = bubble_sort(word_list)
print("Sorted list:", sorted_list)



