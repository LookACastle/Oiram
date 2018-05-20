from entities.enemies.balumba import *

class Shelly(Balumba):
	def __init__(self, sheet, id, length, x, y, speed, animationSpeed, vx, shell):
		Balumba.__init__(self, sheet, id, length, x, y, speed, animationSpeed, vx)
		self.shell = shell
		self.height = 2
		self.flip = self.vx <= 0

	def clone(self, x, y):
		return Shelly(self.sheet, self.id, self.length, x, y, self.speed, self.animationSpeed, self.vx, self.shell)	

	def tick (self, level):
		if (self.mark):
			level.addEntity(self.shell, self.x, self.y + 16)
			self.dead = True
			return
		self.simpleMovement(level)

	def kill (self):
		self.mark = True
	
	def wallCollide(self):
		self.vx = -self.vx
		self.flip = not self.flip

	def render (self, screen):
		screen.drawFlippedSprite( self.sheet, self.id, self.x, self.y, self.flip)