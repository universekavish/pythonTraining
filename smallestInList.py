# FUNCTION TO CREATE LIST
def createList(x) :
	l = []
	
	i = 0
	while i < x :
		number = int(input('Enter elements: '))
		l.append(number)
		i = i + 1
	return l
	
# SMALLEST ITEM IN LIST AND ITS POSITION
def smallest() :
	i = 1
	smallest = createdList[0]
	while i < x :
		if createdList[i] < smallest :
			smallest = createdList[i]
		i = i + 1
	print(smallest) 
	
#MAIN APP BEGINS HERE
x = int(input('Enter number of elements: '))

createdList = createList(x)
print(createdList)

smallest = smallest()

print(smallest)
