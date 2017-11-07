import pygame
from constants import *
from gfx.spritesheet import SpriteSheet

class Screen:
	def __init__(self, display):
		self.display = display
		self.sheets = []
		self.xOffset = 0
		self.yOffset = 0
		for path in SPRITE_LIST:
			self.sheets.append(SpriteSheet(path))

	def setOffset(self, x, y):
		self.xOffset = x
		self.yOffset = y

	def drawSprite(self, id, tileId, x, y):
		self.display.blit(self.sheets[id].getSprite(tileId), (x+self.xOffset, y+self.yOffset))

	def drawFlippedSprite(self, id, tileId, x, y, flip):
		self.display.blit(pygame.transform.flip(self.sheets[id].getSprite(tileId), flip, False), (x+self.xOffset,y+self.yOffset))

	def drawScaledSprite(self, id, tileId, x, y):
		self.display.blit(self.sheets[id].getScaledSprite(tileId), (x+self.xOffset,y+self.yOffset))