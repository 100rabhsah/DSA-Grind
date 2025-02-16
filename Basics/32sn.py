#perfect number- sum of its positive divisors excluding the number itself

def perfect(n):
    sum_divisors = 0

    for i in range(1, n):  
        if n % i == 0:  
            sum_divisors += i  

    if sum_divisors == n:  
        print(True)  
    else:  
        print(False)

n = int(input("Enter number n to check if perfect or not: "))
perfect(n)   