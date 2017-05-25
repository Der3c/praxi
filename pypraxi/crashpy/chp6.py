#Dictionaries are wrapped in {}
#A dictionairy is  a collection of key-value pairs. Each key is connected to a value
#Values can be strings, numbers, list, or even another dictionary. 

me = {'name': 'Derek', 'birth_month': 'June', 'guitar': 'Tele', 'bike': 'Trek'}
print(me['guitar'])

#add to dictionary by calling the dictionary name and using [] = value
#Can start with an empty dictionary and add

you = {}
you['name'] = 'You'
you['bike'] = 'Surly'
you['guitar'] = 'Strat'
print(you)

#Delete a ket value pair by
del you['guitar']
print(you)

#Loop thorugh with multiple variable
for key, value in me.items():
	print('\nKey: ' + key)
	print('Value: ' + value)