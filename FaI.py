def sum_of_digits(n):
    if n < 0:
        print("Error. Number is not positive. ")
    elif n % 1 != 0:
        print("Error. Number is not an integer. ")
    else:
        digit_sum = sum(int(d) for d in str(n))
        print(f"The sum of the digits of {n} is {digit_sum}")

sum_of_digits(12345)
sum_of_digits(-12345)
sum_of_digits(1.2345)
