class Complex :
	def __init__(self, x, y) :
		self.rPart = x
		self.iPart = y
		
	def __str__(self) :
		return 'Complex({0} + i{1})'.format(self.rPart, self.iPart)
		
	def __eq__(self, other) :
		return self.rPart == other.rPart and self.iPart == other.iPart
		
	def __add__(self, other) :
		temp = Complex(self.rPart + other.rPart, self.iPart + other.iPart)
		return temp
		
	
#Main App Begins here
C1 = Complex(2, 3)
print(C1)

C2 = Complex(3, 4)
print(C2)

if C1 == C2 : print('Same number ')
print('Not same number')

C3 = C1 + C2
print('Added : ', C3)
