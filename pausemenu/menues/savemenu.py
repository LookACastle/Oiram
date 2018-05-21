from pausemenu.menuitem.button import *
from pausemenu.menuitem.textbox import *
from constants import *
from pathlib import Path
import configparser
import os

class SaveMenu:
	def __init__(self, screen):
		self.objects = [TextBox("Save files", 0, 20, screen, 0),Button("back", 0, 125, screen, 2, backAction, 0)]
		self.objects[0].center(200)
		self.objects[1].center(200)

		options = ["Slot 1", "Slot 2", "Slot 3"]
		x = 0
		y = 47
		for i in range(0, len(options)):
			textbox = TextBox(options[i], x + 20, y, screen, 1)
			self.objects.append(textbox)
			x += 60

		x = 0
		y += 15
		for i in range(0, len(options)):
			textbox = TextBox("None", x + 20, y, screen, 1)
			self.objects.append(textbox)
			x += 60
		self.updateSaves()

		x = 0
		y += 15
		actions = [save1Action, save2Action, save3Action]
		for i in range(0, len(options)):
			button = Button("Save", x + 20, y, screen, 2, actions[i], 1)
			self.objects.append(button)
			x += 60
		
		options = ["Load", "Load", "Load"]
		actions = [load1Action, load2Action, load3Action]
		x = 0
		y += 15
		for i in range(0, len(options)):
			button = Button(options[i], x + 20, y, screen, 2, actions[i], 1)
			self.objects.append(button)
			x += 60

		actions = [delete1Action, delete2Action, delete3Action]
		x = 0
		y += 15
		for i in range(0, len(options)):
			button = Button("delete", x + 20, y, screen, 2, actions[i], 1)
			self.objects.append(button)
			x += 60

	def updateSaves(self):
		text = ""
		options = ["save1.txt", "save2.txt", "save3.txt"]
		for i in range(0,len(options)):
			saveName = SAVE_URL + options[i]
			if (Path(saveName).is_file()):
				file = configparser.ConfigParser()
				file.read(saveName)
				text = file["META"]["date"]
			else:
				text = "None"
			self.objects[5+i].text = text


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
	main.pausemenu.menues["save"].updateSaves()
	main.configManager.metasettings["last_save"] = "save1.txt"

def save2Action(main):
	main.createSaveFile(SAVE_URL + "save2.txt")
	main.pausemenu.menues["save"].updateSaves()
	main.configManager.metasettings["last_save"] = "save2.txt"

def save3Action(main):
	main.createSaveFile(SAVE_URL + "save3.txt")
	main.pausemenu.menues["save"].updateSaves()
	main.configManager.metasettings["last_save"] = "save3.txt"

def load1Action(main):
	save = main.loadFile(SAVE_URL + "save1.txt")
	if (save != None):
		main.loadSaveFile(save)
		main.configManager.metasettings["last_save"] = "save1.txt"

def load2Action(main):
	save = main.loadFile(SAVE_URL + "save2.txt")
	if (save != None):
		main.loadSaveFile(save)
		main.configManager.metasettings["last_save"] = "save2.txt"

def load3Action(main):
	save = main.loadFile(SAVE_URL + "save3.txt")
	if (save != None):
		main.loadSaveFile(save)
		main.configManager.metasettings["last_save"] = "save3.txt"

def delete1Action(main):
	if (Path(SAVE_URL + "save1.txt").is_file()):
		os.remove(SAVE_URL + "save1.txt")
		main.pausemenu.menues["save"].updateSaves()

def delete2Action(main):
	if (Path(SAVE_URL + "save2.txt").is_file()):
		os.remove(SAVE_URL + "save2.txt")
		main.pausemenu.menues["save"].updateSaves()

def delete3Action(main):
	if (Path(SAVE_URL + "save3.txt").is_file()):
		os.remove(SAVE_URL + "save3.txt")
		main.pausemenu.menues["save"].updateSaves()

def backAction(main):
	main.pausemenu.changeMenu("main")