from entities.entity import *
from constants import *

class Mob (Entity):
	def __init__(self, sheet, id, x, y, collision, speed):
		Entity.__init__(self, sheet, id, x, y)
		self.speed = speed
		self.collision = collision
		self.mobcontrol = False
		self.flip = False

	def clone(self, x, y):
		return Mob(self.sheet, self.id, x, y, self.collision, self.speed)

	def render (self, screen):
		screen.drawSprite( self.sheet, self.id, self.x, self.y)