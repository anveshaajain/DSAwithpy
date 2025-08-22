s = input("Enter a string: ")

vowels = ""
consonants = ""

for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += ch
        else:
            consonants += ch

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Number of vowels:", len(vowels))
print("Number of consonants:", len(consonants))
