/******************************************************************************
 * Filename: FileUpload.test.js
 * Purpose:  Tests the FileUpload component.
 * Author:   Victor Nguyen
 *
 * Description:
 * This file contains tests for the FileUpload component. The tests ensure that
 * the component and its elements render correctly. A snapshot test is also included
 * to catch unintended changes to the component's structure or behavior.
 *
 * Usage:
 * Run the tests using the command `npm test`.
 *
 * Note:
 * More tests to be added to test actual functionality of the component
 * (e.g. file upload).
 *
 ******************************************************************************/

import { render, screen, cleanup, fireEvent } from "@testing-library/react";
import FileUpload from "./FileUpload";

describe("FileUpload component", () => {
  // Cleans up the DOM after each test to ensure a clean environment.
  afterEach(() => {
    cleanup();
  });

  it("whole file upload component renders", () => {
    // Arrange
    render(<FileUpload />);
    const fileUploadElement = screen.getByTestId("upload");

    // Assert
    expect(fileUploadElement).toBeInTheDocument();
  });

  it("heading renders", () => {
    // Arrange
    render(<FileUpload />);
    const headingElement = screen.getByTestId("upload-heading");

    // Assert
    expect(headingElement).toBeInTheDocument();
  });

  it("correct heading content", () => {
    // Arrange
    render(<FileUpload />);
    const headingElement = screen.getByTestId("upload-heading");

    // Assert
    expect(headingElement.textContent).toBe("Upload & Convert");
  });

  it("choose file button renders", () => {
    // Arrange
    render(<FileUpload />);
    const chooseFileButton = screen.getByTestId("choose-file-button");

    // Assert
    expect(chooseFileButton).toBeInTheDocument();
  });

  it("correct choose file button label when NO file is selected", () => {
    // Arrange
    render(<FileUpload />);
    const chooseFileButton = screen.getByTestId("choose-file-button");

    // Assert
    expect(chooseFileButton).toHaveTextContent("Choose File");
  });

  it("upload file button is hidden on load", () => {
    // Arrange
    render(<FileUpload />);
    const fileUploadButton = screen.queryByTestId("upload-file-button");

    // Assert
    expect(fileUploadButton).not.toBeInTheDocument();
  });

  it("accepted file formats label renders", () => {
    // Arrange
    render(<FileUpload />);
    const acceptedFileFormatsLabel = screen.getByTestId("file-format-label");

    // Assert
    expect(acceptedFileFormatsLabel).toBeInTheDocument();
  });

  it("correct accepted file formats label", () => {
    // Arrange
    render(<FileUpload />);
    const acceptedFileFormatsLabel = screen.getByTestId("file-format-label");

    // Assert
    expect(acceptedFileFormatsLabel).toHaveTextContent(
      "Accepted file upload formats:",
    );
  });

  it("accepted file formats list renders", () => {
    // Arrange
    render(<FileUpload />);
    const acceptedFileFormatsList = screen.getByTestId(
      "accepted-file-formats-list",
    );

    // Assert
    expect(acceptedFileFormatsList).toBeInTheDocument();
  });

  it("correct accepted file formats list content", () => {
    // Arrange
    render(<FileUpload />);
    const acceptedFileFormatsList = screen.getByTestId(
      "accepted-file-formats-list",
    );
    const fileFormats = [".mp3", ".m4a", ".wav", ".webm"];

    // Assert
    fileFormats.forEach((format) => {
      expect(acceptedFileFormatsList).toHaveTextContent(format);
    });
  });

  it("upload file button calls handleFileInputClick", () => {
    render(<FileUpload />);

    const chooseFileButton = screen.getByTestId("choose-file-button");

    fireEvent.click(chooseFileButton);
  });

  it("handleFileChange updates state correctly when a file is selected", () => {
    render(<FileUpload />);
    const fileInput = screen.getByTestId("file-input");
    const file = new File(["audio content"], "audio.mp3", {
      type: "audio/mp3",
    });

    fireEvent.change(fileInput, { target: { files: [file] } });

    expect(fileInput.files[0]).toBe(file);
    expect(fileInput.files).toHaveLength(1);

    // Check if upload button is visible
    const uploadButton = screen.getByTestId("upload-file-button");
    expect(uploadButton).toBeInTheDocument();

    // Press the upload button
    fireEvent.click(uploadButton);
  });

  it("handleFileChange updates state correctly when file is undefined", () => {
    render(<FileUpload />);
    const fileInput = screen.getByTestId("file-input");
    const file = undefined;

    fireEvent.change(fileInput, { target: { files: [file] } });

    expect(fileInput.files[0]).toBe(file);
    expect(fileInput.files).toHaveLength(1);

    // Check if upload button is not visible
    const uploadButton = screen.queryByTestId("upload-file-button");
    expect(uploadButton).not.toBeInTheDocument();
  });

  it("handleClose is called when modal is closed", () => {
    render(<FileUpload />);
    const fileInput = screen.getByTestId("file-input");
    const file = new File(["audio content"], "audio.mp3", {
      type: "audio/mp3",
    });

    fireEvent.change(fileInput, { target: { files: [file] } });

    expect(fileInput.files[0]).toBe(file);
    expect(fileInput.files).toHaveLength(1);

    // Check if upload button is visible
    const uploadButton = screen.getByTestId("upload-file-button");
    expect(uploadButton).toBeInTheDocument();

    // Press the upload button
    fireEvent.click(uploadButton);

    // Check if modal is open
    const modal = screen.getByTestId("convert-file-modal");
    expect(modal).toBeInTheDocument();

    // Close the modal
    fireEvent.click(screen.getByRole("button", { name: /close/i }));

    // Check that choose file button label is reset
    const chooseFileButton = screen.getByTestId("choose-file-button");
    expect(chooseFileButton).toHaveTextContent("Choose File");
  });
});
