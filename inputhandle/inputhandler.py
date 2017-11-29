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
		if (key == pygame.K_LEFT or key == pygame.K_a):
			self.A.toggle()
		if (key == pygame.K_RIGHT or key == pygame.K_d):
			self.D.toggle()
		if (key == pygame.K_UP or key == pygame.K_w):
			self.W.toggle()
		if (key == pygame.K_DOWN or key == pygame.K_s):
			self.S.toggle()
		if (key == pygame.K_RETURN or key == pygame.K_SPACE):
			self.ENTER.toggle()