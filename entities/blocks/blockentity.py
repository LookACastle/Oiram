from entities.entity import *
from constants import *

class BlockEntity (Entity):
	def __init__(self, sheet, id, x, y):
		Entity.__init__(self, sheet, id, x, y)
		self.solid = True
		self.killable = False

	def rightDirection (self, direction):
		return False

	def clone(self, x, y):
		return BlockEntity(self.sheet, self.id, x, y)	

	def trigger(self, target):
		pass