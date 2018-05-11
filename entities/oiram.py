from entities.mob import *
from constants import *
from gfx.animationhandler import *

class Oiram (Mob):
	def __init__(self, x, y):
		Mob.__init__(self, OIRAM, 0, x, y, True, 1)
		#variables
		self.gravity = 0.2
		self.yOffset = 0
		self.ay = 0
		self.ax = 0

		#checkpoint
		self.checkpointx = 0
		self.checkpointy = 0

		#counters
		self.cooldown = 0
		self.lifeCount = 3
		self.gainedLifes = 200
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

		self.animationpause = 0
		self.previousform = 0
		self.newform = 0
		self.heightdifferens = 0

	def tick(self, level):
		self.animationhandling.clearState()
		self.movementTypes[(int(self.onMap)<<1) + int(self.dead)](level)
		self.id = self.animationhandling.getAnimation()
		if (self.gainedLifes > 0 and self.onMap == False):
			self.gainedLifes -= 1
			print(self.gainedLifes)
			level.addEntity(0xFF00FF, self.x, self.y);
	
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
		self.applyGravity(GLOBAL_GRAVITY ,ORIAM_VERTICAL_MAX_SPEED*2)
		self.yOffset += self.vy*SCALE*self.speed
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
		if (self.animationpause > 0):
			level.pauseTimer = self.animationpause
			self.animationpause -= 1
			if (self.animationpause == 0):
				print(self.large)
				self.large = True
				self.sheet = self.newform
				return
			if (self.animationpause % 5 == 0):
				if (self.large):
					self.y += self.heightdifferens*16*SCALE
				else:
					self.y -= self.heightdifferens*16*SCALE
				self.large = not self.large
			if (self.large):
				self.sheet = self.previousform
			else:
				self.sheet = self.newform
			return
		print(self.large)
		if (self.cooldown > 0):
			self.cooldown -= 1
		if (self.prone):
			self.animationhandling.toggleAnimation(0)
		else:
			self.vy += self.ay
			self.ay = 0
			self.verticalmovement(level)
			self.vx += self.ax
			if (self.vx > ORIAM_HORIZONTAL_MAX_SPEED):
				self.vx = ORIAM_HORIZONTAL_MAX_SPEED
			if (self.vx < -ORIAM_HORIZONTAL_MAX_SPEED):
				self.vx = -ORIAM_HORIZONTAL_MAX_SPEED
			if (self.ax == 0):
				self.vx *= (100-ORIAM_RESISTANCE)/100
			self.ax = 0
			if (self.vx < 0.01 and self.vx > -0.01):
				self.vx = 0
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
		self.applyGravity(GLOBAL_GRAVITY, ORIAM_VERTICAL_MAX_SPEED)
		self.ly = self.y
		lvy = self.vy
		col = self.movey(level)
		if (col and self.vy > 0):
			self.jump = False

		if (col and lvy < 0):
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
			self.vx = 0;
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
		self.previousform = self.sheet
		self.animationpause = 60
		if (not self.large):
			self.y -= 1*16*SCALE
		self.heightdifferens = self.height - 2
		self.height = 2
		self.fire = Fire
		if (self.fire):
			self.sheet = WATERORIAM
			self.newform = self.sheet
		else:
			self.sheet = LARGEORIAM
			self.newform = self.sheet

	def highMode(self):
		self.invincibleCounter = 600
		self.currentoverlay = STAROVERLAY

	def addCoin(self):
		self.coinCount += 1

	def kill (self, overwrite):
		if (not self.mark):
			if (self.invincibleCounter <= 0 or overwrite):
				if (not self.dead):
					print(self.large)
					if (not self.large or overwrite):
						self.dead = True
						self.large = False
						self.fire = False
						self.sheet = OIRAM
						self.height = 1
						self.overlayStrength = 0
						self.vy = -5
						self.overlayStrength = 0
						self.invincibleCounter = 0
					else:
						self.large = False
						self.fire = False
						self.sheet = OIRAM
						self.height = 1
						self.invincibleCounter = 90
						self.currentoverlay = SKIPOVERLAY

	def addLife(self):
		self.lifeCount += 1
		self.gainedLifes += 1

	def render (self, screen):
		if (self.onMap):
			screen.drawColouredFlippedSprite(OIRAM, self.id, self.x, self.y + self.yOffset, self.flip, self.overlay, self.overlayStrength)	
		else:
			screen.drawColouredFlippedSprite( self.sheet, self.id, self.x, self.y + self.yOffset, self.flip, self.overlay, self.overlayStrength)
		screen.writeText("X" + str(self.lifeCount), 18*SCALE, 2.5*SCALE)
		screen.drawGUISprite(TEXTURE, SHROOM_HP, 1*SCALE, 1*SCALE)
		screen.writeText("X" + str(self.coinCount),  50*SCALE + 18*SCALE, 2.5*SCALE)
		screen.drawGUISprite(TEXTURE, COIN_FLIP_ANIMATION, 50*SCALE + 1*SCALE, 1*SCALE)