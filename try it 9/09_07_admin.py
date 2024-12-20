class User:
    def __init__(self, first_name, last_name, age, location, email):
        # Initialize the attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.login_attempts = 0  # Default login_attempts attribute

    def describe_user(self):
        # Method to describe the user
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Email: {self.email}\n")

    def greet_user(self):
        # Method to greet the user
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!\n")

    def increment_login_attempts(self):
        # Method to increment login_attempts by 1
        self.login_attempts += 1

    def reset_login_attempts(self):
        # Method to reset login_attempts to 0
        self.login_attempts = 0


# Define the Admin class, inheriting from User
class Admin(User):
    def __init__(self, first_name, last_name, age, location, email, privileges=None):
        # Initialize the parent class (User)
        super().__init__(first_name, last_name, age, location, email)
        # If no list of privileges is provided, initialize an empty list
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        # Method to display the admin's privileges
        if self.privileges:
            print(f"Privileges of {self.first_name} {self.last_name}:")
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print(f"{self.first_name} {self.last_name} has no privileges.")

# Create an instance of Admin
admin = Admin(
    first_name="Alice", 
    last_name="Johnson", 
    age=40, 
    location="Los Angeles", 
    email="alicejohnson@example.com", 
    privileges=["can add post", "can delete post", "can ban user", "can modify settings"]
)

# Call the show_privileges() method
admin.show_privileges()

# Optionally, call other methods inherited from User class
admin.describe_user()
admin.greet_user()