import math
import random

class TicTacToeAgent:
	tag = None

	def __init__(self, tag):
		self.tag = str(tag[0])

	def __str__(self):
		return 'Player with tag: ' + self.get_tag()

	def possible_moves(self, board):
		possible_moves = []
		for i in xrange(len(board)):
			for j in xrange(len(board[i])):
				if board[i][j] is None:
					possible_moves.append((i, j))
		return possible_moves

	def rate_move(self, board, move):
		x, y = move
		score = 0
		count = 0
		opponent_count = 0

		# Row
		for j in xrange(len(board[x])):
			if board[x][j] == self.tag:
				count += 1
			elif board[x][j] is not None:
				opponent_count += 1
		score += math.pow(10, count) - math.pow(10, opponent_count)
		count = 0

		# Column
		for i in xrange(len(board[y])):
			if board[i][y] == self.tag:
				count += 1
			elif board[i][y] is not None:
				opponent_count += 1
		score += math.pow(10, count) - math.pow(10, opponent_count)
		count = 0				

		# Diagonals
		if x == y:
			for i in xrange(len(board)):
				if board[i][i] == self.tag:
					count += 1
				elif board[i][i] is not None:
					opponent_count += 1	
			score += math.pow(10, count) - math.pow(10, opponent_count)
			count = 0

		if x + y == len(board) - 1:
			for i in xrange(len(board)):
				if board[i][len(board) - 1 - i] == self.tag:
					count += 1
				elif board[i][len(board) - 1 - i] is not None:
					opponent_count += 1	
			score += math.pow(10, count) - math.pow(10, opponent_count)

		return score

	def next_move(self, board):
		ratings = []
		possible_moves = self.possible_moves(board)
		
		for move in possible_moves:
			ratings.append(self.rate_move(board, move))

		x, y = random.choice(possible_moves) if len(possible_moves) == math.pow(len(board), 2) else possible_moves[ratings.index(min(ratings))]
		board[x][y] = self.tag


	def get_tag(self):
		return self.tag

