class User:
    def __init__(self, first_name, last_name, age, location, email):
        # Initialize the attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.login_attempts = 0  # Add the login_attempts attribute with a default value of 0

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

# Create an instance of the User class
user = User("John", "Doe", 30, "New York", "johndoe@example.com")

# Call increment_login_attempts() several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Print the current number of login attempts
print(f"{user.first_name} {user.last_name} has attempted to log in {user.login_attempts} times.")

# Call reset_login_attempts() to reset the login attempts
user.reset_login_attempts()

# Print the number of login attempts after reset
print(f"After reset, {user.first_name} {user.last_name} has attempted to log in {user.login_attempts} times.")