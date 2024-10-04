favorite_places = {
    "abdu;": ["Paris", "Tokyo", "New York"],
    "williams": ["London", "Berlin"],
    "mikey": ["Sydney"]
}

for name, places in favorite_places.items():
    print(f"{name}'s favorite places are:")
    for place in places:
        print(f" - {place}")
    print()  