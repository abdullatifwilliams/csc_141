# Open the file and read the entire content at once
with open('learning_python.txt', 'r') as file:
    content = file.read()
    print("Contents read all at once:")
    print(content)

# Open the file and store lines in a list, then loop over them
with open('learning_python.txt', 'r') as file:
    lines = file.readlines()
    print("\nContents read line by line:")
    for line in lines:
        print(line.strip())  # Use strip() to remove the newline character