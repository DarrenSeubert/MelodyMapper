/******************************************************************************
 * Filename: ConvertFileModal.jsx
 * Purpose:  A modal that allows the user to input the required details for the
 * file conversion & convert the file.
 * Author:   Victor Nguyen, Benjamin Goh, & Darren Seubert
 *
 * Description:
 * This file contains the ConvertFileModal component that allows the user to
 * input the required details for the file conversion and convert the file.
 *
 * Usage:
 * To use this component, simply import it into the desired file and render it
 * with the required props.
 *
 ******************************************************************************/

import React from "react";
import { useState } from "react";
import { Button, Form, Modal, Spinner } from "react-bootstrap";
import downloadMidi from "../../utils/downloadMidi";
import downloadXml from "../../utils/downloadXml";

export default function ConvertFileModal(props) {
  // Whether a file is in the process of being converted
  const [isConverting, setIsConverting] = useState(false);

  // Whether the file conversion is complete
  const [conversionComplete, setConversionComplete] = useState(false);

  // Whether there was an error during the file conversion
  const [conversionError, setConversionError] = useState(false);

  // State for the required file conversion details
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [recordingTitle, setRecordingTitle] = useState("");

  // State for response
  const [backendResponse, setBackendResponse] = useState();

  /**
   * Sends file to backend for conversion and updates the UI to reflect the upload progress.
   */
  const handleConvert = () => {
    setIsConverting(true);

    const apiUrl = process.env.REACT_APP_API_URL;

    // Create a new FormData object with the selected file
    const formData = new FormData();
    formData.append("name", name);
    formData.append("email", email);
    formData.append("title", recordingTitle);
    formData.append("file", props.file);

    // Fetch request to backend
    fetch(`${apiUrl}/api/v1/midis`, {
      method: "POST",
      body: formData,
    })
      .then((response) => {
        // console.log("Posting file to backend...");
        const expectedStatus = 201;

        if (response.status === expectedStatus) {
          setConversionComplete(true);
          setIsConverting(false);
          if (props.onConversionSuccess) props.onConversionSuccess();
        } else {
          throw new Error(
            `Expected status ${expectedStatus} but received ${response.status}`,
          );
        }

        return response.json();
      })
      .then((data) => {
        // console.log("Temporary data response:", data);
        setBackendResponse(data);
      })
      .catch((error) => {
        setIsConverting(false);
        setConversionError(true);
      });
  };

  /**
   * Closes the file details modal and clears recording title.
   */
  function handleDismiss() {
    setConversionComplete(false);
    setConversionError(false);
    setRecordingTitle("");
    props.handleClose();
  }

  /**
   * Clears the recording title and file input.
   */
  function handleUploadAnotherFile() {
    // Prevents this field from clearing already cleared
    if (conversionComplete) {
      // Clear recording title but keep name and email
      setRecordingTitle("");
    }
    setConversionComplete(false);

    // Clear file input
    props.fileInputRef.current.value = null;
    props.setFile(null);
    props.handleFileInputClick();
  }

  /**
   * Clears the error message and allows the user to try the conversion again.
   */
  function handleTryAgain() {
    setConversionError(false);
  }

  // Download functions
  const handleDownloadMIDI = () => {
    const data = backendResponse;
    const midiData = data.midi_data; // base64 encoded MIDI data
    const filename = data.title + ".mid"; // Generate a file name

    // Call download function
    downloadMidi(midiData, filename);
  };

  const handleDownloadXml = () => {
    const data = backendResponse;
    const xmlData = data.xml_data; // base64 encoded MIDI data
    const filename = data.title + ".musicxml"; // Generate a file name

    // Call download function
    downloadXml(xmlData, filename);
  };

  const ConversionDetailsForm = () => {
    return (
      <div id="convert-file-modal" data-testid="convert-file-modal">
        <p style={{ color: "grey" }}>
          <em>
            Please fill out the required details below to convert your file.
          </em>
        </p>
        <Form>
          <Form.Label className="form-label">Name</Form.Label>
          <Form.Control
            type="text"
            className="text-input"
            data-testid="name-input"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
          <Form.Label className="form-label">Email</Form.Label>
          <Form.Control
            type="email"
            className="text-input"
            data-testid="email-input"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <Form.Label className="form-label">Recording Title</Form.Label>
          <Form.Control
            type="text"
            className="text-input"
            data-testid="recording-title-input"
            value={recordingTitle}
            onChange={(e) => setRecordingTitle(e.target.value)}
          />
        </Form>
      </div>
    );
  };

  return (
    <Modal
      show={props.handleShow}
      onHide={isConverting ? undefined : handleDismiss}
      centered
      size="md"
      backdrop={isConverting ? "static" : true}
      keyboard={isConverting}
    >
      <Modal.Header closeButton={!isConverting}>
        <Modal.Title>
          {isConverting
            ? "Converting"
            : conversionComplete
            ? "Conversion Complete 🎉"
            : conversionError
            ? "Conversion Error ❌"
            : "Convert File"}
        </Modal.Title>
      </Modal.Header>
      <Modal.Body>
        {isConverting ? (
          <div
            style={{
              display: "flex",
              justifyContent: "center",
            }}
          >
            <Spinner animation="border" role="status" size="lg" />
          </div>
        ) : conversionComplete ? (
          <div>
            <p>
              <b>Success!</b> <br /> <br />
              Your uploaded audio file has been successfully converted to .mid
              format and is now available to view in your conversion history.
            </p>
            <div style={{ display: "flex", justifyContent: "center" }}>
              <Button
                id="download-midi-button"
                data-testid="download-midi-button"
                onClick={handleDownloadXml}
                variant="info"
              >
                Download musicxml
              </Button>
              <Button
                id="download-xml-button"
                data-testid="download-xml-button"
                style={{ marginLeft: 20 }}
                onClick={handleDownloadMIDI}
                variant="info"
              >
                Download MIDI
              </Button>
            </div>
          </div>
        ) : conversionError ? (
          <p>
            <b>Error!</b> <br /> <br />
            There was error converting your file. Please try again.
          </p>
        ) : (
          ConversionDetailsForm()
        )}
      </Modal.Body>
      {!isConverting && (
        <Modal.Footer style={{ justifyContent: "center" }}>
          {conversionError ? (
            <>
              <Button
                id="try-again-button"
                data-testid="try-again-button"
                onClick={handleTryAgain}
                variant="warning"
              >
                Try Again
              </Button>
            </>
          ) : (
            <>
              <Button
                id="select-file-button"
                data-testid="select-file-button"
                variant="secondary"
                onClick={handleUploadAnotherFile}
              >
                {conversionComplete
                  ? "Upload Another File"
                  : props.file
                  ? "Change File"
                  : "Choose File"}
              </Button>
              {props.file && !conversionComplete && (
                <Button
                  id="convert-file-button"
                  data-testid="convert-file-button"
                  onClick={handleConvert}
                  variant="success"
                  disabled={!name || !email || !recordingTitle}
                >
                  Convert {props.getAbbreviatedFileName(props.file.name, 15)}
                </Button>
              )}
            </>
          )}
        </Modal.Footer>
      )}
    </Modal>
  );
}
