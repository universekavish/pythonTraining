# First approach
def returnSum(myDict) :
	list = []
	for i in myDict :
		list.append(myDict[i])
	res = sum(list)
	return res

# Second approach
def returnSum2(dict) :
	sum = 0
	for i in dict.values() :
		sum = sum + i
	return sum 
	
# Third approach
def returnSum3(dict) :
	sum = 0
	for i in dict :
		sum = sum + dict[i]
	return sum
	
dict = {'a' : 100, 'b' : 200, 'c' : 300} 
print('Sum : ', returnSum(dict))

print('Sum : ', returnSum2(dict))

print('Sum : ', returnSum3(dict))
