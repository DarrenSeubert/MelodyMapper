#!/bin/bash

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

basic-pitch --model-serialization coreml --save-note-events /Users/roshnivenkat/CS506/project/MelodyMapper/audio_conversion/midi_output/ /Users/roshnivenkat/CS506/project/MelodyMapper/audio_conversion/audio_sample/sample_m4a.m4a

if [ $? -eq 0 ]; then
    echo "Conversion successful."
else
    echo "Conversion failed."
fi