from scipy import signal
import numpy as np
from scipy.io import wavfile

import matplotlib.pyplot as plt
t = np.linspace(-1, 1, 200, endpoint=False)
fs, data = wavfile.read("SineWave_440Hz.wav")
widths = np.arange(1, 31)

cwtmatr = signal.cwt(data, signal.ricker, widths)
plt.imshow(cwtmatr, extent=[-1, 1, 1, 31], cmap='PRGn', aspect='auto',vmax=abs(cwtmatr).max(), vmin=-abs(cwtmatr).max())
plt.show()
