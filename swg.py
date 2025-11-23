
#Project 1
#Snake, Water, Gun game
import random
choices = ["Snake", "Water", "Gun"]

def play():
    comp_points = 0
    player_points = 0
    while True:
        player = input("Choose from Snake(s), Water(w) and Gun(g): ").upper()
        comp = random.choice(choices)
        print("Computer chose", comp)
        if player not in ["S", "W", "G"]:
            print("Choose from S, W, G")
            continue

        if (player == "S" and comp == "Gun") or \
                (player== "G" and comp == "Water") or \
                (player == "W" and comp == "Snake"):
                comp_points += 1
                print("Computer gets +1", "Player:" , {player_points} , "Computer:",  {comp_points})

        elif(player == "S" and comp == "Water") or \
                (player == "W" and comp == "Gun") or \
                (player == "G" and comp == "Snake"):

                player_points += 1
                print(f"User gets +1", "Player:" , {player_points} , "Computer:",  {comp_points})
        elif (player == "S" and comp == "Snake") or \
                (player == "W" and comp == "Water") or \
                (player == "G" and comp == "Gun"):
                print("It\'s a tie.")


        if comp_points == 5:
                print("Computer wins!")
                break
        elif player_points == 5:
                print("Player wins!")
                break
play()





















