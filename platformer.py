
"""
platformer.py
Author: 
Credit: 
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

blue = Color(0x2EFEC8, 1.0)
black = Color(0x000000, 1.0)
pink = Color(0xFF00FF, 1.0)
red = Color(0xFF5733, 1.0)
white = Color(0xFFFFFF, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
grey = Color(0xC0C0C0, 1.0)
thinline = LineStyle(2, black)
blkline = LineStyle(1, black)
noline = LineStyle(0, white)
coolline = LineStyle(1, grey)
blueline = LineStyle(2, blue)
redline = LineStyle(1, red)
greenline = LineStyle(1, green)
gridline = LineStyle(1, grey)

from math import floor

class Player(Sprite):
    def __init__(self, position):
        player = RectangleAsset(15,35, noline,green)
        self.vx = 0
        self.vy = 5
        super().__init__(player, position)
        

class Box(Sprite):
    def __init__(self, position):
        box = RectangleAsset(50,50, noline, black)
        super().__init__(box, position)

class Game(App):
    def __init__(self):
        super().__init__()
        grid = RectangleAsset(50,50,gridline,white)
        x = 0 
        y = 0 
        for b in range(15):
            for a in range(25):
                Sprite(grid, (x,y))
                x = x + 50
            x = 0
            Sprite(grid,(x,y))
            y = y + 50
        Game.listenMouseEvent('click', self.click)
        Game.listenKeyEvent('keydown', 'p',  self.placement)
        Game.listenKeyEvent('keydown', 'd', self.right)
        Game.listenKeyEvent('keyup', 'd', self.stop)
        Game.listenKeyEvent('keydown', 'a', self.left)
        Game.listenKeyEvent('keyup', 'a', self.stop)
        Game.listenKeyEvent('keydown', 'w', self.jump)
        Game.listenKeyEvent('keyup', 'w', self.stop)
        
    def click(self,event):
        x = floor(event.x/50)*50
        y = floor(event.y/50)*50
        Box((x,y))
    
    def placement(self,event):    
        Player((0,0))
    
    def right(self, event):
        for a in self.getSpritesbyClass(Player):
            a.vx = 2.5
    
    def left(self,event):
        for a in self.getSpritesbyClass(Player):
            a.vx = -2.5
            
    def jump(self,event):
        for a in self.getSpritesbyClass(Player):
            a.vy = -2.5
    
    def stop(self, event):
        for a in self.getSpritesbyClass(Player):
            a.vx = 0
            
            
    def step(self):
        for a in self.getSpritesbyClass(Player):
            a.x += a.vx
            a.y += a.vy
    
            if a.collidingWithSprites(Box):
                a.vy = 0
            
            else:
                a.vy = 5
                
myapp = Game()
myapp.run()