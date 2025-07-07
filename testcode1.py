def max_by_key(list, key_extractor):
    max_value = list[0]
    max_key = key_extractor(max_value)
    for i in list[1:]:
        current_key = key_extractor(i)
        if current_key > max_key:
            max_value = i 
            max_key = current_key 
    return max_value 

numbers = [1, 3, 5, 4, 7, 6]
value = max_by_key(numbers, lambda x: x)
print(value)
