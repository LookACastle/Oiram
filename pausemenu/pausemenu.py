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

	def pressButton(self, pos):
		return self.currentMenu.getCollision(pos[0]-self.x, pos[1]-self.y)

	def hoverButton(self, pos):
		collided = self.currentMenu.getCollision(pos[0]-self.x, pos[1]-self.y)
		for o in collided:
			if (o.isHoverAble()):
				o.hover = True

	def resetHover(self):
		self.currentMenu.resetHover()

	def toggle(self):
		self.active = not self.active

	def render (self, screen):
		screen.drawOverlay()
		screen.drawGUISprite(MENU_SHEET,MAIN_MENU, self.x, self.y)
		self.currentMenu.render(screen, self.x, self.y)
