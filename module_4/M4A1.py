# Name: Jovanny Reyes
# Student ID: 887699056
# Section: 18254
# Assignment: Module 4 Assignment 1

g_list = []

n = 1

for game in range(3):
    fav_game_str = input(f"What is your number {n} favorite PlayStation game? ")
    n += 1
    g_list.append(fav_game_str)

for number, game in enumerate(g_list, start= 1):
    print(f"Your number {number} favorite game was {game}")