# Logan White 05//10/2024
# 05-10-2024_D2L_Final.py
# Final Project D2L
# CC BY-NC-ND 4.0
# Imports
# Classes
class patients:
  def __init__(self, name_F, name_M, name_L, date, address, zip_Code, em_contact_name, em_contact_num):
    self.name_F = name_F
    self.name_M = name_M
    self.name_L = name_L
    self.date = date
    self.address = address
    self.zip_Code = zip_Code
    self.em_contact_name = em_contact_name
    self.em_contact_num = em_contact_num

  def name_F_Get(self)
    return self.name_F
    
  def name_M_Get(self)
    return self.name_M
    
  def name_L_Get(self)
    return self.name_L
    
  def date_Get(self)
    return self.date
    
  def address_Get(self)
    return self.address
  
  def zip_Code_Get(self)
    return self.zip_code
    
  def em_contact_name_Get(self)
    return self.em_contact_name
  
  def em_contact_num_Get(self)
    return self.em_contact_num
  
  def get_all(self)
    print(f"The Patient is {self.name_L}, {self.name_F)} {self.name_M}\nAddress: {self.address}, {self.zip_Code}\nBirthdate: {self.date}\nEmergency Contact: {self.em_contact_name}, Phone: {self.em_contact_num}")

class procedures:
  def __init__(self, patient, procedure, practitioner, charge)
    self.patient = patient
    self.procedure = procedure
    self.practitioner = practitioner
    self.charge = charge
    
  def get(self):
    print(f"{self.patient} is having a {self.procedure}. {self.practitioner} is doing the {self.procedure}. The Cost of the {self.procedure} is ${self.charge}")

# Variables
check_dict = {'1':31, '2':29, '3':31, '4':30, '5':31, '6':30, '7':31, '8':31, '9':30, '10':31, '11':30, '12':31}


# Functions
def birthdate_input():
  month = input("Birth month? \n\t► ")
  day = input("Birth day? \n\t► ")
  year = input("Birth year? \n\t► ")
  while (not isinstance(month, int)) or (0 >= month > 12):
    try:
      month = int(month)
    except:
      print("Please Use Numbers. And make sure you are inputing an actual month. (e.g. November is 11)")
      month = input("Birth month? \n\t► ")
  while not isinstance(year, int):
      try:
        year = int(year)
      except:
        print("Please Use Numbers. (e.g. two-thousand is 2000)")
        month = input("Birth year? \n\t► ")
  while (not (0 < day <= check_dict[str(month)]）s):
    while not isinstance(day, int):
          try:
            day = int(day)
          except:
            print("Please Use Numbers. Ensure you are putting in a day that exists within the month inputted. (e.g. twenty-first is 21)")
            day = input("Birth day? \n\t► ")

  return (f"{month}/{day}/{year}")


def main()
  patient = patients(input("First Name\n\t►"),input("Middle Name\n\t►"),input("Last Name\n\t►"),birthdate_input(),input("Address\n\t►"),input("Zip Code\n\t►"),input("Emergency Contact Name\n\t►"),input("Emergency Contact Phone Number \n\t►"))
  procedure1 = procedures(, , , )
  procedure2 = procedures(, , , )
  procedure3 = procedures(, , , )

  patient.get_all
  print("\n\nProcedures")
  procedure1.get()
  procedure2.get()
  procedure3.get()
  
  
# Code
main()
