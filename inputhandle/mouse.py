class Mouse:
	def __init__(self):
		self.pressed = False
		self.laspress = False
		self.used = False
		self.x = 0
		self.y = 0

	def toggle(self, pos):
		self.laspress = self.pressed
		self.pressed = not self.pressed

		if (self.laspress == False and self.pressed == True):
			self.x = pos[0]
			self.y = pos[1]
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
		