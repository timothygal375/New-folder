import math

def is_prime(n):
    if n < 2:
        return False 
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def ask_user_for_number():
    while True:
        try:
            number = abs(int(input("Please enter a positive integer (>= 0): ")))
            return number 
        except(ValueError, TypeError): 
            print("Please enter a positive integer.")

def test_is_prime(n):
    prime_numbers = []
    for i in range(2, n):
        prime = is_prime(i)
        if prime:
            prime_numbers.append(i)
    return prime_numbers 

def operators(n):
    add_count = 0
    multiply_count = 1
    powers = []
    for i in range(1, n):
        add_count += i 
        multiply_count *= i 
        powers.append(2**i)
    print(add_count)
    print(multiply_count)
    print(powers)

def triangle(n):
    for i in range(1, n, 2):
        print("*"*i)

    for i in range(1, n, 2):
        print()
        print(" " * ((20 - i)//2), end="")
        for j in range(1, i):
            print("*", end="")

def main():
    print(test_is_prime(100))
    number = ask_user_for_number()
    prime = is_prime(number)
    triangle(number)
    operators(number)
    if prime:
        print(f"{number} is prime")
    else: 
        print(f"{number} is not prime")
main()