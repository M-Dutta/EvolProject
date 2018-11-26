import os
import sys
from scipy.io import wavfile
import numpy as np;

root = os.path.abspath('').split('\\'); root.pop();
root = '/'.join(root)+'/'
default = root+'numpyFiles/default.npy'
testDefault = root+'numpyFiles/dirty little secret.npy'
if not os.path.exists(default):
    default = testDefault
saveAs = root+'ConvertedFromNumpy/default.wav'

if len(sys.argv) > 1:
    default = sys.argv[1]
if len(sys.argv) > 2:
    saveAs = sys.argv[2]

data = np.load(default);
scaled = np.int16(data/np.max(np.abs(data)) * 32767)
wavfile.write(saveAs, 44100, data)

