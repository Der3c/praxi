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

#start on page 65	
