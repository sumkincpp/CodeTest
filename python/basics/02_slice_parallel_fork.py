#!/usr/bin/env python
import multiprocessing
import os
import math

input = range(0,1000)

input_len = len(input)

bucket_size = min(input_len/multiprocessing.cpu_count(), 30)
buckets_count = math.ceil(input_len/bucket_size)+1

#buckets = [input[i:i+n] for i in range(0, input_len, n)] 

def get_bucket(i):
	return input[i*bucket_size:(i+1)*bucket_size]

def cprint(text):
	print('C[%s]> %s' % (os.getpid(), text))

def child(i):
	cprint('A new child %d pid: %d' % (i, os.getpid()))
	cprint("Processing %s" % get_bucket(i))
	os._exit(0)  

def parent():
	i = 0
	forked_pids = []
	while i < buckets_count:
		newpid = os.fork()

		if newpid == 0:
			child(i)
		else:
			forked_pids.append(newpid)
		#	print("P> parent: %d, child: %d\n" % (os.getpid(), newpid))

		i += 1

parent()
