#Program to print binary right angled triangle

n=int(input("Enter size of binary right angle triangle"))

for i in range(0, n):  

    for j in range(0, i + 1):  
          
        if (((i + j) % 2) == 0) : 
                print("0", end = "") 
        else: 
            print("1", end = "") 
        print("\t", end = "") 
          
    print("") 