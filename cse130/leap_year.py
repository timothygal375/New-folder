def is_leap_year(year):
    if year % 4 == 0 and ((year % 100 != 0) or (year % 400 == 0)):
        return True
    else:
        return False 
    
def get_total_days(year, month, day):
    total_days = 0 

    for y in range(1753, year):
        if is_leap_year(y):
            total_days += 366
        else: 
            total_days += 365

    month_days = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    if is_leap_year(year):
        month_days[2] = 29
    
    for m in range(1, month):
        total_days += month_days[m]

    total_days += day 

    return total_days 

def is_error(year, month, day):
    if year < 1753:
        print("Error. Year must be later than 1752. ")
        return True 
    if month < 1 or month > 12:
        print("Error. Invalid month. ")
        return True
    if day < 1: 
        print("Error. Invalid day. ")
        return True
    from calendar import monthrange
    max_day = monthrange(year, month)[1]
    if day > max_day:
        print(f"Error. {month}/{year} only has {max_day} days.")
        return True
    
    return False

def main():
    while True:
        start_year = input("Start year: ")
        start_month = input("Start month: ")
        start_day = input("Start day: ")
        end_year = input("End year: ")
        end_month = input("End month: ")
        end_day = input("End day: ")

        try:
            s_y = int(start_year)
            s_m = int(start_month)
            s_d = int(start_day)
            e_y = int(end_year)
            e_m = int(end_month)
            e_d = int(end_day)
        except ValueError:
            print("Error: All inputs must be integers.")
            continue

        if is_error(s_y, s_m, s_d) or is_error(e_y, e_m, e_d):
            continue

        if (e_y, e_m, e_d) < (s_y, s_m, s_d):
            print("Error. End date is earlier than start date.")
            continue

        start_total = get_total_days(s_y, s_m, s_d)
        end_total = get_total_days(e_y, e_m, e_d)
        difference = end_total - start_total

        print(f"The difference between {start_month}/{start_day}/{start_year} and {end_month}/{end_day}/{end_year} is {difference} days. ")
        break

main()