name_set = { "Kate" , "Nastya" , "Andrey"}
print(name_set)

myset = { 1, 2, 3, 4, True , "cherry"}
print(myset)

print(len(name_set))

oddset = set(( 1, 5, 7, 9, 1))
print(oddset)

print(type(myset))

#

for i in oddset : 
    print(i)

print( 2 in oddset)

print( 2 not in myset )

#

evenset = { 2, 4, 6, 8}
evenset.add(10)
print(evenset)

ilove = {"I" , "love" , "my" , "mom"}
yeah = {"so", "much"}

ilove.update(yeah) 
print(ilove)

yourset = {100, 456, 303, 230 }
lists = [390, 1]
yourset.update(lists)
print(yourset)

#remove 
yourset = {100, 456, 303, 230 }
yourset.remove(100)
print(yourset)

yourset = {100, 456, 303, 230 }
yourset.discard(100)
print(yourset)

yourset = {100, 456, 303, 230 }
yourset.pop(0)
print(yourset)

yourset.clear()
print(yourset)

yourset = {100, 456, 303, 230 }
del yourset

#loops 
myset = { 1, 2, 3, 4, True , "cherry"}

for i in myset : 
    print(i)

