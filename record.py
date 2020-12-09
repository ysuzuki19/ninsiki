#!/usr/bin/env python

import tkinter
from tkinter import RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style

import numpy as np
from functools import partial

from utils import ototools

syllables_dir = 'syllables'
dataset_dir = 'dataset'

import os
import json
syllables = []
with open(os.path.join(syllables_dir, 'all.txt'), 'r') as f:
  lines = f.readlines()
  oto_line = []
  for line in lines:
    line = line.strip('\n')
    if line == '':
      syllables.append(oto_line)
      oto_line = []
    else:
      line = line.replace('\'', '"')
      dic = json.loads(line)
      oto_line.append(dic)

print(syllables)

exit ()

class OtoRecorder(Frame):
  def __init__(self, oto):
    super().__init__()
    self.initUI(oto)

  def initUI(self, oto):
    #self.master.title('Buttons')
    #self.style = Style()
    #self.style.theme_use('default')

    msg = tkinter.Message(self, text=oto["kana"])
    msg.pack()

    record_btn = Button(self, text='record', command=partial(ototools.record,oto))
    record_btn.pack()

    play_btn = Button(self, text='play', command=partial(ototools.play,oto))
    play_btn.pack()


def main():
  tki = tkinter.Tk()
  tki.title('RECORD GOJUON')
  #tki.geometry('300x200+300+300')

  max_column = len(otos)
  for i in range(len(otos)):
    for j in range(len(otos[i])):
      app = OtoRecorder(otos[i][j])
      app.grid(row=j, column=max_column-i)

  save_btn = tkinter.Button(tki, text='save\notos', command=partial(ototools.save,otos))
  save_btn.grid(row=len(otos[0])-1, column=max_column-len(otos)+1, rowspan=2, columnspan=2, sticky='nsew')

  tki.mainloop()

if __name__ == '__main__':
  main()
