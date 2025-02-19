#Program to calculate the length of the diagonal in a rectangle

import math

a,b=map(int,(input("Enter length and width of rectangle: ")).split())

print(f"Diagonal length: {math.sqrt(a**2+b**2)}")