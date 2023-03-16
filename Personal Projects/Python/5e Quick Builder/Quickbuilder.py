import random
import os
import time

start_time = time.time()

# Defining needed items

# D20


def d20():
    return random.randint(1, 20)


# dice rolls
dice_rolls = []

# ability scores
ability_scores = {}
ability1 = {}
ability2 = {}

# Ask for player name
player_name = (input("What is your name? "))

# Arrays

# classes
classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk',
           'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

# races
races = ['Dwarf', 'Elf', 'Halfling', 'Human', 'Gnome', 'Half-Elf',
         'Half-Orc', 'Tiefling']
# Abilities

abilities = {
    "barbarian": ["Strength", "Constitution"],
    "bard": ["Charisma", "Dexterity"],
    "cleric": ["Wisdom", "Constitution"],
    "druid": ["Wisdom", "Constitution"],
    "fighter": ["Strength", "Constitution"],
    "monk": ["Dexterity", "Wisdom"],
    "paladin": ["Strength", "Charisma"],
    "ranger": ["Dexterity", "Wisdom"],
    "rogue": ["Dexterity", "Charisma"],
    "sorcerer": ["Charisma", "Constitution"],
    "warlock": ["Charisma", "Constitution"],
    "wizard": ["Intelligence", "Constitution"]
}

# Create a dictionary to store the names for each race
names = {
    "Dwarf": ["Bofur", "Dwalin", "Fili", "Gloin", "Kili", "Nori", "Thorin"],
    "Elf": ["Ara", "Cadeo", "Enara", "Lirien", "Myrin", "Sariel", "Thia"],
    "Halfling": ["Alton", "Cade", "Evan", "Kipp", "Oliver", "Perrin", "Toby"],
    "Human": ["Alex", "Chris", "Jamie", "Jordan", "Riley", "Taylor", "Casey"],
    "Gnome": ["Bimpnottin", "Glimfeather", "Fibblestib", "Jebeddo", "Namfoodle", "Raulnor", "Zook"],
    "Half-Elf": ["Adran", "Aelar", "Erevan", "Galinndan", "Rolen", "Thamior", "Varis"],
    "Half-Orc": ["Dench", "Feng", "Gell", "Henk", "Holg", "Imsh", "Keth"],
    "Tiefling": ["Akmenos", "Amnon", "Barakas", "Damakos", "Ekemon", "Iados", "Kairon"]
}

class_desc = [
    "Barbarian: A fierce warrior who relies on primal instincts and rage in battle.",
    "Bard: A versatile performer who uses music, storytelling, and magic to inspire and manipulate others.",
    "Cleric: A divine spellcaster who channels the power of the gods to heal and protect allies and smite enemies.",
    "Druid: A spellcaster who channels the power of nature to cast spells and transform into animals.",
    "Fighter: A skilled warrior who relies on strength and skill in combat.",
    "Monk: A disciplined warrior who combines martial arts and meditation to achieve extraordinary physical and mental feats.",
    "Paladin: A holy warrior who combines martial prowess with divine magic to serve a righteous cause.",
    "Ranger: A versatile warrior who specializes in archery and tracking enemies through the wilderness.",
    "Rogue: A cunning adventurer who excels at deception and trickery.",
    "Sorcerer: A spellcaster who draws upon innate magical power to cast spells.",
    "Warlock: A spellcaster who makes a pact with a powerful being for magical power in exchange for service or sacrifice.",
    "Wizard: A master of the arcane arts who casts spells and specializes in manipulating the fundamental forces of reality."
]


while True:
    # Prompt the user to select a D&D class or get more info
    print(f"\nPlease select a D&D class, {player_name}, or enter 'i' to get more information about a class: ")
    for i, c in enumerate(classes, start=1):
        print(f"{i}. {c}")
    class_choice = input("\nEnter the number of your chosen class, or 'i' for more information: \n")

    # If the user entered 'i', prompt them for a class number and print the description
    if class_choice.lower() == 'i':
        class_num = input("\nEnter the number of the class you'd like more information about: \n")
        if class_num.isdigit() and int(class_num) in range(1, len(class_desc)+1):
            print(class_desc[int(class_num)-1])
        else:
            print("Invalid input. Please try again and enter the number of the class you'd like more information about.")
    # If the user entered a valid class number, print their selection
    elif class_choice.isdigit() and int(class_choice) in range(1, len(classes)+1):
        print(f"\nYou have chosen the {classes[int(class_choice)-1]} class.")
        break
    else:
        print("Invalid input. Please try again and enter the number of your chosen class or 'i' for more information.\n")


while True:
    # Prompt the user to select a D&D race
    print(f"Please select a D&D race, {player_name}: \n")
    for i, c in enumerate(races, start=1):
        print(f"{i}. {c}")
    race_choice = input("\nEnter the number of your chosen race: \n")

    # Verify that the user has entered a valid number and print their selection
    if race_choice.isdigit() and int(race_choice) in range(1, len(races)+1):
        print(f"\nYou have chosen the {races[int(race_choice)-1]} race.")
        break
    else:
        print("\nInvalid input. Please try again and enter the number of your chosen race.")

# Prompt the user to select a name or enter their own
print(f"\nPlease select a name for your {races[int(race_choice)-1]} character, or enter your own name: \n")
for i, name in enumerate(names[races[int(race_choice)-1]], start=1):
    print(f"{i}. {name}")
print(f"{len(names[races[int(race_choice)-1]])+1}. Enter your own name")

name_choice = input("\nEnter the number of your chosen name: \n")
if name_choice.isdigit() and int(name_choice) in range(1, len(names[races[int(race_choice)-1]])+1):
    character_name = names[races[int(race_choice)-1]][int(name_choice)-1]
    print(f"\nYour character's name is {character_name}")
else:
    character_name = input("\nEnter your own name: \n")
    print(f"\nYour character's name is {character_name}")



print(
f"Greetings mighty hero, {character_name} the {races[int(race_choice)-1]} {classes[int(class_choice)-1]}! They will be played by {player_name}.")


# roll stats
stat_trigger = input("Ready to Roll? Y/N: ")
if stat_trigger.lower() == 'y':
    dice_rolls = []
    for roll in range(6):
        dice_rolls.append(d20())
    print("Dice rolls:", dice_rolls)
else:
    print("Skipping dice roll...")
sorted_rolls = sorted(dice_rolls, reverse=True)

# assigning stats
if str(class_choice) in abilities:
    ability1, ability2 = abilities[class_choice.lower()]
    ability_scores = {ability1: sorted_rolls[0], ability2: sorted_rolls[1]}
    print("Ability scores:", ability_scores)

# exporting the data
file_path = "C:/Users/Brian/Documents/Software Development Portfolio/Personal Projects/Python/5e Quick Builder"
file_name = character_name
file_ext = ".txt"
file_path = os.path.join(
    os.getcwd(), f"{file_name}{file_ext}")

with open(file_path, "w") as file:
    file.write(f"Player:{player_name}\n")
    file.write(f"Player:{character_name}\n")
    file.write(f"Race:{races[int(race_choice)-1]}\n")
    file.write(f"Class:{classes[int(class_choice)-1]}\n")
    file.write(f"Rolls: {sorted_rolls}\n")
    class_name = classes[int(class_choice)-1]

    ability1, ability2 = abilities[class_name.lower()]

    file.write(f"Since you are playing a {class_name}, you should assign your two highest rolls to {ability1} and {ability2}. ")

os.startfile(file_path)

# next steps
# print to correct location
# add formating
# add checksum to prevent non numerical entries