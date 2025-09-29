################################################################################
# Filename: frequency_analysis.py
# Purpose:  Visualize the frequencies of audio file and convert into MIDI file.
# Author:   Roshni Venkat, Livia Chandra, & Darren Seubert
#
# Description:
# This file is used to visualize the frequencies of audio file in frequency
# graph which help converting frequencies into MIDI file.
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

import numpy as np
import scipy.io.wavfile as wav
import librosa as lb
import matplotlib.pyplot as plt
from mido import MidiFile, MidiTrack, Message


def wav_to_frequency_scipy(input_file, output_file):
    sample_rate, raw_audio = wav.read(input_file)
    print(f"Sample Rate (scipy): {sample_rate}")
    print(f"Raw Audio Data (scipy): {raw_audio}")

    # Compute the Fourier Transform
    frequencies = np.fft.fftfreq(len(raw_audio)) * sample_rate
    spectrum = np.fft.fft(raw_audio)

    # Plot the frequencies
    plt.figure(figsize=(10, 4))
    plt.plot(frequencies, np.abs(spectrum))
    plt.title("Frequency Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid(True)
    plt.show()

    # Use the librosa function to convert frequencies into midi note
    converted_frequencies = []
    for frequency in frequencies:
        if frequency > 0:
            converted_frequencies.append(lb.hz_to_midi(frequency))
        else:
            converted_frequencies.append(0)

    # Plot the frequency against the MIDI note
    plt.figure(figsize=(12, 6))
    plt.plot(frequencies, converted_frequencies, color="blue")
    plt.title("Frequency to MIDI")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("MIDI Notes")
    plt.grid(True)
    plt.xlim(0, 10000)  # Limit x-axis to focus on lower frequencies
    plt.ylim(0, 127)  # Limit y-axis to MIDI note range
    plt.xticks(np.arange(0, 10001, 500))  # Set x-axis ticks every 500 Hz
    plt.yticks(np.arange(0, 128, 12))  # Set y-axis ticks every octave
    plt.show()

    # Test output by creating a new MIDI file
    mid = MidiFile()

    # Add a track to the MIDI file
    track = MidiTrack()
    mid.tracks.append(track)

    # Iterate over the converted frequencies and add note on/off messages to the track
    for midi_note in converted_frequencies:
        if 0 <= midi_note <= 127:  # Skip MIDI notes with value 0
            midi_note = int(np.abs(midi_note))
            track.append(Message("note_on", note=midi_note, velocity=64, time=0))
            track.append(Message("note_off", note=midi_note, velocity=0, time=480))

    # Save the MIDI file
    mid.save(output_file)


def wav_to_frequency_librosa(input_file, output_file):
    # Read the WAV file using librosa library
    raw_audio, sample_rate = lb.load(input_file)
    print(f"Raw Audio Data (librosa): {raw_audio}")
    print(f"Sample Rate (librosa): {sample_rate}")

    frequencies = np.fft.fftfreq(len(raw_audio)) * sample_rate
    spectrum = np.fft.fft(raw_audio)

    # Plot the frequencies using librosa library
    plt.figure(figsize=(10, 4))
    plt.plot(frequencies, np.abs(spectrum))
    plt.title("Frequency Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid(True)
    plt.show()

    # Use the librosa function to convert frequencies into midi note
    converted_frequencies = []
    for frequency in frequencies:
        if frequency > 0:
            converted_frequencies.append(lb.hz_to_midi(frequency))
        else:
            converted_frequencies.append(0)

    # Plot the frequency against the MIDI note
    plt.figure(figsize=(12, 6))
    plt.plot(frequencies, converted_frequencies, color="blue")
    plt.title("Frequency to MIDI")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("MIDI Notes")
    plt.grid(True)
    plt.xlim(0, 10000)  # Limit x-axis to focus on lower frequencies
    plt.ylim(0, 127)  # Limit y-axis to MIDI note range
    plt.xticks(np.arange(0, 10001, 500))  # Set x-axis ticks every 500 Hz
    plt.yticks(np.arange(0, 128, 12))  # Set y-axis ticks every octave
    plt.show()

    # Test output by creating a new MIDI file
    mid = MidiFile()

    # Add a track to the MIDI file
    track = MidiTrack()
    mid.tracks.append(track)

    # Iterate over the converted frequencies and add note on/off messages to the track
    for midi_note in converted_frequencies:
        if 0 <= midi_note <= 127:  # Skip MIDI notes with value 0
            midi_note = int(np.abs(midi_note))
            track.append(Message("note_on", note=midi_note, velocity=64, time=0))
            track.append(Message("note_off", note=midi_note, velocity=0, time=480))

    # Save the MIDI file
    mid.save(output_file)


if __name__ == "__main__":
    wav_file = "../audio_sample/sample.wav"
    wav_to_frequency_scipy(wav_file, "../midi_output/sample_scipy.mid")
    wav_to_frequency_librosa(wav_file, "../midi_output/sample_librosa.mid")
