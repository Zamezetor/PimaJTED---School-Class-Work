# Logan White 01/30/2024
# 01-30-2024_Triangle_Sides.py
# Operational lesson #2 calculate sides of triangle 
# CC BY-NC-SA 4.0
# Imports 
import math
# Variables 
# Functions
def choose():
    chosen = input("The Pythagorean Theorem is a^2 + b^2 = c^2\nDo you have:\n 1) a and b\n 2) a and c\n 3) b and c\n\n")
    try:
        chosen = int(chosen)
    except:
        print("Please Enter 1,2, or 3 From the Above Options")
    if chosen == 1:
        print(math.sqrt((int(input("Side a is: ")) ** 2) + ((int(input("Side b is: "))) ** 2)))
    if chosen == 2:
        print(math.sqrt((int(input("Side c is: ")) ** 2) - ((int(input("Side a is: "))) ** 2)))
    if chosen == 3:
        print(math.sqrt((int(input("Side c is: ")) ** 2) - (int(input("Side b is: ")) ** 2)))


# Code 
choose()