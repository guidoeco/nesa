#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import sys
import re

#filecodes = ["0051"]
with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  filecodes = [i.strip() for i in f.readlines()]

print("\t".join(["page","route","sequence","name","date","location","miles","chains","restriction"]))
for filecode in filecodes:
  with open("a_"+filecode+".txt", 'r') as afile:
    for line in afile:
      #words = [i.strip() for i in re.split(r"\?+|'| I |\\",line.decode('utf-8').encode('ascii', 'replace'))]
      if line == '':
        continue
      words = [i.strip().decode('utf-8').encode('ascii', 'replace') for i in line.split(" ")]
      if len(words) == 1:
        continue
      (route, sequence) = words[:2]
      name = " ".join(words[2:-1])
      date = words[-1]
      #break
  #print("\t".join([filecode, route, sequence, name, date]))
  blist = []
  with open("b_"+filecode+".txt", 'r') as file:
    blist += [j for j in [i.strip() for i in file] if j != '']
      
  clist = []
  with open("c_"+filecode+".txt", 'r') as file:
    clist += [j for j in [i.strip() for i in file] if j != '']
  #print(blist)
  #print(clist)

  (rname, mile, chain, star) = ("", "", "", "")
  (omile, ochain) = ("", "")
  
  for i in clist:
    i = re.sub("([(]) *", " \g<1>",re.sub(" *([)])", "\g<1> ", i))
    i = re.sub("(Jn[)]*)", " \g<1> ", i)
    i = re.sub("t0", " ", i)
    i = re.sub(r"[$]","s", i)
    i = re.sub(r"8:","&", i)
    i = re.sub(r"I'","P", i)
    i = re.sub(" +"," ", i)

    words = i.strip().split(" ")
    #print(words)
    if len(words) == 1:
      if len(words[0]) > 3:
        print("\t".join([filecode, route, sequence, name, date, words[0], "", "", "Z"]))
      continue
    #print i
    match = False
    k = 0
    #print words
    for j in range(2):
      (rname, mile, chain, star) = (" ".join(words[:-2-j]), words[-2-j], words[-1-j], "")
      #rname = re.sub("\|", "l", rname)
      mile = re.sub(' +|[()]', '', mile)
      mile = re.sub("[oOD]", "0", mile)      
      mile = re.sub("[T]", "7", mile)      
      mile = re.sub("[?BQ]", "8", mile)
      mile = re.sub('(\d{1,3})[mt"]o*', "\g<1>", mile)
      chain = re.sub(' +|[()]', '', chain)
      chain = re.sub("[oOD]", "0", chain)
      chain = re.sub("[?BQ]", "8", chain)
      chain = re.sub("[T]", "7", chain)      
      chain = re.sub("^(\d)$", "0\g<1>", chain)
      if re.match("^-{0,1}\d{1,3}$", mile) and re.match("^\d{2}$|^\d{2}.5$", chain):
        match = True
        if j == 1:
          star = "*"
          break
        if len(words) <= 3:
          break
        if re.match("[()]",words[-3]):          
          star = re.sub("[()]", '', words[-3])
          rname = " ".join(words[:-3])
        break
      if len(words) <= 2:
        break

    if match:
      print("\t".join([filecode, route, sequence, name, date, rname, mile, chain, star]))
      omile = mile
      ochain = chain
    else:
      rname = " ".join(words)
      print("\t".join([filecode, route, sequence, name, date, rname, omile, ochain, "X"]))

  dlist = []
  with open("d_"+filecode+".txt", 'r') as file:
    for i in file:
      i = re.sub(" +"," ",re.sub("([(])", " \g<1>",re.sub("([)])", "\g<1> ", i)))
      words = i.strip().split(" ")
      if words[0] == 'T' and words[1] == '=':
        mile = words[-2]
        chain = words[-1]
        star = re.sub("[()]",'',words[-4])
        rname = " ".join(words[2:-4])        

        if len(star) > 3:
          rname = " ".join(words[2:-3])        
          star = ""
        print("\t".join([filecode, route, sequence, name, date, rname, mile, chain, star]))
