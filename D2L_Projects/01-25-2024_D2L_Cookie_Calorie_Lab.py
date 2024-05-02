# Logan White 01/25/2024
# 01-25-2024_D2L_Cookie_Calorie_Lab
# D2L Cookie Calories Lab - Calculate The Amount Of Calories Consumed Based Off Of Amount Of Cookies Eaten
# CC BY-NC-SA 4.0
# Imports
# Variables
cookies_eaten = int(input("How Many Cookies Did You Eat: "))
calories_per_serving = int(input("How Many Calories Are In One Serving: "))
cookies_per_serving = int(input("How Many Cookies Are In One Serving: "))
# Functions
# Code
print(f"You Ate {(cookies_eaten/cookies_per_serving)*calories_per_serving} Calories From {cookies_eaten} Cookies")