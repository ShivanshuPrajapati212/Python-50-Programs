# Lets Code Our Program 5. Enjoy!!!
# This is by GeeksForGeeks
import random

userInputone = int(input("Enter the Starting Number : "))
userInputtwo = int(input("Enter the Ending Number : "))


number = random.randint(userInputone,userInputtwo)
guess = 1

while True:
    guessnum = int(input(f"Guess the Number between {userInputone} and {userInputtwo} : "))

    if guessnum == number:
        print("You Have Guessed the Number!!!")
        print(f"The Number was {number}")
        print(f"You have Gussed the number in {guess} Tries.")
        break
    elif guessnum > number:
        print("Guess Lesser Number.")
        guess = guess + 1
    elif guessnum < number:
        print("Guess Greater Number.")
        guess = guess + 1
    else:
        print("Try again....")
