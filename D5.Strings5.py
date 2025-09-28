#count of vowels and consonants present in the user nme
String=input("Enter the String: ")
vowels,consonants=0,0
for ch in String:
    char_lower = ch.lower()
    
    # First, check if the character is an alphabet
    if char_lower.isalpha():
        # If it is an alphabet, then check if it is a vowel
        if char_lower in 'aeiou':
            vowels += 1
        # Otherwise, it must be a consonant
        else:
            consonants += 1

print(f"Count of vowels: {vowels}")
print(f"Count of consonants: {consonants}")