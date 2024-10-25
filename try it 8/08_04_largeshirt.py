def make_shirt(size="Large", message="I love Python"):
    print(f"You ordered a {size} shirt with the message: '{message}'.")

# Call the function to make a large shirt with the default message
make_shirt()

# Call the function to make a medium shirt with the default message
make_shirt(size="Medium")

# Call the function to make a small shirt with a different message
make_shirt(size="Small", message="Coding is Fun!")
