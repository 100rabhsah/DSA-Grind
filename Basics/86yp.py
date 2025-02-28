#Program to count the number of months between given two years

startYear=int(input("Enter start year: "))
endYear=int(input("Enter end year: "))

if (startYear > endYear):
    print("Invalid Input")
else:
    print(f"The no of months b/w {startYear} and {endYear} is: ",(endYear - startYear + 1) * 12)