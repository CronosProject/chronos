#  Copyright (C) 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008 Alan W. Irwin

#  plshade demo, using color fill.
#
#  This file is part of PLplot.
#
#  PLplot is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Library General Public License as published
#  by the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  PLplot is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Library General Public License for more details.
#
#  You should have received a copy of the GNU Library General Public License
#  along with PLplot; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#

from plplot_py_demos import *

NS = 20
NX = 35
NY = 46
PERIMETERPTS = 100
NUM_AXES = 1
NUM_LABELS = 1

XSPA = 2./(NX-1)
YSPA = 2./(NY-1)

tr = array((XSPA, 0.0, -1.0, 0.0, YSPA, -1.0))

def mypltr(x, y, data):
    result0 = data[0] * x + data[1] * y + data[2]
    result1 = data[3] * x + data[4] * y + data[5]
    return array((result0, result1))
		
def main():

    fill_width = 2.
    cont_color = 0
    cont_width = 0.

    n_axis_opts  = NUM_AXES
    axis_opts = zeros(NUM_AXES,"S100")
    axis_opts[0] = "bcvtm"
    num_values = zeros(NUM_AXES,"int");
    values = reshape(zeros(NUM_AXES*(NS+1)),[NUM_AXES,NS+1])
    axis_ticks = zeros(NUM_AXES)
    axis_subticks = zeros(NUM_AXES,"int")

    n_labels = NUM_LABELS
    label_opts = zeros(NUM_LABELS,"int")
    labels = zeros(NUM_LABELS,"S100")
    label_opts[0] = PL_COLORBAR_LABEL_BOTTOM
    labels[0] = "Magnitude"

    # Set up data array

    x = (arange(NX) - (NX/2)) / float(NX/2)
    x.shape = (-1,1)
    y = (arange(NY) - (NY/2)) / float(NY/2) - 1.
    zz = -sin(7.*x) * cos(7.*y) + x*x - y*y
    ww = -cos(7.*x) * sin(7.*y) + 2.*x*y
    
    zmin = min(zz.flat)
    zmax = max(zz.flat)

    clevel = zmin + (zmax - zmin) * (arange(NS)+0.5)/NS
    shedge = zmin + (zmax - zmin) * (arange(NS+1))/NS

    # Build the identity transformation between grid and world coordinates
    # using mypltr.
    # Note that *for the given* tr, mypltr(i,j,tr)[0] is only a function of i
    # and mypltr(i,j,tr)[1] is only function of j.
    xg0 = mypltr(arange(NX),0,tr)[0]
    yg0 = mypltr(0,arange(NY),tr)[1]
	    
    # Build the 1-d coord arrays.

    distort = .4
    
    xx =  xg0
    xg1 = xx + distort * cos( .5 * pi * xx )
    yy =  yg0
    yg1 = yy - distort * cos( .5 * pi * yy )

    # Build the 2-d coord arrays.
    xx.shape = (-1,1)
    xg2 = xx + distort*cos((0.5*pi)*xx)*cos((0.5*pi)*yy)
    yg2 = yy - distort*cos((0.5*pi)*xx)*cos((0.5*pi)*yy)

    # Plot using identity transform

    pladv(0)
    plvpor(0.1, 0.9, 0.1, 0.9)
    plwind(-1.0, 1.0, -1.0, 1.0)
    plpsty(0)

#   Note another alternative to produce the identical result in a different way
#   is to use the command:
#   plshades(zz, -1.0, 1.0, -1.0, 1.0, shedge, fill_width, 1)
#   The above command works because xmin, xmax, ymin, and ymax do an effective
#   linear transformation on the index ranges.  (We could have dropped
#   xmin, xmax, ymin, ymax since the defaults are -1.0, 1.0, -1.0, 1.0, but
#   for pedagogical reasons we left them in.)  The alternative below using 
#   mypltr does the exact same linear transformation because of the way that
#   the tr array has been defined.  Note that when pltr and pltr_data are 
#   defined, xmin, xmax, ymin, ymax are completely ignored so we can drop 
#   them from the argument list.
    plshades(zz, shedge, fill_width, 1, mypltr, tr)

    # Smaller text
    plschr(0.0, 0.75 )
    # Small ticks on the vertical axis
    plsmaj( 0.0, 0.5 )
    plsmin( 0.0, 0.5 )

    num_values[0] = NS + 1
    values[0] = shedge
    (colorbar_width, colorbar_height) = plcolorbar ( PL_COLORBAR_SHADE | PL_COLORBAR_SHADE_LABEL, 0, 0.005, 0.0, 0.0375, 0.875, 0, 1, 1, 0.0, 0.0, cont_color, cont_width, label_opts, labels, axis_opts, axis_ticks, axis_subticks, num_values, values)

    # Reset text and tick sizes
    plschr( 0.0, 1.0 )
    plsmaj( 0.0, 1.0 )
    plsmin( 0.0, 1.0 )

    plcol0(1)
    plbox( "bcnst", 0., 0, "bcnstv", 0., 0 )
    plcol0(2)

    pllab( "distance", "altitude", "Bogon density" )
    
    # Plot using 1d coordinate transform

    plspal0("cmap0_black_on_white.pal")
    plspal1("cmap1_blue_yellow.pal",1)
    plscmap0n(3)

    pladv(0)
    plvpor(0.1, 0.9, 0.1, 0.9)
    plwind(-1.0, 1.0, -1.0, 1.0)
    plpsty(0)

    plshades(zz, shedge, fill_width, 1, pltr1, xg1, yg1)

    # Smaller text
    plschr(0.0, 0.75 )
    # Small ticks on the vertical axis
    plsmaj( 0.0, 0.5 )
    plsmin( 0.0, 0.5 )

    num_values[0] = NS + 1
    values[0] = shedge
    (colorbar_width, colorbar_height) = plcolorbar ( PL_COLORBAR_SHADE | PL_COLORBAR_SHADE_LABEL, 0, 0.005, 0.0, 0.0375, 0.875, 0, 1, 1, 0.0, 0.0, cont_color, cont_width, label_opts, labels, axis_opts, axis_ticks, axis_subticks, num_values, values)

    # Reset text and tick sizes
    plschr( 0.0, 1.0 )
    plsmaj( 0.0, 1.0 )
    plsmin( 0.0, 1.0 )

    plcol0(1)
    plbox( "bcnst", 0.0, 0, "bcnstv", 0.0, 0 )
    plcol0(2)
	       
    pllab( "distance", "altitude", "Bogon density" )

    # Plot using 2d coordinate transform

    plspal0("cmap0_black_on_white.pal")
    plspal1("cmap1_blue_red.pal",1)
    plscmap0n(3)

    pladv(0)
    plvpor(0.1, 0.9, 0.1, 0.9)
    plwind(-1.0, 1.0, -1.0, 1.0)
    plpsty(0)

    plshades(zz, shedge, fill_width, 0, pltr2, xg2, yg2)

    # Smaller text
    plschr(0.0, 0.75 )
    # Small ticks on the vertical axis
    plsmaj( 0.0, 0.5 )
    plsmin( 0.0, 0.5 )

    num_values[0] = NS + 1
    values[0] = shedge
    (colorbar_width, colorbar_height) = plcolorbar ( PL_COLORBAR_SHADE | PL_COLORBAR_SHADE_LABEL, 0, 0.005, 0.0, 0.0375, 0.875, 0, 1, 1, 0.0, 0.0, cont_color, cont_width, label_opts, labels, axis_opts, axis_ticks, axis_subticks, num_values, values)

    # Reset text and tick sizes
    plschr( 0.0, 1.0 )
    plsmaj( 0.0, 1.0 )
    plsmin( 0.0, 1.0 )

    plcol0(1)
    plbox( "bcnst", 0.0, 0, "bcnstv", 0.0, 0 )
    plcol0(2)

    plcont(ww, clevel, pltr2, xg2, yg2)
    pllab( "distance", "altitude", "Bogon density, with streamlines" )

    # Plot using 2d coordinate transform (with contours generated by plshades)

    plspal0("")
    plspal1("",1)
    plscmap0n(3)

    pladv(0)
    plvpor(0.1, 0.9, 0.1, 0.9)
    plwind(-1.0, 1.0, -1.0, 1.0)
    plpsty(0)

    # Note default cont_color and cont_width are zero so that no contours
    # are done with other calls to plshades.  But for this call we specify
    # non-zero values so that contours are drawn.
    plshades(zz, shedge, fill_width, 2, 3.0, 0, pltr2, xg2, yg2)

    # Smaller text
    plschr(0.0, 0.75 )
    # Small ticks on the vertical axis
    plsmaj( 0.0, 0.5 )
    plsmin( 0.0, 0.5 )

    num_values[0] = NS + 1
    values[0] = shedge
    (colorbar_width, colorbar_height) = plcolorbar ( PL_COLORBAR_SHADE | PL_COLORBAR_SHADE_LABEL, 0, 0.005, 0.0, 0.0375, 0.875, 0, 1, 1, 0.0, 0.0, 2, 3.0, label_opts, labels, axis_opts, axis_ticks, axis_subticks, num_values, values)

    # Reset text and tick sizes
    plschr( 0.0, 1.0 )
    plsmaj( 0.0, 1.0 )
    plsmin( 0.0, 1.0 )

    plcol0(1)
    plbox( "bcnst", 0.0, 0, "bcnstv", 0.0, 0 )
    plcol0(2)

#    plcont(ww, clevel, "pltr2", xg2, yg2, 0)
    pllab( "distance", "altitude", "Bogon density" )

    # Example with polar coordinates that demonstrates python wrap support.

    plspal0("cmap0_black_on_white.pal")
    plspal1("cmap1_gray.pal",1)
    plscmap0n(3)

    pladv(0)
    plvpor(0.1, 0.9, 0.1, 0.9)
    plwind(-1.0, 1.0, -1.0, 1.0)

    # Build new coordinate matrices.
    
    r = arange(NX)/(NX-1.)
    r.shape = (-1,1)
    t = (2.*pi/(NY-1.))*arange(NY-1)
    xg = r*cos(t)
    yg = r*sin(t)
    z = exp(-r*r)*cos(5.*pi*r)*cos(5.*t)

    # Need a new shedge to go along with the new data set.

    zmin = min(z.flat)
    zmax = max(z.flat)
    shedge = zmin + ((zmax - zmin)/NS) * (arange(NS+1))

    plpsty(0)

    # Now we can shade the interior region.  Use wrap=2 to simulate additional
    # point at t = 2 pi.
    plshades(z, shedge, fill_width, 0, pltr2, xg, yg, 2)

    # Smaller text
    plschr(0.0, 0.75 )
    # Small ticks on the vertical axis
    plsmaj( 0.0, 0.5 )
    plsmin( 0.0, 0.5 )

    num_values[0] = NS + 1
    values[0] = shedge
    (colorbar_width, colorbar_height) = plcolorbar ( PL_COLORBAR_SHADE | PL_COLORBAR_SHADE_LABEL, 0, 0.005, 0.0, 0.0375, 0.875, 0, 1, 1, 0.0, 0.0, cont_color, cont_width, label_opts, labels, axis_opts, axis_ticks, axis_subticks, num_values, values)

    # Reset text and tick sizes
    plschr( 0.0, 1.0 )
    plsmaj( 0.0, 1.0 )
    plsmin( 0.0, 1.0 )

    # Now we can draw the perimeter.  (If do before, plshades may overlap.)
    t = 2.*pi*arange(PERIMETERPTS)/(PERIMETERPTS-1.)
    px = cos(t)
    py = sin(t)


    plcol0(1)
    plline( px, py )

    # And label the plot.

    plcol0(2)
    pllab( "", "",  "Tokamak Bogon Instability" )

    # Restore defaults
    #plcol0(1)

main()
