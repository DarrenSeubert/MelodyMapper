################################################################################
# Filename: magnitude_analysis.py
# Purpose:  Visualize the magnitude of the frequency analysis.
# Author:   Livia Chandra, Roshni Venkat, & Darren Seubert
#
# Description:
# This file is used to create graph to visualize the magnitude of the frequency
# from conversion of wav file to MIDI file.
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
import librosa as lb
import matplotlib.pyplot as plt


def wav_to_magnitude_numpy(input_file):
    # Obtain audio data of audio file using librosa
    raw_audio, _ = lb.load(input_file)
    print(f"Raw Audio Data (librosa): {raw_audio}")

    # Use fast-fourier transform from numpy
    raw_audio_arr = np.array(raw_audio, dtype=float)
    audio_fft = np.fft.fft(raw_audio_arr)
    print(f"Fast-Fourier Transform: {audio_fft}")

    # Obtain the magnitudes of the frequencies
    magnitude_fft, _ = lb.magphase(audio_fft)
    print(f"Magnitudes of the frequencies: {magnitude_fft}")

    # Convert magnitudes into decibels
    db_fft = lb.amplitude_to_db(magnitude_fft)
    print(f"Decibel representation of the magnitudes: {db_fft}")

    # Visualize the magnitude of the frequencies
    plt.figure(figsize=(10, 6))
    plt.imshow(
        np.abs(db_fft[np.newaxis, :]), aspect="auto", origin="lower", cmap="viridis"
    )
    plt.colorbar(format="%+2.0f dB")
    plt.title("Magnitude Spectrum of FFT")
    plt.xlabel("Time")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    # Plotting the frequency spectrum against amplitude in decibels
    plt.figure(figsize=(10, 6))
    plt.plot(db_fft)
    plt.title("Frequency Spectrum (in Decibels)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude (dB)")
    plt.grid(True)
    plt.show()


def wav_to_magnitude_librosa(input_file):
    # Obtain audio data of audio file using librosa
    raw_audio, _ = lb.load(input_file)
    print(f"Raw Audio Data (librosa): {raw_audio}")

    # Use short-time fourier transform to analyze frequencies in the audio file
    audio_stft = lb.stft(raw_audio)
    print(f"Short-Time Fourier Transform: {audio_stft}")

    # Obtain the magnitudes of the frequencies
    magnitudes_stft, _ = lb.magphase(audio_stft)
    print(f"Magnitudes of the frequencies: {magnitudes_stft}")

    # Convert magnitudes into decibels
    db_stft = lb.amplitude_to_db(magnitudes_stft)
    print(f"Decibel representation of the magnitudes: {db_stft}")

    # Visualize the magnitude of the frequencies
    plt.figure(figsize=(10, 6))
    plt.imshow(np.abs(db_stft), aspect="auto", origin="lower", cmap="viridis")
    plt.colorbar(format="%+2.0f dB")
    plt.title("Magnitude Spectrum of STFT")
    plt.xlabel("Time")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    # Plot the frequency spectrum against amplitude in decibels
    plt.figure(figsize=(10, 6))
    plt.plot(db_stft, color="blue")
    plt.title("Frequency Spectrum (STFT) in Decibels")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude (dB)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    wav_file = "../audio_sample/sample.wav"
    wav_to_magnitude_numpy(wav_file)
    wav_to_magnitude_librosa(wav_file)
