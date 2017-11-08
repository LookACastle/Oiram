from constants import *
import math

class Entity:
	def __init__(self, sheet, id, x, y):
		self.id = id
		self.sheet = sheet
		self.x = x
		self.y = y
		self.vx = 0
		self.vy = 0
		self.speed = 0
		self.collision = False
		self.width = 1
		self.height = 1
		self.xmovement = False

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
					col1 = level.isSolidTile(nx, int(cy + 0.1))
					col2 = level.isSolidTile(nx, int(cy + self.height - 0.2))
					if (col1 or col2):
						self.x = int(cx + tileoffset)*16*SCALE
						return True
				self.x += movement
			else:
				tileMovement = math.floor(movement/16)
				for tileoffset in range(0, tileMovement, -1):
					nx = int(cx) + tileoffset
					col1 = level.isSolidTile(nx, int(cy + 0.1))
					col2 = level.isSolidTile(nx, int(cy + self.height - 0.2))
					if (col1 or col2):
						self.x = int(cx + 1 + tileoffset)*16*SCALE -1
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
				for tileoffset in range(0, tileMovement+2):
					ny = int(cy) + tileoffset + self.height
					col1 = level.isSolidTile(int(cx + self.width - 0.1),ny)
					col2 = level.isSolidTile(int(cx + 0.1),ny)
					if (col1 or col2):
						self.y = int(cy + tileoffset)*16*SCALE
						return 1
				self.y += movement
			else:
				tileMovement = math.floor(movement/16)
				for tileoffset in range(0, tileMovement - 1, -1):
					ny = int(cy) + tileoffset
					col1 = level.isSolidTile(int(cx + self.width - 0.1),ny)
					col2 = level.isSolidTile(int(cx + 0.1),ny)
					if (col1 or col2):
						self.y = int(cy + 1 + tileoffset)*16*SCALE
						return 1
				self.y += movement	
		return 0



	def collide(self, victim):
		pass

	def tick(self, level):
		pass

	def render (self, screen):
		screen.drawSprite( self.sheet, self.id, self.x, self.y)
		
