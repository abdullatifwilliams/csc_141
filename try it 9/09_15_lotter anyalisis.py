mport random

# List containing 10 numbers and 5 letters
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Define my ticket (the combination I want to match)
my_ticket = [5, 8, 1, 'D']

# Counter for how many attempts it takes to win
attempts = 0

# Loop until we get a winning ticket
while True:
    attempts += 1
    # Randomly select 4 elements from the lottery pool
    winning_ticket = random.sample(lottery_pool, 4)

    # Check if the selected ticket matches my ticket
    if winning_ticket == my_ticket:
        break  # Exit the loop if we have a match

# Print the result after winning
print(f"Your ticket {my_ticket} matched the winning ticket {winning_ticket} after {attempts} attempts!")