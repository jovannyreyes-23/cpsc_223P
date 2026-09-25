# Name: Jovanny Reyes
# Student ID: 887699056
# Section: 18254
# Assignment: Module 4 Assignment 3

games_dict = {}

for games in range(3):
    game_suggestion_str = input("What is a great game? ")
    system_str = input("What system can I play that on? ")
    games_dict[game_suggestion_str] = system_str

print("That's too many, let's get rid of one")
remove_game_str = input("What game should we remove? ")
del games_dict[remove_game_str]
print("The new dictionary is:")

for games, system in games_dict.items():
    print(f"You can play {games} on {system}")