attempts = 0
max_attempts = 5 
while attempts < max_attempts:
    age_input = input("Please enter your age (or type 'quit' to exit): ")

   
    if age_input.lower() == 'quit':
        print("Thank you for using the ticket pricing program. Goodbye!")
        break

   
    try:
        age = int(age_input)
    except ValueError:
        print("Please enter a valid age or 'quit'.")
        continue 

   
    if age < 3:
        print("Your ticket is free!")
    elif 3 <= age <= 12:
        print("Your ticket costs $10.")
    else: 
        print("Your ticket costs $15.")

    
    attempts += 1

if attempts == max_attempts:
    print("You've reached the maximum number of attempts. Goodbye!")