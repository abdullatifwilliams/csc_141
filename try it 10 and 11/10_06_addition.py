# Prompt the user for two numbers
try:
    # Get the first number from the user and convert it to an integer
    num1 = int(input("Enter the first number: "))
    
    # Get the second number from the user and convert it to an integer
    num2 = int(input("Enter the second number: "))
    
    # Add the numbers together and print the result
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}.")
    
except ValueError:
    # Handle the case where the user enters something that's not a number
    print("Oops! That was not a valid number. Please enter only numerical values.")
