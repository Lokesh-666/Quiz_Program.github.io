# A dictionary that stores questions and answers. 
# Have a variable that tracks the score of the player. 
# Loop through the dictionary using the key values pairs. 
# Display each question to the user and allow them to answer. 
# Tell them if they are right or wrong. 
# Show the final results when quiz is complete.

quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question4": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question5": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question6": {
        "question": "What is the capital of Switzerland?",
        "answer": "Bern"
    },
    "question7": {
        "question": "What is the capital of Austria?",
        "answer": "Vienna"
    },
}
score = 0
passing_limit = 0.7
i=0
for key, value in quiz.items():
    print(value['question'])
    answer = input("Your answer: ")

    if answer.lower() == value['answer'].lower():
        print("Correct!")
        score += 1
        print("Your score is: " + str(score))
        print("\n")
    else:
        print("Incorrect!")
        print("The correct answer is: " + value['answer'])
        print("Your score is: " + str(score))
        print("\n")

print("You got " + str(score) + " out of " + str(len(quiz)) + " correct!")
print("Your percentage is: " + str(int(score / len(quiz) * 100)) + "%")

if score / len(quiz)  >= passing_limit:
    print("Congratulations, you passed the quiz!")

else:
    print("Sorry, you did not pass the quiz.")