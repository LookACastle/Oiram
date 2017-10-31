import pygame
import math
from constants import *
from gfx.screen import Screen
from levels.level import *
from tile.tilemanager import *
class Game:
    def __init__ (self):
        self.running = True
        pygame.init()
        self.display = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.screen = Screen(self.display)
        self.x = 1
        """
        self.level = Level(identifier)
        self.inputHandler = InputHandler()
        """

    def start(self):
        self.run()
        self.stop()

    def init(self):
        self.tileManager = TileManager()
        self.currentlevel = Level("level1.png", self.tileManager)
        #self.screen.set_caption("Oriam")
        pass

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
                    self.x -= 100
                if event.key == pygame.K_RIGHT:
                    self.x += 100
        #self.level.tick()

    def render (self,dt):
        self.currentlevel.drawlevel(self.screen, self.x, 0)
        if (self.x >= X_TILE_COUNT*8*SCALE-8*SCALE ):
            if (self.x >= (self.currentlevel.width*16 - X_TILE_COUNT*8)*SCALE):
                self.screen.drawSprite( 0, 4,self.x-(self.currentlevel.width*16-X_TILE_COUNT*16)*SCALE-16*SCALE, 64)
            else:
                self.screen.drawSprite( 0, 4, X_TILE_COUNT*8*SCALE-8*SCALE, 0)
        else:
            self.screen.drawSprite( 0, 4, self.x, 64)
        pygame.display.update()
        """
        self.level.drawTiles(self.screen, self.player.getPos())
        self.level.drawEntities(self.screen)
        """

    
    def stop(self):
        pygame.quit()

Game().start()
