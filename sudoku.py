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
        for row in self.sudoku:
            print [cell['value'] for cell in row]

    def solve(self):
        pass


sudoku = Sudoku("sudoku.txt")
sudoku.display()