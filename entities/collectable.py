from entities.mob import *

class Collectable (Mob):
	def __init__(self, sheet, id, length, x, y, pause, animationSpeed):
		Mob.__init__(self, sheet, id, x, y, True, 0)
		self.idOffset = id
		self.length = length
		print(self.length)
		self.animationTick = 0
		self.animationSpeed = animationSpeed
		self.pause = 0
		self.addPause = pause
		self.yOffset = 0
		self.dir = False
		
	def clone(self, x, y):
		return Collectable(self.sheet, self.id, self.length, x, y, self.addPause, self.animationSpeed)	

	def tick(self, level):
		if (self.pause <= 0):
			if (self.animationTick <= self.length):
				self.id = self.idOffset+int(self.animationTick)%self.length
				self.animationTick += self.animationSpeed
			else:
				self.animationTick = 0
				self.id = self.idOffset
				self.pause = self.addPause
		else:
			self.pause -= 1
	'''
		if (self.yOffset > 0):
			self.dir = False
		if(self.yOffset < -10):
			self.dir = True

		if (self.dir):
			self.yOffset += 0.2
		else:
			self.yOffset -= 0.2
	'''
	def render (self, screen):
		screen.drawSprite( self.sheet, self.id, self.x, self.y + self.yOffset)