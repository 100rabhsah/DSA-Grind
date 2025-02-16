#Program to print InvertedLeft Half Pyramid Pattern (Star Pattern)

n=int(input("size of inverted left half pyramid: "))

for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end=" ")
    for j in range(n-i+1):
        print("*",end=" ")
    print()

    #done