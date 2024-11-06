class Battery:
    def __init__(self, battery_size=60):
        self.battery_size = battery_size  # Default battery size is 60

    def get_range(self):
        # Return range based on the battery size
        if self.battery_size == 60:
            range = 180  # Assume range is 180 miles for a 60 kWh battery
        elif self.battery_size == 65:
            range = 220  # Assume range is 220 miles for a 65 kWh battery
        else:
            range = 0
        return range

    def upgrade_battery(self):
        # Check if the battery size is already 65; if not, upgrade it
        if self.battery_size != 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh.")
        else:
            print("Battery is already at 65 kWh. No upgrade needed.")

# Define the ElectricCar class
class ElectricCar:
    def __init__(self, make, model, year):
        # Initialize the attributes
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()  # Default battery size is 60

    def get_car_info(self):
        # Return basic information about the car
        return f"{self.year} {self.make} {self.model}"

# Create an electric car with a default battery
my_car = ElectricCar("Tesla", "Model S", 2023)

# Display car info and range with the default battery size
print(f"Car Info: {my_car.get_car_info()}")
print(f"Range with default battery (60 kWh): {my_car.battery.get_range()} miles")

# Upgrade the battery to 65 kWh
my_car.battery.upgrade_battery()

# Display the range after upgrading the battery
print(f"Range after upgrading battery (65 kWh): {my_car.battery.get_range()} miles")