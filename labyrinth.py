from collections import deque
import math
import cv2
import numpy as np


def get_neighbors(image, position):
	size = image.shape
	x = position[0]
	y = position[1]
	neighbors = []

	if x < size[0] - 1 and y < size[1] - 1 and is_viable_neighbor(image, x + 1, y + 1): #down right
		neighbors.append([x + 1, y + 1])
	if 0 < y - 1 and is_viable_neighbor(image, x, y - 1): #up
		neighbors.append([x, y - 1])
	if x < size[0] - 1 and 0 < y - 1 and is_viable_neighbor(image, x + 1, y - 1): #up right
		neighbors.append([x + 1, y - 1])
	if 0 < x - 1 and 0 < y - 1 and is_viable_neighbor(image, x - 1, y - 1): #up left
		neighbors.append([x - 1, y - 1])
	if 0 < x - 1 and is_viable_neighbor(image, x - 1, y): #left
		neighbors.append([x - 1, y])
	if 0 < x - 1 and y < size[1] - 1 and is_viable_neighbor(image, x - 1, y + 1): #down left
		neighbors.append([x - 1, y + 1])
	if x < size[0] - 1 and is_viable_neighbor(image, x + 1, y) : #right
		neighbors.append([x + 1, y])
	if y < size[1] - 1 and is_viable_neighbor(image, x, y + 1): #down
		neighbors.append([x, y + 1])

	return neighbors
	
def is_viable_neighbor(image, x, y):
	return not is_black(image, x, y) and not is_blue(image, x, y)

def set_blue(image, x, y):
	image.itemset((x,y,0), 255)
	image.itemset((x,y,1), 0)
	image.itemset((x,y,2), 0)

def is_blue(image, x, y):
	return image.item(x,y,0) == 255 and image.item(x,y,1) == 0 and image.item(x,y,2) == 0

def is_red(image, x, y):
	return image.item(x,y,0) != 255 and image.item(x,y,1) != 255 and image.item(x,y,2) == 255

def is_white(image, x, y):
	return image.item(x,y,0) == 255 and image.item(x,y,1) == 255 and image.item(x,y,2) == 255

def is_black(image, x, y):
	return image.item(x,y,0) == 0 and image.item(x,y,1) == 0 and image.item(x,y,2) == 0

def solve_labyrinth(image, starting_point=[244,31], success=[15, 424], strategy='bfs', debug=True):
	set_blue(image, starting_point[0], starting_point[1])
	if (strategy == 'bfs'):
		pending = deque(get_neighbors(image, starting_point))
	elif(strategy == 'dfs'):
		pending = get_neighbors(image, starting_point)
	while pending:
		if (strategy == 'bfs'):
			neighbors = get_neighbors(image, pending.popleft())
		elif (strategy == 'dfs'):
			neighbors = get_neighbors(image, pending.pop())
		for pixel in neighbors:
			if pixel == success:
				return image
			set_blue(image, pixel[0], pixel[1])
			if (isinstance(neighbors[0], list)):
				for neighbor in neighbors:
					pending.append(neighbor)
			else:
				pending.append(neighbors)
		if debug:
			cv2.imshow('labyrinth', image)
			cv2.waitKey(1)

def get_best_pixel(neighbors, goal):
	minDistance = float('inf')
	destPixel = []
	for i in neighbors:		
		dist = distance(i, goal)
		if dist < minDistance:
			minDistance = dist
			destPixel = i
	return destPixel

def get_heuristic_best_pixel(neighbors, goal):
	return get_best_pixel(neighbors, goal)

def distance(source, target):
	return math.sqrt(math.pow(source[0] - target[0], 2) + math.pow(source[1] - target[1], 2))

def solve_labyrinth_informed(image, starting_point=[244,60], success=[15,424], strategy = 'greedy', debug=True):
	current = starting_point
	while current != success:
		if strategy == 'greedy':
			current = get_best_pixel(get_neighbors(image, current), success)
		elif strategy == 'a_star':
			current = get_heuristic_best_pixel(get_neighbors(image, current), success)
		set_blue(image, current[0], current[1])
		if debug:
			cv2.imshow('labyrinth', image)
			cv2.waitKey(1)
	return image


if __name__ == '__main__':
	image = cv2.imread('labyrinth.png')
	#solvedLabyrinth = solve_labyrinth(image, strategy = 'dfs', debug=False)
	solvedLabyrinth = solve_labyrinth_informed(image, strategy = 'a_star', debug = True)
	cv2.imshow('solvedLabyrinth', solvedLabyrinth)
	cv2.waitKey(0)	