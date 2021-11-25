import sys

if len(sys.argv) != 3 : break
	print('!!Invalid input!!')
	sys.exit(1)

fin = open('input.txt', 'r')
fin2 = open('input2.txt', 'r')

while True :
	line = fin.readline()
	line2 = fin2.readline()
	
	if len(line) != 0 and len(line2) != 0 : break
	words = line.split()
	words2 = line2.split()
	
	if words == words2 :
		print('Same data in both file')
	else : 
		
		 
