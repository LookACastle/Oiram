from entities.blocks.blockentity import *
from constants import *

class Brick (BlockEntity):
	def __init__(self, sheet, id, x, y):
		BlockEntity.__init__(self, sheet, id, x, y)
		self.broken = False
		self.breakoriginx = 0
		self.breakoriginy = 0
		self.placed = False

	def clone(self, x, y):
		return Brick(self.sheet, self.id, x, y)	

	def rightDirection (self, direction):
		if (direction[1] < 0):
			return True
		return False

	def tick(self, level):
		if (self.placed):
			self.dead = True
			level.setTile(int(self.x/(16*SCALE) + 0.1), int(self.y/(16*SCALE) + 0.1), 0xFFFFFF)
		if (self.broken):
			self.placed = True
			yoffset = -1

			for y in range(len(PARTS)):
				for x in range(len(PARTS[y])):
					level.addEntity(PARTS[y][x], self.x + OFFSET[y][x]*SCALE, self.y + yoffset*SCALE)
					fragment = level.getQueuedEntity()
					fragment.addOrigin(self.breakoriginx, self.breakoriginy)
				yoffset += 4

	def trigger(self, target):
		if (target.large):
			self.broken = True
			self.breakoriginx = target.x + target.width*SCALE*0.7
			self.breakoriginy = target.y