import numpy as np
from scipy.io import wavfile
from raf_tools import *
# from playsound import playsound
# playsound('music.wav')


samplerate, data = wavfile.read('music.wav')
samps = data[samplerate*38:samplerate*151, 0]
peak = 1.05 * np.max(np.abs(samps))
samps = samps/peak
write_raf('music.raf', samples=samps, fs_Hz=samplerate, low_v=-1., high_v=1.)

#  python raf_tools.py -f music.raf -c 1 --vpp 2 -r 0 -o 1
