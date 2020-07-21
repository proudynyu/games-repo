import colors from './colors'

class Spot {
  constructor(row, col, width, totalRows){
    this._row = row;
    this._col = col;
    this._x = this.row * width;
    this._y = this.col * width;
    this._color = colors.white;
    this._neighbors = []
    this._width = width;
    this._totalRows = totalRows;
  }
    
  get position() {
    return this.row, this.col;
  }

  get isClose() {
    return this.color === colors.red;
  }

  get isOpen() {
    return this.color === colors.green;
  }

  get isBarrier() {
    return this.color === colors.black;
  }

  get isStart() {
    return this.color === colors.orange;
  }

  get isEnd() {
    return this.color === colors.purple;
  }

  set reset() {
    this._color = colors.white;
  }

  set makeClose() {
    this._color = colors.red;
  }

  set makeOpen() {
    this._color = colors.green;
  }

  set makeBarrier() {
    this._color = colors.black;
  }

  set makeStart() {
    this._color = colors.white;
  }

  set makePath() {
    this._color = colors.purple;
  }

  set makeEnd() {
    this._color = colors.purple;
  }
}

export default Spot;

/*
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
*/