################################################################################
# Filename: test_conversion.py
# Purpose:  Contains pytest test cases for audio conversion functions.
# Author:   Darren Seubert
#
# Description:
# This file contains pytest test cases for audio conversion functions,
# including tests for file format validation, WEBM to MP3 conversion,
# and audio to MIDI conversion. It uses fixtures to provide sample audio files
# for testing.
#
# Usage (Optional):
#
# Notes:
#
###############################################################################

import app.utils.conversion as conversion
import os
import pytest


@pytest.fixture
def audio_files():
    """
    Fixture to provide sample audio files for testing.

    Returns:
        dict: Dictionary containing sample audio file paths.
    """
    return {
        "mp3": "./server/app/utils/audio_sample/sample_mp3.mp3",
        "m4a": "./server/app/utils/audio_sample/sample_m4a.m4a",
        "wav": "./server/app/utils/audio_sample/sample_wav.wav",
        "webm": "./server/app/utils/audio_sample/sample_webm.webm",
        "flac": "./server/app/utils/audio_sample/sample_flac.flac",
    }


def test_is_webm_file(audio_files):
    """
    Test the is_webm_file function.

    Args:
        audio_files (dict): Fixture providing sample audio file paths.
    """
    assert conversion.is_webm_file(audio_files["webm"])
    assert not conversion.is_webm_file(audio_files["mp3"])


def test_replace_extension():
    """
    Test the replace_extension function.
    """
    assert conversion.replace_extension("folder/file.webm", "mp3") == "folder/file.mp3"
    assert conversion.replace_extension("folder/file.webm", ".m4a") == "folder/file.m4a"


def test_validate_audio_file_supported_formats(audio_files):
    """
    Test the validate_audio_file function for supported formats.

    Args:
        audio_files (dict): Fixture providing sample audio file paths.
    """
    for ext in ["mp3", "m4a", "wav"]:
        assert conversion.validate_audio_file(audio_files[ext]) == audio_files[ext]


def test_validate_audio_file_unsupported(audio_files, capsys):
    """
    Test the validate_audio_file function for unsupported formats.

    Args:
        audio_files (dict): Fixture providing sample audio file paths.
        capsys: Pytest fixture to capture stdout/stderr.
    """
    result = conversion.validate_audio_file(audio_files["flac"])
    out = capsys.readouterr().out
    assert result is None
    assert "Unsupported audio format" in out


def test_validate_audio_file_webm_conversion_success(audio_files):
    """
    Test the validate_audio_file function for WEBM conversion success.

    Args:
        audio_files (dict): Fixture providing sample audio file paths.
    """
    # Save original function to restore later
    original = conversion.convert_webm_to_mp3
    called = {}

    def fake_convert(src, dst):
        called["args"] = (src, dst)

    conversion.convert_webm_to_mp3 = fake_convert
    try:
        expected_mp3_path = conversion.replace_extension(audio_files["webm"], "mp3")
        result = conversion.validate_audio_file(audio_files["webm"])
        assert result == expected_mp3_path
        assert called["args"] == (audio_files["webm"], expected_mp3_path)
    finally:
        conversion.convert_webm_to_mp3 = original


def test_convert_to_midi_success(audio_files):
    """
    Test the convert_to_midi function for successful conversion.

    Args:
        audio_files (dict): Fixture providing sample audio file paths.
    """
    # Save originals
    orig_validate = conversion.validate_audio_file
    orig_predict = conversion.predict
    recorded = {}

    def fake_validate(path):
        return audio_files["mp3"]

    class FakeMidi:
        def write(self, midi_path):
            recorded["midi_path"] = midi_path

    def fake_predict(path):
        return None, FakeMidi(), None

    conversion.validate_audio_file = fake_validate
    conversion.predict = fake_predict

    try:
        os.makedirs(conversion.MIDI_OUTPUT_DIR, exist_ok=True)
        midi_path = conversion.convert_to_midi(audio_files["mp3"])
        expected = os.path.join(conversion.MIDI_OUTPUT_DIR, "sample_mp3.mid")
        assert midi_path == expected
        assert recorded["midi_path"] == expected
    finally:
        conversion.validate_audio_file = orig_validate
        conversion.predict = orig_predict


def test_convert_to_midi_invalid_file(audio_files):
    """
    Test the convert_to_midi function with an invalid audio file.

    Args:
        audio_files (dict): Fixture providing sample audio file paths.
    """
    orig_validate = conversion.validate_audio_file
    orig_predict = conversion.predict
    called = {}

    def fake_validate(path):
        return None

    def fake_predict(path):
        called["predict"] = True
        return None, None, None

    conversion.validate_audio_file = fake_validate
    conversion.predict = fake_predict

    try:
        result = conversion.convert_to_midi(audio_files["flac"])
        assert result is None
        assert "predict" not in called  # Predict should not have been called
    finally:
        conversion.validate_audio_file = orig_validate
        conversion.predict = orig_predict
