# Balneo CSC, Logan White, Nick Russell, Zachary Jenkins, Brody Villaman, Harry Barsiwal 01/23/2024
# 01-23-2024_number_guess_revised.py
# number guessing game
# CC BY-NC-SA 4.0
# Imports
import random


# Variables


# Functions
def game_mode_select():  # Allows user to choose difficulty
    game_mode = 0
    print("Greetings, Which difficulty would you like to play? \n"
          "Easy - No Guess Limit, You choose the range of numbers\n"
          "Medium - 10 Guess Limit, Small Predetermined range of numbers\n"
          "Hard - 10 Guess Limit, Predetermined range of numbers \n")
    choice = input()
    if 'E' in choice.upper():
        game_mode = 1
    elif 'M' in choice.upper():
        game_mode = 2
    elif 'H' in choice.upper():
        game_mode = 3
    game(game_mode)  # calls game() with proper difficulty


def game(gm):
    guesses = 0
    guess = 0
    if gm == 1:  # easy difficulty
        start_num = int(input("What number should be the lower limit? "))
        end_num = int(input("What number should be the upper limit? "))
        number = random.randint(start_num, end_num)
        while guess != number:
            guess = int(input(f"Choose a number between {start_num} and {end_num}.    "))
            guesses += 1
            if guess > number:
                print("Too High, Guess again.\n\n")
            elif guess < number:
                print("Too Low, Guess again.\n\n")
        print(f"Correct! {number} was the number. You took {guesses} guesses to get the number.")

    elif gm == 2:  # medium difficulty
        print("The range of numbers is 1 to 100, you have 10 guesses")
        number = random.randint(1, 100)
        while guess != number and guesses <= 9:
            guess = int(input(f"Choose a number between 1 and 100.  "))
            guesses += 1
            if guess > number:
                print("Too High, Guess again.\n\n")
            elif guess < number:
                print("Too Low, Guess again.\n\n")
        if guess == number:
            print(f"Correct! {number} was the number. You took {guesses} guesses to get the number. You had")
        else:
            print(f"Sorry but you exceeded the amount of Guesses allowed. The number was {number}. ")

    elif gm == 3:  # hard difficulty
        print("The range of numbers is 1 to 1000, you have 10 guesses")
        number = random.randint(1, 1000)
        while guess != number and guesses <= 9:
            guess = int(input(f"Choose a number between 1 and 1000.  "))
            guesses += 1
            if guess > number:
                print("Too High, Guess again.\n\n")
            elif guess < number:
                print("Too Low, Guess again.\n\n")
        if guess == number:
            print(f"Correct! {number} was the number. You took {guesses} guesses to get the number. You had")
        else:
            print(f"Sorry but you exceeded the amount of Guesses allowed. The number was {number}. ")

    retry()


def retry():  # asks the user if they want to replay
    play_again = input("would you like to play again?  Y/N ")
    if "Y" in play_again.upper():
        game_mode_select()
    elif "N" in play_again.upper():
        print("Thank you for playing")


# Code
game_mode_select()
