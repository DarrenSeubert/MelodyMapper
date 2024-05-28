################################################################################
# Filename: webm_to_mp3.py
# Purpose:  To convert the WEBM file into a MP3 file
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

import subprocess

def convert_webm_to_mp3(input_file, output_file):
    # command to convert the WEBM file to MP3
    command = ['ffmpeg', '-i', input_file, '-vn', '-ab', '192k', '-ar', '44100', '-y', output_file]
    
    # run the command through the subprocess module
    try:
        result = subprocess.run(command, check=True)
        print("Conversion completed successfully.")
    except subprocess.CalledProcessError:
        print("An error occurred during conversion.")

input_webm = '/Users/roshnivenkat/CS506/project/MelodyMapper/audio_conversion/audio_sample/sample_webm.webm'
output_mp3 = '/Users/roshnivenkat/CS506/project/MelodyMapper/audio_conversion/midi_output/sample_webm.mp3'

convert_webm_to_mp3(input_webm, output_mp3)