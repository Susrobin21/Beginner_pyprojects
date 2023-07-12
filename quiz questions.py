quiz = {
    "question1": {
        "question": "Who is the winner of Fifa world cup 2022 ?",    #using dictionaries to store information 
        "answer": "Argentina"
    },
    "question2": {
        "question": "What is the national bird of India ?",
        "answer": "Peacock"
    },
    "question3": {
        "question": "Who is the No 1 team in odi cricket at present ?",
        "answer": "Australia"
    },
    "question4": {
        "question": "What is the director of the film Interstellar ?",
        "answer": "Christopher Nolan"
    },"question5": {
        "question": "What is the most selling manga of all time ?",
        "answer": "One Piece"
    },"question6": {
        "question": "Who is the #1 singer in the world right now ?",
        "answer": "The weeknd"
    },"question7": {
        "question": "what is the top rated web series in imdb ?",
        "answer": "Breaking Bad"
    },
}

score = 0         #tracks our score 

for key, value in quiz.items():
    print(value['question' ])
    answer = input("Answer :")

    if answer.lower() == value[ 'answer'] . lower():     #This enables us to get score for the question even if the answer is entered in lower case letters
        print('Correct')
        score = score + 1
        print("Your score is : " + str(score))
    else:
        print("Incorrect")
        print("The answer is : " + value[ 'answer'])
        print("Your score is : " + str(score))

print("Your final score is " + str(score) + "out of 7 questions " )