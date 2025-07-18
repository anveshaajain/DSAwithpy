#write a python program to read 5 integers in a list print the first, last and all the elements using loop. reverse the list
n=5
lst=[1,2,3,4,5]
print("First element:", lst[0])
print("Last element:", lst[-1])
print("All elements:")
for i in lst:
    print(i, end=' ')
print("\nReversed list:")
lst.reverse()
for i in lst:
    print(i, end=' ')