from entities.entity import *
from constants import *

class Checkpoint (Entity):
	def __init__(self, sheet, id, x, y):
		Entity.__init__(self, sheet, id, x, y)
		self.collision = True

	def clone(self, x, y):
		return Checkpoint(self.sheet, self.id, x, y)	

	def collide(self, victim):
		self.dead = True
		victim.checkpointx = self.x
		victim.checkpointy = self.y