#!/usr/bin/env python
import multiprocessing
import os, sys
import math
import time

def check_pid(pid):        
    """ Check For the existence of a unix pid. """
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True

class SplittableData(object):
	def __init__(self, data, bucket_size = None):
		self.data = data
		if bucket_size:
			self.bucket_size = bucket_size
		else:
			input_len = len(data) 
			self.bucket_size = min(input_len/multiprocessing.cpu_count(), 20)

	def get_bucket(self, index):
		return self.data[index*self.bucket_size:(index+1)*self.bucket_size]

	def len(self):
		return len(input_data)

	def buckets_count(self):
		return math.ceil(float(self.len())/self.bucket_size)

class Task(object):
	def __init__(self, index):
		self.index = index


class ForkableTaskProcessor(object):
	def __init__(self):
		self.max_concurrent = 0

input_data = range(0,40)
split_data = SplittableData(input_data)



#buckets = [input[i:i+n] for i in range(0, input_len, n)] 

def process_bucket(i, read_pipe_id, write_pipe_id):
	res = split_data.get_bucket(i)

	time.sleep(i)

	write_pipe = os.fdopen(write_pipe_id, 'w')
	write_pipe.write("%s" % res)
	write_pipe.close()

	return res

def cprint(text):
	print('C[%s]> %s' % (os.getpid(), text))

def child(i, read_pipe_id, write_pipe_id):
	cprint('A new child %d pid: %d' % (i, os.getpid()))
	cprint("Processing %s" % process_bucket(i, read_pipe_id, write_pipe_id))

	os._exit(0)  

def read_task_result(pid, read_pipe_id):
	print('PARENT> Receiving from %s ' % pid)

	read_pipe = os.fdopen(read_pipe_id)
	txt = read_pipe.read()
	read_pipe.close()

	print('PARENT[%s<--%s]> Received %s' % (os.getpid(), pid, txt))

	os.waitpid(pid, 0)


def parent():
	tasks = []


	print "PARENT> Spawning workers"

	running_tasks    = 0
	concurrent_tasks = 2
	total_tasks      = split_data.buckets_count()
	processed_tasks  = 0

	while True:
		i = running_tasks

		while i < concurrent_tasks:
			task_index = i + processed_tasks

			read_pipe_id, write_pipe_id = os.pipe()
			newpid = os.fork()

			if newpid == 0:
				os.close(read_pipe_id)
				child(task_index, read_pipe_id, write_pipe_id)
			else:
				os.close(write_pipe_id)
				tasks.append([newpid, read_pipe_id])

			i += 1

		# Blocking bucket receive solution
		new_tasks = []

		for task in tasks:
			pid = task[0]
			read_pipe_id = task[1]

			# if (check_pid(pid)):
			# 	running_tasks += 1
			# 	new_tasks.append(task)
			# else:
			# 	read_task_result(pid, read_pipe_id)
			# 	processed_tasks += 1
			read_task_result(pid, read_pipe_id)
			processed_tasks += 1

		if processed_tasks == total_tasks:
			break

		tasks = new_tasks


	# print "PARENT> Receiving results"

	# for task in tasks:
	# 	print('PARENT> Receiving %s ' % task)
	# 	pid = task[0]
	# 	read_pipe_id = task[1]

	# 	read_pipe = os.fdopen(read_pipe_id)
	# 	txt = read_pipe.read()
	# 	read_pipe.close()

	# 	print('PARENT[%s<--%s]> Received %s' % (os.getpid(), pid, txt))

	# 	os.waitpid(pid, 0)

parent()
