#!/usr/bin/env python
import multiprocessing
import os, sys
import math

input_data = range(0,102)

input_len = len(input_data)

bucket_size = min(input_len/multiprocessing.cpu_count(), 20)
buckets_count = math.ceil(float(input_len)/bucket_size)

#buckets = [input[i:i+n] for i in range(0, input_len, n)] 

def process_bucket(i, write_pipe_id):
	res = input_data[i*bucket_size:(i+1)*bucket_size]
	write_pipe = os.fdopen(write_pipe_id, 'w')
	write_pipe.write("%s" % res)
	write_pipe.close()

	return res

def cprint(text):
	print('C[%s]> %s' % (os.getpid(), text))

def child(i, write_pipe_id):
	cprint('A new child %d pid: %d' % (i, os.getpid()))
	cprint("Processing %s" % process_bucket(i, write_pipe_id))
	os._exit(0)  

def parent():
	i = 0
	tasks = []

	print "PARENT> Spawning workers"

	while i < buckets_count:
		read_pipe_id, write_pipe_id = os.pipe()
		newpid = os.fork()

		if newpid == 0:
			os.close(read_pipe_id)
			child(i, write_pipe_id)
		else:
			os.close(write_pipe_id)
			tasks.append([newpid, read_pipe_id])

		i += 1

	print "PARENT> Receiving results"

	for task in tasks:
		print('PARENT> Receiving %s ' % task)
		pid = task[0]
		read_pipe_id = task[1]

		read_pipe = os.fdopen(read_pipe_id)
		txt = read_pipe.read()

		print('PARENT[%s<--%s]> Received %s' % (os.getpid(), pid, txt))

		os.waitpid(pid, 0)

parent()
