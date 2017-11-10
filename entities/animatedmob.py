from entities.mob import *

class animatedMob (Mob):
	def __init__(self, sheet, id, length, x, y, pause, animationSpeed, collision):
		Mob.__init__(self, sheet, id, x, y, collision, 0)
		self.idOffset = id
		self.length = length
		self.animationTick = 0
		self.animationSpeed = animationSpeed
		self.pause = 0
		self.addPause = pause
		self.yOffset = 0
		self.dir = False
		
	def clone(self, x, y):
		return animatedMob(self.sheet, self.id, self.length, x, y, self.addPause, self.animationSpeed, self.collision)	

	def animationtick(self):
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
		
	def tick(self, level):
		self.animationtick()

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

	def collide(self, victim):
		victim.dead = True

	def render (self, screen):
		screen.drawSprite( self.sheet, self.id, self.x, self.y + self.yOffset)