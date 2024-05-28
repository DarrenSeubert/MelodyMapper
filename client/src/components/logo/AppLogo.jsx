/******************************************************************************
 * Filename: AppLogo.jsx
 * Purpose: A component that displays the Melody Mapper logo.
 * Author:   Victor Nguyen
 *
 * Description:
 * This file contains the AppLogo component that displays the Melody Mapper logo.
 *
 * Usage:
 * To use this component, simply import it into the desired file and render it.
 *
 ******************************************************************************/

import logo from "../../images/melody_logo.png";

export default function AppLogo() {
  return (
    <div id="logo-container">
      <img
        id="logo"
        data-testid="melody-logo"
        className="melody_logo"
        src={logo}
        alt="Melody Mapper Logo"
        height="80"
        style={{ margin: "1rem" }}
      />
    </div>
  );
}
