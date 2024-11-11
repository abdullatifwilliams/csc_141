# Function to ask for user information and store it in a dictionary
def remember_user():
    # Prompt the user for information
    name = input("What is your name? ")
    favorite_color = input("What is your favorite color? ")
    hobby = input("What is your hobby? ")

    # Store the information in a dictionary
    user_info = {
        'name': name,
        'favorite_color': favorite_color,
        'hobby': hobby
    }

    # Write the dictionary to a file using json.dumps()
    with open('user_info.json', 'w') as file:
        json.dump(user_info, file)

    print("\nYour information has been saved!")

# Function to read the user information from the file and display it
def display_user_info():
    # Check if the file exists
    if os.path.exists('user_info.json'):
        # Read the dictionary from the file using json.loads()
        with open('user_info.json', 'r') as file:
            user_info = json.load(file)

        # Display a summary of the user information
        print("\nHere is what I remember about you:")
        print(f"Name: {user_info['name']}")
        print(f"Favorite Color: {user_info['favorite_color']}")
        print(f"Hobby: {user_info['hobby']}")
    else:
        print("\nNo information found. Please enter your details first.")

# Main program flow
def main():
    # Check if we have stored user info, if so display it
    display_user_info()

    # If the file doesn't exist (first time running), ask for details
    if not os.path.exists('user_info.json'):
        remember_user()

    # After saving the user info, display it again to confirm it's saved
    display_user_info()

# Run the program
main()
