import pygame
import random

# 0 -> 3 live -> 1
# 1 -> < 2 live -> 0 // underpopulation
# 1 -> > 3 live -> 0 // overpopulation

# pygame window
pygame.init()
width = 800
gRange = 80
win = pygame.display.set_mode((width, width))
pygame.display.set_caption('Game of Life')

# set states of cells
def grid():
	arr = [[random.randint(0, 1) for y in range(gRange)] for x in range(gRange)]
	return arr

def rules(arr, x, y):
	sum = 0
	newArr = []

	for rows in range(-1, 1):
		for cols in range(-1, 1):
			sum += arr[x-rows][y-cols]

	if sum == 3:
		pass
	elif sum > 3:
		pass
	elif sum < 2:
		pass
	
	return newArr


def drawRect(surface):
	color = (0, 0, 0)
	for x in range(gRange):
		for y in range(gRange):
			
			if arr[x][y] == 1:
				stroke = 0
			else: 
				stroke = 1

			pygame.draw.rect(surface, color, (x*10, y*10, 10, 10), stroke)

	

# window update
def reDraw(surface):
	surface.fill((255, 255, 255))
	drawRect(surface)
	pygame.display.update()

run = True
arr = grid()

# main loop
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	reDraw(win)

pygame.quit()
