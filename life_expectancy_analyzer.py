interest_year = input("Enter the year of interest: ")

with open("Life Expectancy Data.csv") as file:
    next(file)

    min_life = float("inf")
    max_life = float("-inf")
    min_country = ""
    max_country = ""
    min_year = 0
    max_year = 0

    year_total = 0
    year_count = 0
    year_min = float("inf")
    year_max = float("-inf")
    year_min_country = ""
    year_max_country = ""

    for line in file:
        parts = line.strip().split(",")
        country = parts[0]
        year = int(parts[2])
        life = float(parts[3])

        if life < min_life:
            min_life, min_country, min_year = life, country, year

        if life > max_life:
            max_life, max_country, max_year = life, country, year

        if year == int(interest_year):
            year_total += life
            year_count += 1

            if life < year_min:
                year_min, year_min_country = life, country

            if life > year_max:
                year_max, year_max_country = life, country

print(f"The overall max life expectancy is: {max_life:.2f} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {min_life:.2f} from {min_country} in {min_year}")

if year_count > 0:
    year_avg = year_total / year_count
    print(f"\nFor the year {interest_year}:")
    print(f"The average life expectancy across all countries was {year_avg:.2f}")
    print(f"The max life expectancy was in {year_max_country} with {year_max:.2f}")
    print(f"The min life expectancy was in {year_min_country} with {year_min:.2f}")
