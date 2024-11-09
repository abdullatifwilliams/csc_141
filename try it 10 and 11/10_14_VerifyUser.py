# Function to ask for a new username and save it
def get_new_username():
    username = input("What's your username? ")
    # Save the new username to the file
    with open('username.json', 'w') as file:
        json.dump({'username': username}, file)
    print(f"Your username has been updated to {username}.")
    return username

# Function to greet the user or ask for a new username if necessary
def greet_user():
    # Check if the username file exists
    if os.path.exists('username.json'):
        # Load the stored username
        with open('username.json', 'r') as file:
            user_data = json.load(file)
            stored_username = user_data.get('username')

        # Ask the user if the username is correct
        username_check = input(f"Is your username '{stored_username}'? (yes/no): ").lower()
        
        if username_check == 'yes':
            print(f"Welcome back, {stored_username}!")
        else:
            # If the username is incorrect, ask for a new username
            stored_username = get_new_username()
            print(f"Welcome, {stored_username}!")
    else:
        # If no username is stored, ask for a new username
        stored_username = get_new_username()
        print(f"Welcome, {stored_username}!")

# Main program flow
def main():
    greet_user()

# Run the program
main()