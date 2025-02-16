#Find n-th term of series 1, 3, 6, 10, 15, 21...

def series(n):
    return n*(n+1)//2

n = int(input("Enter n to find nth term of series: "))
print("The nth term is : ",series(n))