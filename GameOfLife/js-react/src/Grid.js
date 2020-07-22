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

    for (let row = 0; row < this.rows; row++) {
      for (let col = 0; col < this.cols; col++) {
        grid.push(
          <Box boxClass={'box'}/>
        )
      }
    }

    return (
      <div style={{'width': this.width}}>
        { grid }
      </div>
    )
  } 
}

export default Grid;