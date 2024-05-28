/******************************************************************************
 * Filename: ConvertFileModal.test.js
 * Purpose:  Tests the ConvertFileModal component.
 * Author:   Victor Nguyen
 *
 * Description:
 * This file contains tests for the ConvertFileModal component. The tests
 * ensure that the component renders correctly. The tests also check that the
 * conversion process works as expected. The tests simulate the user filling
 * out the form, uploading a file, and downloading the converted file. The
 * tests also check that the modal can be dismissed and that the user can
 * upload another file after a successful conversion.
 *
 * Usage:
 * Run the tests using the command `npm test`.
 ******************************************************************************/

import React from "react";
import {
  screen,
  render,
  fireEvent,
  waitFor,
  cleanup,
} from "@testing-library/react";
import ConvertFileModal from "./ConvertFileModal";
import "@testing-library/jest-dom/extend-expect";

describe("ConvertFileModal", () => {
  let handleClose,
    handleShow,
    file,
    fileInputRef,
    setFile,
    handleFileInputClick;

  beforeEach(() => {
    handleClose = jest.fn();
    handleShow = true; // or false depending on the initial state you want to test
    file = new File(["(⌐□_□)"], "chillSong.mp3", { type: "audio/mpeg" });
    fileInputRef = { current: { value: null } };
    setFile = jest.fn();
    handleFileInputClick = jest.fn();

    global.URL.createObjectURL = jest.fn(() => "http://dummy-url.com");
  });

  afterEach(() => {
    jest.clearAllMocks();
    cleanup();
  });

  it("renders without crashing", () => {
    render(
      <ConvertFileModal
        handleClose={handleClose}
        handleShow={handleShow}
        file={file}
        fileInputRef={fileInputRef}
        setFile={setFile}
        handleFileInputClick={handleFileInputClick}
        getAbbreviatedFileName={() => "chillSong.mp3"}
      />,
    );

    // Add your assertions here
    expect(screen.getByTestId("convert-file-modal")).toBeInTheDocument();
  });

  it("test handleConvert conversion success", async () => {
    // Mock fetch and URL.createObjectURL
    global.fetch = jest.fn(() =>
      Promise.resolve({
        status: 201,
        json: () =>
          Promise.resolve({ midi_data: "mockMidiData", title: "mockTitle" }),
      }),
    );
    global.URL.createObjectURL = jest.fn(() => "mockUrl");

    // Render the component
    render(
      <ConvertFileModal
        handleClose={handleClose}
        handleShow={handleShow}
        file={file}
        fileInputRef={fileInputRef}
        setFile={setFile}
        handleFileInputClick={handleFileInputClick}
        getAbbreviatedFileName={() => "chillSong.mp3"}
      />,
    );

    // Fill out the form
    fireEvent.change(screen.getByTestId("name-input"), {
      target: { value: "John Doe" },
    });
    fireEvent.change(screen.getByTestId("email-input"), {
      target: { value: "john@email.com" },
    });
    fireEvent.change(screen.getByTestId("recording-title-input"), {
      target: { value: "recording title" },
    });

    // Click the convert button
    fireEvent.click(screen.getByTestId("convert-file-button"));

    // Wait for the conversion success message to appear
    await waitFor(() => {
      expect(screen.getByText("Conversion Complete 🎉")).toBeInTheDocument();
    });
    expect(screen.getByText("Success!")).toBeInTheDocument();
    expect(
      screen.getByText(
        "Your uploaded audio file has been successfully converted to .mid format and is now available to view in your conversion history.",
      ),
    ).toBeInTheDocument();

    // Check for download midi, xml and upload another file button
    expect(screen.getByText("Upload Another File")).toBeInTheDocument();
    expect(screen.getByTestId("download-midi-button")).toBeInTheDocument();
    expect(screen.getByTestId("download-xml-button")).toBeInTheDocument();
  });

  it("test upload another file", async () => {
    // Mock fetch and URL.createObjectURL
    global.fetch = jest.fn(() =>
      Promise.resolve({
        status: 201,
        json: () =>
          Promise.resolve({ midi_data: "mockMidiData", title: "mockTitle" }),
      }),
    );
    global.URL.createObjectURL = jest.fn(() => "mockUrl");

    // Render the component
    render(
      <ConvertFileModal
        handleClose={handleClose}
        handleShow={handleShow}
        file={file}
        fileInputRef={fileInputRef}
        setFile={setFile}
        handleFileInputClick={handleFileInputClick}
        getAbbreviatedFileName={() => "chillSong.mp3"}
      />,
    );

    // Fill out the form
    fireEvent.change(screen.getByTestId("name-input"), {
      target: { value: "John Doe" },
    });
    fireEvent.change(screen.getByTestId("email-input"), {
      target: { value: "john@email.com" },
    });
    fireEvent.change(screen.getByTestId("recording-title-input"), {
      target: { value: "recording title" },
    });

    // Click the convert button
    fireEvent.click(screen.getByTestId("convert-file-button"));

    // Wait for the conversion success message to appear
    await waitFor(() => {
      expect(screen.getByText("Conversion Complete 🎉")).toBeInTheDocument();
    });

    // Click the upload another file button
    fireEvent.click(screen.getByText("Upload Another File"));

    // Check that the form is displayed
    expect(screen.getByTestId("name-input")).toBeInTheDocument();
    expect(screen.getByTestId("email-input")).toBeInTheDocument();
    expect(screen.getByTestId("recording-title-input")).toBeInTheDocument();

    // Check that name and email have not been cleared
    expect(screen.getByTestId("name-input")).toHaveValue("John Doe");
    expect(screen.getByTestId("email-input")).toHaveValue("john@email.com");

    // Check that recording title has been cleared
    expect(screen.getByTestId("recording-title-input")).toHaveValue("");
  });

  it("test handleConvert conversion error try again", async () => {
    global.fetch = jest.fn(() =>
      Promise.resolve({
        json: () =>
          Promise.resolve({ midi_data: "mockMidiData", title: "mockTitle" }),
      }),
    );
    render(
      <ConvertFileModal
        handleClose={handleClose}
        handleShow={handleShow}
        file={file}
        fileInputRef={fileInputRef}
        setFile={setFile}
        handleFileInputClick={handleFileInputClick}
        getAbbreviatedFileName={() => "chillSong.mp3"}
      />,
    );

    // Fill out the form
    fireEvent.change(screen.getByTestId("name-input"), {
      target: { value: "John Doe" },
    });

    fireEvent.change(screen.getByTestId("email-input"), {
      target: { value: "john@email.com" },
    });

    fireEvent.change(screen.getByTestId("recording-title-input"), {
      target: { value: "recording title" },
    });

    // Click the convert button
    fireEvent.click(screen.getByTestId("convert-file-button"));

    // Wait for the try again button to appear
    await waitFor(() => {
      expect(screen.getByTestId("try-again-button")).toBeInTheDocument();
    });

    // Click the try again button
    fireEvent.click(screen.getByTestId("try-again-button"));

    // Check for form to appear again
    expect(screen.getByTestId("name-input")).toBeInTheDocument();
    expect(screen.getByTestId("email-input")).toBeInTheDocument();
    expect(screen.getByTestId("recording-title-input")).toBeInTheDocument();

    // Check that name and email are not cleared
    expect(screen.getByTestId("name-input")).toHaveValue("John Doe");
    expect(screen.getByTestId("email-input")).toHaveValue("john@email.com");
    expect(screen.getByTestId("recording-title-input")).toHaveValue(
      "recording title",
    );
  });

  it("dismiss the modal", async () => {
    render(
      <ConvertFileModal
        handleClose={handleClose}
        handleShow={handleShow}
        file={file}
        fileInputRef={fileInputRef}
        setFile={setFile}
        handleFileInputClick={handleFileInputClick}
        getAbbreviatedFileName={() => "chillSong.mp3"}
      />,
    );

    // Fill out the form
    fireEvent.change(screen.getByTestId("name-input"), {
      target: { value: "John Doe" },
    });
    fireEvent.change(screen.getByTestId("email-input"), {
      target: { value: "email.com" },
    });
    fireEvent.change(screen.getByTestId("recording-title-input"), {
      target: { value: "recording title" },
    });

    // Click the close button
    fireEvent.click(screen.getByRole("button", { name: /close/i }));

    // Check that recording title has been cleared
    expect(screen.getByTestId("recording-title-input")).toHaveValue("");
  });
});
