#Regular Expression is used to check if a string contains the specified search pattern 
import re 

txt = "The rain in Spain"
x = re.search("^The.*Spain$" , txt)

if x : 
    print("Yes , we have a match!")
else : 
    print("No match")


#findall() returns a list containing all the matches
txt = "the rain in Spain"
x = re.findall("ai" , txt)
print(x)

a = "I live in Kazakhstan"
b = re.findall("Kazakh" , a )
print(b)
#capital letters does matter, if I put "kazakh" the list would be empty 


#search() returns a match object if there is a match anywhere 
text1 = "This is the text with white space"
text2 = "Textwithnowhitecspace"
 
x = re.search("\s" , text1)
print(x.start())
y = re.search("\s" , text2)
print(y)
#if there is no maches it will return NONE


#split() returns a list where the string has been split at each match 
txt = "I love 2 love my mom"
x = re.split("\s" , txt)
print(x)
#as it goes function splits it by white space, we can also split by another atributes 
y = re.split("2" , txt)
print(y)
#we also can split by maxsplit 
#by adding another parameters 
z = re.split("\s" , txt ,1)
print(z)
#which means to split 1 time at white space 


#sub() replaces one or many matches with a string
txt = "The rain in Spain"
x = re.sub("\s" , "|" , txt)
print(x)
#you can also control the number of replacement by the parameter count 
y = re.sub("\s" , "|" , txt , 2)
print(y)
