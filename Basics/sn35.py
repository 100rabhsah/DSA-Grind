#Neon Number(sum of digits of square of the number is equal to the number)

def Neon(n):
    sq=n*n
    a=[]
    sum=0
    while sq!=0:
        d=sq%10
        a.append(d)
        sq=sq//10
    for i in a:
        sum=sum+i
    if(sum==n):
        return "Neon number"
    else:
        return "Not Neon number"

n=int(input("Enter n number to check if neon or not: "))
print(Neon(n))