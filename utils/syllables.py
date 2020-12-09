import os
import json

syllables_dir = 'syllables'

def load():
  otos = []
  with open(os.path.join(syllables_dir, 'all.txt'), 'r') as f:
    lines = f.readlines()
    oto_line = []
    for line in lines:
      line = line.strip('\n')
      if line == '':
        otos.append(oto_line)
        oto_line = []
      else:
        line = line.replace('\'', '"')
        dic = json.loads(line)
        oto_line.append(dic)
  return otos

def onlyVowel(otos):
  vowel = []
  vowel.append(otos[0])
  return vowel
