from entities.animatedmob import *
from constants import *
import random

class CarnivorousPlant (animatedMob):
	def __init__(self, sheet, id, length, x, y, pause, animationSpeed):
		animatedMob.__init__(self, sheet, id, length, x + 4, y + 8, pause, animationSpeed, False)
		self.sleepTimer = random.randint(0,60)
		self.direction = False

		self.downTimer = -1
		self.upTimer = 32
		self.travelTime = 32
		self.collision = True

	def clone(self, x, y):
		return CarnivorousPlant(self.sheet, self.id, self.length, x, y, self.addPause, self.animationSpeed)	

	def tick(self, level):
		self.animationtick()
		if (self.sleepTimer > 0):
			self.sleepTimer -= 1
			self.vy = 0
		else:
			if (self.downTimer > 0):
				self.downTimer -= 1
				self.vy = 1
				self.flip = True

			if (self.upTimer > 0):
				self.upTimer -= 1
				self.vy = -1
				self.flip = False
			self.y += self.vy

		if (self.upTimer == 0):
			self.upTimer -= 1
			self.vy = -1
			self.downTimer = self.travelTime
			self.sleepTimer = 120

		if (self.downTimer == 0):
			self.downTimer -= 1
			self.vy = 1
			self.sleepTimer = 120
			self.upTimer = self.travelTime


	def trigger(self, target):
		if (self.hit == False):
			self.empty = True
			self.hit = True
			self.hitTime = 6

	def collide(self, victim):
		if (victim.invincibleCounter > 0 and self.upTimer < ):
			self.kill(False)
			return
		if (victim.mobcontrol):
			victim.kill(False)

