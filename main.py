import pygame
import math
from constants import *
from gfx.screen import Screen
from levels.level import *
from tile.tilemanager import *
from entities.entitymanager import *
from entities.oiram import *

class Game:
    def __init__ (self):
        self.running = True
        pygame.init()
        self.display = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.screen = Screen(self.display)
        self.player = Oiram(100, SCREEN_HEIGHT-32*SCALE)

    def start(self):
        self.run()
        self.stop()

    def init(self):
        self.tileManager = TileManager()
        self.entityManager = EntityManager()
        self.currentlevel = Level("level1.png", self.tileManager, self.entityManager)

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.vx -=1
                if event.key == pygame.K_RIGHT:
                    self.player.vx +=1
                if event.key == pygame.K_UP:
                    if (not self.player.jump):
                        self.player.jump = True
                        self.player.vy = -2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.vx +=1
                if event.key == pygame.K_RIGHT:
                    self.player.vx -=1

        self.player.tick(self.currentlevel)
        self.currentlevel.tick()

        #self.level.tick()

    def render (self, dt):
        self.currentlevel.drawlevel(self.screen, self.player.x, 0)
        self.player.render(self.screen)
        pygame.display.update()

    
    def stop(self):
        pygame.quit()

Game().start()
