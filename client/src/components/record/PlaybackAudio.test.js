/******************************************************************************
 * Filename: PlaybackAudio.test.js
 * Purpose:  Tests the PlaybackAudio component.
 * Author:   Victor Nguyen
 *
 * Description:
 * This file contains tests for the PlaybackAudio component. The tests ensure
 * that the component renders correctly. A snapshot test is included to catch
 * unintended changes to the component's structure or behavior.
 *
 * Usage:
 * Run the tests using the command `npm test`.
 ******************************************************************************/

import { cleanup, render, screen, fireEvent } from "@testing-library/react";
import PlaybackAudio from "./PlaybackAudio";
import React from "react";

describe("Playback Audio Component", () => {
  beforeEach(() => {
    // Mock the play and pause methods of HTMLMediaElement
    window.HTMLMediaElement.prototype.play = jest.fn();
    window.HTMLMediaElement.prototype.pause = jest.fn();
  });

  // Cleans up the DOM after each test to ensure a clean environment.
  afterEach(() => {
    cleanup();
  });

  // Basic render test
  it("renders the component", () => {
    // Arrange
    render(<PlaybackAudio />);

    // Assert
    expect(screen.getByText("Play Recording")).toBeInTheDocument();
  });

  it("presses the play button", () => {
    // Arrange
    render(<PlaybackAudio />);

    // Act
    fireEvent.click(screen.getByText("Play Recording"));

    // Assert
    expect(screen.getByText("Pause")).toBeInTheDocument();
  });

  it("tests handlePlayPause function when audio is playing", () => {
    // Render the Playback component
    render(<PlaybackAudio />);

    // Act
    fireEvent.click(screen.getByText("Play Recording"));
    fireEvent.click(screen.getByText("Pause"));

    // Assert
    expect(screen.getByText("Resume")).toBeInTheDocument();
  });
});
