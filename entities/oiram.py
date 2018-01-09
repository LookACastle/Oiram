from entities.mob import *
from constants import *
from gfx.animationhandler import *

class Oiram (Mob):
	def __init__(self, x, y):
		Mob.__init__(self, OIRAM, 0, x, y, True, 1)
		#variables
		self.gravity = 0.2
		self.yOffset = 0

		#checkpoint
		self.checkpointx = 0
		self.checkpointy = 0

		#counters
		self.cooldown = 0
		self.liveCount = 3
		self.coinCount = 0
		self.invincibleCounter = 0

		#overlay handler
		self.overlay = [0, 0, 0]
		self.currentoverlay = STAROVERLAY
		self.overlayStrength = 0

		#flags
		self.deadanimation = False
		self.large = False
		self.done = False
		self.jump = False
		self.onMap = False
		self.fire = False
		self.mark = False
		self.lockinput = False

		#types of movement
		self.movementTypes = [self.normalMovement, self.deadMovement, self.mapMovement, self.mapMovement]

		#animation handler
		self.animationhandling = AnimationHandler(5)

		#add animations
		# dead - 0
		self.animationhandling.addAnimation(11)

		# jump - 1
		self.animationhandling.addAnimation(3)
		
		# push - 2
		self.animationhandling.addAnimation(4)
		
		# walk - 3
		self.animationhandling.addAnimation(0, 3, 4)

		self.y1 = 4*SCALE

	def tick(self, level):
		self.animationhandling.clearState()
		self.movementTypes[(int(self.onMap)<<1) + int(self.dead)](level)
		self.id = self.animationhandling.getAnimation()
	
	def setCheckpoint (self, x, y):
		self.checkpointx = x
		self.checkpointy = y

	def reset (self):
		print(self.checkpointx, self.checkpointy)
		self.x = self.checkpointx
		self.y = self.checkpointy
		self.vx = 0
		self.vy = 0
		self.dead = False
		self.yOffset = 0

	def deadMovement(self, level):
		self.animationhandling.toggleAnimation(0)
		self.applyGravity(3)
		self.yOffset += self.vy*SCALE
		if (self.yOffset + self.y > level.height*16*SCALE):
			level.endFlag = True

	def mapMovement(self, level):
		if (level.movementTicks > 0):
			vel = level.getVelocity()
			self.vx = vel[0]
			self.vy = vel[1]
			self.movex(level)
			self.movey(level)
			if (self.vx != 0 or self.vy != 0):
				self.animationhandling.toggleAnimation(3)
				if (self.vx > 0):
					self.flip = False
				if (self.vx < 0):
					self.flip = True

	def normalMovement(self, level):
		if (self.cooldown > 0):
			self.cooldown -= 1
		if (self.prone):
			self.animationhandling.toggleAnimation(0)
		else:
			self.verticalmovement(level)

			if (self.vx != 0):
				self.horizontalmovement(level)
				self.animationhandling.toggleAnimation(3)

		if (self.invincibleCounter != 0):
			self.overlayStrength = 0.6
			self.invincibleCounter -= 1
			section = int((self.invincibleCounter/3)%len(self.currentoverlay))
			self.overlay = self.currentoverlay[section]
		else:
			self.overlayStrength = 0

	def verticalmovement(self, level):
		self.vy = self.vy + self.gravity
		if (self.vy > 2):
			self.vy = 2
		self.ly = self.y
		lvy = self.vy
		col = self.movey(level)

		if (col and self.vy > 0):
			self.jump = False

		if (col and lvy < 0):
			print("trigger")
			level.triggerBlock(int((self.x + self.width*8*SCALE)/(16*SCALE))*SCALE*16,int((self.y/(16*SCALE)))*SCALE*16, self)
			self.vy = 0

		if (col and self.done):
			self.vx = 1
			level.cleared = True

		if (self.y > level.height*16*SCALE):
			self.kill(True)

		if (self.jump and (self.ly != self.y or not col)):
			self.animationhandling.toggleAnimation(1)

	def horizontalmovement(self, level):
		self.flip = False
		if (self.vx < 0):
			self.flip = True

		col = self.movex(level)

		if (col and self.done):
			level.endFlag = True
			self.mark = True

		if (col):
			self.animationhandling.toggleAnimation(2)

	def firewater(self, level):
		if (self.cooldown <= 0 and self.fire):
			self.cooldown = 60
			if (self.flip):
				level.addProjectile(0x060000, self.x, self.y, self.vx, self.vy)
			else:
				level.addProjectile(0x060001, self.x + 9*SCALE, self.y + 2*SCALE, self.vx, self.vy)

	def victory(self):
		self.done = True
		self.vx = 0
		self.vy = 0.8
		self.lockinput = True

	def enlarge(self, Fire):
		if (not self.large):
			self.y -= 16*SCALE
		self.large = True
		self.height = 2
		self.fire = Fire
		if (self.fire):
			self.sheet = WATERORIAM
		else:
			self.sheet = LARGEORIAM

	def highMode(self):
		self.invincibleCounter = 600
		self.currentoverlay = STAROVERLAY

	def addCoin(self):
		self.coinCount += 1

	def kill (self, overwrite):
		if (not self.mark):
			if (self.invincibleCounter <= 0 or overwrite):
				if (not self.dead):
					if (not self.large or overwrite):
						self.dead = True
						self.large = False
						self.fire = False
						self.sheet = OIRAM
						self.height = 1
						self.overlayStrength = 0
						self.vy = -6
						self.overlayStrength = 0
						self.invincibleCounter = 0
					else:
						self.large = False
						self.fire = False
						self.sheet = OIRAM
						self.height = 1
						self.invincibleCounter = 90
						self.currentoverlay = SKIPOVERLAY

		
	def render (self, screen):
		if (self.onMap):
			screen.drawColouredFlippedSprite(OIRAM, self.id, self.x, self.y + self.yOffset, self.flip, self.overlay, self.overlayStrength)	
		else:
			screen.drawColouredFlippedSprite( self.sheet, self.id, self.x, self.y + self.yOffset, self.flip, self.overlay, self.overlayStrength)
		screen.writeText("X" + str(self.liveCount), 18*SCALE, 2.5*SCALE)
		screen.drawGUISprite(TEXTURE, SHROOM_HP, 1*SCALE, 1*SCALE)
		screen.writeText("X" + str(self.coinCount),  50*SCALE + 18*SCALE, 2.5*SCALE)
		screen.drawGUISprite(TEXTURE, COIN_FLIP_ANIMATION, 50*SCALE + 1*SCALE, 1*SCALE)