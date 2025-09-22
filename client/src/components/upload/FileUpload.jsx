/******************************************************************************
 * Filename: FileUpload.jsx
 * Purpose:  A component that allows the user to upload an audio file.
 * Author:   Victor Nguyen, Don Ma, & Darren Seubert
 *
 * Description:
 * This file contains the FileUpload component that allows the user to upload an
 * audio file. The component displays a file input and a button that the user can
 * click to upload the selected file. The component also displays the name of the
 * selected file and the accepted file formats.
 *
 * Usage:
 * To use this component, simply import it into the desired file and render it.
 *
 * Notes:
 * [Any additional notes, considerations, or important information
 * about the file that may be relevant to developers or users.]
 *
 ******************************************************************************/

import React, { useState, useRef } from "react";
import { Button } from "react-bootstrap";
import "./FileUpload.css";
import ConvertFileModal from "./ConvertFileModal";

const FileUpload = ({ onConversionSuccess }) => {
  // File to be uploaded
  const [file, setFile] = useState(null);

  // Whether a file has been selected
  const [fileSelected, setFileSelected] = useState(false);

  // Label for the file input
  const [chooseFileLabel, setChooseFileLabel] = useState("Choose File");

  // Reference to the file input
  const fileInputRef = useRef();

  // State for the file details modal
  const [showFileDetailsModal, setShowFileDetailsModal] = useState(false);

  /**
   * Closes the file details modal.
   */
  const handleClose = () => {
    setShowFileDetailsModal(false);
    setFileSelected(false);
    setChooseFileLabel("Choose File");
    setFile(null);
    fileInputRef.current.value = null;
  };

  /**
   * Opens the file details modal.
   */
  const handleShow = () => {
    setShowFileDetailsModal(true);
  };

  /**
   * Opens the file input dialog when the button is clicked.
   */
  const handleFileInputClick = () => {
    fileInputRef.current.click();
  };

  /**
   * Update the file name when a new file is selected and enables the upload button.
   *
   * @param {*} event - Event object
   */
  const handleFileChange = (event) => {
    let input = event.target.files[0];

    if (input === undefined) {
      setFileSelected(false);
      setChooseFileLabel("Choose File");
      return;
    } else {
      setFileSelected(true);
      setChooseFileLabel("Change File");
      setFile(input);
    }
  };

  // MARK: Helper Functions

  /**
   * Get the abbreviated file name.
   * @param {*} fileName - Name of the file
   * @returns {string} Abbreviated file name
   */
  const getAbbreviatedFileName = (fileName, length) => {
    let fileExtension = fileName.split(".").pop();
    let baseName = fileName.replace(`.${fileExtension}`, "");

    return baseName.length > length
      ? `${baseName.substring(0, length)}... .${fileExtension}`
      : fileName;
  };

  return (
    <div id="upload" data-testid="upload" style={{ padding: "1rem" }}>
      {/* File Details Modal */}
      <ConvertFileModal
        file={file}
        setFile={setFile}
        fileInputRef={fileInputRef}
        handleFileInputClick={handleFileInputClick}
        handleShow={showFileDetailsModal}
        handleClose={handleClose}
        getAbbreviatedFileName={getAbbreviatedFileName}
        onConversionSuccess={onConversionSuccess}
      />

      {/* Upload & Convert Heading */}
      <h3 id="upload-heading" data-testid="upload-heading">
        Upload & Convert
      </h3>

      <>
        <div>
          {/* File Input - hidden */}
          <input
            id="file-input"
            data-testid="file-input"
            ref={fileInputRef}
            type="file"
            onChange={handleFileChange}
            accept=".mp3, .m4a, .wav, .webm"
            hidden
          />

          {/* Choose File Button */}
          <Button
            id="choose-file-button"
            data-testid="choose-file-button"
            onClick={handleFileInputClick}
            variant="secondary"
          >
            {chooseFileLabel}
          </Button>

          {file && fileSelected && (
            /* Upload Button */
            <Button
              id="upload-file-button"
              data-testid="upload-file-button"
              onClick={handleShow}
              variant="primary"
              disabled={!fileSelected}
            >
              Upload {getAbbreviatedFileName(file.name, 10)}
            </Button>
          )}
        </div>
      </>

      {/* Accept File Formats */}
      <p id="file-format-label" data-testid="file-format-label">
        Accepted file upload formats:
      </p>
      <ul
        id="accepted-file-formats-list"
        data-testid="accepted-file-formats-list"
      >
        <li>.mp3</li>
        <li>.webm</li>
        <li>.m4a</li>
        <li>.wav</li>
      </ul>
    </div>
  );
};

export default FileUpload;
