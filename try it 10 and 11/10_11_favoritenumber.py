# Prompt the user for their favorite number
favorite_number = input("What's your favorite number? ")

# Ensure that the input is a valid number (integer)
while not favorite_number.isdigit():
    print("Please enter a valid number.")
    favorite_number = input("What's your favorite number? ")

# Convert the favorite number to an integer
favorite_number = int(favorite_number)

# Store the favorite number in a file using json.dumps
with open('favorite_number.json', 'w') as file:
    json.dump(favorite_number, file)

print("Your favorite number has been saved!")
