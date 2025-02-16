#Program for Decimal to Binary Conversion

def dtob(n):
    binary=""
    while n>0:
        binary=str(n%2)+binary
        n//=2
    if binary:
        return binary
    else:
        "0"

    #return binary if binary else "0"

n = int(input("Enter the decimal number to convert: "))
print("The binary form is: ",dtob(n))