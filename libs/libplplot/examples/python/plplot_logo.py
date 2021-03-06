#!/usr/bin/env python

# Copyright (C) 2008  Alan W. Irwin
#
# This file is part of PLplot.
#
# PLplot is free software; you can redistribute it and/or modify
# it under the terms of the GNU Library General Public License as published
# by the Free Software Foundation; version 2 of the License.
#
# PLplot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public License
# along with the file PLplot; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA


# Generate PLplot logo.

# Append to effective python path so that can find plplot modules.
from plplot_python_start import *

import sys
from plplot import *

# Parse and process command line arguments
plparseopts(sys.argv, PL_PARSE_FULL)

# Initialize plplot
plinit()

from plplot_py_demos import *

XPTS = 35		# Data points in x
YPTS = 46		# Data points in y

alt = 60.0
az = 30.0
# Routine for defining a specific color map 1 in HLS space.
# if gray is true, use basic grayscale variation from half-dark to light.
# otherwise use false color variation from blue (240 deg) to red (360 deg).
def cmap1_init(gray):
    # Independent variable of control points.
    i = array((0., 1.))
    if gray:
	# Hue for control points.  Doesn't matter since saturation is zero.
	h = array((0., 0.))
	# Lightness ranging from half-dark (for interest) to light.
	l = array((0.5, 1.))
	# Gray scale has zero saturation
	s = array((0., 0.))
    else:
	# Hue ranges from blue (240 deg) to red (0 or 360 deg)
	h = array((240., 0.))
	# Lightness and saturation are constant (values taken from C example).
	l = array((0.6, 0.6))
	s = array((0.8, 0.8))

    # number of cmap1 colours is 256 in this case.
    plscmap1n(256)
    # Interpolate between control points to set up cmap1.
    plscmap1l(0, i, h, l, s)

def main():

    x = (arange(XPTS) - (XPTS / 2)) / float(XPTS / 2)
    y = (arange(YPTS) - (YPTS / 2)) / float(YPTS / 2)
    x = 1.5*x
    y = 0.5 + y
    x.shape = (-1,1)
    r2 = (x*x) + (y*y)
    z = (1. - x)*(1. - x) + 100 * (x*x - y)*(x*x - y)
    # The log argument may be zero for just the right grid.  */
    z = log(choose(greater(z,0.), (exp(-5.), z)))

    x.shape = (-1,)
    zmin = min(z.flat)
    zmax = max(z.flat)
    nlevel = 10
    step = (zmax-zmin)/(nlevel+1)
    clevel = zmin + step + arange(nlevel)*step
    plschr(0., 1.8)
    plwidth(1)
    pladv(0)
    plvpor(0.0, 1.0, 0.0, 1.0)
    plwind(-0.43, 0.840, 0.05, 0.48)
    plcol0(1)
    plw3d(1.0, 1.0, 1.0, -1.5, 1.5, -0.5, 1.5, zmin, zmax,
          alt, az)
    plbox3("bnstu", "", 0.0, 0,
           "bnstu", "", 0.0, 0,
           "bcdmnstuv", "", 0.0, 0)
    # If converting the -dev svg result later with the ImageMagick
    # "convert" application or viewing the svg result with the ImageMagick
    # "display" application must compensate for the librsvg-2.22 
    # positioning bug since librsvg is what ImageMagick uses
    # to interpret SVG results.
    if_rsvg_bug = True
    if if_rsvg_bug:
        shift = 1.00
    else:
        shift = 1.07
    plmtex3("zs", 5.0, shift, 1.0, "z axis")

    plcol0(2)
    # magnitude colored plot with faceted squares
    cmap1_init(0)
    plsurf3d(x, y, z, MAG_COLOR | FACETED, ())
    
    # Shading to provide a good background for legend.
    x1 = 0.10
    x2 = 0.8
    plvpor(0.0, 1.0, 0.0, 1.0)
    plwind(0.0, 1.0, 0.0, 1.0)
    # Completely opaque from 0. to x1
    plscol0a(15, 0, 0, 0, 1.0)
    plcol0(15)
    x=array([0., 0., x1, x1])
    y=array([0., 1., 1., 0.])
    plfill(x,y)
    # Black transparent gradient.
    pos = array([0.0, 1.0])
    rcoord = array([0.0, 0.0])
    gcoord = array([0.0, 0.0])
    bcoord = array([0.0, 0.0])
    acoord = array([1.0, 0.0])
    rev = array([0, 0])
    plscmap1n(2)
    plscmap1la(1, pos, rcoord, gcoord, bcoord, acoord, rev)
    x=array([x1, x1, x2, x2])
    plgradient(x,y,0.)
    # Logo Legend
    plscol0a(15, 255, 255, 255, 1.0)
    plcol0(15)
    x1 = 0.03
    plschr(0., 2.9)
    plsfont(PL_FCI_SANS, PL_FCI_UPRIGHT, PL_FCI_BOLD)
    plptex(x1, 0.57, 1.0, 0.0, 0.0, "PLplot")
    plschr(0., 1.5)
    plptex(x1, 0.30, 1.0, 0.0, 0.0,
           "The ultimate in cross-platform plotting")
    
main()
# Terminate plplot
plend()
