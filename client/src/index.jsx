/******************************************************************************
 * Filename: index.jsx
 * Purpose:  Main application file for the Melody Mapper application.
 * Author:   Victor Nguyen & Don Ma
 *
 * Description:
 * This file contains the main application component that renders the entire
 * application. It imports and renders the App component.
 *
 ******************************************************************************/

import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import "bootstrap/dist/css/bootstrap.min.css";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
