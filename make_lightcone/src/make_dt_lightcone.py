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
    parse_options()