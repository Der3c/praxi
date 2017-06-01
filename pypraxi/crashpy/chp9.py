#Classes represent model cases and objects are created from instances of a class
class Dog():
	"""Simple model of a dog"""
	def __init__(self, name, age):
		"""Initialize name and age atributes"""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting on command"""
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		print(self.name.title() + " rolled over!")

	#self is passed automatically when we create a new instance based on Dog class
				
#Class is a set of instructions on how to make an instance. 
#To access attributes on an instance use dot notation 

my_dog = Dog('Willie', 7)


print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

