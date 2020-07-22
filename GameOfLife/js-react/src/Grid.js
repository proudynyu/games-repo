import React from 'react';
import Box from './Box';

class Grid extends React.Component {
  constructor(rows, cols, width) {
    super();
    this.rows = rows;
    this.cols = cols;
    this.width = `${width}px`;
  }
  render () {
    let grid = []
    const gap = Math.floor(this.props.width / 10);

    for (let row = 0; row < this.props.rows; row++) {
      for (let col = 0; col < this.props.cols; col++) {
        grid.push(
          <div className="box">{row}</div>
        )
      }
    }

    console.log(grid);
    return (
      <div className="grid">
        {grid}
      </div>
    )
  } 
}

export default Grid;