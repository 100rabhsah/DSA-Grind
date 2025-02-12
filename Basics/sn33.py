#Spy Number (Sum and Products of Digits are same)

def Spy(n):
    sum = 0
    product = 1
    a=[]
    while n!=0:
        d=n%10
        a.append(d)
        n=n//10
    for i in a:
        sum=sum+i
        product=product*i
    if sum==product:
        return "Spy Number"
    else:
        return "Not Spy Number"
    
n=int(input("Enter number to check if Spy Number or not: "))
print(Spy(n))