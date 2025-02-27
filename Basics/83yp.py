#Program to print the number of days in a given year

year = int(input("Enter year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year -> 366 days")
else:
    print("Not a leap year -> 365 days")