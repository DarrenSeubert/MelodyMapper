################################################################################
# Filename: test_conversion.py
# Purpose:  Contains pytest test cases for audio conversion functions.
# Author:   Livia Chandra & Darren Seubert
#
# Description:
# This file contains pytest test cases for audio conversion functions,
# including tests for converting audio files to WAV format, dividing audio
# data into segments, and converting WAV files to MIDI format.
#
# Usage (Optional):
#
# Notes:
#
###############################################################################

import pytest
import os
from app.utils.conversion import (
    audio_to_wav,
    convert_webm_to_mp3,
    divide_audio_data,
    wav_to_midi,
)


@pytest.fixture
def audio_files():
    """
    Fixture to provide sample audio files for testing.

    Returns:
        dict: Dictionary containing sample audio file paths.
    """

    files = {
        "mp3": "./server/app/utils/audio_sample/sample_mp3.mp3",
        "m4a": "./server/app/utils/audio_sample/sample_m4a.m4a",
        "wav": "./server/app/utils/audio_sample/sample_wav.wav",
        "webm": "./server/app/utils/audio_sample/sample_webm.webm",
        "flac": "./server/app/utils/audio_sample/sample_flac.flac",
    }
    return files


# def test_audio_input(audio_files):
#     """
#     Test audio_to_wav function for converting acceptable audio files
#     (MP3, M4A, WAV, WEBM) to WAV.
#     Reject audio files other than these four file formats.

#     Args:
#         audio_files (dict): Dictionary containing sample audio file paths.
#     """

#     # Valid test case 1 - MP3
#     mp3_output = audio_to_wav(audio_files["mp3"])
#     assert mp3_output is not None

#     # Valid test case 2 - M4A
#     m4a_output = audio_to_wav(audio_files["m4a"])
#     assert m4a_output is not None

#     # Valid test case 3 - WAV
#     wav_output = audio_to_wav(audio_files["wav"])
#     assert wav_output is not None

#     # Valid test case 4 - WEBM
#     webm_output = audio_to_wav(audio_files["webm"])
#     assert webm_output is not None

#     # Invalid test case - FLAC
#     flac_output = audio_to_wav(audio_files["flac"])
#     assert flac_output is None


def test_divide_audio_data():
    """
    Test divide_audio_data helper function for segmenting audio data.

    This function tests if the audio data is correctly divided into segments
    based on the provided sample rate and tempo.
    """

    # Audio data, sample rate and bpm setup
    sample_rate = 44100
    audio_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    tempo = 120

    # Expected output
    expected_num_segments = len(audio_data) // (sample_rate * 60 / tempo * 2) + 1

    segments = list(divide_audio_data(audio_data, sample_rate, tempo))
    assert len(segments) == expected_num_segments


# def test_midi_conversion(audio_files):
#     """
#     Test wav_to_midi function for converting WAV file to MIDI file.

#     Args:
#         audio_files (dict): Dictionary containing sample audio file paths.
#     """

#     curr_dirr = os.getcwd()
#     # Pass in WAV file for MIDI conversion
#     audio_wav = audio_files["wav"]
#     midi_file = wav_to_midi(curr_dirr)
#     assert midi_file is not None
