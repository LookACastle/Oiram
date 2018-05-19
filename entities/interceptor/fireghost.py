from entities.mob import *
from constants import *
from gfx.animationhandler import *

class FireGhost (Mob):
	def __init__(self, sheet, id, x, y):
		Mob.__init__(self, sheet, id, x, y, True, 3.5)
		self.scale = 1.5
		self.ty = y
		self.travelTime = 0
		self.travelTimeSet = False

		#animation handler
		self.animationhandling = AnimationHandler(FIRE_GHOST)

		# Hover - 0
		self.animationhandling.addAnimation(FIRE_BALL, 2, 4)

		self.upTimer = -1
		self.downTimer = 9999
		self.sleepTimer = 0
		self.flip = False
		self.offset = 0
		self.dir = False

		self.y2 = 2
		self.x1 = 2
		self.x2 = 2

	def clone(self, x, y):
		return FireGhost(self.sheet, self.id, x, y)	

	def kill(self):
		pass

	def collide(self, victim):
		if (victim.invincibleCounter <= 0):
			victim.kill(False)

	def tick(self, level):
		self.animationhandling.clearState()

		if (self.sleepTimer > 0):
			self.sleepTimer -= 1
			self.vy = 0
			self.flip = False
			if (self.offset > 0):
				self.dir = False
			if(self.offset < -10):
				self.dir = True

			if (self.dir):
				self.offset += 0.4
			else:
				self.offset -= 0.4

		else:
			self.animationhandling.toggleAnimation(0)
			if (self.downTimer > 0):
				self.downTimer -= 1
				self.vy = 1
				self.flip = True

			if (self.upTimer > 0):
				self.upTimer -= 1
				self.vy = -1
				self.flip = False

		if (self.upTimer == 0):
			self.upTimer -= 1
			self.downTimer = self.travelTime
			self.sleepTimer = 60

		if (self.downTimer == 0):
			self.downTimer -= 1
			self.sleepTimer = 60
			self.upTimer = self.travelTime

		self.y += self.vy*self.speed

		if (not self.travelTimeSet):
			self.travelTime += 1
			if (self.y >= level.height*16 + 16):
				self.downTimer = 0
				self.travelTimeSet = True

		self.id = self.animationhandling.getAnimation()

	def render(self, screen):
		screen.drawFlippedSprite( self.sheet, self.id, self.x, self.y + self.offset, False, self.flip)