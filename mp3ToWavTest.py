import pydub
sound = AudioSegment.from_wav("sample1.wav")
sound = sound.set_channels(1)
sound.export("sample1mono.wav", format="wav")
