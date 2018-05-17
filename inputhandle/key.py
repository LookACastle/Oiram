class Key:
	def __init__(self):
		self.pressed = False
		self.laspress = False
		self.used = False

	def toggle(self):
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