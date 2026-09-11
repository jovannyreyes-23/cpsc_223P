# Name: Jovanny Reyes
# Student ID: 887699056
# Section: 18254
# Assignment: Module 2 Assignment 2

g_list = ["Mortal Kombat", "Contra", "Sheets Of Rage", "Shinobi", "Sonic", "Phantasy Star"]
print("Here are the top Sega games: ")

for item in g_list:
    print(item)

remove_str = input("Which one do you think should be removed? ")
g_list.remove(remove_str.title())
print("Here are the top Sega games: ")

for item in g_list:
    print(item)