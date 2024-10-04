person_1={"first_name": "micheal",
    "last_name": "Stewart",
    "age": 28,
    "city": "New York"
}

person_2 = {
    "first_name": "abdu;",
    "last_name": "william",
    "age": 35,
    "city": "Los Angeles"
}

person_3 = {
    "first_name": "Charlie",
    "last_name": "Brown",
    "age": 22,
    "city": "Chicago"
}

people = [person_1, person_2, person_3]


for person in people:
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    