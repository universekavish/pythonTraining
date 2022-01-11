#handling missing keys in python dictionaries

country_code = {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}

# 1. Using get()
# get(key, def_val)

print(country_code.get('India', 'Not Found'))
print(country_code.get('Japan', 'Not found'))

# 2. Using setdefault()
# setdefault(key, def_value)
#works same as get() but each time key is missing, a new key is created with the def_value provided

country_code.setdefault('Japan', 'Not present')
print(country_code['India'])
print(country_code['Japan'])

# IMPORTANT
# 3. Using defaultdict
# defaultdict is present in collections module, so import
# defaultdict takes a function(default factory) as its argument. 
# if a key is not present in the defaultdict, the default factory value is returned and displayed. 
import collections

# declaring defaultdict
# sets default value 'Key not found' to absent keys
defd = collections.defaultdict(lambda : 'Key Not Found')

defd['a'] = 1
defd['b'] = 2

print('Value associated with \'a\' : ', end = '')
print(defd['a'])

print('Value associated with \'c\' : ', end = '')
print(defd['c'])

