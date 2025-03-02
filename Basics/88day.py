#Find number of days between two given dates

class Date: 
    def __init__(self, d, m, y): 
        self.d = d 
        self.m = m 
        self.y = y 

# To store number of days in all months from January to December 
monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

# Function to count number of leap years before the given date 
def countLeapYears(d): 
    years = d.y 
    if d.m <= 2: 
        years -= 1
    return years // 4 - years // 100 + years // 400

# Function to calculate the difference in days between two dates 
def getDifference(dt1, dt2): 
    n1 = dt1.y * 365 + dt1.d 
    for i in range(0, dt1.m - 1): 
        n1 += monthDays[i] 
    n1 += countLeapYears(dt1) 

    n2 = dt2.y * 365 + dt2.d 
    for i in range(0, dt2.m - 1): 
        n2 += monthDays[i] 
    n2 += countLeapYears(dt2) 

    return n2 - n1 

# Taking user input for the two dates
d1, m1, y1 = map(int, input("Enter first date (dd mm yyyy): ").split())
d2, m2, y2 = map(int, input("Enter second date (dd mm yyyy): ").split())

# Creating Date objects
dt1 = Date(d1, m1, y1)
dt2 = Date(d2, m2, y2)

# Calculating and printing the difference
print("Difference between two dates is", getDifference(dt1, dt2), "days")