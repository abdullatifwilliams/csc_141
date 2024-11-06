class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        # Initialize the restaurant's name and cuisine type
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        # Method to describe the restaurant
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        # Method to indicate that the restaurant is open
        print(f"{self.restaurant_name} is now open!")