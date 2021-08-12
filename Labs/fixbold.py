#! /usr/bin/env python3

# fix the **bold**  tags in html pre sections

import sys
from tempfile import mkstemp
import os

filename = sys.argv[1]
inf = open(filename, "r")
fd, tfile = mkstemp('','tmp','.',True) 
outf = open(tfile, "w")
INPRE = False
for line in inf:
  if line[:5] == "<pre>":
    INPRE = True
  if line[len(line)-7:] == "</pre>":
    INPRE = False
  # look for **some stuff** that's INSIDE a pre section
  if INPRE:
    if line.count("**") == 2 and line.count("****") == 0:
      # convert them from ** to <strong>xxx</strong>
      new = line.replace("**","<strong>", 1)
      line = new.replace("**","</strong>", 1)
  outf.write(line)
inf.close()
outf.close()
os.close(fd)
os.rename(tfile, filename)
