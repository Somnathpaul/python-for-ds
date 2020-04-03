# employee details
class Employee:
  def __init__(self, name, id_no, role):
    self.e_name = name
    self.e_id_no = id_no
    self.e_role = role
  
  # update employee details methods
  def Update_name(self, name):
    self.e_name = name
  
  def Update_id_no(self, id_no):
    self.id_no = id_no
  
  def Update_role(self, role):
    self.e_role = role
  
  # show all emplyee details
  def All_employee(self):
    print(self.e_id_no, self.e_name, self.e_role)


class Group:
  def __init__(self, name, max_employee):
    self.g_name = name
    self.g_max_employee = max_employee
    self.g_employee = []

  def Add_employee(self, employee):
    if len(self.g_employee) < self.g_max_employee:
      self.g_employee.append(employee)
      return True
    return False
  
  def Show_all_grops(self):
    for x in self.g_employee :
     print(x.e_id_no ,x.e_name)



# instance
drik = Employee("Drik", "01","Jr Developer")
mark = Employee("Mark", "05","Jr Developer")
sana = Employee("Sana", "09","Sr Developer")
brad = Employee("Brad", "011","Marketing")
jill = Employee("Jill", "018","Sales VP")
 # drik.All_employee()

g1 = Group("developers", 10)
g1.Add_employee(drik)
g1.Add_employee(mark)
g1.Add_employee(sana)

g2 = Group("Sales and Marketing", 5)
g2.Add_employee(brad)
g2.Add_employee(jill)

g2.Show_all_grops()
# g1.Show_all_grops()