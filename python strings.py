# String Reverse
text = input("Enter a string ")
print(text[::-1])

# String Palindrome
text = input("Enter a string ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

# Count Vowels in a string
text = input("Enter text: ")
count = 0
for char in text.lower():
    if char in "aeiou":
        count += 1
print("Vowels:", count)

# Unique vowel count
text = input("Enter text: ")
unique_vowels = set()
for char in text.lower():
    if char in "aeiou":
        unique_vowels.add(char)
print("Unique vowel count:", len(unique_vowels))
