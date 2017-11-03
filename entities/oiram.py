from entities.mob import *
from constants import *

class Oiram (Mob):
	def __init__(self, x, y):
		Mob.__init__(self, OIRAM, 0, x, y, True, 1)
		self.steps = False
		self.lstep = x
		self.cstep = 0
		self.jump = False
		self.push = False

	def tick(self, level):
		if (self.vy < 2):
			self.vy += 0.25
		else:
			self.vy = 5

		col = self.movey(level)

		if (self.jump):
			if (col == 1):
				if (self.vy > 0):
					self.jump = False
				else:
					self.vy = 0

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
				self.push = True
		else:
			self.steps = False

	def render (self, screen):
		if (not self.jump):
			if (self.steps):
				self.cstep += 1
				self.id = int(self.cstep/1.5)%3
			elif (self.push):
				self.id = 4
				self.push = False
			else:
				self.id = 5
		else:
			self.id = 3
		screen.drawFlippedSprite( self.sheet, self.id, self.x, self.y, self.flip)