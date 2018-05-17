from entities.blocks.brick import *
from constants import *
import random

class CoinBrick (Brick):
	def __init__(self, sheet, id, x, y):
		Brick.__init__(self, sheet, id, x, y)
		self.coinCount = random.randint(5, 10)
		print(self.coinCount)
		self.deltaCount = 0
		self.oy = y
		self.hitTime = 0
		self.hit = False

	def clone(self, x, y):
		return CoinBrick(self.sheet, self.id, x, y)	

	def rightDirection (self, direction):
		if (direction[1] < 0):
			return True
		return False

	def tick(self, level):
		if (self.placed):
			self.dead = True
			level.setTile(int(self.x/(16*SCALE) + 0.1), int(self.oy/(16*SCALE) + 0.1), 0xFFFFFF)
		if (self.hitTime > 0):
			self.y -= 7
			self.hitTime -= 1
		else:
			if (self.y >= self.oy):
				self.y = self.oy
			else:
				if (self.hit):
					level.addEntity( 0x01FFFF, self.x, self.oy - 16*SCALE)
					self.hit = False
				self.y += 7

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
		if (target.large and self.hit == False):
			self.coinCount -= 1
			self.hit = True
			self.deltaCount += 1;
			self.hitTime = 4
			if (self.coinCount == -1):
				self.broken = True
				self.breakoriginx = target.x + target.width*SCALE*0.7
				self.breakoriginy = target.y