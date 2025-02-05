#Program to find the sum and difference of two numbers

def sumdiff(x,y):
    return x+y,x-y

x = int(input("Enter no 1:"))
y = int(input("Enter no 2:"))
print("the sum and difference are: ",sumdiff(x,y))