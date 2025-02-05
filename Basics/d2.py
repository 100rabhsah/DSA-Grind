##write a program to reverse digits of a number

def rev(n):
    rev_num=0
    while n!=0:
        d=n%10
        rev_num=rev_num*10+d
        n=n//10
    return rev_num

n = int(input("Enter the number:"))
print("reversed number:",rev(n))