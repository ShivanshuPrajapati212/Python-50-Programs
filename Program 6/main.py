# Lets Code Our Program 6. Enjoy!!!

import random

words = ["Wow","Shivanshu","Himanshu","Noob","God","Bot"]

print(f"Hint: {words}")
word = random.choice(words)
guess = 1

while True:
    userint = input("Enter the Word : ")

    if userint == word.lower():
        print("You Guessed the word!!!")
        print(f"The word was {word}")
        print(f"You Guessed it in {guess} Tries.")
        break
    else:
        print("Try again....")
        guess = guess + 1