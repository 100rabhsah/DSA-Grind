#Program to print first 10 prime numbers

def is_Prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def n_Primes(count):
    primes=[]
    num = 2
    while len(primes)<count:
        if is_Prime(num):
            primes.append(num)
        num+=1
    return primes

print("first 10 prime numbers are: ",n_Primes(10))