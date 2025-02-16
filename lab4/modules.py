#module can be seen same as a code library
#a file that contains a set of functions that will be included in many applications  


#create a module 
#using a module 
import mymodule 
mymodule.myfunc("Inkar")

a = mymodule.person1["age"]
print(a)


#we can create an alias when we import a module, 
#by using the as keyword 
import mymodule as mx 
a = mx.person1["country"]
print(a)


#build in modules  
import platform 
x = platform.system()
print(x)


y = dir(platform)
print(y)


#u can choose to import only parts from a module 
#by using from 
from mymodule import person1

print(person1["age"])
#when we import by using from 
#do not use module name like mymodule.smth
