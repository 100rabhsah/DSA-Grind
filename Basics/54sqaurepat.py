#Program to print hollow rectangle or square star patterns

n=int(input("Enter rows of sqaure star pattern: "))
m=int(input("Enter columns of sqaure star pattern: "))

for i in range(1,n+1):
    for j in range(1,m+1):
        if(i==1 or i==n or j==1 or j==m):
            print("*",end="")
        else:
            print(" ",end="")
    print()