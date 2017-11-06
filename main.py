import pygame
import math
from constants import *
from gfx.screen import Screen
from levels.levelmanager import *
from tile.tilemanager import *
from entities.entitymanager import *
from entities.oiram import *
import os

class Game:
    def __init__ (self):
        self.running = True
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, SCREEN_RES_HEIGHT*0.1)
        pygame.init()
        self.display = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.screen = Screen(self.display)
        self.player = Oiram(16*SCALE, 16*SCALE)

    def start(self):
        self.run()
        self.stop()

    def init(self):
        self.tileManager = TileManager()
        self.entityManager = EntityManager()
        self.levelManager = LevelManager(self.tileManager, self.entityManager)

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
            
            timeToSleep = 1000 / 120 + last - pygame.time.get_ticks();
            if (timeToSleep > 0):
                pygame.time.delay(int(timeToSleep))

    
    def tick(self):
        currentlevel = self.levelManager.getCurrentLevel()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if (currentlevel != None):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.player.x = 100
                        self.player.y = SCREEN_HEIGHT-32*SCALE
                        #self.levelManager.changeLevel()
                    if event.key == pygame.K_LEFT:
                        self.player.vx -= 1
                    if event.key == pygame.K_RIGHT:
                        self.player.vx += 1
                    if event.key == pygame.K_UP:
                        if (not self.player.jump):
                            self.player.jump = True
                            self.player.vy = -4
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.player.vx += 1
                    if event.key == pygame.K_RIGHT:
                        self.player.vx -= 1
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                            self.player.x = 100
                            self.player.y = SCREEN_HEIGHT-32*SCALE
                            self.levelManager.changeLevel()
                    if (self.levelManager.movementTicks <= 0):
                        if event.key == pygame.K_LEFT:
                            self.levelManager.goLeft()
                        if event.key == pygame.K_RIGHT:
                            self.levelManager.goRight()
                        if event.key == pygame.K_UP:
                            self.levelManager.goUp()
                        if event.key == pygame.K_DOWN:
                            self.levelManager.goDown()
        
        if (currentlevel == None):
            self.player.onMap = True
            self.player.tick(self.levelManager)
        else:
            self.player.onMap = False
            self.player.tick(currentlevel)

        self.levelManager.tick()


    def render (self, dt):
        self.levelManager.drawCurrentlevel(self.screen, self.player.x, self.player.y)
        self.player.render(self.screen)
        pygame.display.update()

    
    def stop(self):
        pygame.quit()

Game().start()
