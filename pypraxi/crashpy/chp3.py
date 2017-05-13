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