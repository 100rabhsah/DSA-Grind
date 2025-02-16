#Program to count the number of words in a sentence

w=str(input("Enter a sentence :"))
c=1
for i in w:
    if i==" ":
        c+=1

print("No of words in the sentence is : ",c)