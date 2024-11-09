def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()  # Read the entire content of the file
            print(contents)
    except FileNotFoundError:
        print(f"Sorry, the file '{filename}' was not found.")

# Try to read 'cats.txt'
print("Contents of cats.txt:")
read_file('cats.txt')

# Try to read 'dogs.txt'
print("\nContents of dogs.txt:")
read_file('dogs.txt')