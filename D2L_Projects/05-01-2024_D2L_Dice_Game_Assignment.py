# Logan White 05/01/2024
# 05-01-2024_D2L_Dice_Game_Assignment.py
# D2L Dice Game Assignment
# CC BY-NC-SA 4.0
# Imports 
import random


# Variables 
# Functions
def main():
    end_program = False
    p1 = "No Name"
    p2 = "No Name"
    p1, p2 = player_names(p1, p2)
    while not end_program:
        p1num = 0
        p2num = 0
        winner = "No Name"
        winner = roll_die(p1, p2, p1num, p2num)
        win_display(winner)

        end_program = 'y' in input('Do you want to end program? (yes/no): \n→ ').lower()


def roll_die(p1, p2, p1num, p2num):
    p1num = random.randint(1, 6)
    p2num = random.randint(1, 6)
    print(f'{p1} rolls a {p1num} \n{p2} rolls a {p2num}')
    if p1num == p2num:
        return "Tie"
    elif p1num > p2num:
        return p1
    else:
        return p2
    

def player_names(p1, p2):
    p1 = input("Player One, please enter your name \n ►  ")
    p2 = input("Player Two, please enter your name \n ►  ")
    return p1, p2


def win_display(winner):
    print(f'the winner is {winner}')

    
# Code
main()

