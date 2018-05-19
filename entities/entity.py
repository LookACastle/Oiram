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
		self.held = False
		self.solid = False
		self.width = 1
		self.height = 1
		self.xmovement = False
		self.dead = False
		self.x1 = 0
		self.x2 = 0
		self.y1 = 0
		self.y2 = 0
		self.killable = True
		self.mobControl = False
		self.visible = True

	def clone(self, x, y):
		return Entity(self.sheet, self.id, x, y)

	def movex(self, level):
			if(self.vx != 0):
				cy = (self.y + self.y1)/16 + 0.1
				cyh = (self.y - self.y2)/16 + self.height - 0.2
				movement = self.vx*self.speed
				self.x += movement
				if (self.vx > 0):
					tileMovement = int(movement/16)
					cx = (self.x - self.x2)/16
					for tileoffset in range(0, tileMovement+1):
						nx = int(cx) + tileoffset + self.width
						if (nx < 0 or nx >= level.width): 
							self.x = int(cx + tileoffset)*16
							return True
						else:
							col1 = level.isSolidTile(nx, int(cy))
							col2 = level.isSolidTile(nx, int(cyh))
							if (col1 or col2):
								self.x = int(cx + tileoffset)*16 + 0.1 + self.x2
								return True
				else:
					cx = (self.x + self.x1)/16
					tileMovement = math.floor(movement/16)
					for tileoffset in range(0, tileMovement, -1):
						nx = int(cx) + tileoffset
						if (cx <= 0 or nx >= level.width): 
							self.x = int(cx + tileoffset)*16
							return True
						else:
							col1 = level.isSolidTile(nx, int(cy))
							col2 = level.isSolidTile(nx, int(cyh))
							if (col1 or col2):
								self.x = int(cx + 1 + tileoffset)*16 - 0.1 - self.x1
								return True
			return False
	
	def movey(self, level):
		cx = self.x/16 + 0.2
		cxh = (self.x - self.x2)/16 + self.width - 0.2
		movement = self.vy*self.speed
		self.y += movement
		if (self.vy > 0):
			cy = (self.y - self.y2)/16
			tileMovement = int((movement)/16)
			for tileoffset in range(0, tileMovement+1):
				ny = int(cy) + tileoffset + self.height
				col1 = level.isSolidTile(int(cxh),ny)
				col2 = level.isSolidTile(int(cx),ny)
				if (col1 or col2):
					self.y = int(cy + tileoffset)*16 + self.y2
					return True
		else:
			tileMovement = math.floor(movement/16)
			cy = (self.y + self.y1)/16
			for tileoffset in range(0, tileMovement, -1):
				ny = int(cy) + tileoffset
				col1 = level.isSolidTile(int(cxh),ny)
				col2 = level.isSolidTile(int(cx),ny)
				if (col1 or col2):
					self.y = int(cy + 1 + tileoffset)*16 - self.y1
					return True	
		return False

	def entityCollision(self, target):
		for h in range(0, target.height):
			for w in range(0, target.width):
				tx = target.x + w + 3*w + target.x1
				ty = target.y + h + 3*w + target.y1
				txw = tx + target.width*16 - target.x1 - target.x2 - 2
				tyh = ty + target.height*16 - target.y1 - target.y2 - 2
				xcol = False
				ycol = False
				if (txw > self.x + self.x1 and txw < self.x + self.x1 + self.width*16):
					xcol = True
				if (tx > self.x - self.x2 and tx < (self.x + self.width*16)-self.x2):
					xcol = True

				if (tyh > self.y + self.y1 and tyh < self.y + self.y1 + self.height*16):
					ycol = True
				if (ty > self.y -self.y2 and ty < (self.y + self.height*16)-self.y2):
					ycol = True
				if (xcol and ycol):
					break
		return xcol and ycol

	def applyGravity(self, gravity, maxSpeed):
		self.vy = self.vy + gravity
		if (self.vy > maxSpeed):
			self.vy = maxSpeed

	def collide(self, victim):
		pass

	def tick(self, level):
		pass

	def render (self, screen):
		screen.drawSprite( self.sheet, self.id, self.x, self.y)
		
