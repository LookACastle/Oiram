from constants import *
from pausemenu.menues.mainmenu import *

class PauseMenu ():
	def __init__(self, screen):
		self.active = False
		self.pause = 0
		self.mainMenu = MainMenu(0, 0, screen)
		self.currentMenu = self.mainMenu
		self.x = SCREEN_WIDTH/2 - 100*SCALE
		self.y = SCREEN_HEIGHT/2 - 80*SCALE

	def checkCollision(self, pos):
		self.currentMenu.checkCollision(pos[0], pos[1])

	def toggle(self):
		self.active = not self.active

	def render (self, screen):
		screen.drawOverlay()
		screen.drawGUISprite(MENU_SHEET,MAIN_MENU, self.x, self.y)
		self.currentMenu.render(screen, self.x, self.y)
