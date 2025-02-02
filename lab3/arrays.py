#we can use lists as arrays
names = [ "Inkar" , "Aisha" , "Aizere" ]


#get a value of a first array item 
x = names[0]


#modify the value of item in array 
names[0] = "Rayana"


#length of an array 
x = len(names)


#to print every item in array 
for i in names : 
    print(i)


#we use append() to add element to array(to the back)
names.append("Inkar")


#we use pop() to remove element(by the index)
names.pop(3)


#we can also use remove()(deletes element by its name)
names.remove("Aisha")


#here is other methods we can use 
evennumbers = [ 2, 4, 6, 8 ]
print(evennumbers)

#clear() removes all the elements 
evennumbers.clear()
print(evennumbers)

#copy() returns a copy of a list(copies the list to another list)
oddnumbers = [ 1, 3, 5, 7 ]
print(oddnumbers)
mylist = oddnumbers.copy()
print(mylist)

#count() returns the number of element its looking for
x = oddnumbers.count(1)
print(x)

#extend() ands two lists together 
my = [ 1, 2, 3, 4 ]
list1 = [ 5, 6, 7, 8 ]
print(my)
print(list1)
my.extend(list1)
print(my)

#index() returns the position of specific item 
y = oddnumbers.index(3)
print(y)

#inser() adds element by the index(to some position)
oddnumbers.insert(9 , 2)
print(oddnumbers)

#reverse() reverses the order of the list(Does NOT sors it in reverse)
print(oddnumbers)
oddnumbers.reverse()
print(oddnumbers)

#sort() sorts the list
print(oddnumbers)
oddnumbers.sort()
print(oddnumbers)