#Program to print Right Half Pyramid Pattern (Star Pattern)

n=int(input("size of right half pyramid: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


