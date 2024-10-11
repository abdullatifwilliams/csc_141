while True:
    age_input = input("Please enter your age (or type 'quit' to exit): ")

    
    if age_input.lower() == 'quit':
        print("Thank you for using the ticket pricing program. Goodbye!")
        break

 
    try:
        age = int(age_input)
    except ValueError:
        print("Please enter a valid age or 'quit'.")
     
    if age < 3:
        ticket_price = 0
        print("Your ticket is free!")
    elif 3 <= age <= 12:
        ticket_price = 10
        print("Your ticket costs $10.")
    else:  
        ticket_price = 15
        print("Your ticket costs $15.")