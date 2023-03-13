import random
import os
import time


def d20():
    total = 0
    for roll in range(int(input("How many dice are you rolling?: "))):
        total += random.randint(1, 20)
    return total


# Ask for player name
player_name = (input("What is your name? "))

# Arrays

#classes
classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk',
           'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

#races
races = ['Dwarf', 'Elf', 'Halfling', 'Human', 'Gnome', 'Half-Elf',
         'Half-Orc', 'Tiefling']
#Abilities

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


print(f"Please select a D&D class, {player_name}: ")

# Display the list of classes with a corresponding number
for i, c in enumerate(classes, start=1):
    print(f"{i}. {c}")

# Prompt the user to enter a number
class_choice = int(input("Enter the number of your chosen class: "))

# Verify that the user has entered a valid number and print their selection
if class_choice in range(1, len(classes)+1):
   print(f"You have chosen the {classes[class_choice-1]} class. The most important abilities are {', '.join(abilities[classes[class_choice-1].lower()])}")
else:
    print("Invalid input. Please try again and enter the number of your chosen class.")
# Ask for player race



print(f"Please select a D&D Race from the SRD, {player_name}: ")

# Display the list of classes with a corresponding number
for i, c in enumerate(races, start=1):
    print(f"{i}. {c}")

# Prompt the user to enter a number
race_choice = int(input("Enter the number of your chosen race: "))

# Verify that the user has entered a valid number and print their selection
if race_choice in range(1, len(races)+1):
    print(f"You have chosen the {races[race_choice-1]} race.")
else:
    print("Invalid input. Please try again and enter the number of your chosen class.")
# Ask for character name
character_name = (input("What is your hero's name? "))

print(f"Greetings mighty hero, {character_name} the {races[race_choice-1]} {classes[class_choice-1]}! They will be played by {player_name}.")
