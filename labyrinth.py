import cv2
import numpy as np


def get_neighbors(image, position):
	size = image.shape
	

def solve_labyrinth(image, success=[], strategy=None):
	for i in range(0, image.shape[0]):
		for j in range(0, image.shape[1]):
			if (image.item(i,j,0) == 255 and image.item(i,j,1) == 255 and image.item(i,j,2) == 255):
				image.itemset((i,j,0), 255)
				image.itemset((i,j,1), 0)
				image.itemset((i,j,2), 0)
		cv2.imshow('labyrinth', image)
		cv2.waitKey(1)
	cv2.imshow('labyrinth', image)
	cv2.waitKey(0)


if __name__ == '__main__':
	labyrinth = cv2.imread('lab.png')
	solve_labyrinth(labyrinth)
