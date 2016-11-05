#!/usr/bin/env python
import multiprocessing

input = range(0,1000)

input_len = len(input)
n = min(input_len/multiprocessing.cpu_count(), 30)

print [input[i:i+n] for i in range(0, input_len, n)] 
