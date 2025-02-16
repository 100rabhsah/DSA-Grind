#Program to print first 10 fibonacci series

a=-1
b=1
for i in range(1,11):
    c=abs(a+b)
    b=a
    a=c
    print(c)
    