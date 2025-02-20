#Program to find the Interior and Exterior Angle of a Regular Polygon

n=int(input("Enter no of sides of polygon: "))

print(f"Interior angle: {((n-2)*180)//n} Exterior angle: {360//n}")