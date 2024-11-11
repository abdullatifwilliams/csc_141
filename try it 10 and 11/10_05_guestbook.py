# Open the file in append mode to add new names without overwriting
with open('guest_book.txt', 'a') as file:
    while True:
        # Prompt the user for their name
        name = input("Please enter your name (or type 'quit' to stop): ")

        # Check if the user wants to exit the loop
        if name.lower() == 'quit':
            break

        # Write the name to the file
        file.write(name + '\n')  # Add a new line after each name

        print(f"Thank you, {name}! Your name has been added to the guest book.")
    
print("The guest book has been updated.")
