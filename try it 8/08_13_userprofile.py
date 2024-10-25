def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Create a profile for yourself
my_profile = build_profile(
    "John", 
    "Doe", 
    age=30, 
    location="New York", 
    favorite_color="Blue"
)

# Print the profile
print(my_profile)