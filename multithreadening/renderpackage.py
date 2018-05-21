from multithreadening.workpackage import*

class RenderPackage(WorkPackage):
	def __init__(self, package, screen, x, y):
		WorkPackage.__init__(self, package)
		self.screen = screen
		self.x = x
		self.y = y

	def process(self):
		self.package(self.screen, self.x, self.y)
