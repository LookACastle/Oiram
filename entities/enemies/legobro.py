from entities.enemies.simpleenemy import *

class Legobro (Simpleenemy):
	def __init__(self, sheet, id, length, x, y, pause, animationSpeed, flip):
		Simpleenemy.__init__(self, sheet, id, length, x, y, pause, 1, animationSpeed, 0)
		self.height = 2
		self.flip = flip

	def clone(self, x, y):
		return Legobro(self.sheet, self.id, self.length, x, y, self.addPause, self.animationSpeed, self.flip)	

	def tick(self, level):
		self.movey(level)
		if (self.pause == self.addPause and self.visible):
			if (self.flip):
				level.addEntity(0x040001, self.x, self.y)
			else:
				level.addEntity(0x040000, self.x, self.y)
		self.animationtick()

	def render(self, screen):
		screen.drawFlippedSprite(self.sheet, self.id, self.x, self.y, self.flip)