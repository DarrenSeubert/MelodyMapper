################################################################################
# Filename: pitch_conversion_research.py
# Purpose:  Research file to convert audio file into MIDI file.
# Author:   Livia Chandra, Roshni Venkat, & Darren Seubert
#
# Description:
# This file is used to convert audio file into MIDI file using librosa, pydub,
# and mido libraries.
#
# Usage (Optional):
# [Instructions or examples demonstrating how to use the code in this file.
# Include any dependencies or prerequisites required for proper usage.]
#
# Notes:
# [Any additional notes, considerations, or important information
# about the file that may be relevant to developers or users.]
#
###############################################################################

import os
import librosa
import numpy as np
from mido import MidiFile, MidiTrack, Message
from pydub import AudioSegment as auseg


def convert_to_midi(input_file, output_file):
    """
    Function that convert raw audio file into MIDI file and saves it.

    Args:
        input_file (String): Path to the audio file with the format of wav
        output_file (String): Path to save the output MIDI file
    """

    available_extension = ["m4a", "mp3", "wav"]

    # Get the name and the extension type of the input audio file
    file_path, file_basename = os.path.split(input_file)
    file_name, extension = os.path.splitext(file_basename)
    extension = extension.lstrip(".")

    # Check the extension of the input audio file
    if extension not in available_extension:
        return None

    # Create a temporary WAV file path in the same directory as the input file
    temp_wav_path = os.path.join(file_path, file_name + ".wav")

    # Export to the temporary path
    auseg.from_file(input_file, extension).export(temp_wav_path, format="wav")

    # Load audio file using librosa
    y, sr = librosa.load(temp_wav_path, sr=None)

    # Get pitches using librosa's pitch detection
    pitches, _ = librosa.piptrack(y=y, sr=sr)

    # Create a new MIDI file and track
    midi = MidiFile()
    track = MidiTrack()
    midi.tracks.append(track)

    # Define velocity and time values for MIDI messages
    velocity = 64
    time_increment = 0.001

    # Process the pitches and create MIDI messages
    # Use a context manager to suppress the divide-by-zero warning
    with np.errstate(divide="ignore"):
        for i in range(pitches.shape[1]):  # iterate over frames
            for j in range(pitches.shape[0]):  # iterate over pitches
                midi_note = librosa.hz_to_midi(pitches[j, i])

                # Check if the MIDI note is a finite number
                if np.isfinite(midi_note):
                    midi_note = int(round(midi_note))

                    if midi_note > 0:

                        # Write MIDI message and append to the MIDI track
                        message_on = Message(
                            "note_on",
                            note=midi_note,
                            velocity=velocity,
                            time=int(i * time_increment * sr),
                        )
                        message_off = Message(
                            "note_off",
                            note=midi_note,
                            velocity=velocity,
                            time=int((i + 1) * time_increment * sr),
                        )

                        track.append(message_on)
                        track.append(message_off)

    # Save MIDI file
    midi.save(output_file)


if __name__ == "__main__":
    convert_to_midi(
        "../audio_sample/sample.wav", "../midi_output/pitch_conversion_research.mid"
    )
