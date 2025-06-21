def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False
count = 0
for y in range(0, 2003):
    if is_leap_year(y):
        count += 366
    else:
        count += 365

print(count)

month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
              7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

for m in range(1, 3):
    count += month_days[m]

print(count)

count += 6 
print(count)