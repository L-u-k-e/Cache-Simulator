'''
  Author:  Lucas Parzych
  LICENSE: MIT
  SOURCE:  https://github.com/L-u-k-e/Cache-Simulator
'''
import sys
import argparse




########################### ARGUMENT CONFIGURATION ###########################
arg_parser = argparse.ArgumentParser(
  description='Simulates a configurable set-accociative cache on \
  a provided trace of memory accesses. '
)
arg_parser.add_argument('--slots', 
  type=int, required=True,
  help='number of slots in the cache (top level)'
)
arg_parser.add_argument('--sets',
  type=int, required=True,
  help='number of sets in each slot (middle level)'
)
arg_parser.add_argument('--addr', 
  type=int, required=True, 
  help='number of addresses in each set (bottom level)'
)
arg_parser.add_argument('--file', 
  type=str, required=True, 
  help='name of the trace file to run the simulation on'
)
args = arg_parser.parse_args()











#################################### MAIN ####################################
def main():
  lines = readlines(args.file)










################################ I/O HELPERS ################################
def readlines(filename):
  try:
    return [ line.strip() for line in open(filename) ]
  except:
    sys.exit('Error: The provided filename "{0}" does not exist in this directory.'.format(filename))











main()