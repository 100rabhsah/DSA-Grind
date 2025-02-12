#Program to count the number of vowels in a word

w=str(input("Enter a word :"))
c=0
for i in w:
    if i in ("a", "e", "i", "o", "u"):  
        c += 1  

print(f"No of vowels in the word {w} is : ",c)