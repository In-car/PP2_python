#1

numbers = [1, 2, 3, 4, 5, 6 ]
def multi(x):
    begin = 1
    for num in x:
        begin *= num
    return begin

print(multi(numbers))

#2

x = input("Write a sentence : ")
def count(s):
    upper = sum(c.isupper() for c in s)
    lower = sum(c.islower() for c in s)
    return upper, lower

print(count(x))

#3
itis = input("Write a word that is a polidrome : ") 
isnot = input("Write a word that is not a polidrome : ") 
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome(itis))
print(is_palindrome(isnot))

#4

import time
import math

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)
    print(f"Square root of {number} after {delay} milliseconds is {math.sqrt(number)}")

delayed_sqrt(25100, 2123)

#5

def all_true(tup):
    return all(tup)

print(all_true((True, True, True)))
print(all_true((True, False, True)))