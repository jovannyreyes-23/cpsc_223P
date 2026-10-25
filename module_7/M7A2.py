# Name: Jovanny Reyes
# Student ID: 887699056
# Section: 18254
# Assignment: Module 7 Assignment 2

class User:
    def __init__(self, first_name, last_name, user_id, last_login, password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.last_login = last_login
        self.password = password

    def describe_user(self):
        print(f"Accessing user {self.user_id}:")
        print(f"{self.first_name} {self.last_name} last logged in on {self.last_login}")

    def greet_user(self):
        print(f"Welcome to the jungle {self.first_name} {self.last_name}, you gonna die")
    
    def new_login(self, month, day, year):
        if month < 1 or month > 12:
            print("That is not a valid month")
            return

        if day < 1 or day > 31:
            print("That is not a valid day")
            return

        if year < 0:
            print("That is not a valid year")
            return

        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August', 'September', 'October', 'November', 'December']

        self.last_login = f"{months[month - 1]} {day}, {year}"

jim = User(first_name='Jim',
           last_name='Bob',
           user_id=1000,
           last_login='June 12, 1998',
           password='password123')
jim.describe_user()
jim.greet_user()
joe = User('Joe',
           'Bob',
           1001,
           'July 4, 2001',
           'babygirl')
joe.greet_user()
joe.describe_user()
joe.new_login(2, 3, 2025)
joe.describe_user()
joe.new_login(15, 3, 2025)
joe.new_login(2, 35,  2025)
joe.new_login(2, 3, -55)