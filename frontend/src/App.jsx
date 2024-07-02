// src/App.js

import React from 'react';
import { RouterProvider, createBrowserRouter, createRoutesFromElements, Route } from 'react-router-dom';
import Login from './components/Login';
import Register from './components/Register';

const router = createBrowserRouter(
    createRoutesFromElements(
        <>
            <Route path="/" element={<Login />} />
            <Route path="/register" element={<Register />} />
        </>
    )
);

const App = () => {
    return <RouterProvider router={router} />;
};

export default App;
