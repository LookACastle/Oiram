import threading

class BaseThread(threading.Thread):
	def __init__(self, threadid, q):
		threading.Thread.__init__(self)
		self.threadid = threadid
		self.q = q

	def run(self):
		while not self.q.empty():
			self.q.Lock()
			work = self.q.get()
			self.q.Release()
			self.doWork(work)

	def doWork(self, work):
		if (work[0] == 0):
			work[1]()
		if (work[0] == 1):
			work[1](work[2])
		if (work[0] == 3):
			work[1](work[2], work[3], work[4])
		if (work[0] == 5):
			work[1](work[2], work[3], work[4], work[5], work[6])

		
		