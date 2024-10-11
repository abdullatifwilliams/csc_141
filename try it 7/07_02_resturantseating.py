dinner_group_size = int(input("How many people are in your dinner group? "))

# Check if the group size is greater than 8
if dinner_group_size > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready!")