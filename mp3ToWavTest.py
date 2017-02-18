import pydub
sound = pydub.AudioSegment.from_wav("test1.mp3")
sound.export("test1.wav", format="wav")
