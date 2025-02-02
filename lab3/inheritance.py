#creating a parent class 
class Person : 
    def __init__(self, fname , lname):
        self.firstname = fname 
        self.lastname = lname 

    def printname(self):
        print(self.firstname , self.lastname)

x = Person("Inkar" , "Farkhatkyzy")
x.printname()


#creating a child class 
class Person : 
    def __init__(self, fname , lname):
        self.firstname = fname 
        self.lastname = lname 

    def printname(self):
        print(self.firstname , self.lastname)

class Student(Person):
    pass 

x = Student("Aisha" , "Farkhatkyzy")
x.printname()