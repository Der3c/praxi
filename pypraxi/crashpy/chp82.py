#Functions can be used to build dictionaries 
def build_person(first, last):
	person = {'first': first, 'last': last}
	return person
musician = build_person('Jim', 'Heath')
print(musician)

#can pass a list by building a variable as a listg and passing as argument
#usernames = ['name1', 'name2', 'name3']
#greet_users(usernames)	- assumes function that greets users for example

#Prevent a function from modifying a list by inserting a slice notation [:]
#function_name(list_name[:])

#pass an arbitrary number of arguments with *. Must be placed last in a function
def make_pizza(*toppings):
	print(toppings)
make_pizza('pepperoni', 'mushrooms', 'olives')	

#import entire modules with the 'import' command
#call a function by module_name.function_name()

#import individual functions with from module_name import function_0, function_1, function_2
