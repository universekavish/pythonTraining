rows = int(input('Enter number of rows: '))
cols = int(input('Enter number of columns: '))

i = 0; j = 0

l = []

while i < rows :
	while j < cols :
		print('Enter l[', i, '][', j, '] th element: ')
		number = int(input())
		l[i].append(l[j])
		j = j + 1
	i = i + 1
	
		
print(l)
