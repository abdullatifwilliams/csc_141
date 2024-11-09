# Prompt the user for their name
name = input("abdullatif: ")

# Open the file in write mode and write the name to the file
with open('guest.txt', 'w') as file:
    file.write(name)

print(f"Hello, {name}! Your name has been written to 'guest.txt'.")