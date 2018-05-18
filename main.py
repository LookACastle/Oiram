import pygame
import math
from constants import *
from gfx.screen import Screen
from levels.levelmanager import *
from tile.tilemanager import *
from entities.entitymanager import *
from entities.oiram import *
from inputhandle.inputhandler import *
from pausemenu.pausemenu import *
import os
import configparser

class Game:
    def __init__ (self):
        self.running = True
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, SCREEN_RES_HEIGHT*0.1)
        self.loadConfig()
        pygame.init()
        dis = pygame.display.Info()
        self.display = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.screen = Screen(self.display)
        self.player = Oiram(14*16, 6*4*16 + 2*16)
        self.pausemenu = PauseMenu(self.screen)
        self.tps = TPS
        self.log = ""
    
    def rescaleDislpay(self, newscale):
        self.screen.rescale(newscale)
        self.resizeDisplay()

    def resizeDisplay(self):
        SCREEN_WIDTH = 16*self.screen.scale*self.levelManager.horizontaltilecount
        SCREEN_HEIGHT = 16*self.screen.scale*self.levelManager.verticaltaltilecount
        self.screen.width = SCREEN_WIDTH
        self.screen.height = SCREEN_HEIGHT
        self.screen.renderOverlay()
        self.pausemenu.setPostition(SCREEN_WIDTH, SCREEN_HEIGHT, self.screen)
        self.display = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    def loadConfig(self):
        self.config = configparser.ConfigParser()
        self.config.read(CONFIG_URL)
        graphicsettings = self.config["GRAPHICS"]
        print (graphicsettings["SCALE"])

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
            dt += float(dMs * (self.tps) / 1000.0);
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
                self.log = "fps: " + str(fps) + "  tps: " + str(tps)
                frames = 0;
                ticks = 0;

    
    def tick(self):

        currentlevel = self.levelManager.getCurrentLevel()

        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN or event.type == pygame.KEYUP):
                self.inputHandler.toggleKey(event.key)

            if event.type == pygame.QUIT:
                self.running = False

        mousepress = pygame.mouse.get_pressed()
        if (mousepress[0] != self.inputHandler.MOUSE.pressed):
            self.inputHandler.toggleMouse(0)

        if (self.inputHandler.ESC.isNewPress() and self.player.dead == False and self.player.onMap == False):
            if (self.pausemenu.active):
                self.pausemenu.active = False
            else:
                self.screen.renderOverlay()
                self.pausemenu.open()

        if (self.pausemenu.active):
            mousedisplaypos = pygame.mouse.get_pos()
            mousepos = (mousedisplaypos[0]/self.screen.scale, mousedisplaypos[1]/self.screen.scale)
            if (self.inputHandler.MOUSE.isNewPress()):
                pressedbutton = self.pausemenu.pressButton(mousepos)
                if (len(pressedbutton) > 0):
                    for b in pressedbutton:
                        b.pressed = True
                        if (pressedbutton[0].action != None):
                            pressedbutton[0].action(self)
            self.pausemenu.resetStates(self.inputHandler.MOUSE.isPressed())
            self.pausemenu.hoverButton(mousepos)
            dragged = self.pausemenu.dragButton(mousepos)
            if (len(dragged) > 0):
                dragged[0].dragaction(self, dragged[0])
            return

        if (not self.player.lockinput):
            if (currentlevel != None):
                if (self.inputHandler.S.isPressed()):
                    self.levelManager.currentlevel.triggerBlock(int((self.player.x + self.player.width*8)/16)*16,int(((self.player.y)/16)+self.player.height)*16, self.player)
                if (not self.inputHandler.S.isPressed() or not self.player.large or self.player.jump):
                    self.player.prone = False

                    #movement handling
                    if (self.inputHandler.A.isPressed() and not self.inputHandler.D.isPressed()):
                        self.player.ax = -ORIAM_ACCELERATION
                    elif (self.inputHandler.D.isPressed() and not self.inputHandler.A.isPressed()):
                        self.player.ax = ORIAM_ACCELERATION
                    else:
                        self.player.ax = 0


                    if (self.inputHandler.W.isNewPress()):
                        if (not self.player.jump):
                            self.player.vy = -ORIAM_JUMP_FORCE
                            self.player.jump = True
                            self.player.gravity = 0.2
                        if(self.player.vy > 0):
                            self.player.gravity = 0.3
                    else:
                        self.player.gravity = 0.3

                    if (self.inputHandler.ENTER.isPressed()):
                        if (self.player.fire):
                             self.player.firewater(currentlevel)

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
            #check collision between player and objects
            currentlevel.entityCollision(self.player)

    def render (self, dt):
        self.levelManager.drawCurrentlevel(self.screen, self.player.x, self.player.y)
        self.player.render(self.screen)
        if(self.pausemenu.active):
            self.pausemenu.render(self.screen)
        self.screen.writeSmallText(self.log,  0, 20)
        pygame.display.update()

    def stop(self):
        pygame.quit()

Game().start()
