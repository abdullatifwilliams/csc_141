import random

# Define the Die class
class Die:
    def __init__(self, sides=6):
        # Initialize the die with a specified number of sides (default is 6)
        self.sides = sides

    def roll_die(self):
        # Return a random number between 1 and the number of sides
        return random.randint(1, self.sides)

# Create a 6-sided die
six_sided_die = Die(6)

# Roll the 6-sided die 10 times and print the results
print("Rolling a 6-sided die 10 times:")
for _ in range(10):
    print(six_sided_die.roll_die())

# Create a 10-sided die
ten_sided_die = Die(10)

# Roll the 10-sided die 10 times and print the results
print("\nRolling a 10-sided die 10 times:")
for _ in range(10):
    print(ten_sided_die.roll_die())

# Create a 20-sided die
twenty_sided_die = Die(20)

# Roll the 20-sided die 10 times and print the results
print("\nRolling a 20-sided die 10 times:")
for _ in range(10):
    print(twenty_sided_die.roll_die())