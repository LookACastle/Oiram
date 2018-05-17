class Mouse:
	def __init__(self):
		self.pressed = False
		self.laspress = False
		self.used = False
		self.pressx = 0
		self.pressy = 0

	def toggle(self, pos):
		self.laspress = self.pressed
		self.pressed = not self.pressed

		if (self.laspress == False and self.pressed == True):
			self.used = False

	def isNewPress(self):
		if (self.pressed):
			if (self.used):
				return False
			else:
				self.used = True
				return True

	def isPressed(self):
		return self.pressed
		