import ReactDOM from 'react-dom';
import Router from './js/router';
import React from 'react';
import './css/index.css';

// attach react to #root in home.html
const root = document.getElementById('root');
ReactDOM.createRoot(root).render(
      <React.StrictMode>
        <Router/>
      </React.StrictMode>
  );
