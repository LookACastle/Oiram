from entities.animatedmob import *

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
		self.applyGravity(self.gravity, NORMAL_VERTICAL_MAX_SPEED)
		coly = self.movey(level)
		if (self.y > level.height*16):
			self.mark = True
		colx = self.movex(level)
		if (colx):
			self.wallCollide()

	def tick(self, level):
		pass

	def collide(self, victim):
		if (self.deadTime <= 0):
			if (victim.invincibleCounter > 0 or victim.vy > 0 and victim.ly != victim.y):
				cx = victim.x + (victim.width)/2
				if (cx > self.x or cx < self.x + self.width):
					self.kill(False)
					self.collision = False
					victim.ay = -5
					victim.jump = True
					return
			else:
				victim.kill(False)
