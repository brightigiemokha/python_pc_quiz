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
    # question 3
    {
        'question': 'What word means to switch a computer off and on again?',
        'a': 'Hibenate',
        'b': 'Sleep',
        'c': 'Reboot',
        'd': 'shut down',
        'correct': 'b',
    },
]