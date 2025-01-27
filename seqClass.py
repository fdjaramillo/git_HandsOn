#!/usr/bin/env python

# Import necessary libraries
import sys, re
from argparse import ArgumentParser

# Set up argument parser
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

# Print help and exit if no arguments are provided
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Parse the input arguments
args = parser.parse_args()
args.seq = args.seq.upper()

# Classify the sequence
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq):
        print ('The sequence is DNA')
    elif re.search('U', args.seq):
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')

# Perform motif search if a motif is provided
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("FOUND.")
    else:
        print("motif NOT FOUND")
