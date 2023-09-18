# get user info
import random

score = 0
name = ""


def user_info():
    global name
    name = input("Enter your username ")
    age = int(input("Enter your age "))
    if age < 0:
        print("you should be at least 13 years to play!")
        exit()
    print("\nHello " + name + " welcome to Legend adventure!")


# print menu function
def menu():
    # print menu
    print("\nWhere do you want to go?")
    print("1. Go north")
    print("2. Go south")
    print("1. Go west")
    print("1. Go east")
    print("5. look")
    print("0. Quit game")
    print("Score: " + str(score))


# Define possible encounters
def random_encounter():
    encounters = [
        "You run into a pleasant traveler who gives you a useful hint,",
        "You discover a treasure box and uncover some priceless things,",
        "A wild beast arrives!  You engage in combat.",
        "You discover an old map that could point to buried treasure."
    ]
    return random.choice(encounters)


def combat_details():
    global score
    combat_options = random.randint(1, 4)
    if combat_options == 1:
        print("Well you won the battle!")
        score += 100  # Add 10 points for winning a battle
    elif combat_options == 2:
        print("You got to escape. Hurry find somewhere to go now!")
        score += 50
    elif combat_options == 3:
        print("You got unlucky you didnt survive.")
        print(name + " Your score is: " + str(score))
        print("\nPlay Again!")
        exit()
    else:
        print("\nYou got lucky. Continue your journey and Good Luck!")


user_info()
description = "big room with chandelier hanging from the roof."
doors = ["north", "south", "west", "east"]
run = True
while run:
    print("\nYou are standing in a " + description)
    print("There are doors to your: " + ", ".join(doors))

    menu()

    # Ask for choice
    choice = input("please enter your choice")

    # check user input
    if not choice.isnumeric():
        print("Sorry! Please give a number")
        continue

    # Do something
    choice = int(choice)
    if choice == 0:
        run = False
    elif choice == 1:
        print("\nYou going to north")
    elif choice == 2:
        print("\nYou going to south")
    elif choice == 3:
        print("\nYou going to west")
    elif choice == 4:
        print("\nYou going to east")
    elif choice == 5:
        print("\nYou are looking around")
        encounter_result = random_encounter()
        print(encounter_result)
        if "beast" in encounter_result:
            print("Uh-oh! It's a tough battle!")
            combat_details()
        elif "treasure" in encounter_result:
            print("You found a treasure!")
            score += 100  # Add 20 points for finding treasure
        else:
            score += 20
    else:
        print("You asked something i can not do!")
