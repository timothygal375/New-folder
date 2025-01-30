answer = input("What would you like to calculate? ").capitalize

if answer == "newtons":
    kilogram = float(input("Enter kilograms: "))
    meter = float(input("Enter meters: "))
    second = float(input("Enter seconds: "))
    newton = kilogram * (meter/(second ** 2))
    print(f"{newton} newtons were generated. ")

if answer == "joules":
    newton = float(input("Enter newtons: "))
    meter = float(input("Enter meters: "))
    joule = newton * meter
    print(f"{joule} joules were generated. ")

if answer == "watts":
    joule = float(input("Enter joules: "))
    second = float(input("Enter seconds: "))
    watt = joule/second
    print(f"{watt} watts were generated. ")

