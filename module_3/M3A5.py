# Name: Jovanny Reyes
# Student ID: 887699056
# Section: 18254
# Assignment: Module 3 Assignment 5

start_int = int(input("What is the first number? "))
end_int = int(input("What is the second number? "))

num_list = list(range(start_int, end_int + 1))

sum_int = 0

for number in num_list:
    if number % 5 == 0:
        sum_int += number

print(f"The total values of multiples of 5 from {start_int} to {end_int} is {sum_int}")