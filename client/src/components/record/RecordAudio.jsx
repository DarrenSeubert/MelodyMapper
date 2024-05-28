/******************************************************************************
 * Filename: RecordAudio.jsx
 * Purpose:  A component that allows the user to record audio.
 * Author:   Victor Nguyen & Don Ma
 *
 * Description:
 * This file contains the RecordAudio component that allows the user to record
 * audio. The component displays a button that the user can click to start and
 * stop recording audio. The recorded audio is displayed to the user once the
 * recording has stopped and can be played back and downloaded.
 *
 * Usage:
 * To use this component, import it into the desired file and render it.
 *
 ******************************************************************************/

import React, { useState, useRef } from "react";
import { Button } from "react-bootstrap";
import Playback from "./PlaybackAudio";
import "./RecordAudio.css";

const RecordAudio = () => {
  // State to store whether the user is currently recording or not
  const [isRecording, setIsRecording] = useState(false);

  // State to store the MediaRecorder object
  const [mediaRecorder, setMediaRecorder] = useState(null);

  // State to store the recorded audio
  const [recordedAudio, setRecordedAudio] = useState(null);

  // State to store the stream
  const streamRef = useRef(null);

  // State to store the label of the record button
  const [recordButtonLabel, setRecordButtonLabel] = useState("Start Recording");

  /**
   * Requests access to the user's microphone. If access is granted, the MediaRecorder object is created and the recording starts.
   */
  const startRecording = () => {
    // Return if user media not available
    if (!navigator.mediaDevices) {
      return;
    }

    // Reset the recorded audio
    setRecordButtonLabel("Stop Recording");
    setRecordedAudio(null);

    navigator.mediaDevices
      .getUserMedia({ audio: true })
      .then((stream) => {
        streamRef.current = stream; // Assign the stream to the ref
        const recorder = new MediaRecorder(stream);
        setMediaRecorder(recorder);

        recorder.start();
        setIsRecording(true);

        recorder.ondataavailable = (e) => {
          // e.data contains the audio data

          // Create a new Blob object and create an object URL for it
          const blob = new Blob([e.data], { type: "audio/webm" });
          const url = URL.createObjectURL(blob);

          setRecordedAudio(url);
        };

        recorder.onerror = (e) => console.error(e.error);
      })
      .catch((error) => {
        // Alert the user if they denied microphone access and prompt them to give permission in order to record audio
        if (error.name === "NotAllowedError") {
          alert(
            "Microphone permission denied. You need to give permission to record audio",
          );
        }
      });
  };

  /**
   * Stops the recording.
   */
  const stopRecording = () => {
    if (mediaRecorder) {
      setIsRecording(false);
      setRecordButtonLabel("Start Another Recording");
      mediaRecorder.stop();
      streamRef.current.getTracks().forEach((track) => track.stop());
    }
  };

  /**
   * Downloads the recording webm file to the user's device.
   */
  const handleDownload = () => {
    const link = document.createElement("a");
    link.href = recordedAudio;
    link.download = "melody-mapper-recording.webm";
    link.click();
  };

  return (
    <div id="record-group" data-testid="record-group">
      {/* Heading */}
      <h3 id="record-heading" data-testid="record-heading">
        Record
      </h3>

      {/* Record Button */}
      <div id="button-group" style={{ display: "flex", style: {} }}>
        <Button
          id="record-button"
          className="button"
          data-testid="record-button"
          onClick={isRecording ? stopRecording : startRecording}
          variant={isRecording ? "danger" : "success"}
        >
          {recordButtonLabel}
        </Button>

        {/* Currently Recording Indicator */}
        {isRecording && <div className="recording-indicator"></div>}

        {/* Download Recorded Audio Button */}
        {recordedAudio && (
          <Button
            id="download-button"
            className="button"
            data-testid="download-button"
            onClick={handleDownload}
            variant="dark"
          >
            Download Recording
          </Button>
        )}
      </div>

      {/* Recorded Audio */}
      {recordedAudio && <Playback audioSrc={recordedAudio} />}
    </div>
  );
};

export default RecordAudio;
