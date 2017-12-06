from constants import *
import math

class Entity:
	def __init__(self, sheet, id, x, y):
		self.id = id
		self.sheet = sheet
		self.x = x
		self.y = y
		self.vx = 0
		self.vy = 1
		self.speed = 0
		self.collision = False
		self.solid = False
		self.width = 1
		self.height = 1
		self.xmovement = False
		self.dead = False
		self.x1 = 0
		self.x2 = 0
		self.y1 = 0
		self.y2 = 0

	def clone(self, x, y):
		return Entity(self.id, self.sheet, x, y, self.width, self.height, self.speed)

	def movex(self, level):
			if(self.vx != 0):
				cx = self.x/(16*SCALE)
				cy = self.y/(16*SCALE)
				movement = self.vx*self.speed*SCALE
				if (self.vx > 0):
					tileMovement = int(movement/16)
					for tileoffset in range(0, tileMovement+1):
						nx = int(cx) + tileoffset + self.width
						if (nx < 0 or nx >= level.width): 
							self.x = int(cx + tileoffset)*16*SCALE
							return True
						else:
							col1 = level.isSolidTile(nx, int(cy + 0.1))
							col2 = level.isSolidTile(nx, int(cy + self.height - 0.2))
							if (col1 or col2):
								self.x = int(cx + tileoffset)*16*SCALE + 0.1
								return True
				else:
					tileMovement = math.floor(movement/16)
					for tileoffset in range(0, tileMovement, -1):
						nx = int(cx) + tileoffset
						if (cx <= 0 or nx >= level.width): 
							self.x = int(cx + tileoffset)*16*SCALE
							return True
						else:
							col1 = level.isSolidTile(nx, int(cy + 0.1))
							col2 = level.isSolidTile(nx, int(cy + self.height - 0.2))
							if (col1 or col2):
								self.x = int(cx + 1 + tileoffset)*16*SCALE - 0.1
								return True
				self.x += movement
			return False
	
	def movey(self, level):
		if (self.vy != 0):
			cx = self.x/(16*SCALE)
			cy = self.y/(16*SCALE)
			movement = self.vy*self.speed*SCALE
			if (self.vy > 0):
				tileMovement = int(movement/16)
				for tileoffset in range(0, tileMovement+1):
					ny = int(cy) + tileoffset + self.height
					col1 = level.isSolidTile(int(cx + self.width - 0.1),ny)
					col2 = level.isSolidTile(int(cx + 0.1),ny)
					if (col1 or col2):
						self.y = int(cy + tileoffset)*16*SCALE
						return True
				self.y += movement
			else:
				tileMovement = math.floor(movement/16)
				for tileoffset in range(0, tileMovement, -1):
					ny = int(cy) + tileoffset
					col1 = level.isSolidTile(int(cx + self.width - 0.1),ny)
					col2 = level.isSolidTile(int(cx + 0.1),ny)
					if (col1 or col2):
						self.y = int(cy + 1 + tileoffset)*16*SCALE
						return True
				self.y += movement	
		return False

	def entityCollision(self, target):
		for h in range(0, target.height):
			for w in range(0, target.width):
				tx = target.x + w + 3*w*SCALE + target.x1
				ty = target.y + h + 3*w*SCALE + target.y1
				txw = tx + target.width*16*SCALE - target.x1 - target.x2 - 2
				tyh = ty + target.height*16*SCALE - target.y1 - target.y2 - 2
				xcol = False
				ycol = False
				if (txw > self.x + self.x1 and txw < self.x + self.x1 + self.width*16*SCALE):
					xcol = True
				if (tx > self.x - self.x2 and tx < (self.x + self.width*16*SCALE)-self.x2):
					xcol = True

				if (tyh > self.y + self.y1 and tyh < self.y + self.y1 + self.height*16*SCALE):
					ycol = True
				if (ty > self.y -self.y2 and ty < (self.y + self.height*16*SCALE)-self.y2):
					ycol = True
				if (xcol and ycol):
					break
		return xcol and ycol

	def applyGravity(self, maxSpeed):
		self.vy = self.vy + 0.2
		if (self.vy > maxSpeed):
			self.vy = maxSpeed

	def collide(self, victim):
		pass

	def tick(self, level):
		pass

	def render (self, screen):
		screen.drawSprite( self.sheet, self.id, self.x, self.y)
		
