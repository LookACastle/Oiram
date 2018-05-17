from constants import *
from pausemenu.menues.mainmenu import *
from pausemenu.menues.optionmenu import *

class PauseMenu ():
	def __init__(self, screen):
		self.active = False
		self.pause = 0
		self.menues = {
		"main" : MainMenu(screen),
		"option" : OptionMenu(screen)
		}
		self.currentMenu = self.menues["main"]
		self.x = SCREEN_WIDTH/2 - 100*SCALE
		self.y = SCREEN_HEIGHT/2 - 80*SCALE

	def pressButton(self, pos):
		return self.currentMenu.getCollision(pos[0]-self.x, pos[1]-self.y)

	def hoverButton(self, pos):
		collided = self.currentMenu.getCollision(pos[0]-self.x, pos[1]-self.y)
		for o in collided:
			if (o.isHoverAble()):
				o.hover = True

	def dragButton(self, pos):
		x = pos[0] - self.x
		y = pos[1] - self.y
		dragged = []
		for o in self.currentMenu.objects:
			if (o.isDragAble() and o.pressed):
				o.drag(x, y)
				dragged.append(o)
		return dragged

	def changeMenu(self, id):
		self.currentMenu = self.menues[id]

	def resetStates(self, pressed):
		self.currentMenu.resetHover()
		if (pressed == False):
			self.currentMenu.resetPress()

	def open(self):
		self.changeMenu("main")
		self.active = True

	def render (self, screen):
		screen.drawOverlay()
		screen.drawGUISprite(MENU_SHEET,MENU_ITEM, self.x, self.y)
		self.currentMenu.render(screen, self.x, self.y)
