print("Welcome to my Python Quiz!")

playing = input("Would you like to Play? ")

if playing.lower() != "yes":
    quit()

print("Great Choice! Lets Play :)")

display_question(questions[0])