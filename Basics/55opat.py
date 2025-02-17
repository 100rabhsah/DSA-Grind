#Program to print Butterfly Pattern (Star Pattern)

n=int(input("Enter size of butterfly pattern"))

spaces=2*n-1
stars=0

for i in range(1,2*n):
    if i <= n:
        spaces = spaces - 2
        stars += 1
    else:
        spaces = spaces + 2
        stars -= 1
    for j in range(1,stars+1):
        print("*",end="")
    for j in range(1,spaces+1):
        print(" ",end="")
    for j in range(1,stars+1):
        if j!=n:
            print("*",end="")
    print()
