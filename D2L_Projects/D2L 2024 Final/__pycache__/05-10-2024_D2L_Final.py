# Logan White 05/10/2024
# 05-10-2024_D2L_Final.py
# Final Project D2L
# CC BY-NC-ND 4.0
# Imports
import datetime
from patients import patients
from procedures import procedures
# Classes
# Variables
check_dict = {'1':31, '2':29, '3':31, '4':30, '5':31, '6':30, '7':31, '8':31, '9':30, '10':31, '11':30, '12':31}
today_ref = datetime.datetime.now()
year_ref = today_ref.strftime("%Y")

# Functions
def birthdate_input():
  exit_loop = False
  while not exit_loop:
    month = input("Birth month? \n\t► ")
    while not(isinstance(month, int)):
      try:
        month = int(month)
      except:
        print("Please Use Numbers. (e.g. November is 11)")
        month = input("Birth month? \n\t► ")
    
    month = int(month)
    if (month > 12 or month < 0) and isinstance(month, int):
      while month > 12 or month <= 0:
        print("Ensure You have inputted a real month (e.g. 1 to 12)")
        month = int(input("Birth month? \n\t► "))

    year = input("Birth year? \n\t► ")
    while not isinstance(year, int):
      try:
        year = int(year)
      except:
        print("Please Use Numbers. (e.g. two-thousand is 2000)")
        year = input("Birth year? \n\t► ")
      
    if isinstance(year, int):
      while year > int(year_ref) or year < 0:
        print(f"Ensure you have inputted a year between 0 and {year_ref}")
        year = int(input("Birth year? \n\t► "))
    
    day = input("Birth day? \n\t► ")
    while not isinstance(day, int):
      try:
        day = int(day)
      except:
        print("Please Use Numbers. Ensure you are putting in a day that exists within the month inputted. (e.g. twenty-first is 21)")
        day = input("Birth day? \n\t► ")
  
    while not ((0 < int(day)) and (int(day) <= int(check_dict[str(month)]))):
      print(f"Ensure You have inputted a real day (e.g. 1 to {check_dict[str(month)]})")
      day = int(input("Birth day? \n\t► "))
      print(day)
    
    date = (datetime.datetime(year, month, day)).strftime('%B %d, %Y')
    exit_loop = ('y' in input(f"Is the following birthdate correct: \n\t {date} y/n\n\t ► " ).lower())
  return (datetime.datetime(year,month,day).strftime('%Y-%m-%d'))
  

def main():
  patient = patients(input("First Name\n\t► "), input("Middle Name\n\t► "), input("Last Name\n\t► "), birthdate_input(), input("Address\n\t► "), input("Zip Code\n\t► "), input("City\n\t► "), input("State\n\t► "), input("Emergency Contact Name\n\t► "), input("Emergency Contact Phone Number \n\t► "))
  procedure1 = procedures((today_ref.strftime('%Y-%m-%d')),"Physical Exam", "Dr. Irvine", 250.00 )
  procedure2 = procedures((today_ref.strftime('%Y-%m-%d')), "X-ray", "Dr. Jamison", 500.00)
  procedure3 = procedures((today_ref.strftime('%Y-%m-%d')), "Blood test", "Dr. Smith", 200.00)

  print('\n\n\n')
  print(f'''The Patient is {patient.name_L_Get()}, {patient.name_F_Get()} {patient.name_M_Get()}\n
        Address: {patient.address_Get()}, {patient.zip_Code_Get()}, {patient.city_Get()}, {patient.state_Get()}\n
        Birthdate: {patient.date_Get()}\n
        Emergency Contact: {patient.em_contact_name_Get()}, Phone: {patient.em_contact_num_Get()}''')

  print(f"\nProcedures")
  procedure1.get()
  procedure2.get()
  procedure3.get()
  print(f"the total cost of all procedures is ${(procedure1.get_charge() + procedure2.get_charge() + procedure3.get_charge()):.2f}")
  

# Code
main()


"""
def get_all(self):


class patients:
  def __init__(self, name_F, name_M, name_L, date, address, zip_Code, city, state, em_contact_name, em_contact_num):
    self.name_F = name_F
    self.name_M = name_M
    self.name_L = name_L
    self.date = date
    self.address = address
    self.zip_Code = zip_Code
    self.city = city
    self.state = state
    self.em_contact_name = em_contact_name
    self.em_contact_num = em_contact_num

  def name_F_Get(self):
    return self.name_F
    
  def name_M_Get(self):
    return self.name_M
    
  def name_L_Get(self):
    return self.name_L
    
  def date_Get(self):
    return self.date
    
  def address_Get(self):
    return self.address
  
  def zip_Code_Get(self):
    return self.zip_Code

  def city_Get(self):
    return self.city
  
  def state_Get(self):
    return self.state
  def em_contact_name_Get(self):
    return self.em_contact_name
  
  def em_contact_num_Get(self):
    return self.em_contact_num
  
  def get_all(self):
    print(f"The Patient is {self.name_L}, {self.name_F} {self.name_M}\nAddress: {self.address}, {self.zip_Code}, {self.city}, {self.state}\nBirthdate: {self.date}\nEmergency Contact: {self.em_contact_name}, Phone: {self.em_contact_num}")
  
  def name_F_Set(self, name_F):
    self.name_F = name_F
    
  def name_M_Set(self, name_M):
    self.name_M =name_M
    
  def name_L_Set(self, name_L):
    self.name_L =name_L
    
  def date_Set(self, date):
    self.date =date
    
  def address_Set(self, address):
    self.address = address
  
  def zip_Code_Set(self, zip_Code):
    self.zip_Code = zip_Code

  def city_Set(self, city):
    self.city = city
  
  def state_Set(self, state):
    self.state = state
  def em_contact_name_Set(self, em_contact_name):
    self.em_contact_name =em_contact_name
  
  def em_contact_num_Set(self, em_contact_num):
    self.em_contact_num  = em_contact_num


class procedures:
  def __init__(self, date, procedure, practitioner, charge):
    self.date = date
    self.procedure = procedure
    self.practitioner = practitioner
    self.charge = charge
    
  def get(self):
    print(f"On {self.date} a {self.procedure} is being done by {self.practitioner}. The Cost of the {self.procedure} is ${self.charge}")
"""