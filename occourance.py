 #count the occurance of each element in the list and print them


lst=[1,5,2,7,8,2,1,4,7,9,3,12,1,4,6,8,1,4,6]
print("Original list: ",lst)

occurrences={}
for element in lst:
    if element in occurrences:
        occurrences[element] += 1
    else:
        occurrences[element] = 1


for element, count in occurrences.items():
    print(f'Element {element} occurs {count} times')

s=set(lst)
print(s)

