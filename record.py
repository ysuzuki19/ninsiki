#!/usr/bin/env python

import tkinter
from tkinter import RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style

import numpy as np
from functools import partial
import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100
seconds = 1

otos = [
    [
      {
        "kana": "あ",
        "alphabet": "a",
        },
      {
        "kana": "い",
        "alphabet": "i",
        },
      {
        "kana": "う",
        "alphabet": "u",
        },
      {
        "kana": "え",
        "alphabet": "e",
        },
      {
        "kana": "お",
        "alphabet": "o",
        },
      ],
    [
      {
        "kana": "か",
        "alphabet": "ka",
        },
      {
        "kana": "き",
        "alphabet": "ki",
        },
      {
        "kana": "く",
        "alphabet": "ku",
        },
      {
        "kana": "け",
        "alphabet": "ke",
        },
      {
        "kana": "こ",
        "alphabet": "ko",
        },
      ],
    [
      {
        "kana": "が",
        "alphabet": "ga",
        },
      {
        "kana": "ぎ",
        "alphabet": "gi",
        },
      {
        "kana": "ぐ",
        "alphabet": "gu",
        },
      {
        "kana": "げ",
        "alphabet": "ge",
        },
      {
        "kana": "ご",
        "alphabet": "go",
        },
      ],
    [
        {
          "kana": "さ",
          "alphabet": "sa",
          },
        {
          "kana": "し",
          "alphabet": "si",
          },
        {
          "kana": "す",
          "alphabet": "su",
          },
        {
          "kana": "せ",
          "alphabet": "se",
          },
        {
          "kana": "そ",
          "alphabet": "so",
          },
        ],
    [
        {
          "kana": "ざ",
          "alphabet": "za",
          },
        {
          "kana": "じ",
          "alphabet": "zi",
          },
        {
          "kana": "ず",
          "alphabet": "zu",
          },
        {
          "kana": "ぜ",
          "alphabet": "ze",
          },
        {
          "kana": "ぞ",
          "alphabet": "zo",
          },
        ],
    [
        {
          "kana": "た",
          "alphabet": "ta",
          },
        {
          "kana": "ち",
          "alphabet": "ti",
          },
        {
          "kana": "つ",
          "alphabet": "tu",
          },
        {
          "kana": "て",
          "alphabet": "te",
          },
        {
          "kana": "と",
          "alphabet": "to",
          },
        ],
    [
        {
          "kana": "だ",
          "alphabet": "da",
          },
        {
          "kana": "ぢ",
          "alphabet": "di",
          },
        {
          "kana": "づ",
          "alphabet": "du",
          },
        {
          "kana": "で",
          "alphabet": "de",
          },
        {
          "kana": "ど",
          "alphabet": "do",
          },
        ],
    [
        {
          "kana": "な",
          "alphabet": "na",
          },
        {
          "kana": "に",
          "alphabet": "ni",
          },
        {
          "kana": "ぬ",
          "alphabet": "nu",
          },
        {
          "kana": "ね",
          "alphabet": "ne",
          },
        {
          "kana": "の",
          "alphabet": "no",
          },
        ],
    [
        {
          "kana": "は",
          "alphabet": "ha",
          },
        {
          "kana": "ひ",
          "alphabet": "hi",
          },
        {
          "kana": "ふ",
          "alphabet": "hu",
          },
        {
          "kana": "へ",
          "alphabet": "he",
          },
        {
          "kana": "ほ",
          "alphabet": "ho",
          },
        ],
    [
        {
          "kana": "ば",
          "alphabet": "ba",
          },
        {
          "kana": "び",
          "alphabet": "bi",
          },
        {
          "kana": "ぶ",
          "alphabet": "bu",
          },
        {
          "kana": "べ",
          "alphabet": "be",
          },
        {
          "kana": "ぼ",
          "alphabet": "bo",
          },
        ],
    [
        {
          "kana": "ぱ",
          "alphabet": "pa",
          },
        {
          "kana": "ぴ",
          "alphabet": "pi",
          },
        {
          "kana": "ぷ",
          "alphabet": "pu",
          },
        {
          "kana": "ぺ",
          "alphabet": "pe",
          },
        {
          "kana": "ぽ",
          "alphabet": "po",
          },
        ],
    [
        {
          "kana": "ま",
          "alphabet": "ma",
          },
        {
          "kana": "み",
          "alphabet": "mi",
          },
        {
          "kana": "む",
          "alphabet": "mu",
          },
        {
          "kana": "め",
          "alphabet": "me",
          },
        {
          "kana": "も",
          "alphabet": "mo",
          },
        ],
    [
        {
          "kana": "や",
          "alphabet": "ya",
          },
        {
          "kana": "ゆ",
          "alphabet": "yu",
          },
        {
          "kana": "よ",
          "alphabet": "yo",
          },
        ],
    [
        {
          "kana": "わ",
          "alphabet": "wa",
          },
        {
          "kana": "を",
          "alphabet": "wo",
          },
        ],
    [
        {
          "kana": "ん",
          "alphabet": "n",
          },
        ]
    ]

def recordCallBack(oto):
  oto_recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
  sd.wait()
  oto["wave"] = oto_recording

def playCallBack(oto):
  sd.play(oto["wave"], fs)
  sd.wait()

def saveCallBack(otos):
  not_recorded = ''
  for line in otos:
    for oto in line:
      if 'wave' not in oto.keys():
        not_recorded += oto["kana"]

  if not_recorded:
    print('PLESE RECORD THE OTO:', not_recorded)
    return

  for line in otos:
    for oto in line:
      print(oto)
      filename = oto["alphabet"] + '.wav'
      write(filename, fs, oto["wave"])

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

    record_btn = Button(self, text='record', command=partial(recordCallBack,oto))
    record_btn.pack()

    play_btn = Button(self, text='play', command=partial(playCallBack,oto))
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

  save_btn = tkinter.Button(tki, text='save\notos', command=partial(saveCallBack,otos))
  save_btn.grid(row=len(otos[0])-1, column=max_column-len(otos)+1, rowspan=2, columnspan=2, sticky='nsew')

  tki.mainloop()

if __name__ == '__main__':
  main()
