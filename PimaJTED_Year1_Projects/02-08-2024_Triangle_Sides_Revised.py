# Logan White 02/08/2024
# 02-08-2024_Triangle_Sides_Revised.py
# Operational lesson #3 calculate sides of triangle Revised
# CC BY-NC-SA 4.0
# Imports 
import math


# Variables 
# Functions
def user_input(side, start):
    if start == True:
        return input("The Pythagorean Theorem is a^2 + b^2 = c^2\nDo you have:\n 1) a and b\n 2) a and c\n 3) b and c\n\n\t► ")
    elif side == 1:
        return input("Side a is: ")
    elif side == 2:
        return input("Side b is: ")
    elif side == 3:
        return input("Side c is: ")
 

def side_calc():
    chosen = (user_input(0,True))
    try:
        chosen = int(chosen)
    except:
        print("Please Enter 1,2, or 3 From the Above Options")
        side_calc()
    if chosen == 1:
        side = (math.sqrt((int(user_input(1,False)) ** 2) + ((int(user_input(2,False))) ** 2)))
    elif chosen == 2:
        side = (math.sqrt((int(user_input(3,False)) ** 2) - ((int(user_input(1,False)) ** 2))))
    elif chosen == 3:
        side = (math.sqrt((int(user_input(3,False)) ** 2) - (int(user_input(2,False)) ** 2)))
    return side


def round_sides(num):
    rounded = str(input("Would you like to round the answer \n yes or no \n\t► "))
    if "Y" in rounded.upper():
        places = int(input("How many Places do you want to round to \n e.g. 1.888 rounded to 1 place → 1.9, rounded to 2 places → 1.89\n\t► "))
        print(f'{round(num, places)} is your side length')
    else:
        print(f'{num} is your side length')


def main():
    round_sides(side_calc())


# Code 
main()