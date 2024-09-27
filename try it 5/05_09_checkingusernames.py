current_users = ['abdul', 'chris', 'mike', 'dev', 'Eve']

new_users = ['bron', 'bob', 'jier', 'keith', 'drae']

current_users_lower = [user.lower() for user in current_users]


for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The username '{new_user}' has already been used. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")