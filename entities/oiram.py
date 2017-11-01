from entities.mob import *
from constants import *

class Oiram (Mob):
	def __init__(self, x, y):
		Mob.__init__(self, OIRAM, 0, x, y, True, 1)
		self.steps = False
		self.lstep = x
		self.cstep = 0
		self.w1 = 2/16
		self.w2 = 3/16
		self.jump = 0
		self.jumpAnimation = False

	def tick(self, level):
		if (self.jump > 0):
			self.jump -= 1
			self.vy += 0.01
			self.jumpAnimation = True
		else:
			if(self.vy<1):
				self.vy += 0.05
			else:
				self.vy = 1

		col = self.movey(level)

		if (self.jumpAnimation):
			if (col == 1):
				self.jumpAnimation = False

		if (self.vx != 0):
			if (self.vx > 0):
				self.flip = False
			if (self.vx < 0):
				self.flip = True

			col = self.movex(level)

			if (col == 0):
				self.steps = True
			else:
				self.steps = False
			if (col == 1):
				self.id = 3
		else:
			self.steps = False
			self.id = 5

	def render (self, screen):
		if (self.steps):
			self.cstep += 1
			self.id = int(self.cstep/1.5)%3
		if (self.jumpAnimation):
			self.id = 4
		screen.drawFlippedSprite( self.sheet, self.id, self.x, self.y, self.flip)
		