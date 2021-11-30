class Matrix:
	def __init__(self, r, c, d):
		self.row = r
		self.column = c
		self.data = d

	def __str__(self):
		return "Matrix({0}, {1}, {2})".format(self.row, self.column, self.data)
              
	def __add__(self, other):
		temp = Matrix(self.row, self.column,[])
		if (self.row == other.row and self.column == other.column):
			for i in range(len(self.data)):
				list = []
				for j in range(len(self.data[0])):
					list.append(self.data[i][j] + other.data[i][j])
				temp.data.append(list)    
		return temp

	def __mul__(self,other):
		temp = Matrix(self.row, other.column,[])
		sum = 0
		if (self.column == other.row):
			for i in range(len(self.data)):
				list = []
				for j in range(len(other.data[0])):
					for k in range(len(other.data)):
						sum += self.data[i][k] * other.data[k][j]
					list.append(sum)
					sum = 0
				temp.data.append(list)    
		return temp 
	
	def __eq__(self, other) :
		return self.row == other.row and self.column == other.column and self.data == other.data
		
	def transpose(self):
		B = [[self.data[j][i] for j in range(len(self.data))] for i in range(len(self.data[0]))]
		return B

	def is_square_matrix(self):
		return self.row == self.column 

	def diagonals(self):
		temp = []
		n = len(self.data[0])
		l = [self.data[i][i] for i in range(n)]
		temp.append(l)
		l = [self.data[i][n-i-1] for i in range(n)]
		temp.append(l)
		return temp	

	def swap_row(self, r1 = 0, r2 = 0):
		self.row1 = r1
		self.row2 = r2
		for i in range(len(self.data)):
			temp = self.data[self.row1 - 1][i]
			self.data[self.row1-1][i] = self.data[self.row2 - 1][i]
			self.data[self.row2-1][i] = temp
		temp = Matrix(self.row, self.column, self.data)
		return temp

	def swap_col(self, c1 = 0, c2 = 0):
		self.col1 = c1
		self.col2 = c2
    
		for i in range(len(self.data)):
			#self.data[i][self.col], self.data[i][self.col1] = self.data[i][self.col1], self.data[i][self.col]
			temp = self.data[i][self.col1 - 1]
			self.data[i][self.col1-1] = self.data[i][self.col2 - 1]
			self.data[i][self.col2-1] = temp
		temp = Matrix(self.row, self.column, self.data)
		return temp
       
	def __sub__(self, other) :
		temp = Matrix(self.row, self.column,[])
		if (self.row == other.row and self.column == other.column):
			for i in range(len(self.data)):
				list = []
				for j in range(len(self.data[0])):
					list.append(self.data[i][j] - other.data[i][j])
				temp.data.append(list)    
		return temp

r1, c1 = 3, 3
data = [[11,22,33], [44,55,66], [77,88,99]]
M1 = Matrix(3, 3, data)
print(M1)


r2, c2 = 3, 3
data2 = [[10,20,30], [40,5,60], [70,80,90]]
M2 = Matrix(r2, c2, data2)
print(M2)

#1. Add
M3 = M1 + M2
print('Added ', M3)

#2. Multiply
M4 = M1 * M2
print('Multiplied ', M4)

#3. Transpose
M5 = M1.transpose()
print('Transpose ', M5)

#4. Square matrix or not
if M1.is_square_matrix(): print("Square matrix")
else: print("Not a square matrix")

#5. Diagonals
diagonal = M1.diagonals()
print('Diagonal ', diagonal)

#6. Swap two rows
M1.swap_row(2,3)
print('After swapping rows ', M1)

#7. Swap two columns
M1.swap_col(1,3)
print('Ater swapping columns ', M1)

#8. Same or not
if M1 == M2 : print('Same Matrix')
else : print('Not same matrix')

#9. Substraction
M6 = M1 - M2
print(M6)


