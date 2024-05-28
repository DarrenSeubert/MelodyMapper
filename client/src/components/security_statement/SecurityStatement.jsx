/******************************************************************************
 * Filename: SecurityStatements.jsx
 * Purpose:  An overlay component that displays security statement to user.
 * Author:   Victor Nguyen & Don Ma
 *
 * Description:
 * This file contains the SecurityStatement component that displays a security
 * statement to the user. The component is designed to be displayed as an overlay
 * on top of the main application content and is hidden by default. The user can
 * click on the overlay to close it and return to the main application content.
 *
 * Usage:
 * To use this component, simply import it into the desired file and render it.
 *
 ******************************************************************************/

import React, { useState, useEffect } from "react";
import "./SecurityStatement.css";

const SecurityStatement = () => {
  // State to store the visibility of the security statement
  const [isVisible, setIsVisible] = useState(true);

  // Add an event listener to close the popup when the user clicks outside of it
  useEffect(() => {
    const closePopup = () => setIsVisible(false);

    if (isVisible) {
      window.addEventListener("click", closePopup);
    }

    return () => window.removeEventListener("click", closePopup);
  }, [isVisible]);

  if (!isVisible) return null;

  return (
    <div
      id="security-statement-overlay"
      data-testid="security-statement-overlay" // Test id for testing
    >
      <div>
        <h1
          id="security-statement-heading"
          data-testid="security-statement-heading"
        >
          Security Statement
        </h1>
        <p id="security-statement-body" data-testid="security-statement-body">
          • Our system will only record audio in between when the user has
          clicked the start and stop recording button. <br />
          <br />
          • Our system will only store the MIDI file converted from audio
          recordings. <br />
          <br />
          • The system will state that the audio recordings will only be used
          for converting into the MIDI file. <br />
          <br />
          • MIDI files will be stored in the database and open for all users to
          see. <br />
          <br />
          • The system will not save audio recordings because users may want to
          avoid having their voice being recorded and stored on the system.
          <br />
          <br />• Our system will be vulnerable to denial-of-service attacks.
        </p>
      </div>
    </div>
  );
};

export default SecurityStatement;
