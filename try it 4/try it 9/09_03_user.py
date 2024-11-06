class User:
    def __init__(self, first_name, last_name, age, location, email):
        # Initialize the attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email

    def describe_user(self):
        # Method to describe the user
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Email: {self.email}\n")

    def greet_user(self):
        # Method to greet the user
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!\n")

# Create several instances representing different users
user_1 = User("John", "Doe", 30, "New York", "johndoe@example.com")
user_2 = User("Jane", "Smith", 25, "Los Angeles", "janesmith@example.com")
user_3 = User("Emily", "Johnson", 35, "Chicago", "emilyjohnson@example.com")

# Call describe_user() and greet_user() for each user
user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()