import random
num = input("Please enter a number from 1 - 10: ")
num2 = int(num)
guess = random.randint(1, 10)
while True:
    if num2 == guess:
        print("you guessed right")
    elif num2 > guess:
        print("too high, try again.")
    elif num2 < guess:
        print("too low, try again")
    else:
        print("enter a number")
    break  