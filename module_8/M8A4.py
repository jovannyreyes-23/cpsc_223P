# Name: Jovanny Reyes
# Student ID: 887699056
# Section: 18254
# Assignment: Module 8 Assignment 4

def dictionary_maker(file_path):
    ret_dict = {}

    try:
        with open(file_path) as file:
            for line in file:
                key, value = line.strip().split(":", 1)
                ret_dict[key.strip()] = value.strip()

    except FileNotFoundError:
        print(f"The file {file_path} does not exist on this system")

    return ret_dict

file_name = input("What is the file with the data? ")
data_dictionary = dictionary_maker(file_name)
print(data_dictionary)