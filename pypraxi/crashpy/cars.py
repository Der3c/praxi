#normal class setu but with attribute that changes over time odometer
class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		print("This car has " + str(self.odometer) + " miles on it.")

	def update_milage(self, mileage):
		"""Rejects mileage rollback"""
		if mileage >= self.odometer:
			self.odometer = mileage
		else:
			print("You cant roll back the odometer knucklehead")	

my_new_car = Car('ford', 'f-150', 2015)
print(my_new_car.get_descriptive_name())
#Start with 0 odometer. Can access directly through instance like so
my_new_car.odometer = 352
my_new_car.read_odometer()

#Can create methods to update attributes for you. See above line 16 
my_new_car.update_milage(482)
my_new_car.read_odometer()

#Can add logic to method as in line 17+

