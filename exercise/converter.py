
# Ask for input
userInput = float(input("Enter a volume in liter: "))
userInput2 = float(input("Do you want to convert volume to: "
                         + "\n" + "1. Milliliter"
                         + "\n" + "2. Centiliter"
                         + "\n" + "3. Deciliter"
                         + "\n" + "4. Cubic decimeter"
                         + "\n" + "5. Cubic meter "
                         ))

if userInput2 == 1:
    milliliters = float(userInput * 1000)
    print("litters is the same as " + str(milliliters) + " Milliliters")
elif userInput2 == 2:
    centiliter = float(userInput * 100)
    print("litters is the same as " + str(centiliter) + " Centiliters")
elif userInput2 == 3:
    deciliter = float(userInput * 10)
    print("litters is the same as " + str(deciliter) + " Deciliter")
elif userInput2 == 4:
    cubicDecimeter = float(userInput * 1)
    print("litters is the same as " + str(cubicDecimeter) + "Cubic decimeter")
elif userInput2 == 5:
    cubicMeter = float(userInput / 1000)
    print("litters is the same as " + str(cubicMeter) + " Cubic decimeter")
else:
    print("Choose a correct conversion!")
