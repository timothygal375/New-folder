def min_by_key(lst, key_extractor):
    return min(lst, key=key_extractor)

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# Find the person with the minimum age
youngest = min_by_key(people, lambda person: person["age"])

print(youngest)
