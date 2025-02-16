#Program to check if a number is divisible by 5 or not

def divby5(n):
    if n%5==0:
        return "divisible"
    else:
        return "not divisible"

n = int(input("Enter a number to check if it is divisible by 5 or not:"))
print("Number is: ", divby5(n))