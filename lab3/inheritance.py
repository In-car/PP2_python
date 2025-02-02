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


#adding __init__() function 
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Aikorkem", "Zhumas")
x.printname()


#using super() function 
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Miras" , "Shokibay")
x.printname()


#adding properties 
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2028

x = Student("Inakr" , "Farkhatkyzy")
print(x.graduationyear)


#adding methods 
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Inkar" ,"Farkhatkyzy", 2028)
x.welcome()