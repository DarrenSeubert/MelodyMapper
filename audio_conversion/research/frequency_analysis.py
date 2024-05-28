################################################################################
# Filename: frequency_analysis.py
# Purpose:  Convert the wav file into a frequency plot
# Author:   Roshni Venkat & Livia Chandra
#
# Description:
# This file is used to convert an audio file in wav format to a frequency graph.
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
import matplotlib.pyplot as plt


def wav_to_frequency(wav_file):
    # read the WAV file
    rate, data = wav.read(wav_file)

    # compute the Fourier Transform
    frequencies = np.fft.fftfreq(len(data)) * rate
    spectrum = np.fft.fft(data)

    # plot the frequencies
    plt.figure(figsize=(10, 4))
    plt.plot(frequencies, np.abs(spectrum))
    plt.title("Frequency Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    wav_file = "sample1.wav"
    wav_to_frequency(wav_file)
