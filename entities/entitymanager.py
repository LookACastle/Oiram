from entities.entity import Entity
from entities.baseenemy import *
from entities.collectable import *
from constants import *

class EntityManager:
	def __init__ (self):
		# fra paint 0xRRGGBB
		# til farve 0xBBGGRR
		self.entities = [None]*(0xFFFFFF+1)
		self.entities[0xb469ff] = Baseenemy(OIRAM,0,0,True, 0.8)
		self.entities[0x00C7FF] = Collectable(TEXTURE, STAR, 11,0,0)
	def getEntity(self,color):
		return self.entities[color]
