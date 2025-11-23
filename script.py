import random
from email.quoprimime import header_check


'''def play():
    user= input("choose rock, paper or scissors: ")
    computer= random.choice(["rock", "paper", "scissors"])
    print("computer chose: " + computer)
    if user==computer:
        return "IT'S A TIE"
    if user=="rock" and computer == "scissors" or user=="paper" and computer=="rock" or user=="scissors" and computer=="paper":
        return "USER WON"
    return "USER LOST"

def play_again():
    user_points = 0
    comp_points = 0

    winning_mapping =  { 'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
    while True:
        
        user= input("choose rock, paper or scissors: ").lower()
        comp= random.choice(["rock", "paper", "scissors"])
        print(f'computer chose {comp}')
        if user==comp:
            print("It's a tie")
            continue
        if winning_mapping[user] == comp:
            user_points += 1
            print(f"user's points: {user_points} and computer's points: {comp_points}")
            print("user won the round!!")
            continue
        
        else:
            comp_points += 1
            print(f"computer's points: {comp_points} and user points: {user_points} ")
            print("ug-oh computer won the round")
            continue
        
        if user_points == 5:
            print("User won")
            break
        elif comp_points == 5:
            print("Computer won")
            break '''

#project 2 - hangman
def hangman():
    words= ['python', 'java', 'apple', 'banana', 'guava', 'onion', 'vibhu', 'archit', 'friends']
    word = random.choice(words).lower()
    word_letters = set(word)
    guessed_letters = set()
    attempts= 7

    print("Welcome to Hangman!")


    while len(word_letters) > 0 and attempts > 0:
        print(f"You have {attempts} guesses left")
        print("Guessed letter: " + ",".join(sorted(guessed_letters)))

        word_display = [letter if letter in guessed_letters else "_" for letter in word]
        print("Current word: ", "".join(word_display))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single alphabet: ")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter BAKA!")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)
            print("Correct!")
        else:
            attempts -= 1
            print("Wrong guess")

    if attempts ==  0:
        print(f"You Died! The word was {word}")
    else:
        print(f"Congratulations! You are alive. The word was {word}.")

hangman()





