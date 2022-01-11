#ways to sort list of dictionaries by values in Python - using itemgetter

from operator import itemgetter

lis = [{'name' : 'Nandini', 'age' : 20}, {'name' : 'Manjeet', 'age' : 20}, {'name' : 'Nikhil', 'age' : 19}]

#Using sorted and itemgetter to print list sorted by age
print('the list printed sorting by age : ')
print(sorted(lis, key = itemgetter('age')))

#using sorted and itemgetter to print list sorted by both name and age
print('the list printed sorting by name and age : ')
print(sorted(lis, key = itemgetter('age', 'name')))

#using sorted and itemgetter to print list sorted by age in descending order

print('the list printed sorting by age in reverse : ')
print(sorted(lis, key = itemgetter('age'), reverse = True))




