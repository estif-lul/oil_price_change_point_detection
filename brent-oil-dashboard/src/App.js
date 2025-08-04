import './App.css';
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import theme from './theme';
import Dashboard from './pages/Dashboard';

import Prices from './components/Prices';
import Events from './components/Events';
import ChangePoints from './components/ChangePoints';


function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/prices" element={<Prices />} />
          <Route path="/events" element={<Events />} />
          <Route path="/change-points" element={<ChangePoints />} />
        </Routes>
      </Router>
    </ThemeProvider>
  );
}

export default App;
