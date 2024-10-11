sandwich_orders = [
    'tuna sandwich',
    'ham sandwich',
    'vegetable sandwich',
    'club sandwich',
    'BLT sandwich'
]

finished_sandwiches = []


for sandwich in sandwich_orders:
    print(f"I made your {sandwich}.")
    finished_sandwiches.append(sandwich) 

print("\nAll sandwiches made:")
for finished in finished_sandwiches:
    print(f"- {finished}")