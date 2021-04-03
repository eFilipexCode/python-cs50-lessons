people = [
    {"name": "Harry", "house": "SP"},
    {"name": "Peter", "house": "RJ"},
    {"name": "Marc", "house": "ES"},
]

def f(person):
    return person["name"]

people.sort(key=f)
print(people)

#or 

people.sort(key=lambda person: person["name"])
print(people)
