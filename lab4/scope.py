#scope is the variable that is available from inside the region it is created 
#a variable that is created inside of the function 
# belongs to local scope of that function 
def myfunc():
    x = 4500
    print(x)

myfunc()


# a local variable can be accessed from a funtion within the function 
def my_func():
    x = 380 
    def myinnerfunc():
        print(x)
    myinnerfunc()

my_func()


#global scope 
# as we said can be used everywhere if its created in the main of the Python 
x = 900

def Func():
    print(x)

Func()

print(x)


#if the x is used in the global scope and the local 
#python will treat them as different variables 
x = 900

def Func():
    x = 500
    print(x)

Func()
print(x)
#Func() will print 500 while print() 900


#global keyword 
#we can use it to make a variable belong to global scope 
def Func():
    global x 
    x = 800
    print(x)

Func()
print(x)


#also can use global to change global variable 
x = 900

def Func():
    global x 
    x = 700 

Func()

print(x)


#using nonlocal kewword , will make variable belong to outer function 
def myfunc1():
  x = "Inkar"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())