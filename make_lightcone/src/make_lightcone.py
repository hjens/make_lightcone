#!/usr/bin/python
'''
Created on Oct 9, 2013

@author: Hannes Jensen
'''

import numpy as np
import c2raytools as c2t
import argparse
import sys  
import os
import glob

def parse_options():
    
    parser = argparse.ArgumentParser(prog='make_lightcone', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('files', nargs='*', type=str, \
                        help='Directory or regexp for the files to make the lightcone from.')
    parser.add_argument('--min_z', type=float, default = None, help='The minimum redshift to include in the lightcone.')
    parser.add_argument('--max_z', type=float, default = None, help='The maximum redshift to include in the lightcone.')
    parser.add_argument('--los_axis', type=str, default = 'x', \
                        help='The axis to use as the line-of-sight for the coeval cubes. Can be x, y, or z.')
    parser.add_argument('--output', '-o', type=str, help='The name of the output file.',\
                         default='lightcone.cbin')
    parser.add_argument('--boxsize', '-b', type=float, default=425, help='The side of the box in Mpc/h.')
    args = parser.parse_args()
    args.files = process_files_list(args.files)
    return args
  

def process_files_list(files_list):
    if _is_nonstring_list(files_list):
        newlist = [process_files_list(f) for f in files_list]
        if _is_nonstring_list(newlist):
            return newlist[0]
        return newlist
    if os.path.isfile(files_list):
        return files_list
    else:
        return glob.glob(files_list)
    
    
def _is_nonstring_list(l):
    return hasattr(l, '__iter__') and (not isinstance(l, basestring))


def make_redshifts_filename(output_filename):
    basefilename = os.path.splitext(output_filename)[0]
    return basefilename + '_z.dat'

    
if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print 'No arguments given. Use -h to print help.'
        sys.exit(2)
    args = parse_options()
    c2t.set_sim_constants(args.boxsize)
    c2t.set_verbose(True)
    lightcone, redshifts = c2t.make_lightcone(args.files, z_low=args.min_z, z_high=args.max_z)
    c2t.save_cbin(args.output, lightcone)
    np.savetxt(make_redshifts_filename(args.output), redshifts)
    
    
    
    