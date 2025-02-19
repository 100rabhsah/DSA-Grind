#Program to check if a rectangle is a square or not

a,b=map(int,(input("Enter length and breadth: ")).split())

if a==b:
    print("it is a square")
else:
    print("it is a rectangle")