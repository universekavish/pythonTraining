# link to GFG Problem
#https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/

def dictionary() :
	key_value = {}
	
	key_value[2] = 56
	key_value[1] = 2
	key_value[5] = 12
	key_value[4] = 24
	key_value[6] = 18
	key_value[3] = 323
	
	print('Task 1  : ')
	print('keys are : ')
	
	for i in sorted(key_value.keys()) :
		print(i, end = ' ')
		
	print('\nTask 2 : ')
	print('sorted key and values are : ')
	
	for i in sorted(key_value) :
		print('(', i, ',', key_value[i], ')', end = ' ')
		
	print('\nTask 3 : ')
	print('keys and values sorted in alphabatical order by values : ')
	print(sorted(key_value.items(), key = lambda kv : (kv[1], kv[0])))
	
def main() :
	dictionary()
	
if __name__ == '__main__' :
	main()
	

