# Logan White 02/06/2024
# 02-06-2024_D2L-Tip-Tax-Total.py
# D2L Tip Tax & Total Lab
# CC BY-NC-SA 4.0
# Imports 
# Variables 
# Functions
def main():
    cost = float(input("How Much Did the Food Cost: $"))
    tax = cost *0.06
    tip = tips(cost)
    total = (round((tip + cost + tax),2))
    print(f"Your Total is ${total}")

def tips(cost):
    if 0.01 <= cost <= 5.99:
        tip = cost * 0.1
    elif 6.00 <= cost <= 12.00:
        tip = cost * 0.13
    elif 12.01 <= cost <= 17.00:
        tip = cost * 0.16
    elif 17.01 <= cost <= 25.00:
        tip = cost * 0.19
    else:
        tip = cost * 0.22
    return tip
# Code
main()