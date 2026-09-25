# Name: Jovanny Reyes
# Student ID: 887699056
# Section: 18254
# Assignment: Module 4 Assignment 5

food_dict = {'Jim': 'Tacos',
             'Bob': 'Burgers',
             'Janelle': '',
             'Lisa': 'Pizza',
             'Thomas': '',
             'Yolanda': '',
             'Finn': 'Bread',
            }

for person, food in food_dict.items():
    if food == '':
        fav_food_str = input(f"What is {person}'s favorite food? ")
        food_dict[person] = fav_food_str

print("Here are the favorite foods:")

for person, food in food_dict.items():
    print(f"{person}'s favorite food is {food}")