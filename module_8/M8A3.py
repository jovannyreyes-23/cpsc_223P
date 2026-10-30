# Name: Jovanny Reyes
# Student ID: 887699056
# Section: 18254
# Assignment: Module 8 Assignment 3

while True:
    first_num = input("What is the first number? (or type q to quit) ")

    if first_num == "q":
        break

    second_num = input("What is the second number? ")

    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("You cannot divide by zero")
    else:
        print(f"{first_num} / {second_num} is {answer}")

print("The program is over")