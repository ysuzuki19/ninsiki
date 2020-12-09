import os
import sounddevice as sd
from scipy.io.wavfile import write
from . import time

dataset_dir = 'dataset'

fs = 44100
seconds = 0.5

def record(oto):
  oto_recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
  sd.wait()
  oto["wave"] = oto_recording

def play(oto):
  if "wave" not in oto:
    print('OTO NOT FOUND')
    return
  sd.play(oto["wave"], fs)
  sd.wait()

def save(otos):
  not_recorded = ''
  for line in otos:
    for oto in line:
      if 'wave' not in oto.keys():
        not_recorded += oto["kana"]

  if not_recorded:
    print('PLESE RECORD THE OTO:', not_recorded)
    return

  time_stump = time.now()
  for line in otos:
    for oto in line:
      filename = oto["alphabet"] + '_' + time_stump + '.wav'
      filename = os.path.join(dataset_dir, filename)
      write(filename, fs, oto["wave"])
  print('SAVED OTOS')
