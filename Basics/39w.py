#Program to count the number of consonants in a word

w=str(input("Enter a word :"))
c=0
for i in w:
    if i not in ("a", "e", "i", "o", "u"):  
        c += 1  

print(f"No of consonants in the word {w} is : ",c)