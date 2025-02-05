#check whether a given is even or odd

def evenodd(n):
    if(n%2==0):
        return "Even"
    else:
        return "Odd"
    
n = int(input("Enter a number:"))
print("Even or odd:",evenodd(n))