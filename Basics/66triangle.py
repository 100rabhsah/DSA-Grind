#Program to find area of a triangle

import math 

a,b,c=map(float,input("Enter sides of triangle: ").split())

s=(a+b+c)/2

print("Area of triangle is: ",math.sqrt(s*(s-a)*(s-b)*(s-c)))