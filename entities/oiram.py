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
		self.onMap = False

	def tick(self, level):
		if (not self.onMap):
			if (self.vy < -0.5):
				self.vy = self.vy * 0.9
			else:
				if (self.vy < 0.5):
					self.vy = 0.5
				else:
					self.vy = self.vy * 1.1
			if (self.vy > 2.5):
				self.vy = 2.5

			col = self.movey(level)

			if (self.jump):
				if (col == True):
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

				if (col == False):
					self.steps = True
					self.push = False
				else:
					self.steps = False
					self.push = True
			else:
				self.steps = False
				self.push = False

			if (not self.jump):
				if (self.steps):
					self.cstep += 1
					self.id = int(self.cstep/3.5)%3
				elif (self.push):
					self.id = 4
				else:
					self.id = 5
			else:
				self.id = 3
		else:
			if (level.movementTicks > 0):
				vel = level.getVelocity()
				self.vx = vel[0]
				self.vy = vel[1]
				self.movex(level)
				self.movey(level)
				if (self.vx != 0 or self.vy != 0):
					self.steps = True
					if (self.vx > 0):
						self.flip = False
					if (self.vx < 0):
						self.flip = True
				else:
					self.steps = False

				if (self.steps):
					self.cstep += 1
					self.id = int(self.cstep/3.5)%3
			else:
				self.id = 5
				self.vx = 0
				self.vy = 0

	def render (self, screen):
		screen.drawFlippedSprite( self.sheet, self.id, self.x, self.y, self.flip)