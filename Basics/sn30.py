#Program for Armstrong Numbers

def arm(n):
    s=0
    c=0
    x=[]
    while(n!=0):
        d=n%10
        c+=1
        x.append(d)
        n=n//10
    for i in x:
        s=s+pow(i,c)
    return s

n=int(input("Enter the number to check armstrong or not: "))
o=n
if(arm(n)==o):
    print("armstrong")
else:
    print("not armstrong")