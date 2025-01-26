a = 7 
b = 4 

if a>b : 
    print("a is greated that b")
elif a<b: print("b is greater that a")
else : 
    print("a and b are equal")

print("YES") if a>b else print("NO") if a<b else print('Equal')

#

x = 10 
y = 12 
z = 4 

if x>y and x>z : 
    print("x is the max")
elif x>y or x>z :
    ("x is not the lowest")

if not x==3 : 
    print("x is not equal to 3")


# 

list = [ 1, 2, 3, 4 ,5 ]
if list[1]%2 == 0 :
    if list[1] == 2 : 
        print("Bingo! it was 2 ")
    else : print("the number is NOT 2 :(")


if 3 in list : 
    pass 