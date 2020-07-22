import React, { useState, useCallback } from 'react';
import produce from 'immer'
import './styles/global.css';

const numRows = 50;
const numCols = 50;

const App: React.FC = () => {
  const [grid, setGrid] = useState(() => {
    const rows = []
    for (let i = 0; i < numRows; i++) {
      rows.push(Array.from(Array(numCols), () => 0))
    }
    return rows;
  });

  const[run, setRun] = useState(false);

  const runSimullation = useCallback(() => {
    if (!run) return;

    setTimeout(runSimullation, 1000);
  }, [])

  return (
    <>
      <button onClick={() => setRun(!run)}>Start</button>

      <div className="App">
        { grid.map( (rows, i) => rows.map(
          (col, k) => (
            <div 
              key={`${i}-${k}`}
              onClick={() => {
                const newGrid = produce(grid, gridCopy => {
                  gridCopy[i][k] = grid[i][k] ? 0 : 1;
                })

                setGrid(newGrid);
              }}
              style={{
                width: 20,
                height: 20,
                backgroundColor: grid[i][k] ? 'pink' : undefined,
                border: "1px solid black"
              }}
            />
            )
          ))
        }
      </div>
    </>
  );
}

export default App;
