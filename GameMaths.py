import pygame as pg
import math

class Vector:
    def __init__(self,x, y):
        self.x = float(x)
        self.y = float(y)

    # Vector addition
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Vector subtraction
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # Vector scaling
    def __mul__(self,num):
        return Vector(self.x * num, self.y * num)

    # Vector scaling
    def __truediv__(self, num):
        return Vector( round(self.x / num,6), round(self.y / num,6))


    # Length of a vector
    def length(self):
        return round(math.sqrt(self.x * self.x + self.y * self.y),4)

    def lenSquare(self):
        return (self.x * self.x + self.y * self.y)

    # Make a unit vector from existing vector
    def Normalised(self):
        return self / self.length()

    # Dot Product
    def dotProduct(self,other):
        return self.x * other.x + self.y * other.y

class Point:
    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)

    # Add Vector to get make existing point move
    def AddVector(self, v):
        self.x += v.x
        self.y += v.y

    # Add vector and return a new point
    def AddVectorNewPoint(self, v):
        # Determine new position of x,y by adding a vector
        x = self.x + v.x
        y = self.y + v.y
        return Point(x,y)

    def __sub__(self, other):
        # Subtract one position from another to get a target vector
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x,y)


pg.init()

print("Add vector to point to get new point")
p = Point(1, -1)
print("Point 1: x=", p.x, "Y=", p.y)
v = Vector(2,3)
print("Vector x=", v.x, "Y=", v.y)
print("Adding vector...")
p2 = p.AddVectorNewPoint(v)
print("new Pos:", p2.x, ",", p2.y)

print("Vector to get from point 1 to point 2")
pacPoint = Point(0,-1)
print("Target X=", pacPoint.x, "Target Y =", pacPoint.y)
ghostPoint = Point(1,1)
ghost2Point = Point(2, -1)
print("Orig Point X=", ghostPoint.x, "Orig Point Y=", ghostPoint.y)
targVect = pacPoint - ghostPoint
targ2Vect = pacPoint - ghost2Point

print("Vector to get from Ghost 1 to Pacman: ", targVect.x, targVect.y)
print("Vector to get from Ghost 2 to Pacman", targ2Vect.x, targ2Vect.y)

print("Distance between 2 points (length of Vector from Ghost to Pac)")
print("Length of ghost1 Vector", targVect.length())
print("Distance between 2 points (length of a vector from Ghost 2 to Pac)")
print("Length of ghost2 Vector", targ2Vect.length())


print("Compare 2 vectors to see which is closest to target")
d1 = targVect.lenSquare()
d2 = targ2Vect.lenSquare()
if d1 > d2:
    print("First ghost", d1, " is further away than ", d2)
else:
    print("Second ghost", d2, " is further away than", d1)

print("Scaling vectors - used to speed up or slow down characters")
doubled = targVect * 2
halved = targ2Vect / 2
print("Target vector doubled is ", doubled.x, doubled.y)
print("Target 2 vector halved is ", halved.x, halved.y)


print("Unit Length vectors have a length of 1")
print("Take full length vector and dividing by length of itself")
pacPoint2 = Point(3,4)
inkyPoint = Point(1,2)
v = inkyPoint - pacPoint2
print("Pac to inky unnormalised - X:", v.x, "Y: ", v.y, "Len:" , v.length())

PacUnitVector = v.Normalised()
print("Normalised Pac View Vector: ", PacUnitVector.x, PacUnitVector.y)
print("Normalised Pac View Vector Len: ", PacUnitVector.length())

print("Adding horizontal + vertical vectors to get diagonal vector for movement")
print("Add Xs and Add Ys to get new vector")

pacRight = Vector(4,0)
print("Pac Right ", pacRight.x, pacRight.y)
pacDown = Vector(0,-5)
print("Pac Down ", pacDown.x, pacDown.y)
PacDiagVector = pacRight + pacDown
print("Pac Diag Vector: x:",PacDiagVector.x, "Y: ", PacDiagVector.y)

print("A dot product can be used to determine if two vectors are facing the same direction, or at 90 degrees or opposite")
print("If vectors face same direction, dot product is 1, if opposite, -1, if 90 deg, 0")
attackerPos = Point(3,3)
attackedPos = Point(5,3)
attackedVect = Vector(attackedPos.x, attackedPos.y)
attackVector = attackerPos - attackedPos
unitAttackVector = attackVector.Normalised()
unitAttackedVector = attackedVect.Normalised()
AttackDot = unitAttackVector.dotProduct(unitAttackedVector)
print("Dot product of attacker and attacked is",AttackDot)

