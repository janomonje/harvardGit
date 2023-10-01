"""
Basics

print("Welcome")
name = input("Name: ")
print(f"Hello, {name}")
"""

"""
#Conditions
n = int(input("Number: "))
if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")
"""

"""
#Sequences

#list
name = ["Harry", "Ale", "Max", "Ginny"]
name.append("Drako")
name.sort()
print(name);

#sets
s = set()
s.add(1)
s.add(2)
s.add(3)
print(s)
print(f"The set has {len(s)} elements.")


#tuple
coordinateX = 10.0
corrdinateY = 20.0

coordinate = (10.0, 20.0)
print(coordinate[0])
"""

"""
#Loops
for i in range(1, 10, 2): #start, stop, steps
    print(i)

names = ["Harry", "Ale", "Max", "Ginny"]
for name in names:
    print(name)
"""


"""
#Dictionaries
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
print(houses["Harry"])

houses["Hermione"] = "Gryffindor"
print(houses["Hermione"])
print(houses)
"""

#Functions
import squares #importing the whole module from a different file "squares.square(i)"
from squares import square #importing the single function

for i in range(10):
    print(f"The square of {i} is {squares.square(i)}.")


for i in range(10):
    print(f"The square of {i} is {square(i)}.")






