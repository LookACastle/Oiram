from entities.entity import Entity
from entities.baseenemy import *
from entities.animatedmob import *
from entities.star import *
from entities.simpleenemy import *
from entities.shroom import *
from constants import *

class EntityManager:
	def __init__ (self):
		# fra paint 0xRRGGBB
		# til farve 0xBBGGRR
		self.entities = [None]*(0xFFFFFF+1)
		self.entities[0xb469ff] = Baseenemy(OIRAM,0,0,True, 0.8)
		self.entities[0x00C7FF] = Star(TEXTURE, STAR, 11,0,0, 60, 0.3, True)
		self.entities[0xFF00FF] = animatedMob(TEXTURE, POWERUP, 5,0,0, 60, 0.3, True)
		self.entities[0x00FFFF] = animatedMob(TEXTURE, COIN_FLIP_ANIMATION, 8,0,0, 0, 0.1, True)

		#enemy register
		#gumba
		self.entities[0x000001] = Simpleenemy(ENEMIES, GUMBA, 2, 0, 0, 1, 0.1, True, 1)
		self.entities[0x100001] = Simpleenemy(ENEMIES, GUMBA, 2, 0, 0, 1, 0.1, True, -1)
		self.entities[0x000002] = Shroom(TEXTURE, SHROOM, 2, 0, 0, 3, 0.08, True)

	def getEntity(self,color):
		return self.entities[color]
