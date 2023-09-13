for i in range(1, 20, 1):
 print(i)

print()
for i in range(0, 20, 2):
    print(i)

print()
for i in range(1, 20, 2):
    print(i)

number1 = int(input("Write a number"))
number2 = int(input("Write a number"))
if number2 > number1:
    print("Higher")
elif number2 < number1:
    print("Lower")
else:
    print("Same")
