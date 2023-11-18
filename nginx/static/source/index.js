import React from 'react';
import ReactDOM from 'react-dom';

import App from './main';

// attach react to #root in home.html
const root = document.getElementById('root');
ReactDOM.createRoot(root).render(
      <React.StrictMode>
        <App />
      </React.StrictMode>
  );
