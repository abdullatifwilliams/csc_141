# Creating a dictionary to store people's favorite numbers
favorite_numbers = {
    "ahmed": 7,
    "charles": 3,
    "jier": 22,
    "mike": 15,
    "Ethan": 42
}

# Printing each person's favorite number
for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is: {number}")