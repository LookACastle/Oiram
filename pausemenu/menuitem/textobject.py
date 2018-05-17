from constants import *
class TextObject:
	def __init__(self, text, x, y, screen, margin, action):
		self.label = screen.font.render(text, 1, (255,255,255))
		self.shadowlabel = screen.font.render(text, 1, (100,100,100))
		self.hover = False
		self.width = self.label.get_width()
		self.height = self.label.get_height()
		self.x = x
		self.y = y
		self.margin = margin
		self.text = text
		self.action = action

	def checkCollision(self, x, y):
		if (x + self.margin > self.x and x < self.x+self.width + self.margin and y + self.margin > self.y and y < self.y+self.height+self.margin): 
			return True
		return False

	def isPressAble(self):
		return True

	def isHoverAble(self):
		return True

	def center(self, width):
		difference = width-self.width
		self.x += difference/2

	def render(self, screen, x, y):
		if (self.hover):
			screen.display.blit( self.shadowlabel, (self.x + x + 2*SCALE, self.y + y + 4*SCALE))
		screen.display.blit( self.label, (self.x + x, self.y + y))
		

		