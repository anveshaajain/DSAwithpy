def find_longest_word(text):
    # Split the string into words
    words = text.split()
    # Find the longest word by length
    longest_word = max(words, key=len)
    return longest_word

my_string =input("Enter a sentence:")
print("The longest word is:", find_longest_word(my_string))