#Program to find the mid-point of a line

x1,y1=map(int,input("Enter x1 and y1: ").split())
x2,y2=map(int,input("Enter x1 and y1: ").split())

mid_x = (x1 + x2) // 2
mid_y = (y1 + y2) // 2

print(f"Midpoint: ({mid_x}, {mid_y})")