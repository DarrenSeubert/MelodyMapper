import wave
import librosa
import librosa.display
import numpy as np
from mido import MidiFile, MidiTrack, Message
from pydub import AudioSegment as auseg


def convert_to_midi(audio):
    """
    Function that convert raw audio file into WAV file and return MIDI file.

    Args:
        audio (String): Path to the audio file with the format of mp3, m4a and wav

    Returns:
        midi: A MIDI file.
    """

    available_extension = ["m4a", "mp3", "wav"]

    # Get the name and the extension type of the input audio file
    file_name, extension = audio.split(".")

    # Check the extension of the input audio file
    if extension not in available_extension:
        return None

    # Convert input audio file to wav file
    wav_file = auseg.from_file(audio, extension).export(
        file_name + ".wav", format="wav"
    )

    # Load audio file using librosa
    y, sr = librosa.load(wav_file, sr=None)

    # Get pitches using librosa's pitch detection
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

    # Create a new MIDI file and track
    midi = MidiFile()
    track = MidiTrack()
    midi.tracks.append(track)

    # Define velocity and time values for MIDI messages
    velocity = 64
    time_increment = 0.001

    # Process the pitches and create MIDI messages
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
    midi_file_name = file_name + ".mid"
    midi.save(midi_file_name)

    print("MIDI file saved:", midi_file_name)

    # Return midi file
    return midi_file_name


if __name__ == "__main__":
    wav_file = "sample1.wav"
    convert_to_midi(wav_file)
