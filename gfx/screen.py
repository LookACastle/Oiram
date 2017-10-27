import pygame
from constants import *
from gfx.spritesheet import SpriteSheet
class Screen:
	def __init__(self, display):
		self.display = display
		self.sheets = []
		for path in SPRITE_LIST:
			self.sheets.append(SpriteSheet(path))

	def drawSprite(self, id, tileId, x, y):
		self.display.blit(self.sheets[id].getSprite(tileId), (x,y))