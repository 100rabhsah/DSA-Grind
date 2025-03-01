#Program to count the number of days between two years

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_year(year):
    return 366 if is_leap_year(year) else 365


def main():
    startYear=int(input("Enter start year: "))
    endYear=int(input("Enter end year: "))

    number_of_days = sum(days_in_year(year)
                         for year in range(startYear, endYear + 1))

    # Display the result
    print(
        f"Number of days between {startYear} and {endYear} is: {number_of_days} days.")

main()