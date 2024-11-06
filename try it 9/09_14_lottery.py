import random

# List containing 10 numbers and 5 letters
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Randomly select 4 elements from the list
winning_ticket = random.sample(lottery_pool, 4)

# Print the winning ticket
print("The winning ticket consists of the following numbers/letters:")
print(winning_ticket)

# Print the message for the winner
print("\nAny ticket matching these 4 numbers/letters wins a prize!")