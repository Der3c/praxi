#Can use the range() function to generate a list of numbers. range() stops counting before the last vale
#tro print 1-5 would need;
for value in range(1,6):
	print(value)

#can turn a range into a list by pasisng the list() method
numbers = list(range(1,6))
print(numbers)

#can use range() to skip numbers in a given range
even_numbers = list(range(2,13,2))
print(even_numbers)

#Lets make a list of the square of the first ten numbers
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)

#to reduce lines of code can use
reduce = []
for value in range(1,11):
	reduce.append(value**2)
print(reduce)

#List comprehension is awesome. We can exexute all of the above on the same line:
list_comp = [value**2 for value in range(1,11)]
print(list_comp)


#summing the first 1MM numbers
mil = list(range(1,1000001))
print min(mil)
print max(mil)
print sum(mil)

#prints odd numbers to 20
for odd in range(1,21,2):
	print(odd)

#prints multiples of 3
for threes in range(3,30,3):
	print(threes)

#a list of the cube of the first 10 numbers
cubes_list = [value**2 for value in range(1,11)]
print(cubes_list)	

#How to slice a list - Without an index python will start at the beginning or end respectively 
bicycles = ['trek', 'cannondale', 'specialized', 'fuji', 'Surly']
print(bicycles[0:2])

#Copy a list by
bikes = bicycles[:]
print(bikes)

#tuples are immutable list - () instead of []
Rides = ('Rando', 'Crit')
print(Rides)
for ride in Rides:
	print(ride)
Rides = ('Enduro', 'Brevet', 'Rando')
print(Rides)	

