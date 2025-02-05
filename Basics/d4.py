#count digits in a number

def count(n):
    c=0
    if (n==0):
        return 1
    while n!=0:
        n=n//10
        c += 1
    return c

n = int(input("Enter a number"))
print("no of digits are:", count(n))