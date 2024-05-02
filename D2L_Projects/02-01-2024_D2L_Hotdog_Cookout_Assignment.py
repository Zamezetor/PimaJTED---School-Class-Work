# Logan White 02/01/2024
# 02-01-2024_D2L_Hotdog_Cookout_Assignment.py
# Hotdog Cookout Assignment for D2L
# CC BY-NC-SA 4.0
# Imports
import math


# Variables


# Functions
def main():
    total_hotdogs = getTotalHotDogs()
    showResults(total_hotdogs)

def getTotalHotDogs():
    people = int(input("How Many People are Attending the Cookout? \n"))
    hotdogs = int(input("How Many Hotdogs is Each Person Given? \n"))
    return (people * hotdogs)

def showResults(total):
    dogs  = 10
    buns = 8
    leftover_buns = total % buns
    leftover_hotdogs = total % dogs
    hotdog_packages =  math.ceil(total / dogs)
    bun_packages =  math.ceil(total / buns) 
    print(f"You Will Need {bun_packages} Packages of Hotdog Buns and {hotdog_packages} Packages of Hotdogs to Feed all Your Guests at the Cookout.\n In Total You Will Need to Make {total} Hotdogs.\n In the End You Will Have {leftover_buns} Leftover Buns and {leftover_hotdogs} Leftover Hotdogs ")


# Code
main()

