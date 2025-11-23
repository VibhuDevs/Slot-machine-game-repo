#project 6 - Slot Machine
import random

ROWS = 3
COLS = 3
numbers = [1, 2, 3, 4]
balance = 0
bet = 0
def deposit():
    global balance
    deposit = input("Enter your deposit amount: ")
    try:
        deposit = int(deposit)
        if (deposit < 0 or deposit > 1000):
            print("Please enter a valid amount bw 1 and 1000 to deposit")
    except ValueError:
        print("Please enter a valid amount bw 1 and 1000 to deposit")
    balance += deposit
    print(f"Your current balance: {balance}")
deposit()

def bets():
    global bet
    bet = input("Enter bet amount: ")
    try:
        bet = int(bet)
        if bet < 0 or bet > 500:
            print("Enter an amount bw 1 and 500 to bet")
    except ValueError:
        print("Enter a number bw 1 and 500 to bet")
def slot():
    global balance
    global bet
    pattern = []
    for i in range(ROWS):
        row = []
        for j in range(COLS):
            value = random.randint(1,4)
            row.append(value)
            print(value, end = " ")
        print()
        pattern.append(row)
    won = False
    for row in pattern:
        if row[0] == row[1] == row[2]:
            won = True    
            break
    if won:
        print("You won this bet")
        print(" ")
        balance += bet
        print(balance)
    else:
        print("You lost the bet")
        print(" ")
        balance -= bet
        print(balance)
    if balance <= 0:
        print("You are broke")
    bet == 0
while True:
    if balance > 0:
        bets()
    if balance == 0:
        break
    print("*****************")
    input("Press enter to check if you got lucky or not ")
    print("**************")
    slot()

