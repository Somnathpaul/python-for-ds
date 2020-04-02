# student class with their properties

class Student:
  def __init__(self, name, age, grade):
    self.sname = name
    self.sage = age
    self.sgrade = grade
  
  # get student details method

  def get_student_name(self):
    return self.sname
  
  def get_student_age(self):
    return self.sage

  def get_student_grade(self):
    return self.sgrade
  
  # update student details method

  def update_student_name(self, name):
    self.sanme = name
  
  def update_student_age(self, age):
    self.sage = age
  
  def update_student_grade(self, grade):
    self.sgrade = grade

# course class to add students into it

class Course:
  def __init__(self, name, max_students):
    self.cname = name
    self.max_std = max_students
    self.students = []
    self.no = 0

  def add_students(self, student):
    if len(self.students) < self.max_std:
      self.students.append(student)
      return True
    return False
  
  def show_all_students(self):
     for x in self.students:
       print(self.no + 1 , x.sname, x.sage, x.sgrade)
       self.no = self.no + 1

  def get_course_name(self):
    print( self.cname  )



# instance
s1 = Student("Somnath", 22, "A")
#print( somnath.get_student_name() )
#print( somnath.get_student_grade() )

s2 = Student("Brad", 55, "C")
#print( brad.get_student_name())
#print( brad.get_student_grade() )

s3 = Student("Robin", 55, "C+")
s4 = Student("Jill", 55, "C")

s5 = Student("Robin", 75, "B")
s6 = Student("Drik", 85, "B+")
s7 = Student("Natasha", 95, "A+")
s8 = Student("Olark", 99, "A+")
# ----------------------------------------

course_cs = Course("CS", 10)

course_cs.add_students(s1)
course_cs.add_students(s2)
course_cs.add_students(s3)
course_cs.add_students(s4)

course_cs.get_course_name()
print(course_cs.show_all_students())
#------------------------------------------

course_bca = Course("BCA", 10)

course_bca.add_students(s5)
course_bca.add_students(s6)
course_bca.add_students(s7)
course_bca.add_students(s8)

course_bca.get_course_name()
print(course_bca.show_all_students())
  