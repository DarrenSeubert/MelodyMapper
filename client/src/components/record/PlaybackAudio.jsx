/******************************************************************************
 * Filename: PlaybackAudio.jsx
 * Purpose:  Renders a button that plays or pauses an audio recording.
 * Author:   Victor Nguyen
 *
 * Description:
 * This component renders a button that plays or pauses an audio recording.
 *
 * Usage:
 * To use this component, import it into the desired file and render it.
 ******************************************************************************/

import React, { useState, useRef } from "react";
import { Button } from "react-bootstrap";

const PlaybackAudio = ({ audioSrc }) => {
  // Create a reference to the audio element
  const audioRef = useRef();

  // State to store the label of the play/pause button
  const [playPauseLabel, setPlayPauseLabel] = useState("Play Recording");

  /**
   * Plays or pauses the audio.
   */
  const handlePlayPause = () => {
    if (playPauseLabel === "Play Recording" || playPauseLabel === "Resume") {
      setPlayPauseLabel("Pause");
      audioRef.current.play();

      // When the recording ends, change the label of the play/pause button
      audioRef.current.onended = () => setPlayPauseLabel("Play Recording");
    } else {
      setPlayPauseLabel("Resume");
      audioRef.current.pause();
    }
  };

  return (
    <div>
      <audio src={audioSrc} ref={audioRef} controls hidden />
      <Button onClick={handlePlayPause}>{playPauseLabel}</Button>
    </div>
  );
};

export default PlaybackAudio;
