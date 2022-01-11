# ways to sort list of dictionaries by values in python - Using lambda function

lis = [{'name' : 'Nandini', 'age' : 20}, {'name' : 'Manjeet', 'age' : 20}, {'name' : 'Nikhil', 'age' : 19}]

print('the list printed sorted by age : ')
print(sorted(lis, key = lambda i : i ['age']))

print('the list printed sorted by age and name : ')
print(sorted(lis, key = lambda i : (i['age'], i['name'])))

print('the list printed sorted by age in reverse : ')
print(sorted(lis, key = lambda i : i ['age'], reverse = True))
