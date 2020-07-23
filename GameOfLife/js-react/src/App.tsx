import React from 'react';
import Grid from './Grid';

const rows = 20;
const cols = 20;

const App: React.FC = () => {
  return (
    <div className="App">
      <h1>Conway's Game of Life</h1>
      <Grid
        rows={rows}
        cols={cols}
      />
    </div>
  );
}

export default App;
