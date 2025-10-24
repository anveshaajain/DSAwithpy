n=5
lst=[]
while n!=0:
 a=int(input("Enter integer values"))
 lst.append(a)
 n=n-1

print(lst)

print(f"The first element",lst[0])
print(f"The last element",lst[-1])


for i in lst:
  print(i)

lst.reverse()

print(lst)
