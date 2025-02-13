#Program to find the length of the longest word in a sentence

sentence = str(input("Enter a sentence :"))
words = []  
word = ""  

for char in sentence:
    if char == " ":  
        if word:  
            words.append(word) 
            word = "" 
    else:
        word += char 

if word:
    words.append(word)

max_length = 0 

for word in words:  
    if len(word) > max_length:
        max_length = len(word) 

print("Maximum word length:", max_length)

