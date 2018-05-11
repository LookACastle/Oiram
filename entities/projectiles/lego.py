from entities.animatedmob import *
import random
from constants import *

class Lego (animatedMob):
	def __init__(self, sheet, id, length, x, y, pause, animationSpeed, collision, flip):
		animatedMob.__init__(self, sheet, id, length, x, y, pause, animationSpeed, collision)
		self.vy = -random.randint(20, 40)/10
		self.initvy = -self.vy
		self.flip = flip
		if (not flip):
			self.vx = -random.randint(10, 30)/10
		else:
			self.vx = random.randint(10, 30)/10
		self.y2 = 3*SCALE
		self.y1 = 3*SCALE
		self.x2 = 3*SCALE
		self.x1 = 3*SCALE

	def clone(self, x, y):
		return Lego(self.sheet, self.id, self.length, x, y, self.pause, self.animationSpeed, self.collision, self.flip)	
		
	def tick(self, level):
		self.animationtick()
		self.vx = self.vx * 0.98
		colx = self.movex(level)
		self.applyGravity(GLOBAL_GRAVITY, LEGO_VERTICAL_MAX_SPEED)
		coly = self.movey(level)
		if (coly or self.y > level.height*16*SCALE):
			self.dead = True

	def collide(self, victim):
		victim.kill(False)