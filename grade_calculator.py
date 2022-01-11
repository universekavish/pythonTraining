# Student data in form of dictionary
students = {'jack' : {'name' : 'Jack Frost', 'assignment' : [80, 50, 40, 20], 'test' : [75, 75], 'lab' : [78.20, 77.20]}, 
		'james' : { 'name' : 'James Potter', "assignment" : [82, 56, 44, 30], "test" : [80, 80], "lab" : [67.90, 78.72]},
		'dylan' : {"name" : "Dylan Rhodes", "assignment" : [77, 82, 23, 39], "test" : [78, 77], "lab" : [80, 80]},
		'jess' : {"name" : "Jessica Stone", "assignment" : [67, 55, 77, 21], "test" : [40, 50], "lab" : [69, 44.56]},
		'tom' : {"name" : "Tom Hanks", "assignment" : [29, 89, 60, 56], "test" : [65, 56], "lab" : [50, 40.6]}}

'''
jack = {'name' : 'Jack Frost', 
		  'assignment' : [80, 50, 40, 20],
		  'test' : [75, 75],
		  'lab' : [78.20, 77.20]
		}
		  
james = { 'name' : 'James Potter',
		  "assignment" : [82, 56, 44, 30],
          "test" : [80, 80],
          "lab" : [67.90, 78.72]
		}
		
dylan = {"name" : "Dylan Rhodes",
          "assignment" : [77, 82, 23, 39],
          "test" : [78, 77],
          "lab" : [80, 80]
		}
		
jess = {"name" : "Jessica Stone",
         "assignment" : [67, 55, 77, 21],
         "test" : [40, 50],
         "lab" : [69, 44.56]
		}
		
tom = {"name" : "Tom Hanks",
        "assignment" : [29, 89, 60, 56],
        "test" : [65, 56],
        "lab" : [50, 40.6]
		}
'''		
# calculating average respective according to assignment, lab and test
def get_avg(marks) :
	total_sum = sum(marks)
	return total_sum / len(marks)

# calculating total average
def total_avg(students) ;
	assignment = get
for i in students :
	print(i)
	print(students[i]['name'])
	print(students[i]['assignment'])
	print(get_avg(students[i]['assignment']))
	
	
