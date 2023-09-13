# Collect input as varible from user
# print Hej + name
# name = input("What is your name?")
# print("Hej " + name)

# Ask for 2 numbers add and print
# num1 = input("Enter first digit ")
# num2 = input("Enter second digit ")
# sum= int(num1) + int(num2)
# print("..."+str(sum))

name = input("Enter name")
age = input("Enter age")
msg = ("Hej " + name + " du är " + age + " gammal")
print(msg)

num1 = 10
num2 = 20
num3 = 15
sum = num1 + num2 + num3
print("The average is: "+ str(sum/3))

cels = int(input("Enter a celsius temperature: "))
if cels > 20:
    print("Varmt")
if cels < 0:
    print("Kalt")
elif cels > 10:
    print("Ta jacka")
else: print("Som vanligt")


