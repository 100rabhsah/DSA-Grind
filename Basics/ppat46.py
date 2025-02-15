#Program to print Full Pyramid Pattern (Star Pattern)

n=int(input("size of full pyramid: "))

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()

