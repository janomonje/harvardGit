people = [
    {"name" : "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slythering"}
]
"""
#same as lambda
def f(person):
    return person["name"]
"""

people.sort(key=lambda person: person["name"]) #complete function that takes a person and returns his name

print(people)