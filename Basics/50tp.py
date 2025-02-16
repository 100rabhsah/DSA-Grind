#Program to Print Floyd's Triangle

n=int(input("size of floyd's triangle: "))

num = 1  

for i in range(1, n + 1):  
    for j in range(1,i + 1):  
        print(num, end=" ")
        num += 1  
    print()  

