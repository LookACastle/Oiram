from constants import *

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
		"""
		hitbox offset
			__________h1_________
			|		  |	       |
			|		  \/	   |
			w1-->		    <--w2   
			|		  /\	   |
			|		  |		   |	
			__________h2________

		"""
		self.h1 = 0
		self.h2 = 0
		self.w1 = 0
		self.w2 = 0

	def clone(self, x, y):
		return Entity(self.id, self.sheet, x, y, self.width, self.height, self.speed)

	def movex(self, level):
		if(self.vx != 0):

			"""
			cTile___________cwTile
			|				   |
			|				   |
			|				   |
			|				   |
			|				   |	
			chTile__________cwhTile

			"""
			nx = self.x + self.vx*self.speed*SCALE
			nxw = self.x + self.vx*self.speed*SCALE+self.width*SCALE
			if (nx >= -self.w1*16*SCALE and nxw <= level.width*SCALE*16):

				cx = nx/(16*SCALE)
				cy = self.y/(16*SCALE)
				px = 1/(16*SCALE)

				x = int(cx + px + self.w1)
				y = int(cy + px + self.h1)
				xw = int(cx + self.width - self.w2 - px )
				yh = int(cy + self.height - self.h2 - px)


				cTile = (x, y)
				cwTile = (xw, y)

				chTile = (x, yh)
				cwhTile = (xw, yh)

				#[cTile, cwTile, chTile, cwhTile]
				col = level.tileCollision([cTile, cwTile, chTile, cwhTile], True)
				if (not col):
					self.x = nx
				else:
					return 1
		return 0

	def movey(self, level):
		if(self.vy != 0):

			"""
			cTile___________cwTile
			|				   |
			|				   |
			|				   |
			|				   |
			|				   |	
			chTile__________cwhTile

			"""
			ny = self.y + self.vy*self.speed*SCALE
			nyh = self.y + self.vy*self.speed*SCALE+self.height*SCALE
			if (ny > 0 and nyh <= level.height*SCALE*16):

				cx = self.x/(16*SCALE)
				cy = ny/(16*SCALE)
				px = 1/(16*SCALE)

				x = int(cx + px + self.w1)
				y = int(cy + px + self.h1)
				xw = int(cx + self.width - self.w2 - px )
				yh = int(cy + self.height - self.h2 - px)


				cTile = (x, y)
				cwTile = (xw, y)

				chTile = (x, yh)
				cwhTile = (xw, yh)

				#[cTile, cwTile, chTile, cwhTile]
				col = level.tileCollision([cTile, cwTile, chTile, cwhTile], True)
				if (not col):
					self.y = ny
				else:
					return 1
		return 0


	def collide(self, victim):
		pass

	def tick(self, level):
		pass

	def render (self, screen):
		screen.drawSprite( self.sheet, self.id, self.x, self.y, self.flip)
		