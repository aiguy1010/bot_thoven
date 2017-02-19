import math, wave, array

class Wav:
    numChan = 1 #Mono
    dataSize = 2 #2 bytes
    numSampPerCyc = 0
    numSamp = 0
    def __init__(self, dur, freq, vol, data, sampRate):
        self.dur = dur #Duration in seconds
        self.freq = freq #frequency in Hz
        self.vol = vol #Percent of volume
        self.data = data #unsure what this is
        self.sampRate = sampRate #Number of samples per second 44100 is standard
        #self.numSampPerCyc = int(sampRate/freq) 
        #self.numSamp = sampRate * dur

    def createSound(self):
        f = wave.open('SineWave_Of_Fun.wav', 'w')
        for a in range(len(self.freq)):
            numSamp= self.sampRate  * self.dur[a]
            f.setparams((1, 2, self.sampRate, numSamp, "NONE", "Uncompressed"))
            numSampPerCyc = int(self.sampRate/self.freq[a])
            for i in range(numSamp):
                sample = 32767 * float(self.vol) / 100
                sample *= math.sin(math.pi * 2 * (i % numSampPerCyc) / numSampPerCyc)
                self.data.append(int(sample))
        f.writeframes(self.data.tostring())
        f.close()
'''
def main():
    aRay = []
    for i in range(3):
        a = input("Please enter note " + str(i) + ": (a to g, no sharps or flats)")
        if (a.lower() == 'a'):
            aRay.append(440)
        if (a.lower() == 'b'):
            aRay.append(494)
        if (a.lower() == 'c'):
            aRay.append(523)
        if (a.lower() == 'd'):
            aRay.append(587)
        if (a.lower() == 'e'):
            aRay.append(659)
        if (a.lower() == 'f'):
            aRay.append(698)
        if (a.lower() == 'g'):
            aRay.append(783)
    
    sound1 = Wav(1, aRay, 100, array.array('h'), 44100)
    sound1.createSound()

if __name__ == "__main__":
    main()
'''

arrayFreq = [196, 1661, 220, 2637, 293, 311, 329, 349, 1396, 2349, 523, 494, 440, 880, 932, 988, 373, 382, 396, 220, 440, 880]
bray = [1, 2, 1, 3, 1, 4, 1, 7, 3, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 10]
sound1 = Wav(bray, arrayFreq, 100, array.array('h'), 44100)
sound1.createSound()

