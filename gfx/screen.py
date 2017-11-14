import pygame
from constants import *
from gfx.spritesheet import SpriteSheet

class Screen:
	def __init__(self, display):
		self.display = display
		self.sheets = []
		self.xOffset = 0
		self.yOffset = 0
		#self.font = pygame.font.SysFont("monospace", 15)
		self.font = pygame.font.Font("gfx/DefaultFont.ttf", 70)

		for path in SPRITE_LIST:
			self.sheets.append(SpriteSheet(path))

	def setOffset(self, x, y):
		self.xOffset = x
		self.yOffset = y

	def drawSprite(self, id, tileId, x, y):
		self.display.blit(self.sheets[id].getSprite(tileId), (x+self.xOffset, y+self.yOffset))

	def drawColouredFlippedSprite(self, id, tileId, x, y, flip, overlay, strength):
		sprite = pygame.transform.flip(self.sheets[id].getSprite(tileId), flip, False)
		pxarray = pygame.PixelArray(sprite)
		for px in range(0, 16):
			for py in range(0,16):
				color = pxarray[px*SCALE, py*SCALE]
				print(color>>8 & 0xFF, color>>16 & 0xFF, color>>24 & 0xFF, color>>32 & 0xFF)
				if (color>>32 & 0xFF != 0):
					#fade colors here
		ns = pxarray.make_surface()
		del pxarray

		self.display.blit(ns , (x+self.xOffset,y+self.yOffset))

	def drawFlippedSprite(self, id, tileId, x, y, flip):
		self.display.blit(pygame.transform.flip(self.sheets[id].getSprite(tileId), flip, False), (x+self.xOffset,y+self.yOffset))

	def drawScaledSprite(self, id, tileId, x, y):
		self.display.blit(self.sheets[id].getScaledSprite(tileId), (x+self.xOffset,y+self.yOffset))
	
	def writeText (self, txt, x, y):
		label = self.font.render(txt, 1, (255,255,255))
		self.display.blit(label, (x, y))

	def drawGUISprite(self, id, tileId, x, y):
		self.display.blit(self.sheets[id].getSprite(tileId), (x, y))