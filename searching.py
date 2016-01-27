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


def addMovements(tree, node):
	for i in xrange(0,4):
		tag = copy(node.tag)
		data = deepcopy(tag['status'])
		zero = findValue(data, 0)
		if i == 0 and zero[0] < 2:
			tag['status'] = swap(data, zero, [zero[0]+1, zero[1]])
		elif i == 1 and zero[0] > 0:
			tag['status'] = swap(data, zero, [zero[0]-1, zero[1]])
		elif i == 2 and zero[1] < 2:
			tag['status'] = swap(data, zero, [zero[0], zero[1]+1])
		elif i == 2 and zero[1] > 0:
			tag['status'] = swap(data, zero, [zero[0], zero[1]-1])
		tree.create_node(parent=node.identifier, tag=tag)

def solve8Puzzle(tree):
	success = [[0,1,2],[3,4,5],[6,7,8]]
	statuses = dict()
	for node in tree.all_nodes():
		node.tag['distance'] = float('inf')
	root = getRootNode(tree)
	root.tag['distance'] = 0
	statuses[''.join(root.tag['status'])] = True
	print statuses
	addMovements(tree, root)
	q = deque([root])
	while q:
		current = q.popleft()
		for node in tree.children(current.identifier):
			node.tag['distance'] = current.tag['distance'] + 1
			if node.tag == success:
				return node
			q.append(node)


def getRootNode(tree):
	for i in tree.all_nodes():
		if i.is_root():
			return i

def bfs(tree, identifier):
	q = deque([getRootNode(tree)])
	while q:
		for i in tree.children(q.popleft().identifier):
			if i.identifier == identifier:
				return i
			q.append(i)

def dfs(tree, identifier):
	s = [getRootNode(tree)]
	while s:
		for i in tree.children(s.pop().identifier):
			if i.identifier == identifier:
				return i
			s.append(i)

if __name__ == '__main__':
	puzzle = treelib.Tree()
	data = {'status': [[7,2,4],[5,0,6],[8,3,1]]}
	root = puzzle.add_node(treelib.Node(tag=data))
	solve8Puzzle(puzzle)
	print puzzle