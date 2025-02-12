#Automorphic Number(whose square ends in the same digits as the number itself)

def automorphic(n):
    sq=n*n
    d=sq%10
    if d==n:
        return "automorphic"
    else:
        return "not automorphic"
    
n=int(input("Enter number to check if automorphic or not: "))
print(automorphic(n))