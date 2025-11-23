#project 5 - AI bluff game
import random
print("Welcome to AI bluff game")

my_score = 0
comp_score = 0
times_lied = 0
times_truth = 0
suspicion = 0

comp1 = "bluff"
comp2 = "not bluff"

def bluff():
    global suspicion, times_lied, times_truth, my_score, comp_score

    while True:
        player_roll = random.randint(1, 6) 
        print("\nYour real roll:", player_roll) #computer doesn't know this value
        
        while True:
            player_choice = input("Choose the number you want the computer to know (1-6), or q to quit: ")
            if player_choice.lower() == "q":
                print("\nFinal scores:")
                print("You:", my_score)
                print("Computer:", comp_score)
                return

            try:
                player = int(player_choice)
                if player < 1 or player > 6:
                    print("Enter a number only between 1 to 6")
                else:
                    break
            except ValueError:
                print("Enter only an integer between 1 to 6")

        comp_roll = random.randint(1, 6)
        round_suspicion = 0

        #rules
        if comp_roll == player:
            round_suspicion = round_suspicion + 10

        if comp_roll < player:
            round_suspicion = round_suspicion + 5

        if comp_roll > player:
            round_suspicion = round_suspicion + 10

        if player == 1:
            round_suspicion = round_suspicion + 15

        if player == 6:
            round_suspicion = round_suspicion + 5

        if player == 2:
            round_suspicion = round_suspicion + 5

        if player == 3 or player == 4 or player == 5:
            round_suspicion = round_suspicion - 10

        round_suspicion = round_suspicion + (times_lied * 3)
        round_suspicion = round_suspicion - (times_truth * 2)

        if round_suspicion < 0:
            round_suspicion = 0

        suspicion = suspicion + round_suspicion

        if suspicion >= 20:
            decision = comp1   #bluff
        else:
            decision = comp2   #not bluff

        print("Computer roll: ", comp_roll)
        print("Computer's decision: ", decision)

        if player != player_roll:
            lied = True
        else:
            lied = False

        if decision == comp1:
            if lied:
                print("Computer caught your lie. Computer wins this round.")
                comp_score += 1
                times_lied += 1
                print("The pressure is increasing. Be aware :) ")
            else:
                print("You were honest. Computer wrongly accused you. You win this round.")
                my_score =+ 1
                times_truth += 1
                print("Great.")
        else:   
            if lied:
                print("You lied and got away with it. You win this round.")
                my_score =+ 1
                times_lied =+ 1
            else:
                print("You told the truth and computer trusted you. Round is calm.")
                times_truth = times_truth + 1

        print("Suspicion (total): ", suspicion)
        print("Times lied: ", times_lied)
        print("Times told truth: ", times_truth)
        print("Score -> You: ", my_score, "| Computer: ", comp_score)

bluff()


        
        
            
        
        

          
            


    