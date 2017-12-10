from entities.entity import *
from constants import *
import random
import math
class BrickFragment (Entity):
	def __init__(self, sheet, id, x, y):
		Entity.__init__(self, sheet, id, x, y)
		self.vy = 0
		self.vx = 0

		self.rotationSpeed = random.randint(3, 6)

		if(random.randint(0, 1) == 0):
			self.rotationSpeed = -self.rotationSpeed
			
		self.rotation = 0

	def clone(self, x, y):
		return BrickFragment(self.sheet, self.id, x, y)	

	def tick(self, level):
		if (self.y > level.height*16*SCALE):
			self.dead = True
			return

		self.applyGravity(4)
		self.vx = self.vx*0.99

		self.y += self.vy*SCALE
		self.x += self.vx*SCALE

		self.rotation += self.rotationSpeed

	def addOrigin(self, orix, oriy):
		self.vx = self.x - orix
		self.vy = self.y - oriy
		veclen = math.sqrt(self.vy**2 + self.vx**2)
		self.vx = (self.vx/veclen)*2
		self.vy = (self.vy/veclen)*4

	def render(self, screen):
		screen.drawRotateSprite(self.sheet, self.id, self.x, self.y, self.rotation)