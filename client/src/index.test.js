/******************************************************************************
 * Filename: index.test.js
 * Purpose:  Tests the App component
 * Author:   Victor Nguyen
 *
 * Description:
 * This file contains tests for the App component that ensure that the component renders.
 *
 * Usage:
 * Run the tests using the command `npm test`.
 *
 ******************************************************************************/

import React from "react";
import { screen, render } from "@testing-library/react";
import App from "./App";

describe("App", () => {
  it("renders App component correctly", () => {
    render(<App />);
    const appElement = screen.getByTestId("App");
    expect(appElement).toBeInTheDocument();
  });
});
