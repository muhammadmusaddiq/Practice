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
study_room.breadth = 30.8

# access method inside class
study_room.calculate_area()
