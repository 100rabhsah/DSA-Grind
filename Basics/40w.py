#Program to reverse a word

w=str(input("Enter a word :"))
rev=""
for i in range(len(w) - 1, -1, -1):
    rev+= w[i]  

print(rev)