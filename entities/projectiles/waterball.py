from entities.mob import *
from constants import *
from gfx.animationhandler import *

class Waterball (Mob):
	def __init__(self, sheet, id, x, y, flip):
		Mob.__init__(self, sheet, id, x, y, False, 1)
		self.scale = 1.5
		self.vy = 0
		self.flip = flip
		if (not flip):
			self.vx = 2
		else:
			self.vx = -2
		self.y2 = 6
		self.x2 = 6
		self.offset = 0
		self.deadTime = -1
		#animation handler
		self.animationhandling = AnimationHandler(WATER_DOWN)

		# FLAT - 0
		self.animationhandling.addAnimation(WATER_FLAT)
		
		# UP - 1
		self.animationhandling.addAnimation(WATER_UP)
		
		# EXPLODE - 2
		self.animationhandling.addAnimation(WATER_EXPLOSION, 6, 3)

	def clone(self, x, y):
		return Waterball(self.sheet, self.id, x, y, self.flip)	

	def addvel(self, vx, vy):
		self.vx += vx
		if(vy >= 0):
			self.vy += 1
		else:
			self.vy -= 1.5

	def kill(self):
		self.scale = 1.2
		self.y -= 1.5
		if (self.vx > 0):
			self.x += 2.5
		else:
			self.x -= 6

		self.deadTime = 6*3

	def tick(self, level):
		self.animationhandling.clearState()
		if (self.deadTime == 1):
			self.dead = True
			return
		if (self.deadTime > 0):
			self.animationhandling.toggleAnimation(2)
			self.id = self.animationhandling.getAnimation()
			self.deadTime -= 1
			return

		colx = self.movex(level)

		if (colx):
			self.kill()
			return

		self.vy = self.vy + 0.1
		if (self.vy > 3):
			self.vy = 3

		coly = self.movey(level)

		if (self.y > level.height*16):
			self.dead = True
			return

		self.offset = 0
		if (self.vy < 0):
			self.animationhandling.toggleAnimation(1)
		if (self.vy < 0.2 and self.vy > -0.2):
			self.offset = -6
			self.animationhandling.toggleAnimation(0)
		if (coly):
			if (self.vy > 0):
				self.animationhandling.toggleAnimation(0)
				self.vy = -2
			else:
				self.kill()


		collidedentities = level.collideEntity(self)

		kills = 0
		for e in collidedentities:
			if (e.killable):
				e.kill()
				kills += 1

		if (self.deadTime == -1 and len(collidedentities) > 0 and kills > 0):
			self.kill()

		self.id = self.animationhandling.getAnimation()

	def render(self, screen):
		screen.drawScaledFlippedSprite( self.sheet, self.id, self.x, self.y + self.offset, self.scale, self.flip)