# Start a while loop to continuously prompt the user for input
while True:
    try:
        # Prompt the user for the first number
        num1 = int(input("Enter the first number: "))
        
        # Prompt the user for the second number
        num2 = int(input("Enter the second number: "))
        
        # Calculate the sum of the numbers
        result = num1 + num2
        
        # Print the result
        print(f"The sum of {num1} and {num2} is {result}.")
        
        # If the operation is successful, break the loop and exit
        break
    
    except ValueError:
        # Catch the ValueError if input is not a valid integer
        print("Oops! That was not a valid number. Please enter only numerical values.")