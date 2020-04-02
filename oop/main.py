# object oriented programing

class Maths:
  def __init__(self, name, age):
    self.fname = name
    self.fage = age

  def get_name(self):
    return self.fname

  def get_age(self):
    return self.fage

  def update_age(self, age):
    self.fage = age
  
  def update_name(self, name):
    self.fname = name

  def increment(self, x):
   return x + 1
  
  def decrement(self, x):
    return x - 1

# isinstance
m1 = Maths("python", 21)
print(m1.get_age())
m1.update_age(30)
print(m1.get_age())

m2 = Maths("java", 77)
print(m2.get_name())
m2.update_name("jsp")
print(m2.get_name())

print( m1.increment(2) )
print( m1.decrement(2) )
