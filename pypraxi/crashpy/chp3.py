bicycles = ['trek', 'cannondale', 'specialized', 'fuji']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1].upper())
#This is a quick way to access last item in a list aka haxzores
print(bicycles[-1])

#This will add the element to the argument as the first element
bicycles[0] = "BMC"
print(bicycles)

#This will add an argument to the end of a list
bicycles.append('Surly')
print(bicycles)

#This will insert at a speicif spot
bicycles.insert(2, 'Scott')
print(bicycles)

#This will delete a specified in a list
del bicycles[4]
print bicycles

#pop() removes an item from a list but allows you to work with it. Add position pop(3) to remove specific item
pop_bicycles = bicycles.pop()
print pop_bicycles

#can remove an item by value .remove("name")
bicycles.append('Surly')
print bicycles
bicycles.remove('Scott')

