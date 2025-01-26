odd_numbers = [ 1 , 3 , 7 ]
print(odd_numbers)

odd_numbers = [ 1, 3, 7, 9, 3]
print(odd_numbers)

print(len(odd_numbers))

fruits = [ "cherry " , "banana" , "apple "]

print(type(odd_numbers))

all_type = [ 1 , 3, "apple" , False , 23.44]

#list()
mylist = list(( 2, 4, 6, 8))
print(mylist)

print(mylist[2])
print(mylist[-1])
print(mylist[0:2])
print(mylist[1:])
print(mylist[:2])
print(mylist[-4:-1])

if 2 in mylist: 
    print("YES")
else: 
    print("NO")\

mylist[2] = 34 
print(mylist)

mylist[-3:-1] = [ 1, 2, 3 ]
print(mylist)

#insert 
names = ["Aidana" , "Alisher" , "Zhansaya" , "Temirlan"]
print(names)
names.insert(3, "Zhamilya")
print(names)

#append 
names.append("Hanzada")
print(names)

#extend 
list1 = [ 502  , 123 , 1000 , 9090]
list2 = [ 666 , 80085 , 505 ]
list1.extend(list2)
print(list1)

#delete 
longlist = ["a", "p" , "p" , "l" , "e" , "o" ,"f" , "f"]
print(longlist)
longlist.remove("f")
print(longlist)
longlist.pop(0)
print(longlist)
del longlist[3]
print(longlist)

longlist.clear()
print(longlist)

del longlist
