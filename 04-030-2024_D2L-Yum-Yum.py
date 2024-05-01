# Logan White 04/30/2024
# 04-030-2024_D2L-Yum-Yum.py
# D2L Yum Yum Burger Lab
# CC BY-NC-SA 4.0
# Imports 
import random
import time


# Variables
# Functions
def main():
    end_Program=False
    #global end_Program
    while not end_Program:
        end_Order = False
        total_Burgers = 0
        total_Fries = 0
        total_Sodas = 0 
        while not end_Order:
            option = input("""What would you like to purchase? 
                        \n 1 -- Yum Yum Burger 
                        \n 2 -- Grease Yum Fries 
                        \n 3 -- Soda Yum 
                        \n Or Would You Like to End Your Order?
                        \n 4 -- End Order
                        \n Enter the number corresponding to the options
                        \n ►  """)
            if int(option) == 1:
                total_Burgers += int(input("How Many Yum Yum Burgers Do You Want? \n →  "))
            elif int(option) == 2:
                total_Fries += int(input("How Many Yum Yum Fries Do You Want? \n →  "))
            elif int(option) == 3:
                total_Sodas += int(input("How Many Soda Yums Do You Want? \n →  "))
            else:
                print("Ending Order")
                end_Order = True
        print("Processing Recipt")
        time.sleep(random.randint(1,5))
        print(f""" Your Order is as Follows:
            \n {total_Burgers} Yum Yum Burgers at ${.99 * total_Burgers}
            \n {total_Fries} Yum Yum Fries at ${.79 * total_Fries}
            \n {total_Sodas} Soda Yum at ${1.09 * total_Sodas}
            \n Your Total is ${((.99 * total_Burgers) + (.79 * total_Fries) + (1.09 * total_Sodas)) * 1.06}""")
        end_Program = "y" in input("""Would You Like To End The Program? y/n \n ►  """).lower()

# Code
main()

