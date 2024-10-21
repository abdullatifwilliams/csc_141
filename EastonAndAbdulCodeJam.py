import random
import pandas as pd
import matplotlib.pyplot as plt

def generate_superhero_name(num_syllables=3):
    syllables = ['mal', 'kor', 'grim', 'vox', 'dorn', 'tarr', 'vul', 'zer', 'drak', 'mord', 'bhaal', 'rex', 'lux', 'ferr', 'krak']
    prefixes = ['Lord', 'Inquisitor', 'Archon', 'Warlord', 'Primarch', 'Iron', 'Imperator']
    suffixes = ['The Crusader', 'The Reaper', 'The Destroyer', 'The Emperors Champion', 'The Ascendant', 'The Executor', 'The Annihilator', 'The Herald']
    name_core = ''.join(random.choice(syllables) for _ in range(2))
    hero_name = random.choice(prefixes) + " " + name_core.capitalize() + " " + random.choice(suffixes)
    return hero_name

def generate_superhero_data(num_superheroes):
    """Generate random data for superheroes."""
    superhero_data = []
    for _ in range(num_superheroes):
        name = generate_superhero_name(num_syllables=3)
        strength = random.randint(1, 8)
        agility = random.randint(1, 8)
        intelligence = random.randint(1, 8)
        superhero_data.append((name, strength, agility, intelligence))
    return superhero_data

def save_data_to_csv(data, filename='superheroes.csv'):
    """Save superhero data to a CSV file."""
    df = pd.DataFrame(data, columns=['Superhero Name', 'Strength', 'Agility', 'Intelligence'])
    df.to_csv(filename, index=False)
    print(f'Superhero data saved to {filename}.')

def visualize_data(data):
    """Visualize superhero attributes using a bar chart."""
    df = pd.DataFrame(data, columns=['Superhero Name', 'Strength', 'Agility', 'Intelligence'])
    df.set_index('Superhero Name', inplace=True)
    df.plot(kind='bar', figsize=(12, 6))
    plt.title('Superhero Attributes')
    plt.ylabel('Attribute Value')
    plt.xlabel('Superhero Name')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()


def superhero_fight(num_superheroes, superhero_data):
    # This picks which superheroes will fight
    hero_1 = int(input(f"Please pick which hero you want to fight (1 - {num_superheroes}): "))
    hero_2 = int(input(f"Please pick which hero you want to fight (1 - {num_superheroes}): "))
    
    # Validate the input
    if hero_1 < 1 or hero_1 > num_superheroes or hero_2 < 1 or hero_2 > num_superheroes:
        print("Invalid hero selection.")
        return

    # Fetching superhero data
    superhero_1 = superhero_data[hero_1 - 1]
    superhero_2 = superhero_data[hero_2 - 1]
    
    strength_1 = superhero_1[1]
    agility_1 = superhero_1[2]
    intelligence_1 = superhero_1[3]
    total_1 = strength_1 + agility_1 + intelligence_1

    strength_2 = superhero_2[1]
    agility_2 = superhero_2[2]
    intelligence_2 = superhero_2[3]
    total_2 = strength_2 + agility_2 + intelligence_2
    
    hero_1_points = 0
    hero_2_points = 0

    # Comparison logic
    if strength_1 > strength_2:
        hero_1_points += 1
    elif strength_1 < strength_2:
        hero_2_points += 1

    if agility_1 > agility_2:
        hero_1_points += 1
    elif agility_1 < agility_2:
        hero_2_points += 1

    if intelligence_1 > intelligence_2:
        hero_1_points += 1
    elif intelligence_1 < intelligence_2:
        hero_2_points += 1

    # Determine the winner
    if hero_1_points > hero_2_points:
        print(f"{superhero_1[0]} won the fight!")
    elif hero_1_points < hero_2_points:
        print(f"{superhero_2[0]} won the fight!")
    else:  # Points are equal
        if total_1 > total_2:
            print(f"{superhero_1[0]} won the fight!")
        elif total_1 < total_2:
            print(f"{superhero_2[0]} won the fight!")
        else:
            print(f"It is a tie between {superhero_1[0]} and {superhero_2[0]}!")

def main():
    print("Welcome to the Superhero Values Generator!")
    num_superheroes = int(input("How many superheroes would you like to create? "))
    
    superhero_data = generate_superhero_data(num_superheroes)
    print("Generated Superhero Data:")
    for hero in superhero_data:
        print(f"{hero[0]}: Strength = {hero[1]}, Agility = {hero[2]}, Intelligence = {hero[3]}")
    
    fight = input("Would you like to choose two superheroes to fight? (y/n) ")
    if fight.lower() == 'y':
        superhero_fight(num_superheroes, superhero_data)

    save_option = input("Would you like to download the superhero data as a CSV file? (y/n) ")
    if save_option.lower() == 'y':
        save_data_to_csv(superhero_data)

    visualize_option = input("Would you like to visualize the superhero attributes? (y/n) ")
    if visualize_option.lower() == 'y':
        visualize_data(superhero_data)

    print("Thank you for using the Superhero Values Generator!")

if __name__ == '__main__':
    main() 
