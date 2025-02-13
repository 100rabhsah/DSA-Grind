#Program to reverse order of words in a sentence

sentence = str(input("Enter a sentence :"))
words = []  # List to store words
word = ""   # Temporary variable to store each word

# Extract words manually
for char in sentence:
    if char == " ":
        if word:  # Avoid multiple spaces
            words.append(word)
            word = ""  # Reset word after storing
    else:
        word += char

# Append the last word
if word:
    words.append(word)

# Reverse order of words manually
reversed_sentence = ""
for i in range(len(words) - 1, -1, -1):  # Loop from last word to first
    reversed_sentence += words[i]
    if i != 0:  # Add space between words
        reversed_sentence += " "

print("Reversed Sentence:", reversed_sentence)