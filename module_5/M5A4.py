# Name: Jovanny Reyes
# Student ID: 887699056
# Section: 18254
# Assignment: Module 5 Assignment 4

orders_list = ['pastrami', 'turkey', 'pastrami', 'ham', 'turkey']

finished_list = []

while orders_list:
    orders = orders_list.pop()
    print(f"I made your {orders}")
    finished_list.append(orders)

print(f"Here are all the sandwiches I made:")
for sandwich in finished_list:
    print(sandwich)

