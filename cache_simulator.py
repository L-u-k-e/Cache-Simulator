'''
  Author:  Lucas Parzych
  LICENSE: MIT
  SOURCE:  https://github.com/L-u-k-e/Cache-Simulator
'''
import sys
import argparse




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











def main():
  lines = readlines(args.file)
  memory_accesses = parseTraceInfo(lines)
  
  cache = [[None] * args.sets] * args.slots 
  misses = { 'total': 0, 'instruction': 0, 'data': 0  }
  
  for entry in memory_accesses:
    slot = cache[entry['slot']]
    match = next((tag for tag in slot if tag == entry['tag']), None)
    if not match:
      slot.pop()
      slot.insert(0, entry['tag'])
      misses[entry['type']] += 1

  misses['total'] = misses['instruction'] + misses['data']
  number_of_accesses = len(memory_accesses)
  for key, value in misses.items():
    print("{0} : {1} / {2}".format(key, value, number_of_accesses))







def parseTraceInfo(lines):
  #Figure out how many bits we need to reference each level of the cache.
  a = vars(args).items() 
  bit_lengths = { k: len(bin(v-1)[2:]) for k, v in a if k != 'file' }

  #Get the starting positions of the slot/offset portions of the address
  offset_start = -bit_lengths['addr']
  slot_start = -(bit_lengths['slots'] + bit_lengths['addr'])
  
  #Extract useful info from each trace entry. 
  #I won't actually be using all of this info.
  def mappingFunc(line):
    parts = line.split()
    result = {}
    a = bin(int(parts[0], 16))[2:]
    result['address'] = a
    result['offset'] = int(a[offset_start:], 2)
    result['slot'] = int(a[slot_start:offset_start], 2)
    result['tag'] = int(a[:slot_start])
    result['type'] = 'instruction' if parts[1] == 'I' else 'data'
    return result
    
  return list(map(mappingFunc, lines))
  







def readlines(filename):
  try:
    return [ line.strip() for line in open(filename) ]
  except:
    sys.exit('Error: The provided filename "{0}" does not exist in this directory.'.format(filename))











main()