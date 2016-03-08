class Sudoku:
	sudoku = []


	def __init__(self, sudoku = None):
		if type(sudoku) is list:
			self.sudoku = sudoku
		elif type(sudoku) is str:
			self.read_file(sudoku)
		else:
			[[{'value': 0} for col in range(9)] for row in range(9)]

	def read_file(self, path):
		with open(path) as file:
			for line in file:
				row = [{'value': int(val)} for val in line.split()]
				self.sudoku.append(row)

	def display(self):
		for row in xrange(0, len(self.sudoku)):
			if row in [3,6]:
				print '------+-------+------'
			for column in xrange(0, len(self.sudoku[row])):
				print self.sudoku[row][column]['value'],
				if column in [2,5]:
					print '|',
			print ''
		print ''

	def _find_next_cell_to_fill(self, i, j):
		for x in range(i,9):
				for y in range(j,9):
						if self.sudoku[x][y]['value'] == 0:
								return x,y
		for x in range(0,9):
				for y in range(0,9):
						if self.sudoku[x][y]['value'] == 0:
								return x,y
		return -1,-1

	
	def _is_valid(self, i, j, e):
		rowOk = all([e != self.sudoku[i][x]['value'] for x in range(9)])
		if rowOk:
				columnOk = all([e != self.sudoku[x][j]['value'] for x in range(9)])
				if columnOk:
						# finding the top left x,y co-ordinates of the section containing the i,j cell
						secTopX, secTopY = 3 *(i/3), 3 *(j/3)
						for x in range(secTopX, secTopX+3):
								for y in range(secTopY, secTopY+3):
										if self.sudoku[x][y]['value'] == e:
												return False
						return True
		return False

	def solve(self, i=0, j=0, debug=False):
		i,j = self._find_next_cell_to_fill(i, j)
		if i == -1:
			return True
		for e in range(1,10):
			if self._is_valid(i,j,e):
				self.sudoku[i][j]['value'] = e
				if debug:
					print 'DEBUGGING'
					self.display()
				if self.solve(i, j):
					return True
				# Undo the current cell for backtracking
				self.sudoku[i][j]['value'] = 0
		return False


if __name__ == '__main__':
	sudoku = Sudoku("sudoku.txt")
	print 'Solving'
	sudoku.display()
	sudoku.solve(debug=True)
	print 'Solved'
	sudoku.display()
