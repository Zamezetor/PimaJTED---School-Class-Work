# Logan White 02/13/2024
# 02-13-2024_Operational_Lesson_Loops.py
# loop practice
# CC BY-NC-SA 4.0
# Imports 
# Variables 
# Functions

def loopy():
    print("\nSolo 1")
    for i in range(6):
        temp1 = ""
        for o in range(10):
            temp1 += str(str(o) + " ")
        print(temp1)

    print("\nSolo 2\n\n")
    for i in range(10):
        temp2 = ""
        for o in range(10):  
            temp2 += str(str(i) + " ")
        print(temp2)
    
    print("\nSolo 3 \n\n")
    temp3 = ""
    for i in range(10):
        temp3 +=(str(i) + " ")
        print(temp3)

    print("\nSolo 4 \n\n")    
    temp4 = [0,1,2,3,4,5,6,7,8,9]
    temp5 = 0
    for i in range(len(temp4),0,-1):
        print(2 * (" " * temp5),end = "")
        for o in range(len(temp4)):
            print((temp4[o]),end = " ")  
        temp5 += 1  
        temp4.pop(i-1)
        print("\n", end = "")

    print("\nSolo 5 \n\n")
    temp6 = 10
    for i in range(10):
        for u in range(0,i,1):
            temp6 += 1
            print(temp6 - 1, end = " ")
        print("\n", end = "")


# Code
loopy()
