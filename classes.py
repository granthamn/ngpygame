class myClass:
    """Simple Class Example"""

    def __init__(self):
        self.i = 1
    def f(self):
        return('ello')

# Instantiate class and print members
myObj=myClass()
print(myObj.i)
print(myObj.f())


class initExample:
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i = imagpart
    def getPart(self):
        return self.r
# Instantiate class with parameters and print members
myIE=initExample(3.0,1.4)
print(myIE.r, myIE.i)
myIE.madeUpVar = "Ello I'm a new variable"
print(myIE.madeUpVar)
print('You can set a variable to a method object and call it later or use it in a command')
IER=myIE.getPart
print(IER())

print('Generally speaking, instance vars are unique to instance and class vars are for all instances')
#Dog class showing instance and class vars
class Dog:
    species='canine'
    def __init__(self, name):
        self.name = name

d1 = Dog('Bruce')
d2 = Dog('Harry')
d3 = Dog('Dunston')

print('Dog 1 is a', d1.species)
print('Dog 2 is a', d2.species)
print('Dog 3 is a', d3.species)
print('Dog 1 is called', d1.name)
print('Dog 2 is called', d2.name)
print('Dog 3 is called', d3.name)

print('--------------------------------')
print('Need to be careful with class vars as can have unintended consequences')
print('For instance a list or other mutable construct')

class cDog:
    tricks=[]
    def __init__(self, name):
        self.name = name
    def add_trick(self,trick):
        self.tricks.append(trick)

d = cDog('Burt')
e = cDog('Yannick')
d.add_trick('Roll over') # Burt knows Roll Over
e.add_trick('Beg') # Yannick knows Beg
print(d.name,'knows the following tricks',d.tricks) # This isn't what we expect
# It shows Burt knowing 2 tricks when we only added one

class cDog2:

    def __init__(self, name):
        self.name = name
        self.tricks = []
    def add_trick(self,trick):
        self.tricks.append(trick)

g = cDog2('Hal')
h = cDog2('Victor')
g.add_trick('Beg')
h.add_trick('Roll over')
h.add_trick('Sit')
for trick in g.tricks:
    print(g.name,'knows',trick)
for trick in h.tricks:
    print(h.name,'knows',trick)




