print("Welcome to my Python Quiz!")

playing = input("Would you like to Play? ")

if playing.lower() != "yes":
    quit()

print("Great Choice! Lets Play :)")

display_question(questions[0])

# list of questions
questions = [
    # question 1
    {
        'question': 'What does CPU stands for?',
        'a': 'Central Processing Unit',
        'b': 'Open Systems Interconnect',
        'c': 'Organised Stairway Interweb',
        'd': 'Open Safe Internet',
        'correct': 'a',
    },
    # question 2
    {
        'question': 'What is a Computer?',
        'a': 'Computer is a software',
        'b': 'Open Systems Interconnect',
        'c': 'An Electronic device used in processing data',
        'd': 'An Internet device',
        'correct': 'c',
    },
    # question 3
    {
        'question': 'Who released their first antivirus product called VirusScan in 1987?',
        'a': 'John wesley',
        'b': 'John McAfee',
        'c': 'Norton',
        'd': 'Bill Gate',
        'correct': 'b',
    },
    # question 4
    {
        'question': 'What word means to switch a computer off and on again?',
        'a': 'Hibenate',
        'b': 'Sleep',
        'c': 'Reboot',
        'd': 'shut down',
        'correct': 'b',
    },
     # question 5
    {
        'question': 'What term was coined by American John McCarthy in 1956?',
        'a': 'John wesley',
        'b': 'John McAfee',
        'c': 'Norton',
        'd': 'Bill Gate',
        'correct': 'b',
    },
]

score = 0


def display_question(question):
    global score
    print("-------------------------")
    print(question['question'])
    print("-------------------------")
    print(f"A. {question['a']}")
    print(f"B. {question['b']}")
    print(f"C. {question['c']}")
    print(f"D. {question['d']}")

    answer = input("Your answer: ")
    
    if answer.lower() == question['correct']:
        print('Correct! Well Done')
        score = score + 5
    else:
        print(f"Incorrect answer, the answer is {question['correct'].upper()}")

