def make_sandwich(*items):
    print("\nYour sandwich will include the following ingredients:")
    for item in items:
        print(f"- {item}")

# Call the function three times with different numbers of arguments
make_sandwich("ham", "cheese", "lettuce")
make_sandwich("turkey", "tomato")
make_sandwich("peanut butter", "jelly", "banana", "honey")