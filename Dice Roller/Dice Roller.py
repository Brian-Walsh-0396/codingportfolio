import random
import os
import time

def roll_dice(sides, rolls, reroll_ones):
    start_time = time.time()
    roll_results = []
    total = 0
    
    for i in range(rolls):
        roll = random.randint(1, sides)
        while reroll_ones and sides == 20 and roll == 1:
            roll = random.randint(1, sides)
        roll_results.append(roll)
        if sides < 20:
            total += roll
    
    if sides == 20:
        roll_results.sort(reverse=True)
    
    file_path = ""
    file_name = "roll_results"
    file_ext = ".txt"
    file_num = 1
    while True:
        file_path = os.path.join(os.getcwd(), f"{file_name}{file_num}{file_ext}")
        if not os.path.exists(file_path):
            break
        file_num += 1
        
    with open(file_path, "w") as file:
        file.write(f"Dice settings: {sides} sides, {rolls} rolls, {'Reroll 1s' if reroll_ones else 'Do not reroll 1s'}\n")
        file.write(f"Roll Results: {', '.join(str(x) for x in roll_results)}\n")
        if sides < 20:
            file.write(f"Total: {total}\n")
        
        end_time = time.time()
        runtime_ms = round((end_time - start_time) * 1000, 2)
        file.write(f"Runtime: {runtime_ms} ms")

    os.startfile(file_path)

sides = int(input("How many sides does the dice have? "))
rolls = int(input("How many times do you want to roll the dice? "))
reroll_ones = False
if sides == 20:
    reroll_ones = input("Do you want to reroll 1s on a 20-sided dice? (y/n) ").lower() == "y"
roll_dice(sides, rolls, reroll_ones)
