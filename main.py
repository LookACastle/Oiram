import pygame
import math
from constants import *
from gfx.screen import Screen
from levels.levelmanager import *
from tile.tilemanager import *
from entities.entitymanager import *
from entities.oiram import *
from inputhandle.inputhandler import *
import os

class Game:
    def __init__ (self):
        self.running = True
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, SCREEN_RES_HEIGHT*0.1)
        pygame.init()
        dis = pygame.display.Info()
        self.display = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.screen = Screen(self.display)
        self.player = Oiram(16*SCALE, 4*4*16*SCALE + 16*SCALE)

    def start(self):
        self.run()
        self.stop()

    def init(self):
        self.tileManager = TileManager()
        self.entityManager = EntityManager()
        self.levelManager = LevelManager(self.tileManager, self.entityManager)
        self.inputHandler = InputHandler()

    def run(self):
        last = pygame.time.get_ticks()
        deltaMs = 0;
        frames = 0;
        ticks = 0;
        dt = 0;
        self.init();
        while (self.running):
            now = pygame.time.get_ticks()
            dMs = now - last;
            last = now;
            deltaMs += dMs;
            dt += float(dMs * (60) / 1000.0);
            missingTicks = int(math.floor(dt));
            for tick in range(0,missingTicks):
                self.tick();
                dt-=1;
                ticks+=1;
            
            self.render(dt);
            frames+=1;

            if (deltaMs >= 1000):
                deltaMs = 0;
                
                fps = str(frames);
                tps = str(ticks);
                print ("fps: " + str(fps) + "  tps: " + str(tps))
                frames = 0;
                ticks = 0;

    
    def tick(self):

        currentlevel = self.levelManager.getCurrentLevel()

        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN or event.type == pygame.KEYUP):
                self.inputHandler.toggleKey(event.key)

            if event.type == pygame.QUIT:
                self.running = False

        if (not self.player.lockinput):
            if (currentlevel != None):
                if (not self.inputHandler.S.isPressed() or not self.player.large or self.player.jump):
                    self.player.prone = False
                    if self.inputHandler.A.isPressed():
                        self.player.vx = -1
                    elif self.inputHandler.D.isPressed():
                        self.player.vx = 1
                    elif (self.inputHandler.D.isPressed() and self.inputHandler.A.isPressed()):
                        self.player.vx = 0
                    else:
                        self.player.vx = 0
                    if self.inputHandler.W.isPressed():
                        if (not self.player.jump):
                            self.player.vy = -4
                            self.player.jump = True
                else:
                    self.player.prone = True

            else:
                if (self.levelManager.movementTicks < 0):
                    if self.inputHandler.ENTER.isPressed():
                        self.levelManager.changeLevel(self.player)
                    if self.inputHandler.A.isPressed():
                        self.levelManager.goLeft()
                    if self.inputHandler.D.isPressed():
                        self.levelManager.goRight()
                    if self.inputHandler.W.isPressed():
                        self.levelManager.goUp()
                    if self.inputHandler.S.isPressed():
                        self.levelManager.goDown()        
        self.levelManager.tick(self.player)
        
        if (currentlevel == None):
            self.player.onMap = True
            self.player.tick(self.levelManager)
        else:
            self.player.onMap = False
            self.player.tick(currentlevel)
            currentlevel.entityCollision(self.player)

    def render (self, dt):
        self.levelManager.drawCurrentlevel(self.screen, self.player.x, self.player.y)
        self.player.render(self.screen)
        pygame.display.update()

    
    def stop(self):
        pygame.quit()

Game().start()
