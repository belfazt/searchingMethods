from collections import deque
from copy import copy, deepcopy
import treelib
import random

def find_value(matrix, value):
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

def add_movements(tree, node, statuses, heuristic=False):
	for i in xrange(0,4):
		tag = copy(node.tag)
		data = deepcopy(tag['status'])
		zero = find_value(data, 0)
		#swaps
		if i == 0 and zero[0] < 2: #down
			tag['status'] = swap(data, zero, [zero[0] + 1, zero[1]])
		elif i == 1 and zero[0] > 0: #up
			tag['status'] = swap(data, zero, [zero[0] - 1, zero[1]])
		elif i == 2 and zero[1] < 2: #left
			tag['status'] = swap(data, zero, [zero[0], zero[1] + 1])
		elif i == 3 and zero[1] > 0: #right
			tag['status'] = swap(data, zero, [zero[0], zero[1] - 1])

		if heuristic:
			tag['cost'] = get_heuristic_cost(tree, node)
		else:
			tag['cost'] = get_cost(tree, node)

		if str(tag['status']) not in statuses:
			tree.create_node(parent=node.identifier, tag=tag)

def solve_8_puzzle(tree, success=[[0,1,2],[3,4,5],[6,7,8]], strategy='bfs'):
	statuses = dict()
	root = get_root_node(tree)
	statuses[str(root.tag['status'])] = True
	add_movements(tree, root, statuses)
	if (strategy == 'bfs'):
		q = deque([root])
		while q:
			current = q.popleft()
			for node in tree.children(current.identifier):
				statuses[str(node.tag['status'])] = True
				add_movements(tree, node, statuses)
				if node.tag['status'] == success:
					return node
				q.append(node)
	elif(strategy == 'dfs'):
		s = [root]
		while s:
			current = s.pop()
			for node in tree.children(current.identifier):
				statuses[str(node.tag['status'])] = True
				add_movements(tree, node, statuses)
				if node.tag['status'] == success:
					return node
				s.append(node)

# Number of incorrect tiles
def get_cost(tree, node, success=[[0,1,2],[3,4,5],[6,7,8]]):
	cost = 0
	for i in range(len(node.tag["status"])):
		for j in range(len(node.tag["status"][i])):
			if node.tag["status"][i][j] != success[i][j]:
				cost += 1

	return cost

def get_heuristic_cost(tree, node, success=[[0,1,2],[3,4,5],[6,7,8]]):
	cost = get_cost(tree, node)
	if cost != 0: # If cost is 0, is a success state
		cost += tree.level(node.identifier)

	return cost

def get_best_node(tree):
	best_node = None
	lowest_cost = float('inf')
	leaves = [node for node in tree.all_nodes() if node.is_leaf()]
	
	for node in leaves:
		if node.tag['cost'] < lowest_cost:
			lowest_cost = node.tag['cost']
			best_node = node

	return best_node

def informed_search(tree, strategy='greedy_search'):
	statuses = dict()
	root = get_root_node(tree)
	statuses[str(root.tag['status'])] = True
	add_movements(tree, root, statuses)
	current_node = get_best_node(tree)

	if strategy == 'greedy_search':
		while current_node.tag['cost'] != 0:
			add_movements(tree, current_node, statuses) 
			current_node = get_best_node(tree)
	elif strategy == 'a_star':
		while current_node.tag['cost'] != 0:
			add_movements(tree, current_node, statuses, True) 
			current_node = get_best_node(tree)

	return current_node

def get_root_node(tree):
	for i in tree.all_nodes():
		if i.is_root():
			return i

if __name__ == '__main__':
	puzzle = treelib.Tree()
	initial_status = [[1,2,5],
					  [0,3,8],
					  [6,4,7]]
	data = {'status': initial_status, 'cost': 1}
	root = puzzle.add_node(treelib.Node(tag=data))
	result = informed_search(puzzle, 'a_star')
	print puzzle
	print result.tag
	print 'level: ' + str(puzzle.depth(result))
