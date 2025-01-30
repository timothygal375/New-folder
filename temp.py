temp = float(input("What is the temperature in Fahrenheit? "))
celsius = (temp - 32) * (5/9)
round_celsius = round(celsius, 1)
print(f"The temperature in celsius is {round_celsius}")