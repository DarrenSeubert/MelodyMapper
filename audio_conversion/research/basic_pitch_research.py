################################################################################
# Filename: basic_pitch_research.py
# Purpose:  To convert the wav file into a midi file
# Author:   Roshni Venkat & Darren Seubert
#
# Description:
# This file is used to convert an audio file in wav format to a midi file using
# the basic pitch package.
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

from basic_pitch.inference import predict_and_save, Model
from basic_pitch import ICASSP_2022_MODEL_PATH


def convert_to_midi(input_audio_path, output_directory):
    """
    Converts an audio file to MIDI using the Basic Pitch library.

    Args:
    input_audio_path (str): Path to the input audio file.
    output_directory (str): Directory where the MIDI file will be saved.
    """
    model = Model(ICASSP_2022_MODEL_PATH)
    predict_and_save(
        [input_audio_path], output_directory, True, False, False, True, model
    )


if __name__ == "__main__":
    convert_to_midi("../audio_sample/sample.wav", "../midi_output")
