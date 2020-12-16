# General Basics
a,b=0,1
while a < 15:
    print(a, end=',')
    a,b=b,a+b 
print('')
x=int(input("Enter a number: "))
if x < 0:
    print("It's Negative")
elif x == 0:
    print ("It's zero")
else:
    print("It's positive")
print('')ords=['cat','door','window','television']
for w in words:
    print(w, "has", len(w), "letters")
print("List has", len(words), "words")
print("Strings and things....")
word="Banjo"
initial=word[0]
word2="Kazooie"
word3=word+" "+word2
print(word3)
for w in word3:
    print(w)
print("And Backwards..")
for i in range(len(word3)-1,-1,-1):
    print(word3[i])
print("Five times table...")
fives=range(0,60,5)
print("You can't just print a range")
print(fives)
print("But you can iterate over them")
for five in fives:
    print(five)
print("And can use functions on them")
print(sum(fives))
print("And can get a list from a range")
listoffives=list(fives)
print(listoffives)
print("break breaks out of loop")
print("Can use else with a for loop")
print("It executes when range of for loop is exhausted")

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, "equals", x, "*", n//x)
            break
    else:
        print(n, "is a prime number")

print("continue statement skips to next iteration of a loop")
for num in range(1,10):
    if num % 2 == 0:
        print(num, "is an even number")
        continue
    print(num, "is an odd number")
