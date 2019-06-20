s=input("Enter the string:")
l=[]
for char in s:
  if char not in l:
    l.append(char)
print(len(l))
