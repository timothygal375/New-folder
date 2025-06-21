temperature = float(input("Enter the temperature:"))
type = input("Enter the type of temperature (F or C): ")

if type.lower() == "c":
    temperature = temperature * 9/5 + 32

def wind_chill(x,y):
    return 35.74 + 0.6215 * x - 35.75 * y ** 0.16 + 0.4275 * x * y ** 0.16

wind_speed = 5 

while True:
    print(f"With {wind_speed} mph winds, the wind chill is {wind_chill(temperature, wind_speed):.2f}")
    wind_speed += 5
    if wind_speed > 60:
        break
