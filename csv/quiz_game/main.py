import csv
import random


def load_questions(filename):
    #it loads the questions from the file
    questions = []
    with open (filename, 'r') as file:
        reader = csv.reader(file)
        next(reader) #skis  the first line(header)
        for row in reader:
            questions.append(row)
        return questions
print(load_questions("quiz_questions.csv"))

def take_quiz(questions):
    score = 0
    selected_questions = random.sample(questions, 10)
    index = 1

    for question in selected_questions:
        print("Question #" + str(index)  + ": " + question[0])
        print("A: " + question[1])
        print("B: " + question[2])
        print("C: " + question[3])
        print("D: " + question[4])

        answer = input("you answer: (A,B,C,D)").strip().upper()
        if answer == question[5]:
            print("Correct!")
            score +=1
        else:
            print("Incorrect!")
            print("the correct answer is: " + question[5])

        index +=1

    return score

def dislay_result(score,total_questions):
    percentage = (score/total_questions)*100
    if percentage >=80:
        print("you got an A")
    elif percentage <=80:
        print("you got an B")
    elif percentage <=75:
        print("you got an c")
    else:
        print("you got an D") 
    
questions = load_questions("quiz_questions.csv")
score = take_quiz(questions)
dislay_result(score, 10)