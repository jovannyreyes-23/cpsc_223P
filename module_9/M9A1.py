# Name: Jovanny Reyes
# Student ID: 887699056
# Section: 18254
# Assignment: Module 9 Assignment 1

population_dict = {}

while True:
    city = input("What is next city? (enter q to quit) ")
    if city == 'q':
        break
    population = int(input(f"What is the population of {city}? "))
    population_dict[city] = population

population_limit = int(input("What is the largest population for a small town? "))

with open("populationdata.txt", "w") as output_file:
    print("Big Cities:", file=output_file)
    for city, population in population_dict.items():
        if population > population_limit:
            print(f"{city}, {population}", file=output_file)