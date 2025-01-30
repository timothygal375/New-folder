import math

print("Welcome to the velocity calculator. Please enter the following: ")
print()
mass = float(input("Mass (in kg): "))
earth_gravity = 9.8
jupiter_gravity = 24
time = float(input("Time (in seconds): "))
fluid_density = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
area = float(input("Cross sectional area (in m^2): "))
drag = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

c = (1/2) * fluid_density * area * drag 
earth_velocity = math.sqrt((mass * earth_gravity)/c) * (1 - math.exp(-math.sqrt(mass * earth_gravity * c)/mass) * time)
jupiter_velocity = math.sqrt((mass * jupiter_gravity)/c) * (1 - math.exp(-math.sqrt(mass * jupiter_gravity * c)/mass) * time)

round_velocity = round(earth_velocity, 3)
round_velocity2 = round(jupiter_velocity, 3)
round_c = round(c, 3)

print()
print(f"The inner value of c is {round_c: .3f} ")
print(f"The velocity after {time} seconds  on Earth is {round_velocity: .3f} ")
print(f"The velocity after {time} seconds on Jupiter is {round_velocity2: .3f}")