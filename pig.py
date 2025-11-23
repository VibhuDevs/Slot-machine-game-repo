#project 3 - PIG game
import random

print("Welcome to PIG")
def pig():
    print("1st player's turn")
    score1 = 0 
    while True:
        choice1 = input("Do you wanna hold or roll?: ").lower()
        if choice1 == "roll":
            player1 = random.randint(1,6)
            print(f"Player 1 got {player1}")
            if player1 == 1:
                score1 = 0
                print(f"Ug-oh. Your score is {score1}")
                break
            else:
                score1 += player1
                print(f"New score is:{score1}")
        elif choice1 == "hold":
            print(f"Player 1 chose to not roll the dice. Player's final score is: {score1}")
            break    
        else:
            print("Please choose between roll or hold")
    print("2nd player's turn")
    score2 = 0
    while True: 
        choice2 = input("Do you wanna roll or hold?: ").lower()
        if choice2 == "roll":
            player2 = random.randint(1,6)
            print(f"Player 2 got {player2}")
            if player2 == 1:
                score2 = 0
                print(f"Ug-oh. Your score is {score2}")
                break    
            else:    
                score2 += player2
                print(f"New score is:{score2}")
                if score2 > score1:
                    print(f"Player 2 has already overtaken Player 1. player 2 won with a score of {score2}")
        elif choice2 == "hold":
            print(f"Player 2 chose to not roll the dice. Player's final score is: {score2}")
            break    
        else:
            print("Please choose between roll or hold")
        
    if score1 > score2:
        print("Player 1 has won")
    else:    
        print("It's a tie")
    
        
pig()


