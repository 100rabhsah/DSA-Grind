#Program to calculate distance between two points

import math

x1, y1 = map(int, input("Enter x1, y1: ").split())
x2, y2 = map(int, input("Enter x2, y2: ").split())

dist = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))

print("The distance b/w thw two points is: ",dist)