# Name: Jovanny Reyes
# Student ID: 887699056
# Section: 18254
# Assignment: Module 5 Assignment 2

start_int = int(input(f"Enter the start of the loop: "))
limit_int = int(input(f"Enter the limit of the loop: "))

current_int = start_int

while current_int < limit_int:
    print(f"The current value is {current_int}")
    current_int = current_int * 2

print(f"The last value of current that was less than {limit_int} was {int(current_int / 2)}")
