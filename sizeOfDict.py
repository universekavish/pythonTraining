import sys

dict1 = {"A": 1, "B": 2, "C": 3} 
dict2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
dict3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}

print('Size of dict1 : ', str(sys.getsizeof(dict1)), 'bytes')
print('Size of dict2 : ' + str(sys.getsizeof(dict2)) + 'bytes')
print('Size of dict3 : ' + str(sys.getsizeof(dict3)) + 'bytes')
