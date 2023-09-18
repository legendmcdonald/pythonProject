import time


def div_five(numberList):
    for i in numberList:
        if i % 5 == 0:
            print(i)


numberX = [5, 15, 6, 25, 85, 234, 200]
print("Given list " + str(numberX))
div_five(numberX)


def addition(a, b):
    print(a + b)
    time.sleep(1)


addition(2, 5)

