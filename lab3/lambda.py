#lambda is an anonymous function and its syntax is : 
#lambda argument:expression 
x = lambda a : a + 10 
print(x(5)) 


#lambda can have multiple arguments but have only one expression
x = lambda a, b : a*b 
print(x(5 ,4))

x = lambda a, b, c : a + b + c 
print(x( 3, 4, 5))

#using lambda 
def myfunc(y):
    return lambda a : a*y 


#the function returns anonymous function that will later be performed
mydoubler = myfunc(2)
#in mydoubler we have a anonymous func that has a doubler 
#that we set by myfunc(2)
print(mydoubler(10))
#the anonymous func performs when we set an argument to a
#the result is 20 


def myfunc(n):
    return lambda a : a*n

mytripler = myfunc(3)
print(mytripler(10)) 
