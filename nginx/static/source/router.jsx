import React from 'react';
import { createBrowserRouter, RouterProvider, Link, Navigate } from "react-router-dom";
import App from './counter';

// ALWAYS IMPORT REACT from react, it is needed when bundling

const Router = () => {
    const router = createBrowserRouter([
        {
            "path": "/app",
            "element": <App />
        },
        {
            "path": "/hello",
            "element": <div><h1>HELLO</h1><Link to="/app">go to game</Link></div>
        },
        {
            "path": "*",
            "element": <Navigate to="/hello" />
        }
    ]);

    return <RouterProvider router={router}/>
}

export default Router;
