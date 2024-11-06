
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        # Initialize the attributes
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        # Method to describe the restaurant
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}\n")

    def open_restaurant(self):
        # Method to indicate that the restaurant is open
        print(f"{self.restaurant_name} is now open!\n")

# Create three different instances of the Restaurant class
restaurant_1 = Restaurant("Tasty Bites", "Italian")
restaurant_2 = Restaurant("Sushi World", "Japanese")
restaurant_3 = Restaurant("Burger Haven", "American")

# Call describe_restaurant() for each instance
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()