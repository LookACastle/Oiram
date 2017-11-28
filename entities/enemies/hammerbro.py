from entities.enemies.simpleenemy import *

class Hammerbro (Simpleenemy):
	def __init__(self, sheet, id, length, x, y, pause, animationSpeed, flip):
		Simpleenemy.__init__(self, sheet, id, length, x, y, pause, 0, animationSpeed, 0)
		self.height = 2
		self.flip = flip

	def clone(self, x, y):
		return Hammerbro(self.sheet, self.id, self.length, x, y, self.addPause, self.animationSpeed, self.flip)	

	def tick(self, level):
		if (self.deadTime != 0):
			self.dead = True
			return
		coly = self.movey(level)
		if (self.pause == self.addPause):
			if (self.flip):
				level.addEntity(0x000104, self.x, self.y)
			else:
				level.addEntity(0x000004, self.x, self.y)
		self.animationtick()

	def render(self, screen):
		screen.drawFlippedSprite(self.sheet, self.id, self.x, self.y, self.flip)