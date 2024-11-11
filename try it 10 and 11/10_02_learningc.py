
with open('learning_python.txt', 'r') as file:
    lines = file.readlines()

# Replace the word "Python" with "C" and print each modified line
for line in lines:
    modified_line = line.replace('Python', 'C')  # Replace 'Python' with 'C'
    print(modified_line.strip())  # Print the modified line without extra newlines
