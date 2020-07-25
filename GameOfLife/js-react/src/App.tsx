import React from 'react';
import Header from './components/Header';
import Grid from './components/Grid'
import './App.css'

const App: React.FC = () => {
  return (
    <div className="app">
    <Header />

      <div className="container">
        <Grid />
      </div>

    </div>
  );
}

export default App;
