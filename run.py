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
        'question':'What does CPU stands for?',
        'a':'Central Processing Unit',
        'b':'Open Systems Interconnect',
        'c':'Organised Stairway Interweb',
        'd':'Open Safe Internet',
        'correct':'a',
    },

]