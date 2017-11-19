from inputhandle.key import *
import pygame

class InputHandler:
	def __init__(self):
		self.A = Key()
		self.D = Key()
		self.W = Key()
		self.S = Key()
		self.ENTER = Key()

	def toggleKey(self, key):
		if (key == pygame.K_LEFT):
			self.A.toggle()
		if (key == pygame.K_RIGHT):
			self.D.toggle()
		if (key == pygame.K_UP):
			self.W.toggle()
		if (key == pygame.K_DOWN):
			self.S.toggle()
		if (key == pygame.K_RETURN):
			self.ENTER.toggle()