highest = -float("inf")
lowest = float("inf")

highest_data = None 
lowest_data = None

total_expectancy = 0
count = 0

with open("life-expectancy.csv") as life_expectancy:
    next(life_expectancy)

    input_year = input("Enter the year of interest: ")
    input_country = input("Enter the country of interest: ")

    year_highest = -float("inf")
    year_lowest = float("inf")
    year_highest_data = None
    year_lowest_data = None

    country_highest = -float("inf")
    country_lowest = float("inf")
    country_total = 0
    count2 = 0 
    country_highest_data = None 
    country_lowest_data = None
    
    for line in life_expectancy:
        country, abbreviation, year, expectancy = line.strip().split(',')
        expectancy = float(expectancy)
        if expectancy > highest:
            highest = expectancy
            highest_data = (country, abbreviation, year)
        if expectancy < lowest:
            lowest = expectancy
            lowest_data = (country, abbreviation, year)
        
        if year == input_year:
            if expectancy > year_highest:
                year_highest = expectancy
                year_highest_data = (country, abbreviation, year)
            if expectancy < year_lowest:
                year_lowest = expectancy
                year_lowest_data = (country, abbreviation, year)
                
        if country.lower() == input_country.lower():
            if expectancy > country_highest:
                country_highest = expectancy
                country_highest_data = (country, abbreviation, year)
            if expectancy < country_lowest:
                country_lowest = expectancy
                country_lowest_data = (country, abbreviation, year)
            country_total += expectancy
            count2 += 1
            country_average = country_total / count2
            
            total_expectancy += expectancy
            count += 1  

            average = total_expectancy / count 
            
    print(f"The average life expectancy in {input_year} is: {average:.2f}") 
    print(f"The highest life expectancy in {input_year} is: {year_highest:.2f} from {year_highest_data[0]} in {year_highest_data[2]}")
    print(f"The lowest life expectancy in {input_year} is: {year_lowest:.2f} from {year_lowest_data[0]} in {year_lowest_data[2]}")

    print(f"The average life expectancy in {input_country} is: {country_average:.2f}")
    print(f"The highest life expectancy in {input_country} is: {country_highest:.2f} from {country_highest_data[0]} in {country_highest_data[2]}")
    print(f"The lowest life expectancy in {input_country} is: {country_lowest:.2f} from {country_lowest_data[0]} in {country_lowest_data[2]}")

print(f"The overall max life expectancy is: {highest:.2f} from {highest_data[0]} in {highest_data[2]}")
print(f"The overall min life expectancy is: {lowest:.2f} from {lowest_data[0]} in {lowest_data[2]}")