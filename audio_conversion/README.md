# Conversion from an Audio File to MIDI

The primary aim for the audio conversion was to effectively convert between various formats such as WEBM, MP3, MP4a and WAV to a MIDI file.

## File Structure

All our input audio files are under the `audio_sample` folder, while all the MIDI file outputs are under the `midi_output` folder. We also have a `research` folder, which contains additional python files that explore the research that we have done. The current algorithm we are using is in `conversion.py`, while our alternate algorithm is in `convert_to_midi.py`. We also have `convert_to_midi.py` and `convert_to_midi.sh` which make use of the `basic_pitch` package to accomplish the conversion. Finally, `webm_to_mp3.py` is used to convert between WEBM and MP3 file formats.

## Research

We researched several methods that this could be done, exploring the FFFT (Fast Fourier Algorithm) and SFFT (Saccadic Fast Fourier Transform) algorithms in more detail. This is present in the `research` folder in the Python files `frequency_analysis.py` and `magnitude_analysis.py`. The first explores using the FFFT algorithm while the latter explores using the SFFT algorithm. In both these files, we expore the frequencies of the notes by plotting them against the magnitude using the `matplotlib` package. We will now go into a little more detail on our research in `pitch_conversion_research.py` and `beat_frequency_conversion_research.py`

### `pitch_conversion_research.py`

The `convert_to_midi` function is designed to convert an audio file into a MIDI file, supporting audio formats such as mp3, m4a, and wav. Initially, the function parses the filename to extract the extension and verifies if it is one of the supported formats. If the file format is valid, the audio file is converted to a WAV format using the `pydub.AudioSegment` library, which provides an interface for audio format manipulation. Once converted to WAV format, the audio file is loaded into an array using `librosa.load`, which returns the audio data and its sampling rate (`sr`). `librosa's` `piptrack` function is then used to perform pitch tracking on the audio data, extracting pitches and their magnitudes throughout the audio clip.

The script then creates a new MIDI file and a MIDI track to store MIDI messages. For each detected pitch that is a valid MIDI note, a `note_on` and `note_off` message is created and appended to the track, simulating the pressing and releasing of a piano key. Finally, the script saves the constructed MIDI file, providing a MIDI representation of the audio file's pitch content.

### `beat_frequency_conversion_research.py`

This file converts a WAV audio file into a MIDI file by analyzing its rhythmic and pitch content using various libraries including `librosa` and `numpy`. Initially, the audio file is loaded into an array `y` with its respective sampling rate `sr` using `librosa.load()`. Subsequently, the code determines the tempo of the audio in beats per minute (BPM) using `librosa.beat.beat_track()`, and converts beat frames into time (in seconds) using `librosa.frames_to_time()`. These time stamps represent significant rhythmic points in the audio which correlate to the beats, thereby establishing a framework for timing the MIDI notes.

In the next steps, the audio array `y` is segmented into smaller arrays corresponding to the identified beats. This is done by dividing the audio signal into chunks of approximately equal length proportional to the number of beats. For each chunk, a Fast Fourier Transform (FFFT) is applied to determine the spectrum of frequencies present, from which the mean frequency is calculated by weighing frequencies by their amplitudes. These mean frequencies are then converted to MIDI note numbers using a formula that maps frequency to the MIDI scale. The script then creates a MIDI file and constructs MIDI `note_on` and `note_off` messages for each calculated MIDI note at the corresponding beat time, simulating the sequence of notes being played on a MIDI device. The MIDI messages are timed according to the calculated beat times and stored in a track within the MIDI file, which is finally saved as the converted MIDI file.

## Using Packages

We were able to succesfully convert between the audio files to MIDI using the `basic_pitch` package from Spotify. This is present in `basic_pitch_research.py`. The file invokes `predict_and_save` method from the `basic_pitch` package, which predicts the note events using a `TensorFlow` model that is installed with the package itself. It output both the midi file and a csv of the predicted notes. The full documentation for the package can be found [here](https://github.com/spotify/basic-pitch?tab=readme-ov-file).

## Outcome

After exploring several ways of converting the audio file to MIDI, we decided to go with our own algorithm, present in `conversion.py`. This accepts three audio file formats: MP3, M4a and WAV. The function `audio_to_wav` converts the input audio files into a WAV format, ensuring compatibility for further processing. This function checks the file extension, uses `pydub` to handle the conversion, and saves the respective output. Following the conversion to WAV, the main function `wav_to_midi` is responsible for the audio-to-MIDI conversion process. It starts by loading the WAV file using `librosa` to obtain the audio data and sample rate, then utilizes `librosa.yin` for pitch detection to determine the dominant pitch, which helps in setting the key signature for the MIDI file. The code calculates the tempo of the audio and segments the audio data based on this tempo to align the audio frames with the rhythmic beats. These segments undergo a Short-Time Fourier Transform (STFT) using `scipy.signal` to analyze the frequency content, where each segment’s median frequency is determined. These frequencies are then mapped to MIDI note values. The code creates a MIDI file with tracks populated by `note_on` and `note_off` messages corresponding to these notes, timed according to the beats, and saves the output MIDI file in a specified directory.

We also needed a way to convert between WEBM and MP3 audio formats, since we also accept the WEBM audio. We perform this conversion in the `webm_to_mp3.py` file, in which we use the `ffmpeg` framework [documentation](https://ffmpeg.org/documentation.html) to convert between WEBM and MP3. We can then convert the output MP3 file into a MIDI file using the conversion process above.
