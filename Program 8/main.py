# Lets Code Our Program 8. Enjoy!!!
import random


print("Welcome to Dice Roller!!!")

while True:
    user = input("Enter R to Roll the Dice : ")

    if user.lower() == 'r':
        print(f"You Got {random.randint(1,6)}")
    else:
        print("Bye Bye!!")
        break