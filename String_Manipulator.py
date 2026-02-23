sentence=input("enter the sentence :")
print("Original :",sentence)

#Count of characters with spaces
print("Total Charcters(with spaces) :", len(sentence))

#count of characters without spaces
print("Total Characters (without spaces):", len(sentence.replace(" ", "")))

#total words
print("Total Words :",len(sentence.split()))

#UPPERCASE
print("UPPERCASE :",sentence.upper())

#LOWERCASE
print("LOWERCASE :",sentence.lower())

#Title Case
print("TITLE CASE :", sentence.title())

#First Word
words=sentence.split()
print("First Word :", words[0])

#Last Word
print("First Word :", words[-1])


#Reversed Sentence
print("Reversed :",sentence[::-1])
