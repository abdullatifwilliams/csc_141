# Function to check if the favorite number is already stored
def get_favorite_number():
    # Check if the file exists
    if os.path.exists('favorite_number.json'):
        # If the file exists, read the number from the file
        with open('favorite_number.json', 'r') as file:
            favorite_number = json.load(file)
        print(f"I know your favorite number! It's {favorite_number}.")
    else:
        # If the file doesn't exist, ask the user for their favorite number and store it
        favorite_number = input("What's your favorite number? ")

        # Ensure the input is a valid number (integer)
        while not favorite_number.isdigit():
            print("Please enter a valid number.")
            favorite_number = input("What's your favorite number? ")

        # Convert the favorite number to an integer
        favorite_number = int(favorite_number)

        # Store the favorite number in a file using json.dump
        with open('favorite_number.json', 'w') as file:
            json.dump(favorite_number, file)

        print("Your favorite number has been saved!")

# Call the function to check or store the favorite number
get_favorite_number()