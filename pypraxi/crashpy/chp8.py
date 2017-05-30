#Define a function with a variable and pass it to the function
#username is a parameter and 'Derek' is an argument
def greetings (username):
	print ("Hello, " + username.title() + "!"" ")
greetings('Derek')	

#Positional arguments are passed with a ',' and evaulated in the order they appear

def baby_names(gender, name):
	print("If we have a " + gender + " we will call them " + name)
baby_names('boy', 'Micah')
baby_names('girl', 'Ada')

#You can pass keyword arguments by direct association
#baby_names(gender='boy', name='Micah')

#Can assign default values as well. Assign default values after paramenters with no defaults
def baby_name(name, gender='boy'):
	print("If we have a " + gender + " we will call them " + name)
baby_name('Micah')

#Unmatched arguments occur when too few or too many agruments are passed to a function

#Function can process data and then return a set of values, aptly names return value
def format_name(first_name, last_name):
	"""Returns a full name in a tidy format. Also I know how to comment within a function!"""
	full_name = first_name + ' ' + last_name
	return full_name.title()
musician = format_name('jimi', 'hendrix')
print(musician)	
#Can add an optional middle name in this instance by using a default value with an empty string and if/else
