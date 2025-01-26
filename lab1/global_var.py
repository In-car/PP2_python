x = "pizza"

def Ilike():
    print("I like " + x )
Ilike()
#
#
y = "cool"
def func(): 
    y = "awesome"
    print("Symbat is " + y)

func()

print("Symbat is " + y )
#
#
def ilove(): 
    global z 
    z = "Albert"

ilove()

print("I love " + z )
#
#
n = "good"
def score():
    global n 
    n = "awesome"

score()

print("You did " + n )