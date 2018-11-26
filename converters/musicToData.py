import os
import sys
from scipy.io import wavfile
import numpy as np;
root = os.path.abspath('').split('\\'); root.pop();
root = '/'.join(root)+'/'


mpegLoc = root+'packages/ffmpeg/bin/ffmpeg.exe'

default = root+'music/dirty little secret.mp3'
useableFilePath = root+'music/list/'
numpyLoc = root+'numpyFiles/'

if len(sys.argv) > 1:
    default = sys.argv[1]
soundFile = default
name = soundFile.split('/')[len(soundFile.split('/'))-1]
name = name.split('.')[0];
saveAs = numpyLoc+name+'.npy';
if len(sys.argv) > 2:
    saveAs = sys.argv[2]

temp = useableFilePath+name+'.wav';
if soundFile[-3:] == 'mp3':
    if not os.path.exists(temp):
        import subprocess
        print(soundFile)
        subprocess.call([mpegLoc, '-i', soundFile,useableFilePath+name+'.wav'])
    soundFile = temp
fs, data = wavfile.read(soundFile);
data = np.asarray(data, dtype=np.int16)
print(data)
np.save(saveAs, data)
