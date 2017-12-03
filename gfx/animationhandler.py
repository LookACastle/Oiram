from gfx.animation import *

class AnimationHandler:
	def __init__(self, base):
		self.state = []
		self.animation = []
		self.lanimation = 0
		self.base = base

	def addAnimation(self, id,  length = 1, speed = 1):
		self.state.append(False)
		self.animation.append(Animation(id, length, speed))

	def toggleAnimation(self, index):
		self.state[index] = True

	def clearState(self):
		for i in range(0, len(self.state)):
			self.state[i] = False

	def getAnimation(self):
		for i in range(0, len(self.state)):
			if (self.state[i]):
				if (self.lanimation != i):
					self.animation[i].reset()
					self.lanimation = i
				return self.animation[i].getId()
		return self.base

		