# Cache-Simulator
Simulates a configurable set-associative cache on a provided trace of memory accesses


##Required Arguments:
 - **`--slots`**
  - type: `int`
  - desc: number of slots in the cache (top level)

 - **`--sets`**
  - type: `int`
  - desc: number of sets in each slot (middle level)
  
 - **`--addr`**
  - type: `int`
  - desc: number of addresses in each set (bottom level)
  
 - **`--file`**
  - type: `str`
  - desc: name of the trace file to run the simulation on
  
  
  
  
##Input File:
The trace file is line based and in order with each line formatted as follows:
 - address, in hex, of memory access (0x should be a part of the string)
 - tab
 - 'I', 'R', or 'W' indicating the access was and instruction (read), data read, or data write,
respectively

Example input might look like:

```
0x7f1cfd790cd0	I
0x7f1cfd790cd3	I
0x7ffd2087d088	W
0x7f1cfd794c30	I
0x7ffd2087d080	W
0x7f1cfd794c31	I
0x7f1cfd794c34	I
0x7ffd2087d078	W
0x7f1cfd794c36	I
```

##Program Output:

The program will print information about the number of misses to `stdout`
The toal number of misses, number of data misses and number of intruction misses will be printed. 

For Example:

    total = 142 / 3476081 
    inst = 100 / 3475072
    data = 42 / 1009
