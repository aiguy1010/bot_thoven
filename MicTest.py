import pyaudio
import numpy as np
from matplotlib import pyplot as plt
from numpy.fft import *
from scipy.io import wavfile
from numpy import log10, sqrt, array, zeros, ones, multiply
import time
import math
import wave
import struct

RATE=16000
RECORD_SECONDS = 5
CHUNKSIZE = 1024 # fixed chunk size

# initialize portaudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNKSIZE)

frames = []
for _ in range(0,int(RATE/CHUNKSIZE*RECORD_SECONDS)):
    print ("Recording...")
    data = stream.read(CHUNKSIZE)
    frames.append(np.fromstring(data, dtype=np.int16))
print("Recording Ended")

numpydata = np.hstack(frames)

# plot data
plt.figure(1)
plt.plot(numpydata)
#plt.show()

freq_domain = fft(numpydata)
plt.figure(2)
plt.plot(freq_domain)
plt.show()

# close stream
stream.stop_stream()
stream.close()
p.terminate()
wavfile.write("MicTest.wav",RATE,numpydata)
np.savetxt('test.csv',numpydata, delimiter=',')
