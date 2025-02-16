#Program for factorial of a number

def fact(n):
    f=1
    for i in range(1,n+1):
        f=i*f
    return f

n = int(input("Enter the number for finding its factorial: "))
print(f"The factorial of {n} is: ",fact(n))
