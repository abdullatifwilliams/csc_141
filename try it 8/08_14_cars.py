def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing information about a car."""
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

# Call the function with required information and additional name-value pairs
car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Print the car information
print(car)