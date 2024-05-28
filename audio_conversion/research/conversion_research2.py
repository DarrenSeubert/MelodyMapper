import numpy as np
import scipy.io.wavfile as wav
import librosa
from mido import MidiFile, MidiTrack, Message
import math

# Load audio file using librosa
y, sr= librosa.load("guitar.wav")

print(y)



# obtain bpm
tempo, beat_frames = librosa.beat.beat_track(y = y, sr = sr)
print(tempo)

# obtain time
beat_times = librosa.frames_to_time(beat_frames, sr=sr)
print(beat_times)



def divide_y(array, desired_len): 
      
    # looping till length
    trim = int(len(array)/desired_len)
    for i in range(0, len(array), trim):  
        yield array[i:i + trim] 
  
# obtain time signature?
trimmed_frequency = list(divide_y(y, len(beat_times))) 

# analyze frequency for each time frame
# print(len(y)) #325662
# print(len(beat_times)) # 30

frequency_list = []

# use short fourier frequency?
for frequency in trimmed_frequency:
    spec = np.abs(np.fft.rfft(frequency))
    freq = np.fft.rfftfreq(len(frequency), d=1/sr)    
    amp = spec / spec.sum()
    mean = (freq * amp).sum()
    frequency_list.append(mean)

# print(frequency_list)

midi_note = []

for freq in frequency_list:
    n = (int) ( ( 12 * math.log(freq / 220.0) / math.log(2.0) ) + 57.01 )
    midi_note.append(n)

# print(midi_note)


 # Create a new MIDI file and track
midi = MidiFile()
track = MidiTrack()
midi.tracks.append(track)

# Define velocity and time values for MIDI messages
velocity = 100


for time in beat_times:
    times = (60000 / (tempo * 192))

# create MIDI messages
for note, time in zip(midi_note, beat_times):
    if note > 0:
        # Write MIDI message and append to the MIDI track
        message_on = Message("note_on",note=int(round(note)),velocity = velocity, time = math.floor(time))
        message_off = Message("note_off",note=int(round(note)), velocity = velocity,time = math.ceil(time + 1))

        track.append(message_on)
        track.append(message_off)

# # Save MIDI file
midi_file_name = "guitar" + ".mid"
midi.save(midi_file_name)
