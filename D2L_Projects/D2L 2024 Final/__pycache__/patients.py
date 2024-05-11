# Logan White 05/10/2024
# patients.py
# Final Project D2L patients method
# CC BY-NC-ND 4.0
# Classes
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