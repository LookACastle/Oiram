class Animation(object):
	"""docstring for Animation"""
	def __init__(self, id, length, speed):
		self.id = id
		self.length = length
		self.speed = speed
		self.step = 0

	def getId (self):
		self.step += 1
		return int(self.step/self.speed)%self.length + self.id

	def reset(self):
		self.step = 0
		
		