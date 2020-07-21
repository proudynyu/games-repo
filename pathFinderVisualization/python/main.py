import pygame as pg
import math
from queue import PriorityQueue
from colors import *
from Spot import Spot

# Pathfinder algotirhm based on Tech with Tim video
# @youtube https://www.youtube.com/watch?v=JtiK0DOeI4A&t=3597s

WIDTH = 600
WIN = pg.display.set_mode((WIDTH, WIDTH))

# screen title
pg.display.set_caption("A* Pathfinder Algorithm")

def h(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)

def makeGrid(rows, width):
	grid = []
	gap = width // rows

	for i in range(rows):
		grid.append([])
		for j in range(rows):
			spot = Spot(i, j, gap, rows)
			grid[i].append(spot)

	return grid

def drawGrid(window, rows, width):
	gap = width // rows
	for i in range(rows):
		pg.draw.line(window, GREY, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pg.draw.line(window, GREY, (j * gap, 0), (j* gap, width))

def draw(window, grid, rows, width):
	window.fill(WHITE)

	for row in grid:
		for spot in row:
			spot.draw(window)

	drawGrid(window, rows, width)
	pg.display.update()

def getClickPos(pos, rows, width):
	gap = width // rows
	x, y = pos

	row = x // gap
	col = y // gap
	return row, col

def reconstruct_path(cameFrom, current, callback):
	while current in cameFrom:
		current = cameFrom[current]
		current.makePath()
		callback()

def algorithm(callback, grid, start, end):
	count = 0
	openSet = PriorityQueue()
	openSet.put((0, count, start))
	cameFrom = {}
	gScore = {spot: float("inf") for row in grid for spot in row}
	gScore[start] = 0
	fScore = {spot: float("inf") for row in grid for spot in row}
	fScore[start] = h(start.getPos(), end.getPos())

	openSetHash = {start}

	while not openSet.empty():
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()

		current = openSet.get()[2]
		openSetHash.remove(current)

		if current == end:
			reconstruct_path(cameFrom, end, callback)
			end.makeEnd()
			return True

		for neightbor in current.neightbors:
			tempScore = gScore[current] + 1

			if tempScore < gScore[neightbor]:
				cameFrom[neightbor] = current
				gScore[neightbor] = tempScore
				fScore[neightbor] = tempScore + h(neightbor.getPos(), end.getPos())
				if neightbor not in openSetHash:
					count += 1
					openSet.put((fScore[neightbor], count, neightbor))
					openSetHash.add(neightbor)
					neightbor.makeOpen()

		callback()

		if current != start:
			current.makeClose()

	return False

def main(window, width):
	ROWS = 50
	grid = makeGrid(ROWS, width)

	start = None
	end = None

	run = True
	while run:
		draw(window, grid, ROWS, width)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				run = False
			
			if pg.mouse.get_pressed()[0]:
				pos = pg.mouse.get_pos()
				row, col = getClickPos(pos, ROWS, width)
				spot = grid[row][col]
				if not start and spot != end:
					start = spot
					start.makeStart()
				elif not end and spot != start:
					end = spot
					end.makeEnd()
				elif spot != end and spot != start:
					spot.makeBarrier()

			elif pg.mouse.get_pressed()[2]:
				pos = pg.mouse.get_pos()
				row, col = getClickPos(pos, ROWS, width)
				spot = grid[row][col]
				spot.reset()

				if spot == start:
					start = None
				elif spot == end:
					end = None

			if event.type == pg.KEYDOWN:
				if event.key == pg.K_SPACE and start and end:
					for row in grid:
						for spot in row:
							spot.updateNeigthbors(grid)

					algorithm(lambda: draw(window, grid, ROWS, width), grid, start, end)
				
				if event.key == pg.K_c:
					start = None
					end = None
					grid = makeGrid(ROWS, width)

	pg.quit()

main(WIN, WIDTH)