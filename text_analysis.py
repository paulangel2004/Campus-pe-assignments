#Function to count total number of words in the text
def count_words(text):
    return len(text.split())


#Function to count number of vowels(a, e, i, o, u)
def count_vowels(text):
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count
#Function to count number of consonants
def count_consonants(text):
    count = 0
    for char in text.lower():
        if char.isalpha() and char not in "aeiou":
            count += 1
    return count

#Function to reverse the given text
def reverse_text(text):
    return text[::-1]
#Function to check if text is palindrome
def is_palindrome(text):
    clean = text.lower().replace(" ", "")
    return clean == clean[::-1]

#Function to remove vowels from text
def remove_vowels(text):
    result = ""
    for char in text:
        if char.lower() not in "aeiou":
            result += char
    return result

#Function to count frequency of each word
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

#Function to find the longest word in text
def longest_word(text):
    words = text.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def analyze_text(text):
    print("=== TEXT ANALYSIS ===")
    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))
    print("Palindrome:", "Yes" if is_palindrome(text) else "No")
    print("Without vowels:", remove_vowels(text))

    longest = longest_word(text)
    print("Longest word:", longest, f"({len(longest)} letters)")

    freq = word_frequency(text)
    print("Word Frequency:")
    for word, count in freq.items():
        print(word + ":", count)


text = input("Enter text: ")
analyze_text(text)