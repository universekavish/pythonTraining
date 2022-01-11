def Merge(dict1, dict2 ) :
	res = {**dict1, **dict2}
	return res	

'''
# Using | in latest version of python
def Merge2(dict1, dict2) :
	res = dict1 | dict2
	return res
'''

dict1 = {'a' : 1, 'b' : 2}
dict2 = {'c' : 3, 'd' : 4}

dict3 = Merge(dict1, dict2)
#dict4 = Merge2(dict1, dict2)

print('dict3', dict3)
#print('dict4', dict4)
