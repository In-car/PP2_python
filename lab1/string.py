print("Hello")
a = "Hello"
print(a)


#multiline string 
b = """I love having conversations , 
because they you can really
get to know the person you are talking."""
print(b)


#position
print(a[1]) 


#loop
for i in "PIZZA" :
    print(i)


#len 
print(len(b)) 


#check if 
letter = "love"
print(letter in b) 

#check if NOT
txt = "people"
print(txt in b)

#slicing 
print(b[10:30])

print(b[:25])

print(b[5:])

print(b[-1:-25])


#Upper case 
name = "Inkar"
print(name.upper())


#Lower case 
print(name.lower())

#remove whitespace 
x = "  Lame   "
print(x.strip())

#replace
print(name.replace("a" ,"o"))

#split 
sent = " I love my mom " 
print(sent.split())