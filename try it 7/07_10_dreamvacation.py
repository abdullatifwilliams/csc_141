dream_vacation_responses = []

while True:
    response = input("If you could visit one place in the world, where would you go? (type 'quit' to exit): ")
    
   
    if response.lower() == 'quit':
        break
    
   
    dream_vacation_responses.append(response)
print("\n--- Dream Vacation Poll Results ---")
for response in dream_vacation_responses:
    print(f"- {response}")