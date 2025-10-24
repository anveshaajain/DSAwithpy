#string palindrome
def is_palindrome(s):
    s = s.replace(" ", "").lower() # Normalize the string
    return s == s[::-1]


input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.') 
