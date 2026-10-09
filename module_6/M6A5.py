# Name: Jovanny Reyes
# Student ID: 887699056
# Section: 18254
# Assignment: Module 6 Assignment 5

def comp_avg(*integers):
    sum = 0
    total_numbers = 0

    for number in integers:
        sum += number
        total_numbers += 1

    return(sum / total_numbers)

def comp_max(*integers):
    largest_num = integers[0]

    for number in integers:
        if number > largest_num:
            largest_num = number

    return(largest_num)

def comp_min(*integers):
    smallest_num = integers[0]

    for number in integers:
        if number < smallest_num:
            smallest_num = number

    return(smallest_num)