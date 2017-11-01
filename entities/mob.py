from entities.entity import *
from constants import *

class Mob (Entity):
	def __init__(self, sheet, id, x, y, collision, speed):
		Entity.__init__(self, sheet, id, x, y)
		self.speed = speed
		self.collision = collision
		self.flip = False

	def clone(self, x, y):
		return Entity(self.id, self.sheet, x, y, self.width, self.height, self.speed)	

	def tick(self, level):
		self.move(level)

	def render (self, screen):
		screen.drawSprite( self.sheet, self.id, self.x, self.y)
		