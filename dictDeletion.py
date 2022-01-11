Dict = {5 : 'Welcome', 6 : 'To', 7 : 'Geeks', 
		'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'},
		'B' : {1 : 'Geeks', 2 : 'Life'}}
		
print('Starting dictionary : ')
print(Dict)

# deleting a key value
del Dict[6]
print('deleting a specific key : ')
print(Dict)

# deleting a key from nested dictionary
del Dict['A'][2]
print('deleting key from nested dictionary : ')
print(Dict)

print('-----------------------------------------')

#using pop method
dict1 = {1 : 'Geeks', 'name' : 'For', 3 : 'Geeks'}

pop_ele = dict1.pop(1)
print(pop_ele)
print('Dictionary after deletion : ' + str(dict1))
print('Associated value to poped key is : ' + pop_ele)

print('-----------------------------------------')

#using popitem() method
dict2 = {1 : 'Geeks', 'name' : 'For', 3 : 'Geeks'}

#deleting an arbitary key using popitem() function
pop_ele = dict2.popitem()
print('Dict after deletion : ' + str(dict2))
print('The arbitary pair returned is : ' + str(pop_ele))

print('-----------------------------------------')

#deleting all items at once using clear() method
dict3 = {1 : 'Geeks', 'name' : 'For', 3 : 'Geeks'}

#deleting entire dictionary
dict3.clear()
print('Deleting entire dictionary : ')
print(dict3)

print(dict3.has_key(1))
