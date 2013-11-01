make_lightcone
==============

Tools for making lightcone volues from C2-Ray data directly from the command line.

Installation
------------

Make sure you have c2raytools installed. Put the python scripts somewhere in your PATH. Make them executable.

Usage
-----

make_lightcone.py converts a list of xfrac or density files into a lightcone. You can use it like this:

> make_lightcone.py /path/to/data/xfrac3d*.bin -o lightcone.cbin

The script will automatically figure out the data type and redshifts of the files.

For a list of all options available:

> make_lightcone.py -h

If you want to convert an xfrac and a density lightcone into a temperature lightcone, use make_dt_lightcone.py

> make_dt_lightcone.py -xfrac xfrac_lightcone.cbin -density density_lightcone.py -min_z 7.4 -o dt_lightcone.cbin
