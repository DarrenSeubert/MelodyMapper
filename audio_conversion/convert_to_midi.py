################################################################################
# Filename: wav_to_midi.py
# Purpose:  To convert the wav file into a midi file
# Author:   Roshni Venkat
#
# Description:
# This file is used to convert an audio file in wav format to a midi file.
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

from basic_pitch.inference import predict_and_save
from basic_pitch import ICASSP_2022_MODEL_PATH


def convert_to_midi(input_audio_path, output_directory):
    """
    Converts an audio file to MIDI using the Basic Pitch library.
    
    Args:
    input_audio_path (str): Path to the input audio file.
    output_directory (str): Directory where the MIDI file will be saved.
    """

    predict_and_save(
        [input_audio_path],
        output_directory,
        True,
        False,
        False,
        False
    )

if __name__ == "__main__":
    wav_path = "/Users/roshnivenkat/CS506/project/MelodyMapper/audio_conversion/audio_sample/sample_wav.wav"
    output_dir = "/Users/roshnivenkat/CS506/project/MelodyMapper/audio_conversion/midi_output/"
    convert_to_midi(wav_path, output_dir)