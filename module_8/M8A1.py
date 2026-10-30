# Name: Jovanny Reyes
# Student ID: 887699056
# Section: 18254
# Assignment: Module 8 Assignment 1

with open("input.txt") as file:
    data_list = file.readlines()

print("Here are the user agents:")
for line in data_list:
    if line.startswith("User-agent:"):
        print(line.strip())

print("Here are the sitemaps:")
for line in data_list:
    if line.startswith("Sitemap:"):
        print(line.strip())

print("Here are the crawl delays:")
for line in data_list:
    if line.startswith("Crawl-Delay:"):
        print(line.strip())