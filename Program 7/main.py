# Lets Code Our Program 7. Enjoy!!!

print("Welcome to the of Rock Paper Scissors!!!")

while True:
    print("Enter R for Rock, P for Paper, S for Scissors")

    player_1 = input("Player 1 : ")
    player_2 = input("Player 2 : ")

    if player_1.lower() == 'r' and player_2.lower() == 'r':
        print("Game Draw...")

    elif player_1.lower() == 'r' and player_2.lower() == 'p':
        print("Player Two Won!!!")

    elif player_1.lower() == 'r' and player_2.lower() == 's':
        print("Player One Won!!!")
    
    elif player_1.lower() == 'p' and player_2.lower() == 'r':
        print("Player One Won!!!")
    
    elif player_1.lower() == 'p' and player_2.lower() == 's':
        print("Player Two Won!!!")
    
    elif player_1.lower() == 'p' and player_2.lower() == 'p':
        print("Game Draw...")
    
    elif player_1.lower() == 's' and player_2.lower() == 'r':
        print("Player Two Won!!!")
    
    elif player_1.lower() == 's' and player_2.lower() == 's':
        print("Game Draw...")
    
    elif player_1.lower() == 's' and player_2.lower() == 'p':
        print("Player Two Won!!!")
    else:
        print("Bye Bye!!!")
        break