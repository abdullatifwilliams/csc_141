def describe_city(city, country="Iceland"):
    print(f"{city} is in {country}.")

# Call the function for three different cities
describe_city("Reykjavik")  # Default country
describe_city("Oslo", "Norway")  # Different country
describe_city("Copenhagen")  # Default country