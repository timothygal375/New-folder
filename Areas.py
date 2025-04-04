import math 

while True:
    choice = input('What shape would you like to calculate the area for? ')
    length = float(input('What is the length of the shape? '))
    
    def rectangle_area(x,y):
        return x * y
    def square_area(x):
        if choice == 'square':
            rectangle_area(x,x)
        elif choice == 'circle':
            return math.pi * x ** 2
    
    if choice == 'square':
        square_area(length)
    elif choice == 'circle':
        square_area(length)
    elif choice == 'rectangle':
        width = float(input('What is the width of the shape?' ))
        rectangle_area(length, width)
    elif choice == 'quit':
        break
    else:
        print('Invalid choice. Please try again.')
        continue