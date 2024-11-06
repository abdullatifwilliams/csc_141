class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        # Initialize the attributes
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Add the number_served attribute with a default value of 0

    def describe_restaurant(self):
        # Method to describe the restaurant
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        # Method to indicate that the restaurant is open
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        # Method to set the number of customers served
        self.number_served = number

    def increment_number_served(self, number):
        # Method to increment the number of customers served
        self.number_served += number

# Create an instance of the Restaurant class
restaurant = Restaurant("Tasty Bites", "Italian")

# Print the number of customers served (initial value)
print(f"{restaurant.restaurant_name} has served {restaurant.number_served} customers.")

# Change the number of customers served
restaurant.set_number_served(50)
print(f"After an update, {restaurant.restaurant_name} has served {restaurant.number_served} customers.")

# Increment the number of customers served
restaurant.increment_number_served(20)
print(f"After serving more customers, {restaurant.restaurant_name} has served {restaurant.number_served} customers.")