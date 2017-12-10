from entities.entity import *
from constants import *

class Brick (Entity):
	def __init__(self, sheet, id, x, y):
		Entity.__init__(self, sheet, id, x, y)
		self.solid = True
		self.broken = False
		self.breakoriginx = 0
		self.breakoriginy = 0
		self.placed = False

	def clone(self, x, y):
		return Brick(self.sheet, self.id, x, y)	

	def tick(self, level):
		if (self.placed):
			self.dead = True
			level.setTile(int(self.x/(16*SCALE) + 0.1), int(self.y/(16*SCALE) + 0.1), 0xFFFFFF)
		if (self.broken):
			self.placed = True

			parts = [[0x090001, 0x090002],
					 [0x090003, 0x090000, 0x090004],
					 [0x090001, 0x090000],
					 [0x090003, 0x090000, 0x090004]]
			offset = [[0, 7],
					  [0, 3, 11],
					  [0, 7],
					  [0, 3, 11]]

			yoffset = -1

			for y in range(len(parts)):
				for x in range(len(parts[y])):
					level.addEntity(parts[y][x], self.x + offset[y][x]*SCALE, self.y + yoffset*SCALE)
					fragment = level.getQueuedEntity()
					fragment.addOrigin(self.breakoriginx, self.breakoriginy)
				yoffset += 4

	def trigger(self, target):
		self.broken = True
		self.breakoriginx = target.x + target.width*SCALE*0.7
		self.breakoriginy = target.y

	def collide(self, victim):
		pass