def increment_exponentially(base, increment):
    return lambda x: base ** (x + increment)

first_function = increment_exponentially(1, 0)
second_function = increment_exponentially(2, 1)
third_function = increment_exponentially(3, 2)

print(first_function(1))
print(second_function(1))
print(third_function(1))