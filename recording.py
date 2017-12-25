# We're going to convert many audio clips of a user into images for training

from scipy import signal
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
import argparse
import os
import time

## for listening
import pyaudio
import wave



print("You will be generating audio data for training...")
name = input("What is your name: ")
directory = os.path.dirname('voices/training/' + name)

if not os.path.exists(directory):
    os.makedirs(directory)

print("You will now repeat the same word a total of 10 times")
print("This will take approximately 1 minute, and will generate 10 images")

for x in range(0, 10):
    CHUNKSIZE = 1024
    RATE = 44100
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNKSIZE)

    RECORD_SECONDS = 3


    frames = []
    print("Please Say the word: Dog")
    # time.sleep(2)
    print("Recording...")
    # record for a few seconds
    for i in range(0, int(RATE / CHUNKSIZE * RECORD_SECONDS)):
        data = stream.read(CHUNKSIZE)
        frames.append(data)

    # numpydata = np.fromstring(data, dtype=np.int16)
    print("Finished")
    # plt.plot(numpydata)
    # plt.show()

    # close stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open('temp.wav', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


    sample_rate, samples = wavfile.read('temp.wav')
    frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)
    nfft = 256
    fs = 256
    pxx, freqs, bins, im = plt.specgram(samples, nfft,fs)
    plt.axis('off')
    plt.savefig('./voices/validation/' + str(name) + '/' + str(x) + '.png',
                    dpi=100, # Dots per inch
                    frameon='false',
                    aspect='normal',
                    bbox_inches='tight',
                    pad_inches=0) # Spectrogram saved as a .png

print("Training Data Generated...")
