#Check if a number is Palindrome

def palindrome(n):
    rev=0
    while n!=0:
        d=n%10
        rev=rev*10+d
        n=n//10
    return rev

n=int(input("Enter number to check if palindrome: "))
o=n
if o==palindrome(n):
    print("palindrome")
else:
    print("not palindrome")