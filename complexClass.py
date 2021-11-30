import math

class Complex :
	def __init__(self, x, y) :
		self.rPart = x
		self.iPart = y
		
	def __str__(self) :
		return 'Complex({0} {1}i)'.format(self.rPart, self.iPart)
		
	def __eq__(self, other) :
		return self.rPart == other.rPart and self.iPart == other.iPart
		
	def __add__(self, other) :
		temp = Complex(self.rPart + other.rPart, self.iPart + other.iPart)
		return temp
    
	def __mul__(self, other) :
		return Complex(((self.rPart)*(other.rPart)) - ((self.iPart)*(other.iPart)), (self.rPart)*(other.iPart) + (self.iPart)*(other.rPart))
		
	def conjugate(self) :
		return Complex(self.rPart, (-1)*(self.iPart)) 

	def divide(self, other) :
		deno = other.rPart * other.rPart + other.iPart * other.iPart
		if other.iPart > 0 :
			return Complex((((self.rPart)*(other.rPart)) + ((self.iPart)*(other.iPart))/deno), ((self.iPart)*(other.rPart) - (self.rPart)*(other.iPart)/deno))
		else :
			return Complex((((self.rPart)*(other.rPart)) - ((self.iPart)*(other.iPart))/deno), ((self.iPart)*(other.rPart) + (self.rPart)*(other.iPart)/deno))
    
	def __sub__(self, other) :
		return Complex(self.rPart - other.rPart, self.iPart - other.iPart)
        
	def modulus(self) :
		return math.sqrt(self.rPart * self.rPart + self.iPart * self.iPart)
    	
	def carRep(self) :
		return 'Cartesian Rep (' + str(self.rPart) + ' , ' + str(self.iPart) + ')'
    	
	def polarRep(self) :
		return math.sqrt(self.rPart * self.rPart + self.iPart * self.iPart), math.degrees(math.atan(self.rPart/self.iPart))
            
#Main App Begins here
C1 = Complex(2, 3)
print(C1)

C2 = Complex(3, 4)
print(C2)

#1. same or not
if C1 == C2 : print('Same number ')
print('Not same number')

#2. add
C3 = C1 + C2
print('Added : ', C3)

#3. multiply
C4 = C1*C2
print('multiplied result ', C4)

#4. Conjugate
C1conj = C1.conjugate()
print('conjugate ', C1conj) 

#5. divide
C5 = C1.divide(C2)
print('Divided result ', C5)

#6. substraction
C6 = C1 - C2
print('Substracted ', C6)

#7. Modulus
modulus = C1.modulus()
print('modulus ', modulus)

#8. Cartesian Respresentation
rep = C1.carRep()
print(rep)

#9. Polar representation
mod, theta = C1.polarRep()
print('Polar Rep (' + str(mod) + ' , ' + str(theta) + ')')


