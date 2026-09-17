# Name: Jovanny Reyes
# Student ID: 887699056
# Section: 18254
# Assignment: Module 3 Assignment 6

name_str = input("What is the student name? ")
score_int = int(input("What is their score? "))

if score_int >= 90:
    print(f"{name_str} earned an A")
elif score_int >= 80:
    print(f"{name_str} earned a B")
elif score_int >= 70:
    print(f"{name_str} earned a C")
elif score_int >= 60:
    print(f"{name_str} earned a D")
else:
    print(f"{name_str} earned an F")
