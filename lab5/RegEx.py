import re 

txt = """a_b
HelloWorld
Science
aanythingb
lower_case_letters
Lower_Bait
RegexMatch
upperCaseLetters
RegexChallenge
regexTestCase
PythonRegexFun
lower_case_example
Data
Comma, space and dot.
regex_match
regexTestCase
Match
data_science
regex_match
SplitAtCaps
convertThisExample
CodeParserExample
RegexTestCase
abbbbbbb
a123b
aabb
helloWorld
SplitAtCaps
Test this.out, please.
MyVariableName
snake_case_example
Regex is fun, right?
convertThisExample
Regex
hello_world
H3ll0
regex_match
T3st1ng
abbbba
abbb
Python,Regex
regexTestCase
a_b
FooBar42
ThisIsATest
C0d3Br34k3r
regex_match
alphabetb
regexTestCase
secure123
L33tSpeak
python_code
data_science
helloWorld
RegexChallenge
snake_case_conversion
"""

#1 
x = re.findall("a[b]*b" , txt)
print(x)

#2 
x = re.findall("a[b]{2}b|a[b]{1}b", txt)
print(x)

#3
x = re.findall("[a-z]+[_][a-z]*" , txt )
print(x)

#4
x = re.findall("[A-Z][a-z]+" , txt)
print(x)

#5
x = re.findall("a.*b" , txt)
print(x)

#6 
x = re.sub("[ ,.]" , ":" , txt)
print(x)

#7 
x = re.sub("_([a-z])", " \\1", txt).title().replace(" ", "")
print(x)

#8 
x = re.split(".?[A-Z]" , txt)
print(x)

#9
x = re.sub("([a-z])([A-Z])", "\\1 \\2", txt)
print(x)

#10
x = re.sub("([a-z])([A-Z])", "\\1 \\2", txt).lower