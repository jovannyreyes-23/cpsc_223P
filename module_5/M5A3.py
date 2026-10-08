# Name: Jovanny Reyes
# Student ID: 887699056
# Section: 18254
# Assignment: Module 5 Assignment 3

triviabank_dict = {}

print(f"Welcome to the trivia builder 3000")

while True:
    question_str = input("Enter the next question: ")
    if question_str == '':
        print(f"You did not enter a question, let's try again.")
        continue
    if question_str == 'Done':
        print(f"We will stop entering questions now")
        break
    answer_str = input("Enter the correct answer for that question: ")
    triviabank_dict[question_str] = answer_str

print(f"Here is the final trivia dictionary:")

for question_str, answer_str in triviabank_dict.items():
    print(f"The question is: {question_str}")
    print(f"And the answer is: {answer_str}")