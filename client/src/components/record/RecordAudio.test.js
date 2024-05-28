/******************************************************************************
 * Filename: RecordAudio.test.js
 * Purpose:  Tests the RecordAudio component.
 * Author:   Victor Nguyen
 *
 * Description:
 * This file contains tests for the RecordAudio component. The tests check that
 * the component renders correctly and that the startRecording and stopRecording
 * functions work as expected. The tests also check that the component displays
 * the correct content when the user is recording audio.
 *
 * Usage:
 * Run the tests using the command `npm test`.
 ******************************************************************************/

import { act, cleanup, render, screen } from "@testing-library/react";
import RecordAudio from "./RecordAudio";
import React from "react";
import { useState } from "react";

describe("Record Audio Component", () => {
  const originalUseState = React.useState;
  const originalUseRef = React.useRef;

  // Cleans up the DOM after each test to ensure a clean environment.
  afterEach(() => {
    // Reset the mocks
    jest.resetAllMocks();

    // Reset the global objects
    global.navigator.mediaDevices = undefined;
    global.MediaRecorder = undefined;

    // Reset the React hooks
    React.useState = originalUseState;
    React.useRef = originalUseRef;

    cleanup();
  });

  it("whole record button component renders", () => {
    // Arrange
    render(<RecordAudio />);
    const recordButtonElement = screen.getByTestId("record-group");

    // Assert
    expect(recordButtonElement).toBeInTheDocument();
  });

  it("record heading component renders", () => {
    // Arrange
    render(<RecordAudio />);
    const recordHeadingElement = screen.getByTestId("record-heading");

    // Assert
    expect(recordHeadingElement).toBeInTheDocument();
  });

  it("correct record heading content", () => {
    // Arrange
    render(<RecordAudio />);
    const recordHeadingElement = screen.getByTestId("record-heading");

    // Assert
    expect(recordHeadingElement).toHaveTextContent("Record");
  });

  it("record button component renders", () => {
    // Arrange
    render(<RecordAudio />);
    const recordButton = screen.getByTestId("record-button");

    // Assert
    expect(recordButton).toBeInTheDocument();
  });

  it("correct record button content - start recording", () => {
    // Arrange
    render(<RecordAudio />);
    const recordButton = screen.getByTestId("record-button");

    // Assert
    expect(recordButton).toHaveTextContent("Start Recording");
  });

  it("tests startRecording function", async () => {
    // Mock MediaRecorder and its methods
    const mockMediaRecorderInstance = {
      start: jest.fn(),
      ondataavailable: null,
      onerror: null,
      mockOnDataAvailable: jest.fn(),
      mockOnError: jest.fn(),
    };
    global.MediaRecorder = jest.fn(() => mockMediaRecorderInstance);
    global.URL.createObjectURL = jest.fn();

    // Mock navigator.mediaDevices.getUserMedia
    const mockStream = "mockStream";
    act(() => {
      global.navigator.mediaDevices = {
        getUserMedia: jest.fn(() => Promise.resolve(mockStream)),
      };
    });

    // Render the component
    render(<RecordAudio />);

    // Simulate a click on the record button
    await act(async () => {
      screen.getByTestId("record-button").click();
    });

    // Simulate the ondataavailable event
    act(() => {
      const mockEvent = {
        data: new Blob(["audio data"], { type: "audio/webm" }),
      };
      mockMediaRecorderInstance.ondataavailable(mockEvent);
    });

    // Assert that the recording has started
    expect(global.MediaRecorder).toHaveBeenCalledTimes(1);
    expect(global.navigator.mediaDevices.getUserMedia).toHaveBeenCalledTimes(1);
  });

  it("tests startRecording function user media not available error", () => {
    render(<RecordAudio />);
    const recordButton = screen.getByTestId("record-button");

    // Act
    act(() => {
      recordButton.click();
    });
  });

  it("tests startRecording function not allowed error", () => {
    // Arrange - Mock navigator.mediaDevices
    global.navigator.mediaDevices = {
      getUserMedia: jest.fn(() => Promise.reject({ name: "NotAllowedError" })),
    };

    window.alert = jest.fn(); // Mock window.alert

    render(<RecordAudio />);
    const recordButton = screen.getByTestId("record-button");

    // Act
    act(() => {
      recordButton.click();
    });

    // Assert
    expect(recordButton).toHaveTextContent("Stop Recording");
  });

  it("tests the stop recording function", async () => {
    // Mock MediaRecorder and its methods
    act(() => {
      const mockStart = jest.fn();
      const mockStop = jest.fn();
      const mockMediaRecorderInstance = {
        start: mockStart,
        stop: mockStop,
        ondataavailable: null,
        onerror: null,
      };
      global.MediaRecorder = jest.fn(() => mockMediaRecorderInstance);
    });

    // Mock navigator.mediaDevices.getUserMedia
    const mockStream = {
      getTracks: jest.fn().mockReturnValue([{ stop: jest.fn() }]),
    };
    act(() => {
      global.navigator.mediaDevices = {
        getUserMedia: jest.fn(() => Promise.resolve(mockStream)),
      };
    });

    // Render the component
    render(<RecordAudio />);

    // Simulate a click on the record button
    await act(async () => {
      screen.getByTestId("record-button").click();
    });

    // Simulate a click on the record button to stop recording
    await act(async () => {
      screen.getByTestId("record-button").click();
    });

    // Assert that the recording has stopped
    expect(global.MediaRecorder).toHaveBeenCalledTimes(1);
    expect(mockStream.getTracks).toHaveBeenCalledTimes(1);
  });
});
