# Name: Jovanny Reyes
# Student ID: 887699056
# Section: 18254
# Assignment: Module 2 Assignment 1

g_list = []

favorite_game_str = input("What is your favorite game? ")
favorite_game2_str = input("What is your second favorite game? ")
favorite_game3_str = input("What is your third favorite game? ")

g_list.append(favorite_game_str.title())
g_list.append(favorite_game2_str.title())
g_list.append(favorite_game3_str.title())

print(f"One of your favorite games is {g_list.pop()}")
print(f"One of your favorite games is {g_list.pop()}")
print(f"One of your favorite games is {g_list.pop()}")