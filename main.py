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
from configmanager import *
from pathlib import Path
import os
import configparser
import sys
import datetime

class Game:
    def __init__ (self):
        self.running = True
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, SCREEN_RES_HEIGHT*0.1)
        self.configManager = ConfigManager(self.loadFile(CONFIG_URL))
        pygame.init()
        scale = self.configManager.getGraphicInt("scale")
        screen_width = scale*16*self.configManager.getLevelInt("x_tile_count")
        screen_height = scale*16*self.configManager.getLevelInt("y_tile_count")
        self.display = pygame.display.set_mode([screen_width, screen_height])
        self.screen = Screen(self.display, screen_width, screen_height, scale)
        self.tps = self.configManager.getGraphicInt("tps")
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

    def loadFile(self, scr):
        if (Path(scr).is_file()):
            file = configparser.ConfigParser()
            file.read(scr)
        else:
            return None
        return file

    def saveConfig(self):
        self.configManager.save(self, CONFIG_URL)

    def start(self):
        self.run()
        self.stop()

    def init(self):
        self.player = Oiram(14*16, 6*4*16 + 2*16)
        self.pausemenu = PauseMenu(self.screen, self.configManager)
        self.tileManager = TileManager()
        self.entityManager = EntityManager()
        self.levelManager = LevelManager(self.tileManager, self.entityManager, self.configManager)
        lastsave = self.configManager.metasettings["last_save"]
        if(lastsave != "None"):
            save = self.loadFile(SAVE_URL + lastsave)
            if (save != None):
                self.loadSaveFile(save)
            else:
                self.configManager.metasettings["last_save"] = "None"
        self.inputHandler = InputHandler()

    def createSaveFile(self, src):
        save = configparser.ConfigParser()
        save.add_section("META")
        now = datetime.datetime.now()
        save["META"] = {
            "date" : now.strftime("%Y-%m-%d")[2:]
        }

        save.add_section("PLAYER")
        save["PLAYER"] = {
            "coincount" : str(self.player.coinCount),
            "lifecount" : str(self.player.lifeCount),
            "pos" : str((self.player.x, self.player.y)),
            "large" : str(self.player.large),
            "fire" : str(self.player.fire)
        }
        
        clearedList = ""
        openList = ""
        dirList = ""
        for level in self.levelManager.levels:
            if (isinstance(level, Level)):
                clearedList += str(level.cleared) + ","
                openList += str(level.open) + ","
            elif(level != None):
                dirList += str(level) + ","
        clearedList = clearedList[:-1]
        openList = openList[:-1]
        dirList = dirList[:-1]

        save.add_section("LEVEL")
        save["LEVEL"] = {
            "mapPosition" : str(self.levelManager.cpos),
            "mapDirection" : dirList,
            "cleared" : clearedList,
            "open" : openList
        }

        with open(src, "w") as savefile:
            save.write(savefile)

    def stringToBool(self, val):
        if (val == "True"):
            return True
        else:
            return False

    def loadSaveFile(self, save):
        playerSettings = save["PLAYER"]
        self.player.coinCount = int(playerSettings["coincount"])
        self.player.lifeCount = int(playerSettings["lifecount"])

        levelSettings = save["LEVEL"]
        clearedList = levelSettings["cleared"].split(",")
        openList = levelSettings["open"].split(",")
        openList = levelSettings["open"].split(",")
        dirList = levelSettings["mapDirection"].split(",")
        l = 0
        t = 0
        i = 0
        for level in self.levelManager.levels:
            if (isinstance(level, Level)):
                level.cleared = self.stringToBool(clearedList[l])
                level.open = self.stringToBool(openList[l])
                l += 1
            elif (level != None):
                self.levelManager.levels[i] = (int(dirList[t][1:]), int(dirList[t+1][:-1]))
                t += 2
            i += 1

        mapPos = levelSettings["mapPosition"]
        x = mapPos[mapPos.index('[')+1: mapPos.index(',')]
        y = mapPos[mapPos.index(',')+1: mapPos.index(']')]
        self.levelManager.cpos  = [int(x), int(y)]
        self.levelManager.currentlevel = None
        self.levelManager.movementTicks = 0
        self.levelManager.velocity = []    
        self.player.setCheckpoint(int(x)*4*16 + 14*16, int(y)*4*16 + 10*16) 
        self.player.reset()
        self.player.speed = 1

    def stringToTuble(self, txt):
        x = txt[txt.index('(')+1: txt.index(',')]
        y = txt[txt.index(',')+1: txt.index(')')]
        return (int(x, y))

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

        if (self.inputHandler.ESC.isNewPress() and (self.player.dead == False or self.player.onMap == True)):
            if (self.pausemenu.active):
                self.pausemenu.active = False
                self.saveConfig()
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
                        if (self.player.boosttimer > 0):
                            self.player.vy -= 2.5
                            self.player.boosttimer = 0
                    else:
                        self.player.gravity = 0.3
                    if (self.inputHandler.F.isNewPress() and self.player.dead == False):
                        if (self.player.helditem == None):
                            col = currentlevel.pickupEntity(self.player)
                            self.player.helditem = col
                        else:
                            self.player.helditem.align(self.player.flip, self.levelManager.currentlevel)
                            self.levelManager.currentlevel.placeEntity(self.player.helditem)
                            self.player.helditem = None

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
        sys.exit("Error message")

Game().start()
