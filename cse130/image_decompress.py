# 1. Name:
#      Timothy Galbraith
# 2. Assignment Name:
#      Lab 06: Image Compression
# 3. Assignment Description:
#      This project is designed to decompress a compressed image represnted as data in a JSON file. 
# 4. Algorithmic Efficiency
#      The algorithmic efficiency of this program is linear, or O(n), because of how it iterates through the 
#      data figure-by-figure.
# 5. What was the hardest part? Be as specific as possible.
#      The hardest part of this assigmnen was figuring out how to get the program to recognize when it needed
#      to flip a bit from 1 to 0 or vice versa. For the most part, this assignment was fairly straightforward,
#      and implementing the for loops and various functions was not too diffcult. 
# 6. How long did it take for you to complete the assignment?
#      This assigment took about two total hours to complete. 

import json

def decompress_row(row_data, num_columns):
    row = []
    bit = 1  
    for count in row_data:
        row.extend([bit] * count)
        bit = 1 - bit  

    if len(row) < num_columns:
        row.extend([0] * (num_columns - len(row)))
    return row

def display_image(image):
    for row in image:
        line = ''.join('#' if pixel == 1 else ' ' for pixel in row)
        print(line)

def main():
    filename = input("Please select a filename: ")
    try:
        with open(filename, 'r') as file:
            image_data = json.load(file)
        
        num_rows = image_data['num_rows']
        num_columns = image_data['num_columns']
        compressed_data = image_data['data']

        image = []
        for row_data in compressed_data:
            decompressed = decompress_row(row_data, num_columns)
            image.append(decompressed)

        display_image(image)

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON file.")
    except KeyError:
        print("Missing expected keys in JSON data.")

if __name__ == "__main__":
    main()
