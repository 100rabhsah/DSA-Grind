#Program to count the number of characters in a word

w=str(input("Enter a word :"))
c=0
for i in w:
    c=c+1

print(f"No of characters in the word {w} is : ",c)