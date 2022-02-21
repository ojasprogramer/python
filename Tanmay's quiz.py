

print("Welcome to the quiz")
print("type 'stop' to exit\n")

run = True
question = 1


while run:
    if question == 1:
        answer = input("\nIs cheetah the fastest animal in the world?Yes or No?(Land, water, air)\n:")
        if answer == "Yes":
            print("\nIt is false.The peregrine falcon is the fastest animal")
            question = 2
        elif answer == "No":
            print("\nYou are correct.\n")
            print("Next question")
            question = 2
        elif answer == "stop":
            print("\n\nThanks for attempting, Bye.")
            run = False
        else:
            print("\nError, please try again.")
            continue
    elif question == 2:
        answer = input("\nWhat is the scientific name of Pig?\n:")
        if answer == "Sus" or "sus":
            print("\nYou are correct")
            print("\nNext question")
            question = 3
            run = False
        elif answer == "stop":
            print("\nThanks for attempting. Bye")
            run = False
        else:
            print("\nYou are wrong, please try again")
            continue
    elif question == 3:
        answer = input("\nWhich country produces the most coffee?")
        if answer == "Brazil":
            print("\nYou are correct")
            print("\nNext question")
            question = 4
            run = False
        elif answer == "stop":
            print("\nThanks for attempting. Bye")
            run = False
        else:
            print("\nYou are wrong, please try again")
            continue
    elif question == 4:
        answer = input("\nWhat is the capital of Switzerland?\n:")
        if answer == "Bern":
            print("\nYou are correct")
            print("\nNext question")
            question = 5
            run = False
        elif answer == "stop":
            print("\nThanks for attempting. Bye")
            run = False
        else:
            print("\nYou are wrong, please try again")
            continue
    if question == 5:
        answer = input("\nWhich country produces the most coffee?")
        if answer == "Brazil":
            print("\nYou are correct")
            print("\nNext question")
            question = 6
            run = False
        elif answer == "stop":
            print("\nThanks for attempting. Bye")
            run = False
        else:
            print("\nYou are wrong, please try again")
            continue
    if question == 6:
        answer = input("\nWhich is the fastest car in the world?(Exact name)?")
        if answer == "Bugatti Chiron Super Sport 300+":
            print("\nYou are correct")
            print("\nNext question")
            run = False
        elif answer == "stop":
            print("\nThanks for attempting. Bye")
            run = False
        else:
            print("\nYou are wrong, please try again")
            continue



