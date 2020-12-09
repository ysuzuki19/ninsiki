#!/usr/bin/env python

import tkinter
from tkinter import RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style

import numpy as np
from functools import partial

from utils import ototools
from utils import syllables

otos = syllables.load()
otos = syllables.onlyVowel(otos)

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
  if len(otos) == 1:
    save_btn.grid(row=5, column=1, rowspan=1, columnspan=1, sticky='nsew')
  else:
    save_btn.grid(row=len(otos[0])-1, column=max_column-len(otos)+1, rowspan=2, columnspan=2, sticky='nsew')

  tki.mainloop()

if __name__ == '__main__':
  main()
