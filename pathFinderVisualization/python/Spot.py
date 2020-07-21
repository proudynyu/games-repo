from colors import *
import pygame

class Spot:
	def __init__(self, row, col, width, totalRows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = WHITE
		self.neightbors = []
		self.width = width
		self.totalRows = totalRows

	def getPos(self):
		return self.row, self.col

	def isClose(self):
		return self.color == RED

	def isOpen(self):
		return self.color == GREEN

	def isBarrier(self):
		return self.color == BLACK

	def isStart(self):
		return self.color == ORANGE

	def isEnd(self):
		return self.color == PURPLE

	def reset(self):
		self.color = WHITE

	def makeClose(self):
		self.color = RED

	def makeOpen(self):
		self.color = GREEN

	def makeBarrier(self):
		self.color = BLACK

	def makeStart(self):
		self.color = ORANGE

	def makeEnd(self):
		self.color = PURPLE

	def draw(self, window):
		pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

	def updateNeigthbors(self, grid):
		self.neightbors = []
		if self.row < self.totalRows - 1 and not grid[self.row + 1][self.col].isBarrier(): # DOWN
			self.neightbors.append(grid[self.row + 1][self.col])
		
		if self.row > 0 and not grid[self.row - 1][self.col].isBarrier(): # UP
			self.neightbors.append(grid[self.row - 1][self.col])
		
		if self.col < self.totalRows - 1 and not grid[self.row][self.col + 1].isBarrier(): # RIGHT
			self.neightbors.append(grid[self.row][self.col + 1])
		
		if self.col > 0 and not grid[self.row][self.col - 1].isBarrier(): # LEFT
			self.neightbors.append(grid[self.row][self.col - 1])

	def __lt__(self, other):
		return False