list = [ 1, 2, 3, 4, 5, 6] 
for i in list:
    print(i)

for i in range(len(list)):
    print(list[i])

i = 0 
while i<len(list):
    print(list[i])
    i+=1

[print(x) for x in list]

#comprehension

fruits = ["apple", "banana", "cherry"]
nulllist = []

for x in fruits:
  if "a" in x:
    nulllist.append(x)

print(nulllist)