# Lets Code Our Program 11. Enjoy!!!
# In this program I have made a Password Generator using Random Module.

import random

hard_chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','!','@','#','$','%','^','&','*','_','-','+','=','>',',','<','/','1','2','3','4','5','6','7','8','9','0']
medium_chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','!','@','#','$','%','^','&','*','_','-','+','=','>',',','<','/']
weak_chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']



def generate(difficulty,length):
    password = ""
    if difficulty == 'H':
        for i in range(length):
            password = password + random.choice(hard_chars)
        print(f"Your Password is : {password}")
    elif difficulty == 'M':
        for i in range(length):
            password = password + random.choice(medium_chars)
        print(f"Your Password is : {password}")
    elif difficulty == 'W':
        for i in range(length):
            password = password + random.choice(weak_chars)
        print(f"Your Password is : {password}")
    else:
        print("Try Again......")
            

if __name__ == "__main__":
        
    difficulty = input("Enter Difficulty Level, H for Hard; M for Medium; W for Weak : ")
    length = int(input("Enter the Length of The Password : "))

    generate(difficulty,length)