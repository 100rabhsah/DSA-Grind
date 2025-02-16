#Program to print Inverted Right Half Pyramid Pattern (Star Pattern)

n=int(input("size of Inverted Right Half Pyramid : "))

for i in range(1,n+1):
    for j in range(n-i+1):
        print("*",end=" ")
    print()