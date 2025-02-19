#Check if a right-angled triangle can be formed by the given coordinates

x1,y1=map(int,input("Enter x1 and y1: ").split())
x2,y2=map(int,input("Enter x2 and y2: ").split())
x3,y3=map(int,input("Enter x3 and y3: ").split())

A = (int(pow((x2 - x1), 2)) + int(pow((y2 - y1), 2)))
B = (int(pow((x3 - x2), 2)) + int(pow((y3 - y2), 2)))
C = (int(pow((x3 - x1), 2)) + int(pow((y3 - y1), 2)))

if ((A > 0 and B > 0 and C > 0) and (A == (B + C) or B == (A + C) or C == (A + B))):
     print("yes right angled triangle can be formed")
else:
     print("No right angled triangle can't be formed")