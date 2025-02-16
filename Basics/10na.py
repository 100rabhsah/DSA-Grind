#Program for Sum of the digits of a given number

def sumofd(n):
    s=0
    while n!=0:
        d=n%10
        s=s+d
        n=n//10
    return s

n = int(input("Enter a number"))
print("Sum of the digits of the number is: ",sumofd(n))