import pygame
from constants import *

class Game:
    def __init__ (self):

        self.screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.level = Level(identifier)
        self.inputHandler = InputHandler()

    def start(self):

        self.init()
        self.runLoop()
        self.stop()

    def init():
        pass

    def runLoop():
        pass

    def stop():
        pygame.quit()

Game().start()
