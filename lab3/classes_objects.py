#creating a class 
class Myclass : 
    x = 9 


#create an object 
y = Myclass()
print(y.x)


#__init__() function 
class Person:
    def __init__(self , name , age ):
        self.name = name 
        self.age = age 
p1 = Person("Inkar" , 17)

print(p1.name)
print(p1.age)


#__str__() function 
class Me : 
    def __init__(self , name , age ):
        self.name = name 
        self.age = age 

    def __str__(self):
        return f"{self.name}({self.age})"
    
p2 = Me("Aisha" , 13)

print(p2)


#object methods 
class Person : 
    def __init__(self , name , age):
        self.name = name 
        self.age = age 

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("Zhannur" , 19)
p1.myfunc()


#the self parameter does not have to be named "self"
class Person : 
    def __init__(myobject , name , age ):
        myobject.name = name 
        myobject.age = age 
    
    def myfunc(abc):
        print("Hello my name is " + abc.name )

p1 = Person("Tanzilya" , 18)
p1.myfunc()


#modify the properties of object 
p1.age = 19 
print(p1.age)


#delete properties of object 
del p1.age 
#if i run print(p1.age) there will be an error 


#class defenitions can NOT be empty , but we can use pass 
class Person : 
    pass