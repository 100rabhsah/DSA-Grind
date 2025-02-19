#Check whether triangle is valid or not if sides are given

a, b, c = map(int, input("Enter three sides: ").split())

if (a + b > c) and (b + c > a) and (a + c > b):
    print("The given sides form a valid triangle.")
else:
    print("The given sides do NOT form a valid triangle.")