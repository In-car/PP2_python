#to define a function we use def
def myfunc():
    print("Hello! my name is Inkar")

myfunc() 


#functions with arguments 
def myfunc(name):
    print( name + " Farkhatkyzy")

myfunc("Inkar")
myfunc("Aisha")
myfunc("Aizere")

def my_func(fname , lname):
    print(fname + " " + lname)

my_func("Rayana" , "Farkhatkyzy")


#if you dont know how many arguments use * 
def children(*kid):
    print("The youngest child is " + kid[3])

children( "Inkar" , "Aisha" , "Aizere" , "Rayana")


# also can send arguments as key = value 
def my_func(child1 , child2 , child3 , child4):
    print("The youngest is " + child4)

my_func(child1 = "Inkar" , child2 = "Aisha" , child3 = "Aizere" , child4 = "Rayana")


#if you dont know many keyword arguments is gonna be use **
def myname(**kid):
    print("My name is " + kid["fname"])

myname( fname = "Inkar" , lname = "Farkhatkyzy")


#we use default parameter for cases when we have func with no argument 
def mycountry(country = "Kazahstan"):
    print("I am from " + country) 

mycountry("Sweden")
mycountry("Kyrgystan")
mycountry()


#passing list as an argument 
def pass_list(food):
    for i in food :
        print(i)

fruits = ["apple" , "banana" , "cherry", "grape"]
pass_list(fruits)


#we use return to let func to return a value 
def fivetimes(x):
    return 5*x

print(fivetimes(3))
print(fivetimes(5))
print(fivetimes(7))


#func can NOT be empty , but we can use pass to avoid getting an error 
def myfunc():
    pass 


#we use , / to have ONLY positional argument 
def myfunc(z , /):
    print(z)

myfunc(3)
#if we use keyword arguments there will be an error 


#we use * , to have ONLY keyword arguments 
def myfunc(* , y):
    print(y)

myfunc( y = 43)
#if we try to use positional argument there will be an error 


#we also can combine positional,keyword-only in function
def myfunc( a, b, /, *, c, d ):
    print( a + b + c + d )

myfunc( 3 , 4, c = 67 , d = 0 )


#we use recursion for function to call itself , like a loop untill we reach the result  
def recur(x):
    if x>0 :
        result = x/2 
        print(result)
        recur(x-1)
    else : 
        result = 0 
        return result  
    
recur(20)
#in this example func recurs, at recur(x-1) it calls itself
#as the result it prints the numbers devided by 2 , from 20 to 1
