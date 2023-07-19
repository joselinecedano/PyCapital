import random

states = [
    {"Alabama": "Montgomery"},
    {"Alaska": "Juneau"},
    {"Arizona": "Phoenix"},
    {"Arkansas": "Little Rock"},
    {"California": "Sacramento"},
    {"Colorado": "Denver"},
    {"Connecticut": "Hartford"},
    {"Delaware": "Dover"},
    {"Florida": "Tallahassee"},
    {"Georgia": "Atlanta"},
    {"Hawaii": "Honolulu"},
    {"Idaho": "Boise"},
    {"Illinois": "Springfield"},
    {"Indiana": "Indianapolis"},
    {"Iowa": "Des Moines"},
    {"Kansas": "Topeka"},
    {"Kentucky": "Frankfort"},
    {"Louisiana": "Baton Rouge"},
    {"Maine": "Augusta"},
    {"Maryland": "Annapolis"},
    {"Massachusetts": "Boston"},
    {"Michigan": "Lansing"},
    {"Minnesota": "St. Paul"},
    {"Mississippi": "Jackson"},
    {"Missouri": "Jefferson City"},
    {"Montana": "Helena"},
    {"Nebraska": "Lincoln"},
    {"Nevada": "Carson City"},
    {"New Hampshire": "Concord"},
    {"New Jersey": "Trenton"},
    {"New Mexico": "Santa Fe"},
    {"New York": "Albany"},
    {"North Carolina": "Raleigh"},
    {"North Dakota": "Bismarck"},
    {"Ohio": "Columbus"},
    {"Oklahoma": "Oklahoma City"},
    {"Oregon": "Salem"},
    {"Pennsylvania": "Harrisburg"},
    {"Rhode Island": "Providence"},
    {"South Carolina": "Columbia"},
    {"South Dakota": "Pierre"},
    {"Tennessee": "Nashville"},
    {"Texas": "Austin"},
    {"Utah": "Salt Lake City"},
    {"Vermont": "Montpelier"},
    {"Virginia": "Richmond"},
    {"Washington": "Olympia"},
    {"West Virginia": "Charleston"},
    {"Wisconsin": "Madison"},
    {"Wyoming": "Cheyenne"},
]

# print(len(states))  # check that its all 50 states

# function for game
def capitals_game():
    # Welcome Message
    print(
        " \n\nWelcome to State Capital: Console Edition! \n\n *** Instructions *** \n\nYou will be asked 50 questions regarding the Capitals of each U.S State. It's your job to answer them correctly with minimal incorrect guesses. Your score depends on it! For every correct guess you earn a point, but beware for every incorrect guess you'll get docked 1pt! Let's test your skills! GOOD LUCK! \n\n"
    )
    random.shuffle(states)  # randomize states
    left = 50  # questions left
    incorrect = 0  # where wrong guess tally is being stored
    correct = 0  # where right guess tally is being stored
    for state in states:  # each state dic in array
        for (
            state,
            capital,
        ) in (
            state.items()
        ):  # grabs the key and value and stores it into state and capital for each state dic
            print(f"What is the capital of {state} ?")
            while True:
                # until the answer is correct it wont let you move on to next question (break loop)
                user_input = input(" Answer: ").lower()
                # doesnt matter if they put a random uppercase as long as its spelled correctly it'll be converted to lower case and be right
                if user_input == capital.lower():
                    correct = correct + 1
                    left = left - 1
                    print(
                        f" \n\n You got it right! \n\n *** Score: ***\n\n Incorrect Guesses: {incorrect}  \n\n Correct Guesses: {correct} \n\n Points +1 \n\n Questions left: {left} \n\n"
                    )
                    break  # exit while loop
                elif user_input != capital.lower():
                    incorrect = incorrect + 1
                    print(
                        f"\n\n You got it wrong!! \n\n *** Score ***\n\n Incorrect Guesses: {incorrect}  \n\n Correct Guesses: {correct} \n\n Points -1 \n\nPlease try again!"
                    )
            if left == 0:
                print(
                    f" ************* \n\n Game over! Great work! \n\n Total Score: {correct - incorrect} \n\n ************* \n\n Would you like to play again? y/n \n\n"
                )
                user_resp = input("Answer: ").lower()
                if user_resp == "y" or user_resp == "yes":
                    # reset the score and guesses values and call function to restart game
                    left = 50
                    incorrect = 0
                    correct = 0
                    capitals_game()
                elif user_resp == "n" or user_resp == "no":
                    # break the loop and exit capitals_game()
                    break


capitals_game()

# Farewell Message
print(" \n\n Have a good day, come again soon!")
