toppings = []


while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")

    
    if topping.lower() == 'quit':
        break

   
    toppings.append(topping)
    print(f"I'll add {topping} to your pizza.")


print("\nYour pizza will have the following toppings:")
for topping in toppings:
    print(f"- {topping}")