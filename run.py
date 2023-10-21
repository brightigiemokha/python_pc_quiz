print("Welcome to my Python Quiz!")

playing = input("Would you like to Play? ")

if playing.lower() != "yes":
    quit()

print("Great Choice! Lets Play :)")

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
        'question': 'Who released d first antivirus called VirusScan in 1987?',
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
    # question 6
    {
        'question': 'Who developed Python Programming Language?',
        'a': 'Wick van Rossum',
        'b': 'Rasmus Lerdorf',
        'c': 'Guido van Rossum',
        'd': 'Niene Stom',
        'correct': 'c',
    },
    # question 7
    {
        'question': 'Which type of Programming does Python support?',
        'a': 'object-oriented programming',
        'b': 'structured programming',
        'c': 'functional programming',
        'd': 'all of the mentioned',
        'correct': 'd',
    },
    # question 8
    {
        'question': 'Is Python case sensitive when dealing with identifiers?',
        'a': 'no',
        'b': 'yes',
        'c': 'machine dependent',
        'd': 'none of the mentioned',
        'correct': 'b',
    },
    # question 9
    {
        'question': 'Which is the correct extension of the Python file?',
        'a': '.python',
        'b': '.pl',
        'c': '.py',
        'd': '.P',
        'correct': 'c',
    },
    # question 10
    {
        'question': 'Is Python code compiled or interpreted?',
        'a': 'Python code is both compiled and interpreted',
        'b': 'Python code is neither compiled nor interpreted',
        'c': 'Python code is only compiled',
        'd': 'Python code is only interpreted',
        'correct': 'a',
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
        score = score + 1
    else:
        print(f"Incorrect answer, the answer is {question['correct'].upper()}")


for question in questions:
    display_question(question)

print("-------------------------")
print("You got " + str(score) + " questions correctly!")
print("You got " + str((score / 10) * 100) + " %. ")
print("-------------------------")
quit()