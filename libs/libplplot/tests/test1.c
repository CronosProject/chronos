#include "plplot/plplot.h"
#include <stdio.h>
#include <stdlib.h>
#define NSIZE    101

int main()
{
    time_t t;
    srand((unsigned) time(&t));

    plsdev("xwin");

    PLFLT x[NSIZE], y[NSIZE];
    PLFLT xmin = 0., xmax = 100., ymin = 0., ymax = 100.;

    int i, r;
    for(i = 0; i < NSIZE; i++)
    {
      r = rand() % 100;
      x[i] = i;
      y[i] = r;
    }

    // Initialize plplot
    plinit();
    // Create a labelled box to hold the plot.
    plenv( xmin, xmax, ymin, ymax, 0, 0 );
    pllab( "x", "y", "Test01" );
    // Plot the data that was prepared above.
    plline( NSIZE, x, y );
    // Close PLplot library
    plend();
    exit(0);
}
