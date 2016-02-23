#!/usr/bin/env python
# -*- coding: utf-8; -*-

# Append to effective python path so that can find plplot modules.
from plplot_python_start import *

import sys
from plplot import *
from numpy import *

x = [0.5]
y = [0.5]
  
title = [
  "Large Circle + Light Diagonal Cross with plptex",
  "UTF-8 plus",
  "UTF-8 squared plus",
  "UTF-8 heavy plus",
  "UTF-8 minus",
  "UTF-8 squared minus",
  "UTF-8 heavy minus",
  "UTF-8 times",
  "UTF-8 squared times",
  "UTF-8 heavy multiplication x",
  "UTF-8 number sign",
  "UTF-8 full-width number sign",
  "UTF-8 asterisk",
  "UTF-8 four teardrop-spoked asterisk",
  "UTF-8 8-spoked asterisk",
  "UTF-8 asterisk operator",
  "UTF-8 Asterisk operator with plptex",
  "Plplot Encoded Unicode Indexed Asterisk operator with plptex",
  "Plplot Encoded Hershey Indexed Asterisk operator with plptex",
  "Hershey Asterisk operator with plsym",
  "Hershey Asterisk operator with plpoin",
  "Plplot Encoded Hershey Indexed Asterisk operator with plstring",
]
ifunicode = True

# Parse and process command line arguments
plparseopts(sys.argv, PL_PARSE_FULL)

# Initialize plplot
plinit()
for kind in range(len(title)):
  pladv(0)
  plvpor(0.1, 0.9, 0.1, 0.9)
  plwind(0., 1., 0., 1.)
  # Just to show edges of viewport
  plcol0(1)
  plbox("bc", 0., 0, "bc", 0., 0)
  plcol0(2)
  plschr(0., 1.)
  plmtex("t", 1., 0.5, 0.5, title[kind])
  k=0
  for size in 2.**arange(2,-3,-1):
    k+=1
    plcol0(k)
    if kind==0:
      if ifunicode:
        plschr(0., 4.*size)
        # LARGE CIRCLE has a centre of symmetry which is about one-eighth the
        # radius below the centre of symmetry of the box for DejaVu Sans.
        plptex(0.5, 0.5, 1., 0., 0.5, "#[0x25ef]")
        # BOX DRAWINGS LIGHT DIAGONAL CROSS is one of the best centred symmetrical
        # glyphs I have found using gucharmap for DejaVu Sans.
        plptex(0.5, 0.5, 1., 0., 0.5, "#[0x2573]")
      else:
        plschr(0., 4.*size)
        # Large circle via Hershey fonts.
        plptex(0.5, 0.5, 1., 0., 0.5, "#(907)")
    elif kind ==1:
      # Print a utf-8 plus
      plschr(0., 16.*size)
      plstring(x, y, "+")
    elif kind ==2:
      # Print a utf-8 squared plus
      plschr(0., 16.*size)
      plstring(x, y, "⊞")
    elif kind ==3:
      # Print a utf-8 heavy plus
      plschr(0., 16.*size)
      plstring(x, y, "➕")
    elif kind ==4:
      # Print a utf-8 minus
      plschr(0., 16.*size)
      plstring(x, y, "-")
    elif kind ==5:
      # Print a utf-8 squared minus
      plschr(0., 16.*size)
      plstring(x, y, "⊟")
    elif kind ==6:
      # Print a utf-8 heay minus
      plschr(0., 16.*size)
      plstring(x, y, "➖")
    elif kind ==7:
      # Print a utf-8 times
      plschr(0., 16.*size)
      plstring(x, y, "×")
    elif kind ==8:
      # Print a utf-8 squared times
      plschr(0., 16.*size)
      plstring(x, y, "⊠")
    elif kind ==9:
      # Print a utf-8 heavy multiplication x
      plschr(0., 16.*size)
      plstring(x, y, "✖")
    elif kind ==10:
      # Print a utf-8 number sign
      plschr(0., 16.*size)
      plstring(x, y, "##")
    elif kind ==11:
      # Print a utf-8 full-width number sign
      plschr(0., 16.*size)
      plstring(x, y, "＃")
    elif kind ==12:
      # Print a utf-8 asterisk
      plschr(0., 16.*size)
      plstring(x, y, "*")
    elif kind ==13:
      # Print a utf-8 four teardrop-spoked asterisk
      plschr(0., 16.*size)
      plstring(x, y, "✢" )
    elif kind ==14:
      # Print a utf-8 8-spoked asterisk
      plschr(0., 16.*size)
      plstring(x, y, "✳")
    elif kind ==15:
      # Print a utf-8 asterisk operator
      plschr(0., 16.*size)
      plstring(x, y, "∗")
    elif kind ==16:
      # Print a utf-8 asterisk operator using plptex
      plschr(0., 16.*size)
      plptex(0.5, 0.5, 1., 0., 0.5, "∗")
    elif kind ==17:
      # Print a (PLplot encoded) unicode indexed asterisk operator using plptex
      plschr(0., 16.*size)
      plptex(0.5, 0.5, 1., 0., 0.5, "#[0x2217]")
    elif kind ==18:
      # Print a (PLplot encoded) Hershey indexed asterisk operator using plptex
      plschr(0., 16.*size)
      plptex(0.5, 0.5, 1., 0., 0.5, "#(728)")
    elif kind ==19:
      # Print an asterisk operator using plsym
      plssym(0., 16.*size)
      plsym(x, y, 728)
    elif kind ==20:
      # Print an asterisk operator using plpoin
      plssym(0., 16.*size)
      plpoin(x, y, 3)
    elif kind ==21:
      # Print a (PLplot encoded) Hershey indexed asterisk operator using plstring
      plschr(0., 16.*size)
      plstring(x, y, "#(728)")
    else:
      print("missing kind value: bad code")
# Terminate plplot
plend()

