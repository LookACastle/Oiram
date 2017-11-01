from entities.entity import Entity
from constants import *

class EntityManager:
	def __init__ (self):
		# fra paint 0xRRGGBB
		# til farve 0xBBGGRR
		self.entities = [None]*(0xFFFFFF+1)

	def getEntity(self,color):
		return self.entities[color]
