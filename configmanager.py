class ConfigManager(object):
	def __init__(self, configuration):
		self.configurations = configuration
		self.metasettings = configuration["META"]
		self.graphicsettings = configuration["GRAPHICS"]
		self.levelsettings = configuration["LEVEL"]

	def getLevelInt(self, name):
		return int(self.levelsettings[name])
	
	def getMetaInt(self, name):
		return int(self.metasettings[name])

	def getGraphicInt(self, name):
		return int(self.graphicsettings[name])

	def getInt(self, section, name):
		return int(self.configurations.get(section, name))
		
	def save(self, main, url):
		
		self.configurations["GRAPHICS"] ={
			"scale" : str(main.screen.scale),
			"tps" : str(main.tps)
		}
		self.configurations["LEVEL"] = {
			"x_tile_count" : str(main.levelManager.horizontaltilecount),
			"y_tile_count" : str(main.levelManager.verticaltaltilecount)
		}

		with open(url, "w") as file:
			self.configurations.write(file)