#Ugly Numbers (sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15)

def is_ugly(n):
    if n <= 0:
        return False
    for factor in [2, 3, 5]:
        while n % factor == 0:
            n //= factor
    return n == 1

def nth_ugly_number(n):
    count = 0
    num = 1  # Start checking from 1

    while count < n:
        if is_ugly(num):
            count += 1
        num += 1
    
    return num - 1  # Last ugly number found

# Example: Print the 10th ugly number
n = int(input("Enter number to check ugly number or not"))
print(f"The {n}th ugly number is: {nth_ugly_number(n)}")