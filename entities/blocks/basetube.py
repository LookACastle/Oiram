from entities.blocks.blockentity import *
from constants import *

class BaseTube (BlockEntity):
	def __init__(self, sheet, id, x, y, width, height):
		BlockEntity.__init__(self, sheet, id, x, y)
		self.width = width
		self.height = height

	def rightDirection (self, direction):
		if (direction[0] == 0 and direction[1] >= 0):
			return True
		return False

	def clone(self, x, y):
		return BaseTube(self.sheet, self.id, x, y, self.width, self.height)	

	def trigger(self, target):
		print("trigger")