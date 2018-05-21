import threading
import queue
from multithreadening.basethread import *

class ThreadHandler(queue.Queue):
	def __init__(self, threadcount):
		queue.Queue.__init__(self, maxsize = threadcount*2)
		self.queueLock = threading.Lock()
		self.populateThreads(threadcount)

	def isRunning(self):
		return self.going

	def queueWork(self, package):
		if (self.full()):
			self.doWork(package)
		else:
			self.put(package)

	def doWork(self, work):
		if (work[0] == 0):
			work[1]()
		if (work[0] == 1):
			work[1](work[2])
		if (work[0] == 3):
			work[1](work[2], work[3], work[4])
		if (work[0] == 5):
			work[1](work[2], work[3], work[4], work[5], work[6])

	def Lock(self):
		return self.queueLock.acquire()

	def Join(self):
		while self.qsize() > 0:
			self.Lock()
			work = self.get()
			self.Release()
			self.doWork(work)

	def Release(self):
		return self.queueLock.release()

	def wakeThreads(self):
		for t in self.threads:
			if (not t.isAlive()):
				t.run()

	def populateThreads(self, threadcount):
		self.threads = []
		self.threadcount = threadcount
		for i in range(0, threadcount):
			newthread = BaseThread(i, self)
			newthread.start()
			self.threads.append(newthread)
		