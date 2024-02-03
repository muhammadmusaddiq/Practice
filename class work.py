class student:
     name = ""
     gear = 0
     
     
# create object of class
student1 = student()

#access attributes and assign new values
student.subject = "Physics"
student1.name = "M.MUsaddiq"

print(f"Name: {student1.name}, Subject: {student.subject} ")

# Python3 program to
# demonstrate instantiating
# a class
class Human:
	# A simple class
	# attribute
	attr1 = "Musaddiq"
	attr2 = "student"

	# A sample method
	def fun(self):
		print("I'm a", self.attr1)
		print("I'm a", self.attr2)
# Driver code
# Object instantiation
Rodger = Human()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()
class Python:
	def __init__(self, name, company):
		self.name = name
		self.company = company
	def show(self):
		print("Hello my name is " + self.name+" and I" +
			" Study in  "+self.company+".")
obj = Python("Musaddiq", "Bano Qabil")
obj.show()

# create a class
class Room:
    length = 0.0
    breadth = 0.0
    
    # method to calculate area
    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)

# create object of Room class
study_room = Room()

# assign values to all the attributes 
study_room.length = 42.5

class Employee:
    def __init__(self, name, emp_id, salary, department):
        self.name = name
        self.id = emp_id
        self.salary = salary
        self.department = department

    def calculate_salary(self, salary, hours_worked):
        overtime = 0
        if hours_worked > 50:
            overtime = hours_worked - 50
        self.salary = self.salary + (overtime * (self.salary / 50))

    def assign_department(self, emp_department):
        self.department = emp_department

    def print_employee_details(self):
        print("\nName: ", self.name)
        print("ID: ", self.id)
        print("Salary: ", self.salary)
        print("Department: ", self.department)
        print("----------------------")


employee1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
employee2 = Employee("JONES", "E7499", 45000, "RESEARCH")
employee3 = Employee("MARTIN", "E7900", 50000, "SALES")
employee4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

print("Original Employee Details:")
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()
employee4.print_employee_details()

# Change the departments of employee1 and employee4
employee1.assign_department("OPERATIONS")
employee4.assign_department("SALES")

# Now calculate the overtime of the employees who are eligible:
employee2.calculate_salary(45000, 52)
employee4.calculate_salary(45000, 60)

print("Updated Employee Details:")
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()
employee4.print_employee_details()
study_room.breadth = 30.8

# access method inside class
study_room.calculate_area()
