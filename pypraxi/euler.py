#Project Euler Probelm 1 - Find sum of all multiples or 5 or 3 below 1000
#Trying multiple ways

result = sum([x for x in range(1000) if (x % 5 ==0 or x % 3 == 0)])
print(result)

print sum(n for n in range(1,1000) if (n % 5 ==0 or n % 3== 0))

y = 0
for i in range(0,1000):
	if i % 3 == 0 or i % 5 == 0:
		y += i
print(y)





		



