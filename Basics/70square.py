#Program to find Perimeter / Circumference of Square and Rectangle

a=int(input("Enter side of a square: "))
l,b=map(int,(input("Enter length and breadth: ")).split())


print(f"Circumference of square is: {4*a} and Circumference of rectangle is: {2*(l+b)}")