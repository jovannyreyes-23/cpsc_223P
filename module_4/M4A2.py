# Name: Jovanny Reyes
# Student ID: 887699056
# Section: 18254
# Assignment: Module 4 Assignment 2

food_dict = {}

for food in range(3):
    food_suggestion_str = input("What is good to eat? ")
    food_origin_str = input("What country is that from? ")
    food_dict[food_suggestion_str] = food_origin_str

liked_dish_str = input("What dish do you like? ")
if liked_dish_str in food_dict.keys():
    print(f"{liked_dish_str} is from {food_dict[liked_dish_str]}")