cities = {
    "New York": {
        "country": "USA",
        "population": 8419600,
        "fact": "New York City is known as the Big Apple."
    },
    "Tokyo": {
        "country": "Japan",
        "population": 13929286,
        "fact": "Tokyo is the most populous city in the world."
    },
    "Paris": {
        "country": "France",
        "population": 2140526,
        "fact": "Paris is known for the Eiffel Tower and its art museums."
    }
}


for city, info in cities.items():
    print(f"{city}:")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}\n")
