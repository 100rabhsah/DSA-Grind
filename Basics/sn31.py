#Check if given number is perfect square

def square(n):
    if n==pow(n**0.5,2):
        return "perfect square"
    else:
        return "not perfect sqaure"
    
n=int(input("Enter no to check if perfect square or not: "))
print(square(n))

