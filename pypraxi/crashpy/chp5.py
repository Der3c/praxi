# to check whether a value is is within a list use the key word 'in'
a = [1, 2, 3, 4, 5, 6]
3 in a

#to check in value is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
	print('true')

#if statements synax is like
	# if conditional_test:
		#do something

age = 17
if age >= 18:
	print("You are old enough to vote!") 
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")	

#if else chain works like follows:
age = 12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")	
#Note python does not require else at the end of a chain

#Python does not run beyond a first successful test test in an elif chain. Use just 'if' for multiple conditions
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings: 
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings: 
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings: 
	print("Adding extra cheese.")

#Can make a loop using for:
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

#special list practice
user_names = ['admin', 'Derek', 'Amanda', 'Selah', 'Atticus']
for user_name in user_names:
	if user_name == 'admin':
		print('Hello, admin, would you like a status upate?')
	else:
		print("Hello " + user_name + "!")	