import ReactDOM from 'react-dom';
import App from './js/counter';
import React from 'react';
import './css/index.css';

// attach react to #root in home.html
const root = document.getElementById('root');
ReactDOM.createRoot(root).render(
      <React.StrictMode>
        <App />
      </React.StrictMode>
  );
