from entities.mob import *
from constants import *

class Oiram (Mob):
	def __init__(self, x, y):
		Mob.__init__(self, OIRAM, 0, x, y, True, 1)
		self.steps = False
		self.lstep = x
		self.cstep = 0
		self.jump = False
		self.push = False
		self.onMap = False
		self.yOffset = 0
		self.deadanimation = False
		self.liveCount = 3
		self.invincibleCounter = 0
		self.overlay = [0, 0, 0]
		self.currentoverlay = STAROVERLAY
		self.overlayStrength = 0
		self.large = False
		self.flicker = False

	def tick(self, level):
		if (not self.dead):
			if (not self.onMap):
				if (level.pauseTimer <= 0):
					if (self.vy < -0.5):
						self.vy = self.vy * 0.9
					else:
						if (self.vy < 0.5):
							self.vy = 0.5
						else:
							self.vy = self.vy * 1.1
					if (self.vy > 2):
						self.vy = 2

					col = self.movey(level)

					if (self.y > level.height*16*SCALE):
						self.kill(True)

					if (self.jump):
						if (col == True):
							if (self.vy > 0):
								self.jump = False
							else:
								self.vy = 0

					if (self.vx != 0):
						if (self.vx > 0):
							self.flip = False
						if (self.vx < 0):
							self.flip = True

						col = self.movex(level)

						if (col == False):
							self.steps = True
							self.push = False
						else:
							self.steps = False
							self.push = True
					else:
						self.steps = False
						self.push = False

					if (self.large):
						self.sheet = LARGEORIAM
					else:
						self.sheet = OIRAM
					if (not self.jump):
						if (self.steps):
							self.cstep += 1
							self.id = int(self.cstep/3.5)%3
						elif (self.push):
							self.id = 4
						else:
							self.id = 5
					else:
						self.id = 3
					if (self.prone):
						self.id = 11
					if (self.invincibleCounter != 0):
						self.overlayStrength = 0.6
						self.invincibleCounter -= 1
						section = int((self.invincibleCounter/3)%len(self.currentoverlay))
						self.overlay = self.currentoverlay[section]
					else:
						self.overlayStrength = 0
				else:
					print("pause")
			else:
				if (level.movementTicks > 0):
					vel = level.getVelocity()
					self.vx = vel[0]
					self.vy = vel[1]
					self.movex(level)
					self.movey(level)
					if (self.vx != 0 or self.vy != 0):
						self.steps = True
						if (self.vx > 0):
							self.flip = False
						if (self.vx < 0):
							self.flip = True
					else:
						self.steps = False

					if (self.steps):
						self.cstep += 1
						self.id = int(self.cstep/3.5)%3
				else:
					self.id = 5
					self.vx = 0
					self.vy = 0
		else:
			self.id = 11
			if (self.vy < -0.5):
				self.vy = self.vy * 0.9
			else:
				if (self.vy < 0.5):
					self.vy = 0.5
				else:
					self.vy = self.vy * 1.1
			if (self.vy > 3.5):
				self.vy = 3.5
			self.yOffset += self.vy*SCALE
			if (self.yOffset + self.y > level.height*16*SCALE):
				self.dead = False
				level.endFlag = True
	
	def enlarge(self):
		self.large = True
		self.height = 2

	def highMode(self):
		self.invincibleCounter = 600
		self.currentoverlay = STAROVERLAY

	def kill (self, overwrite):
		if (self.invincibleCounter <= 0 or overwrite):
			if (not self.dead):
				if (not self.large):
					self.dead = True
					self.vy = -6
					self.overlayStrength = 0
					self.invincibleCounter = 0
				else:
					self.large = False
					self.height = 1
					self.invincibleCounter = 90
					self.currentoverlay = SKIPOVERLAY

		
	def render (self, screen):
		screen.drawColouredFlippedSprite( self.sheet, self.id, self.x, self.y + self.yOffset, self.flip, self.overlay, self.overlayStrength)
		screen.writeText("X" + str(self.liveCount), 18*SCALE, 2.5*SCALE)
		screen.drawGUISprite(TEXTURE, SHROOM_HP, 1*SCALE, 1*SCALE)