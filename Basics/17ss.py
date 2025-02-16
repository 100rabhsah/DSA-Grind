#Program for nth odd number

def odd(n):
    nums = list(range(1, 2 * n, 2))  # Generate the first n odd numbers
    return nums[-1]  # Return the nth odd number

n = int(input("Enter the nth term to get corresponding odd number: "))
print(f"The {n}th odd number is: {odd(n)}")