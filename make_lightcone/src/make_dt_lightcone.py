#!/usr/bin/python
'''
Created on Oct 25, 2013

@author: Hannes Jensen
'''

import numpy as np
import c2raytools as c2t
import argparse
import sys  
import os
import glob

def parse_options():
    
    parser = argparse.ArgumentParser(prog='make_dt_lightcone', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--xfrac', '-x', type=str, default = None, help='The lightcone file containing the ionized fractions.')
    parser.add_argument('--density', '-d', type=str, default = None, help='The lightcone file containing the density.')
    parser.add_argument('--output', '-o', type=str, help='The name of the output file.',\
                         default='dt_lightcone.cbin')
    parser.add_argument('--min_z', type=float, default = None, help='The lowest_redshift.')
    parser.add_argument('--boxsize', '-b', type=float, default=425, help='The side of the box in Mpc/h.')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print 'No arguments given. Use -h to print help.'
        sys.exit(2)
    args = parse_options()
    c2t.set_verbose(True)
    c2t.set_sim_constants(args.boxsize)
    xfrac, xfile_type = c2t.get_data_and_type(args.xfrac, cbin_bits = 32, cbin_order = 'c')
    density, dfile_type = c2t.get_data_and_type(args.density, cbin_bits = 32, cbin_order = 'c')

    dt_lightcone = c2t.calc_dt_lightcone(xfrac, density, args.min_z)
    c2t.save_cbin(args.output, dt_lightcone)