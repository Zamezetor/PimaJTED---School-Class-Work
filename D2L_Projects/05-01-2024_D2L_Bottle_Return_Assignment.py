# Logan White 05/01/2024
# 05-01-2024_D2L_Bottle_Return_Assignment.py
# D2L Bottle Return Assignment
# CC BY-NC-SA 4.0
# Imports 
# Variables 
# Functions
def main():
    cont = True
    total_pay = 0
    total_bottle = 0
    today_bottle = 0
    counter = 0
    while cont:
        total_bottle = bottle_input(total_bottle,today_bottle,counter)
        total_pay = payout_calc(total_bottle)
        print_info(total_pay,total_bottle)
        cont = ("y" in input("Continue Program? y/n \n\t►  ").lower())


def payout_calc(total_bottle):
    return total_bottle * .10


def bottle_input(total_bottle,today_bottle,counter):
    while counter < 7:
        today_bottle = int(input("How Many Bottles Returned Today? \n\t►  "))
        total_bottle += today_bottle
        counter += 1
    return total_bottle

def print_info(total_pay,total_bottle):
    print(f"Total Bottles Returned -- {total_bottle}\n Total Payout -- ${total_pay}")

# Code
main()

