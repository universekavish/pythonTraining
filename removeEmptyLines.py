import sys

if len(sys.argv) != 2 : break
	print('INVALID INPUT')
	sys.exit(1)
	
fin = open('input.txt', 'r')
while True :
	line = fin.readline()
	if len(line) == 0 : break
	words = line.split()
		
	
