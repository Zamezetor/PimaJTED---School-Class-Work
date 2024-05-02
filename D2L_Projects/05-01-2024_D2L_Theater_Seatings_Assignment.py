# Logan White 05/01/2024
# 05-01-2024_D2L_Theater_Seatings_Assignment.py
# D2L Theater Seating Lab 
# CC BY-NC-SA 4.0
# Imports 
# Variables 
# Functions
def main():
    end_program = False
    while not end_program:
        total_a_seats = -1
        total_b_seats = -1
        total_c_seats = -1
        while not (300 >= total_a_seats >= 0):
            total_a_seats = int(input("Of The 300 Seats In Section A, How Many Seats Were Sold? \n ►  "))
        while not (500 >= total_b_seats >= 0):
            total_b_seats = int(input("Of The 500 Seats In Section B, How Many Seats Were Sold? \n ►  "))
        while not (200 >= total_c_seats >= 0):
            total_c_seats = int(input("Of The 200 Seats In Section C, How Many Seats Were Sold? \n ►  "))

        print(f""" A total of {(total_a_seats) + (total_b_seats) + (total_c_seats)} seats were sold for a total of ${(total_a_seats * 20) + (total_b_seats * 15) + (total_c_seats * 10)} in revenue.
            {total_a_seats} seats in section A were sold for ${20 * total_a_seats}
            {total_b_seats} seats in section B were sold for ${15 * total_b_seats}
            {total_c_seats} seats in section C were sold for ${10 * total_c_seats}""")
        end_program = ('y' in input('Would You Like To End The Program? y/n').lower())
    
# Code
main()


"""A dramatic theater has three seating sections, and it charges the following prices for tickets in each section:
 section A seats cost $20 each, section B seats cost $15 each, and section C seats cost $10 each.
 The theater has 300 seats in section A, 500 seats in section B, and 200 seats in section C. 
 Design a program that asks for the number of tickets sold in each section and then displays the amount of income generated from ticket sales.
 The program should validate the numbers that are entered for each section."""