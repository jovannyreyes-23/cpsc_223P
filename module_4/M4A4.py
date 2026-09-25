# Name: Jovanny Reyes
# Student ID: 887699056
# Section: 18254
# Assignment: Module 4 Assignment 4

guy_dict1 = {
    'name': 'Jimmer',
    'age': 23,
    'scout rank': 'Eagle',
    'scout badges': [],
}

print("I know Jimmer has three scout badges, what are they?")
first_badge_str = input("The first badge is: ")
guy_dict1['scout badges'].append(first_badge_str)
second_badge_str = input("The second badge is: ")
guy_dict1['scout badges'].append(second_badge_str)
third_badge_str = input("The third badge is: ")
guy_dict1['scout badges'].append(third_badge_str)

print(guy_dict1)