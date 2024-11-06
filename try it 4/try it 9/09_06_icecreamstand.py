class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        # Initialize the attributes
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default number_served attribute

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