# Read in a WAV and find the freq's
import pyaudio
import wave
import numpy as np
from math import log

def holyGrail(path):
    rawInput = []
    chunk = 2048

    # open up a wave
    wf = wave.open(path, 'rb')
    swidth = wf.getsampwidth()
    RATE = wf.getframerate()
    # use a Blackman window
    window = np.blackman(chunk)
    # open stream
    p = pyaudio.PyAudio()
    stream = p.open(format =
                    p.get_format_from_width(wf.getsampwidth()),
                    channels = wf.getnchannels(),
                    rate = RATE,
                    output = True)

    # read some data
    data = wf.readframes(chunk)
    # play stream and find the frequency of each chunk
    while len(data) == chunk*swidth:
        # write data out to the audio stream
        stream.write(data)
        # unpack the data and times by the hamming window
        indata = np.array(wave.struct.unpack("%dh"%(len(data)/swidth),\
                                             data))*window
        # Take the fft and square each value
        fftData=abs(np.fft.rfft(indata))**2
        # find the maximum
        which = fftData[1:].argmax() + 1
        # use quadratic interpolation around the max
        if which != len(fftData)-1:
            y0,y1,y2 = np.log(fftData[which-1:which+2:])
            x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
            # find the frequency and output it
            thefreq = (which+x1)*RATE/chunk
            print "The freq is %f Hz." % (thefreq)
            rawInput.append(int(12*log(thefreq/440)/log(2)))
        else:
            thefreq = which*RATE/chunk
            print "The freq is %f Hz." % (thefreq)
            rawInput.append(thefreq)
        # read some more data
        data = wf.readframes(chunk)
    if data:
        stream.write(data)
    stream.close()
    p.terminate()

    print(rawInput, len(rawInput))
    f = open('jank.txt', 'w')
    for i in range(len(rawInput)):
        f.write(str(rawInput[i]) + " ")  # python will convert \n to os.linesep
    f.close()  # you can omit in most cases as the destructor will call it
    return rawInput
#holyGrail("SineWave_Of_Something.wav")
#holyGrail("SineWave_440Hz.wav")
holyGrail("SineWave_Of_Fun.wav")
