# Logan White 05/04/2024
# 05-04-2024_D2L_Classes_Pets.py
# D2L Classes Assignment
# CC BY-NC-SA 4.0
# Imports 
# Variables
# Classes
class pets:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        
    def get(self):
        print(f"{self.name} is a {self.species} that is {self.age} years old.")

    def set(self):
        self.name = input("What Is The Pet's Name \n ► ")
        self.species = input("What Is The Pet's Species \n ► ")
        age_input = input("What Is The Pet's Age \n ► ")
        while not isinstance(age_input, int):
            try:
                age_input = int(age_input)
            except:
                age_input = input("Please Input an Integer\nWhat Is The Pet's Age \n ► ")            
        self.age = age_input
        

# Functions
def main():
    pet = pets("", "", "")
    pet.set()
    pet.get()


# Code
main()

