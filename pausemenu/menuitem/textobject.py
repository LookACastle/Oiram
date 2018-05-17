from constants import *
class TextObject:
	def __init__(self, text, x, y, screen):
		self.x = x
		self.y = y
		self.text = text
		self.label = screen.font.render(text, 1, (255,255,255))
		self.width = self.label.get_width()
		self.height = self.label.get_height()

	def checkCollision(self, x, y):
		print(str(x/SCALE) + "" + str(self.x) )
		if (x > self.x and x < self.x-self.width and y > self.y and y < self.y-self.height): 
			print("pressed:" + self.text)
			return True
		return False

	def render(self, screen, x, y):
		screen.display.blit( self.label, (self.x + x, self.y + y))
		