#!/usr/bin/env python
import multiprocessing
import os, sys
import math
import time


def cprint(text):
	print('C[%s]> %s' % (os.getpid(), text))

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
	def __init__(self, index, data, write_pipe_id):
		cprint('A new child %d pid: %d' % (index, os.getpid()))

		self.index = index
		self.data = data
		self.write_pipe_id = write_pipe_id

	def __call__(self):
		# this is Just a test
		#time.sleep(i)

		write_pipe = os.fdopen(self.write_pipe_id, 'w')
		write_pipe.write("%s" % self.data)
		write_pipe.close()

		cprint('Child %d finished' % (self.index))

		os._exit(0)  

class ForkableTaskProcessor(object):
	def __init__(self, split_data):
		self.concurrent_tasks = multiprocessing.cpu_count()
		self.split_data = split_data

	@staticmethod
	def read_task_result(pid, read_pipe_id):
		print('PARENT> Receiving from %s ' % pid)

		read_pipe = os.fdopen(read_pipe_id)
		txt = read_pipe.read()
		read_pipe.close()

		print('PARENT[%s<--%s]> Received %s' % (os.getpid(), pid, txt))

		os.waitpid(pid, 0)

	def run(self):
		self.tasks = []
		self.running_tasks    = 0
		self.processed_tasks  = 0

		self.total_tasks      = self.split_data.buckets_count()

		print "PARENT> Spawning workers"

		while self.processed_tasks != self.total_tasks:
			self.fork_new_tasks()
			self.process_finished_tasks()

	def process_task(self, task_index, write_pipe_id):
		processor = Task(task_index, 
			self.split_data.get_bucket(task_index), 
			write_pipe_id)
		
		processor()

	def fork_new_tasks(self):
		i = self.running_tasks

		while i < self.concurrent_tasks:
			task_index = i + self.processed_tasks

			read_pipe_id, write_pipe_id = os.pipe()
			newpid = os.fork()

			if newpid == 0:
				os.close(read_pipe_id)

				self.process_task(task_index, write_pipe_id)

			else:
				os.close(write_pipe_id)
				self.tasks.append([newpid, read_pipe_id])

			i += 1

		self.running_tasks = i

	def process_finished_tasks(self):
		''' Non-Blocking bucket receive solution '''
		still_running_tasks = []

		self.running_tasks = 0

		for task in self.tasks:
			pid = task[0]
			read_pipe_id = task[1]

			if (os.WIFCONTINUED(pid)):
				self.running_tasks += 1
				still_running_tasks.append(task)
			else:
				ForkableTaskProcessor.read_task_result(pid, read_pipe_id)
				self.processed_tasks += 1

		self.tasks = still_running_tasks

# def foo(x, y):
# 	return x(y)

# print foo(math.sqrt, 2)

#sys.exit(0)

input_data = range(0, 400)
split_data = SplittableData(input_data)

tp = ForkableTaskProcessor(split_data)
tp.run()
