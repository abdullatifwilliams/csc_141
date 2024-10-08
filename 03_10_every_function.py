cities = ["New York", "Tokyo", "Paris", "London", "Sydney"]

cities.append("Berlin")
print("After append:", cities)

cities.insert(2, "Dubai")
print("After insert:", cities)


cities.remove("Sydney")
print("After remove:", cities)


popped_city = cities.pop(1)
print("After pop:", cities)
print("Popped city:", popped_city)


cities.sort()
print("After sort:", cities)

cities.reverse()
print("After reverse:", cities)


print("City at index 2:", cities[2])

cities_slice = cities[1:4]
print("Slice of list:", cities_slice)

city_to_check = "Paris"
print(f"Is {city_to_check} in the list? {'Yes' if city_to_check in cities else 'No'}")

cities.clear()
print("After clear:", cities)
