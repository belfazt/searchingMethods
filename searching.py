from collections import deque
from copy import copy, deepcopy
import treelib
import random

def generateRandomTree(minSize, maxSize):
	tree = treelib.Tree()
	tree.add_node(treelib.Node())
	nodes = [tree.all_nodes()[0].identifier]
	for i in xrange(0, random.randrange(minSize, maxSize)):
		nodes.append(tree.create_node(parent=random.choice(nodes)).identifier)
	return tree

def findValue(matrix, value):
	for i in xrange(0, len(matrix)):
		for j in xrange(0, len(matrix[i])):
			if value == matrix[i][j]:
				return [i,j]

def swap(matrix, initialCoordinates, finalCoordinates):
	tempMatrix = copy(matrix)
	temp = tempMatrix[initialCoordinates[0]][initialCoordinates[1]]
	tempMatrix[initialCoordinates[0]][initialCoordinates[1]] = tempMatrix[finalCoordinates[0]][finalCoordinates[1]]
	tempMatrix[finalCoordinates[0]][finalCoordinates[1]] = temp
	return tempMatrix

def addMovements(tree, node, statuses):
	for i in xrange(0,4):
		tag = copy(node.tag)
		data = deepcopy(tag['status'])
		zero = findValue(data, 0)
		#swaps
		if i == 0 and zero[0] < 2: #down
			tag['status'] = swap(data, zero, [zero[0] + 1, zero[1]])
		elif i == 1 and zero[0] > 0: #up
			tag['status'] = swap(data, zero, [zero[0] - 1, zero[1]])
		elif i == 2 and zero[1] < 2: #left
			tag['status'] = swap(data, zero, [zero[0], zero[1] + 1])
		elif i == 3 and zero[1] > 0: #right
			tag['status'] = swap(data, zero, [zero[0], zero[1] - 1])
		if str(tag['status']) not in statuses:
			tree.create_node(parent=node.identifier, tag=tag)

def solve8PuzzleByBreadth(tree):
	success = [[0,1,2],[3,4,5],[6,7,8]]
	statuses = dict()
	for node in tree.all_nodes():
		node.tag['distance'] = float('inf')
	root = getRootNode(tree)
	root.tag['distance'] = 0
	statuses[str(root.tag['status'])] = True
	addMovements(tree, root, statuses)
	q = deque([root])
	while q:
		current = q.popleft()
		for node in tree.children(current.identifier):
			node.tag['distance'] = current.tag['distance'] + 1
			statuses[str(node.tag['status'])] = True
			addMovements(tree, node, statuses)
			if node.tag['status'] == success:
				return node
			q.append(node)

def solve8PuzzleByDepth(tree):
	success = [[0,1,2],[3,4,5],[6,7,8]]
	statuses = dict()
	for node in tree.all_nodes():
		node.tag['distance'] = float('inf')
	root = getRootNode(tree)
	root.tag['distance'] = 0
	statuses[str(root.tag['status'])] = True
	addMovements(tree, root, statuses)
	s = [root]
	while s:
		current = s.pop()
		for node in tree.children(current.identifier):
			node.tag['distance'] = current.tag['distance'] + 1
			statuses[str(node.tag['status'])] = True
			addMovements(tree, node, statuses)
			if node.tag['status'] == success:
				return node
			s.append(node)

def getRootNode(tree):
	for i in tree.all_nodes():
		if i.is_root():
			return i

def printMatrix(matrix):
	for i in matrix:
		print i

if __name__ == '__main__':
	puzzle = treelib.Tree()
	#data = {'status': [[7,2,4],[5,0,6],[8,3,1]]}
	data = {'status': [[1,2,3],[0,4,5],[6,7,8]]}
	root = puzzle.add_node(treelib.Node(tag=data))
	result = solve8PuzzleByBreadth(puzzle)
	print puzzle
	print result.tag