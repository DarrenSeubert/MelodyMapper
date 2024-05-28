/******************************************************************************
 * Filename: SecurityStatements.test.js
 * Purpose:  Tests the SecurityStatement component.
 * Author:   Victor Nguyen
 *
 * Description:
 * This file contains tests for the SecurityStatement component. The tests
 * verify that the component renders correctly and that the security statement
 * is displayed to the user. The tests also verify that the security statement
 * can be closed by clicking outside of it.
 *
 * Usage:
 * Run the tests using the command `npm test`.
 *
 ******************************************************************************/

import { act, render, screen, cleanup } from "@testing-library/react";
import SecurityStatement from "./SecurityStatement";

describe("Security Statement Component", () => {
  // Cleans up the DOM after each test to ensure a clean environment.
  afterEach(() => {
    cleanup();
  });

  it("whole security statement component renders", () => {
    // Arrange - Render the component
    render(<SecurityStatement />);
    const securityStatementElement = screen.getByTestId(
      "security-statement-overlay",
    );

    // Assert
    expect(securityStatementElement).toBeInTheDocument();
  });

  it("security statement heading renders", () => {
    // Arrange
    render(<SecurityStatement />);
    const securityStatementHeading = screen.getByTestId(
      "security-statement-heading",
    );

    // Assert
    expect(securityStatementHeading).toBeInTheDocument();
  });

  it("correct security statement heading content", () => {
    // Arrange
    render(<SecurityStatement />);
    const securityStatementHeading = screen.getByTestId(
      "security-statement-heading",
    );

    // Assert
    expect(securityStatementHeading).toHaveTextContent("Security Statement");
  });

  it("security statement body renders", () => {
    // Arrange
    render(<SecurityStatement />);
    const securityStatementBody = screen.getByTestId("security-statement-body");

    // Assert
    expect(securityStatementBody).toBeInTheDocument();
  });

  it("correct security statement body content", () => {
    // Arrange
    render(<SecurityStatement />);
    const securityStatments = [
      "Our system will only record audio in between when the user has clicked the start and stop recording button.",
      "Our system will only store the MIDI file converted from audio recordings.",
      "The system will state that the audio recordings will only be used for converting into the MIDI file.",
      "The system will state that the audio recordings will only be used for converting into the MIDI file.",
      "MIDI files will be stored in the database and open for all users to see.",
      "The system will not save audio recordings because users may want to avoid having their voice being recorded and stored on the system.",
      "Our system will be vulnerable to denial-of-service attacks.",
    ];
    const securityStatementBody = screen.getByTestId("security-statement-body");

    // Assert
    securityStatments.forEach((statement) => {
      expect(securityStatementBody).toHaveTextContent(statement);
    });
  });

  it("security statement closes when document is clicked", () => {
    // Arrange
    render(<SecurityStatement />); // Render the component
    const securityStatementElement = screen.getByTestId(
      "security-statement-overlay",
    );

    // Must wrap code that causes React state updates in act().
    act(() => {
      window.dispatchEvent(new MouseEvent("click")); // Simulates click event on window
    });

    // Assert
    expect(securityStatementElement).not.toBeInTheDocument();
  });
});
