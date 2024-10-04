rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Yangtze": "China"
}


print("Rivers and the countries they run through:")
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

print("\nNames of the rivers:")

for river in rivers.keys():
    print(river)

print("\nNames of the countries:")

for country in rivers.values():
    print(country)