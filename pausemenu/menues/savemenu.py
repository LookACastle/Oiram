from pausemenu.menuitem.button import *
from pausemenu.menuitem.textbox import *
from constants import *

class SaveMenu:
	def __init__(self, screen):
		self.objects = [TextBox("Save files", 0, 20, screen, 0),Button("back", 0, 120, screen, 2, backAction, 0)]
		self.objects[0].center(200)
		self.objects[1].center(200)
		options = ["Save 1", "Save 2", "Save 3"]
		actions = [save1Action, save2Action, save3Action]
		x = 0
		for i in range(0, len(options)):
			textbox = Button(options[i], x + 20, 55, screen, 2, actions[i], 1)
			self.objects.append(textbox)
			x += 60
		
		options = ["Load 1", "Load 2", "Load 3"]
		actions = [load1Action, load2Action, load3Action]
		x = 0
		for i in range(0, len(options)):
			button = Button(options[i], x + 20, 90, screen, 2, actions[i], 1)
			self.objects.append(button)
			x += 60

	def resetHover(self):
		for o in self.objects:
			if (o.isHoverAble):
				o.hover = False

	def resetPress(self):
		for o in self.objects:
			if (o.isPressAble()):
				o.pressed = False

	def getCollision(self, x, y):
		collided = []
		for o in self.objects:
			if (o.checkCollision(x, y)):
				collided.append(o)
		return collided

	def render(self, screen, x, y):
		for o in self.objects:
			o.render(screen, x, y)

def quitAction(main):
	if (main.player.onMap):
		main.stop()
	else:
		main.saveConfig()
		main.levelManager.changeLevel(main.player)
		main.pausemenu.active = False

def save1Action(main):
	main.createSaveFile(SAVE_URL + "save1.txt")

def save2Action(main):
	main.createSaveFile(SAVE_URL + "save2.txt")

def save3Action(main):
	main.createSaveFile(SAVE_URL + "save3.txt")

def load1Action(main):
	save = main.loadFile(SAVE_URL + "save1.txt")
	print("loading")
	if (save != None):
		main.loadSaveFile(save)

def load2Action(main):
	save = main.loadFile(SAVE_URL + "save2.txt")
	if (save != None):
		main.loadSaveFile(save)

def load3Action(main):
	save = main.loadFile(SAVE_URL + "save3.txt")
	if (save != None):
		main.loadSaveFile(save)

def backAction(main):
	main.pausemenu.changeMenu("main")