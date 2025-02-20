#Check if it is possible to create a polygon with a given angle

a=int(input("Enter an angle to check if polygon can be created or not: "))

n = 360 / (180 - a)
 
if n == int(n) :
    print("YES, can be created")
else :
    print("NO, cannot be created")