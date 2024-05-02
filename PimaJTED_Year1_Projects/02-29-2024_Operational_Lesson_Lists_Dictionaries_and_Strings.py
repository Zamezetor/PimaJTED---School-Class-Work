# Logan White 02/29/2024
# 02-29-2024_Operational_Lesson_Lists_Dictionaries_and_Strings.py
# Lists and Strings Operational Lesson 
# CC BY-NC-SA 4.0
# Imports 
# Variables 
list1 = []
list2 = []
diction = {}
list3 = []
# Functions
def list_1_fill():
    for i in range(5):
        list1.append(input(f"What would you like to input? You have {5 - i} inputs remaining \n ► "))
    print(list1)

def list_2_fill():
    for i in range(5):
        templist = []
        for i in range(int(input("Input an integer for the length of this list \n ► "))):
            templist.append(input(f"What would you like to input? You have used {i} inputs \n ► "))
        list2.append(templist)
    print(list2)

def dictionary_1_fill():
    dict_list = []
    for i in range(3):
            dict_list.append(input(f"What would you like to input? You have {3 - i} inputs remaining \n ► "))
    for i in range(3):
        diction.update({input(f"Input A key for {dict_list[i]}\n ► "):dict_list[i]})
    print(diction)

def list_index():
    for i in range(int(input("Input an integer for the length of this list \n ► "))):
            list3.append(input(f"What would you like to input? You have used {i} inputs \n ► "))

    for i in range(len(list3)):
        print(f"The Value at Index {i} is {list3[i]}")
# Code

#list_1_fill()
#list_2_fill()
#dictionary_1_fill()
#list_index()
