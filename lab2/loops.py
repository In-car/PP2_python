#while 
a = 3 
while a !=0 :  
    print(a)
    a-=1 


list = [ 1, 2, 3, 4, 5, 6]
i = 0 
while i<len(list): 
    if list[i] == 5 :
        print("Found it!") 
        break
    i+=1 

while i<len(list):
    if len(list)/2 == i : 
        break
    print(list[i])
    i+=1 
else : print("list is empty")

#for loops 


fruits = [ "apple" , "banana" , "cherry"]
for i in fruits : 
    if i == "cherry" : 
        break
    print(i)

fruit = "grape"
for i in fruit : 
    if i == "r":
        continue
    print(i)


for i in range(7):
    print(i)

for i in range(10 , 2 ,-2) : 
    print(i)

thislist = [ 1, 2, 3, 4, 5, 6]
name = [ "Kate" , "Leon", "Erasyl"]
for i in thislist :
    for j in name : 
        print( i , j )

for x in thislist : 
    pass 