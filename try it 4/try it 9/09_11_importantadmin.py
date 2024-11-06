class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        if self.privileges:
            print("Admin Privileges:")
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("This admin has no privileges.")

# Define the User class
class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# Define the Admin class, inheriting from User
class Admin(User):
    def __init__(self, first_name, last_name, age, location, email, privileges=None):
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = Privileges(privileges)