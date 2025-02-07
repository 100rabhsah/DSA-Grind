#Program to print numbers having remainder 3 when divided by 11 (b/w 1 to 1000)

for i in range(1,1000):
    if(i%11==3):
        print(i,end=" ")