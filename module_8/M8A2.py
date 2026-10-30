# Name: Jovanny Reyes
# Student ID: 887699056
# Section: 18254
# Assignment: Module 8 Assignment 2

with open("input.txt") as file:
    data_list = file.readlines()

with open("output.txt", "w") as output_file:

    print("Here are the user agents:", file=output_file)
    for line in data_list:
        if line.startswith("User-agent:"):
            print(line.strip(), file=output_file)

    print("Here are the sitemaps:", file=output_file)
    for line in data_list:
        if line.startswith("Sitemap:"):
            print(line.strip(), file=output_file)

    print("Here are the crawl delays:", file=output_file)
    for line in data_list:
        if line.startswith("Crawl-Delay:"):
            print(line.strip(), file=output_file)