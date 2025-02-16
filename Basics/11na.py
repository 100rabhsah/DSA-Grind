#Program to Print Multiplication Table of a Number

def mul(n):
    for i in range(1,11):
        print(f"{n}x{i}={n*i}")
    
n = int(input("Enter the number whose table you want:"))
mul(n)