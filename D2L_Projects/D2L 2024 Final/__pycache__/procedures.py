# Logan White 05/10/2024
# procedures.py
# Final Project D2L
# CC BY-NC-ND 4.0
# Classes
class procedures:
  def __init__(self, date, procedure, practitioner, charge):
    self.date = date
    self.procedure = procedure
    self.practitioner = practitioner
    self.charge = charge
    
  def get(self):
    print(f"On {self.date} a {self.procedure} is being done by {self.practitioner}. The Cost of the {self.procedure} is ${self.charge:.2f}")
  
  def get_charge(self):
    return float(self.charge)
  
  def get_date(self):
    return self.date
  
  def get_procedure(self):
    return self.procedure
  
  def get_practitioner(self):
    return self.practitioner