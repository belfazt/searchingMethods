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
				if board[i][j]['value'] is None:
					possible_moves.append((i, j))
		return possible_moves

	def rate_move(self, board, move):
		x, y = move
		score = 0
		count = 0

		# Row
		for j in xrange(len(board[x])):
			if board[x][j]['value'] == self.tag:
				count += 1
			elif board[x][j]['value'] is not None:
				count -= 1
		score += math.pow(10, count)
		count = 0

		# Column
		for i in xrange(len(board[y])):
			if board[i][y]['value'] == self.tag:
				count += 1
			elif board[i][y]['value'] is not None:
				count -= 1
		score += math.pow(10, count)
		count = 0				

		# Diagonals
		if x == y:
			for i in xrange(len(board)):
				if board[i][i]['value'] == self.tag:
					count += 1
				elif board[i][i]['value'] is not None:
					count -= 1	
			score += math.pow(10, count)
			count = 0

		if x + y == len(board) - 1:
			for i in xrange(len(board)):
				if board[i][len(board) - 1 - i]['value'] == self.tag:
					count += 1
				elif board[i][len(board) - 1 - i]['value'] is not None:
					count -= 1	
			score += math.pow(10, count)

		return score

	def next_move(self, board):
		ratings = []
		possible_moves = self.possible_moves(board)
		
		for move in possible_moves:
			ratings.append(self.rate_move(board, move))

		x, y = random.choice(possible_moves) if len(possible_moves) == math.pow(len(board), 2) else possible_moves[ratings.index(min(ratings))]
		board[x][y]['value'] = self.tag


	def get_tag(self):
		return self.tag

