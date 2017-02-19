import wave
import os
import time
import pygame
from scipy.io import wavfile


def sound(filename):
    pygame.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

def properties(filename,p=False):
    names = ["nchannels", "sampwidth", "framerate", "nframes", "comptype", "compname"]
    sound = wave.open(filename)
    facts = sound.getparams()
    if (p==True):
        for i in range(0,len(names)):
            print(names[i] + ": " + str(facts[i]))
    return facts







def main():
    start_time = time.time()
    properties('~/projects/bot_thoven/sample.wav')
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
