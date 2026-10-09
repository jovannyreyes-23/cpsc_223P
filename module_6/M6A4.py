# Name: Jovanny Reyes
# Student ID: 887699056
# Section: 18254
# Assignment: Module 6 Assignment 4

def show_messages(message_list):
    while message_list:
        print(message_list.pop())

my_messages = []

while True:
    message = input("What is the next message? (type 'q' to quit) ")
    if message == 'q':
        break
    my_messages.append(message)

print("First time calling function")
show_messages(my_messages[:])
print("Second time calling function")
show_messages(my_messages[:])