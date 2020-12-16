# Data structures

myList=[]
name="Neil"
surName="Grantham"
middleName="Patrick"
myList.append(name)
myList.append(surName)
myList.insert(1,middleName)
print(myList)

colours=["Blue","Purple","Green","Pink","Yellow","Red","Brown"]
print("Colours:", colours)
colours.insert(2,"Orange")
print("added missing colour:", colours)
rainbow=colours
rainbow.reverse()
rainbow.pop(0)
print("Rainbow:", rainbow)
for colour in rainbow:
    if colour != "Blue":
        print(colour, "and")
    else:
        print(colour, "I can sing a rainbow")

print("A list comprehension consists of square brackets with an expression followed by a for loop")
threetimes = [x*3 for x in range(10)]
print(threetimes)

print("List comprehensions can contain complex expressions and nested functions")
from math import pi
pirounded=[str (round(pi,i)) for i in range(1,6)]
print(pirounded)
print("Initial expression can be another comprehension")
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    ]
print(matrix)
print("Get columns from matrix")
matcols=[[row[i] for row in matrix] for i in range(4)]
print(matcols)
print("Tuples are immutable lists of values")
tup=12345,65323,'hi!'
print(tup[0])
print(tup)
print("You can nest tuples")
tup2=tup, (1,3,5,7,9)
print(tup2)
print("You can add mutable objects to immutable tuple - i.e. add list to tuple")
print("------------")

print("A set is an unordered colletion of items with no dupes")
fruitSet = {'apple', 'orange', 'banana', 'pear', 'grape'}
print(fruitSet)
print('orange' in fruitSet)
print('tomato' in fruitSet)
print('Can use set to determine unique entries in a structure or string')
ngSet = set('neilpatrickgrantham')
print('Set of letters in Neil Patrick Grantham', ngSet)
dgSet = set('dianeelizabethgrantham')
print('Set of letters in Diane Elizabeth Grantham', dgSet)
print('Can  use operators to compare two sets')
ngOnlySet=ngSet-dgSet
print('Letters only in NG not DG:',ngOnlySet)
dgOnlySet=dgSet-ngSet
print('Letters only in DG set not NG:',dgOnlySet)
eitherGSet=ngSet | dgSet
print('Total unique set of letters in both names:',eitherGSet)
bothGSet=ngSet & dgSet
print('Unique letters in both names:',bothGSet)

print("dict is a key-value pair structure")
tel={'jack' : 4099, 'john': 4844}
print(tel)
tel['neil'] = 4842
print(tel)
print(tel['neil'])
del tel['john']
print(tel)
tel['colt'] = 3543
print(tel)
print(list(tel))
print(sorted(tel))
print('vic' in tel)
print('neil' in tel)
sides=dict(circle=1,triangle=3,square=4,hexagon=6,pent=5)
print(sides)
print("Different ways to iterate over a dictionary")
for i, j in sides.items():
    print("A", i, "has", j, "sides")

for i,j in enumerate(sides):
    print(i,j)

for i  in sorted(set(sides)):
    print(i)

print("Can iterate over two or more sequences using zip function")
questions = ['Name', 'Favourite Movie', 'Tastiest Food']
answers = ['Neil', 'The Terminator', 'Pizza']
for q, a in zip (questions, answers):
    print('What is your {0}? It is {1}.' .format(q,a))
    

    


        
