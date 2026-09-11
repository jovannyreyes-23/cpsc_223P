# Name: Jovanny Reyes
# Student ID: 887699056
# Section: 18254
# Assignment: Module 2 Assignment 3

uber_list = list(range(100, 201, 2))

start_int = int(input("What is the start of your slice? "))
end_int = int(input("What is the end of your slice? "))

data_list = uber_list[start_int: end_int]

total_int = 0

for item in data_list:
    total_int += item

average_value_float = total_int / len(data_list)
print(f"Your slice contains {len(data_list)} values and has an average value of {average_value_float}")