print( 10 > 9 )
print( 10 == 9 )
print( 10 < 9 )

#with if/else statements 

a = 520 
b = 49 

if b > a : 
    print("b is greater than a")
else : 
    print("b is not greater than a")

#evaluating values 

print(bool(5669))
print(bool("Okko"))

#evaluating variables 

x = "Inkar"
y = 17 

print(bool(x))
print(bool(y))

#Most values are True except empty ones 

bool(56)
bool("Shayla")
bool([ 1 , 2 , 3 ])

bool(0)
bool([])
bool("")
bool({})

#

class myclass():
    def _len_(self):
        return 0 
myobj = myclass()
print(bool(myobj))

#boolean functions
def myFunction():
    return True 

print(myFunction())
if myFunction():
    print("YES!")
else : 
    print("NO!")

#to check the value 
v = 34 
print(isinstance(v , int))
