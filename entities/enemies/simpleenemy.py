from entities.animatedmob import *
from constants import SCALE

class Simpleenemy (animatedMob):
	def __init__(self, sheet, id, length, x, y, pause, speed, animationSpeed, vx):
		animatedMob.__init__(self, sheet, id, length, x, y, pause, animationSpeed, True)
		self.vx = vx
		self.deadTime = 0
		self.mark = False
		self.speed = speed

	def clone(self, x, y):
		return Simpleenemy(self.sheet, self.id, self.length, x, y, self.speed, self.animationSpeed, self.vx)	
	
	def simpleMovement(self, level):
		self.animationtick()
		self.applyGravity(GLOBAL_GRAVITY, NORMAL_VERTICAL_MAX_SPEED)
		coly = self.movey(level)
		if (self.y > level.height*16):
			self.mark = True
		colx = self.movex(level)
		if (colx):
			self.wallCollide()

	def tick(self, level):
		pass

	def kill(self):
		self.dead = True

	def collide(self, victim):
		if (self.deadTime <= 0):
			if (victim.mobControl):
				self.wallCollide()
				return
			if (victim.invincibleCounter > 0 or victim.vy > 0 and victim.ly != victim.y):
				cx = victim.x + (victim.width)/2
				if (cx > self.x or cx < self.x + self.width):
					self.kill()
					self.collision = False
					if (victim.jump):
						victim.ay = -5
					return
			victim.kill(False)
