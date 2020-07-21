import Spot from './Spot';

class Grid {
  constructor(rows, width) {
    this.rows = rows;
    this.width = width;

    function makeGrid() {
      const gap = Math.floor(this.width / this.rows);
      let grid = [];

      for (let i = 0; i < 10; i++) {
        for (let j = 0; j < 10; j++) {
          const spot = new Spot(i, j, gap, 10);
          grid.push(spot);
        }
      }

      return grid;
    }

  }
}

export default Grid;