sandwich_orders = [
    'tuna sandwich',
    'ham sandwich',
    'pastrami sandwich',
    'pastrami sandwich',
    'vegetable sandwich',
    'club sandwich',
    'pastrami sandwich',
    'BLT sandwich'
]


print("The deli has run out of pastrami.")


while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')


finished_sandwiches = []


for sandwich in sandwich_orders:
    print(f"I made your {sandwich}.")
    finished_sandwiches.append(sandwich)  


print("\nAll sandwiches made:")
for finished in finished_sandwiches:
    print(f"- {finished}")