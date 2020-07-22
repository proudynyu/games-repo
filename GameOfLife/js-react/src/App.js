import React from 'react';
import './styles/global.css';

import Grid from './Grid';

function App() {
  return (
    <div className="app">
      <Grid 
        rows={20}
        cols={20}
      />
    </div>
  );
}

export default App;
