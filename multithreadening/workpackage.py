class WorkPackage:
	def __init__(self, package):
		self.package = package

	def process(self):
		self.package()

		