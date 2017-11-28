from entities.animatedmob import *

class Star (animatedMob):
	def __init__(self, sheet, id, length, x, y, pause, animationSpeed, collision):
		animatedMob.__init__(self, sheet, id, length, x, y, pause, animationSpeed, collision)
		self.yOffset = 0

	def clone(self, x, y):
		return Star(self.sheet, self.id, self.length, x, y, self.addPause, self.animationSpeed, self.collision)	
		
	def tick(self, level):
		self.animationtick()

		if (self.yOffset > 0):
			self.dir = False
		if(self.yOffset < -10):
			self.dir = True

		if (self.dir):
			self.yOffset += 0.2
		else:
			self.yOffset -= 0.2

	def collide(self, victim):
		victim.highMode()
		self.dead = True

	def render (self, screen):
		screen.drawSprite( self.sheet, self.id, self.x, self.y + self.yOffset)