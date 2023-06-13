class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
  self.milton = milton
  def full_time_wage(self,hours):
    return super(Derived,self).calculate_wage()
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00
emp = Employee("Dan")

print full_time_wage(full_time_wage(10))










class Triangle(object):
  def __init__(self,angle1,angle2,angle3,number_of_sides):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        self.number_of_sides = 3 
  def check_angles(angle1,angle2,angle3):
      sum = self.angle1 + self.angle2 + self.angle3
      if sum == 180 :
        return True
      else:
        return False



class Triangle(object):
  number_of_sides = 3
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
    
  def check_angles(self):
    if (self.angle1 + self.angle2 + self.angle3) == 180:
      return True
    else:
      return False

class Equilateral(Triangle):
  angle = 60
  def __init__(self):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
    self.angle = self.angle1 + self.angle2 + self.angle3 



my_triangle = Triangle(90,30,60)
print my_triangle.number_of_sides
print my_triangle. check_angles()
