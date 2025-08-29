#replacing a word 
def replace_word(s):
   print(s)
   old=input("Enter the word to be replaced")
   new=input("Enter the new word")
   print(s.replace(old,new)) 
    
    
s=input("Enter a string")
replace_word(s)