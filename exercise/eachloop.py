print("Hello welcome to my adventure!")

description = "big room with chamdeler hanging from the roof, and paintings all"
doors = ["north", "south", "west", "east"]

run = True
while run:
    print("You are standing in a" + description)
    print("There are doors to your: ")

    directions = ""
    for direction in doors:
        directions = directions + ", " + direction
    directions = directions[2:]
    print(directions)

    # print menu
    print("Where do you want to go?")
    print("1. Go north")
    print("2. Go south")
    print("1. Go west")
    print("1. Go east")
    print("5. look")
    print("0. Quit game")

    # Ask for choice
    choice = input("please enter your choice ")

    # check user input
    if not choice.isnumeric():
        print("Sorry! Please give a number")
        continue

    # Do something
    choice = int(choice)
    if choice == 0:
        run = False
    elif choice == 1:
        print("You going to north")
    elif choice == 2:
        print("You going to south")
    elif choice == 3:
        print("You going to west")
    elif choice == 4:
        print("You going to east")
    elif choice == 5:
        print("You are looking")
    else:
        print("You asked something i can not do!")
