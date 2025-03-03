#1 

f = open("C:\\Users\\Inkar\\Desktop\\PP2\\lab6\\myfile.txt" , "r")
print(f.read())
f.close()

#2

import os 

print("Path exists : ", os.path.exists("C:\\Users\\Inkar\\Desktop\\PP2\\lab6\\myfile.txt"))
    
print("It is readable : " , os.access("C:\\Users\\Inkar\\Desktop\\PP2\\lab6\\myfile.txt" , os.R_OK))
   
print("It is writable : " , os.access("C:\\Users\\Inkar\\Desktop\\PP2\\lab6\\myfile.txt" , os.W_OK))
    
print("It is executable : " , os.access("C:\\Users\\Inkar\\Desktop\\PP2\\lab6\\myfile.txt" , os.X_OK))

#3 

if os.path.exists("C:\\Users\\Inkar\\Desktop\\PP2\\lab6\\myfile.txt"):
    print("Yes it does exist !")
    print(os.path.dirname("C:\\Users\\Inkar\\Desktop\\PP2\\lab6\\myfile.txt"))
    print(os.path.basename("C:\\Users\\Inkar\\Desktop\\PP2\\lab6\\myfile.txt"))
else : 
    print("Path does not exist !")

#4

i = 0 
f = open("myfile.txt" , "r")
for _ in f :
    i=i+1
f.close()
print("The number of lines is : " , i )

#5

mylist = [ "apple" , "orange" , "lime" ]
l = open("myfile2.txt" , "a")

for i in mylist : 
    l.write(i + "\n")
l.close()

l = open("myfile2.txt" , "r")
print(l.read())

#6

import os 

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in letters : 
    file = open(f"{i}.txt" , "x")

#7

v = open("myfile.txt" , "r")
g = open("dublicate.txt" , "a")

g.write(v.read())
g.close()

g = open("dublicate.txt" , "r")
print(g.read())

#8 

import os 

if os.path.exists("C:\\Users\\Inkar\\Desktop\\PP2\\lab6\\deleteme.txt"):
    if os.access("C:\\Users\\Inkar\\Desktop\\PP2\\lab6\\d.txt" , os.W_OK):
        os.remove("C:\\Users\\Inkar\\Desktop\\PP2\\lab6\\deleteme.txt")
        print("Deleted.")
    else : 
        print("There is no access")
else : 
    print("Path does not exist")