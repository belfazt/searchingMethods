from tic_tac_toe_agent import TicTacToeAgent

class TicTacToe:
	board = None
	size = None
	players = []


	def __init__(self, size=3, players=[TicTacToeAgent('o'), TicTacToeAgent('x')]):
		self.size = size
		self.board = [[{'value': None, 'visited': False} for _ in xrange(0, size)] for _ in xrange(0, size)]
		self.players = players

	def __str__(self):
		string = 'Players: \n'
		for i in self.players:
			string += str(i) + '\n'
		string += str(self.size) + 'x' + str(self.size)+' Board: \n'
		for i in self.board:
			string += str(i) + '\n'
		return string

	def did_someone_win(self):
		return False

	def is_game_over(self):		
		if self.did_someone_win():
			return True
		for i in self.get_board():
			for j in i:
				if j['value'] is None:
					return False
		return True

	def play(self, debug=False):
		game_over = False
		while not game_over:
			for i in self.players:
				game_over = self.is_game_over()
				if not game_over:
					i.next_move(self.get_board())
				else:
					break
			if game_over:
				break

			if debug:
				self.display_board()
				print ''

	def display_board(self):
		board = self.get_board()
		for i in xrange(0, self.size):
			for j in xrange(0, self.size):
				print board[i][j]['value'] if board[i][j]['value'] != None else str('_'),
				if j != self.size - 1:
					print '|',
			if i != self.size - 1:
				print '\n' + '-' * (4 * self.size - 1) 
		print '\n'

	def get_board(self):
		return self.board


if __name__ == '__main__':
	tic = TicTacToe()
	tic.play(debug=True)
