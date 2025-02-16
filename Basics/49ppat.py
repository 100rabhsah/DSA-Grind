#Program to print Inverted Full Pyramid Pattern (Star Pattern)

n=int(input("size of inverted full pyramid: "))

for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end=" ")
    for j in range(2*(n-i)+1):
        print("*",end=" ")
    print()