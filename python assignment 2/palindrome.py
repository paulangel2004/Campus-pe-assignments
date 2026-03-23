text = input("Enter word/number: ")

reversed_text = text[::-1]

print("Original:", text)
print("Reversed:", reversed_text)

if text.lower() == reversed_text.lower():
    print("Result: PALINDROME")
else:
    print("Result: NOT A PALINDROME")