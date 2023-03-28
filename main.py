# File Created by Liam Hare

# import libs
import pygame as pg
import random
import os
from os import path
# import settings 
from settings import *
from sprites import *
from random import randint
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")

# create game class to organize the code
class Game:
    # inits the pygame stuff including setting up screen
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Game...")
        self.clock = pg.time.Clock()
        self.running = True
    # method to create a new game, sets it up
    def new(self):
            self.score = 0
            self.all_sprites = pg.sprite.Group()
            self.platforms = pg.sprite.Group()
            self.enemies = pg.sprite.Group()
            # instantiates the player and platfrom class from sprites, and passes the game class as an argument
            self.player = Player(self)
            self.plat1 = Platform (0,HEIGHT-25, WIDTH, 25)
            self.all_sprites.add(self.player)
            self.all_sprites.add(self.plat1)
            self.platforms.add(self.plat1)
            # for i in range(1,10):
            #     e = Mob()
            #     self.all_sprites.add(e)
            self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    def draw_text(text, self, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
    def get_mouse_now():
        x,y = pg.mouse.get_pos()
        return (x,y)
    def update(self):
        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                print("collided with latfroms")
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
    def draw(self):
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

vec = pg.math.Vector2

# game loop
# ints the game
g = Game()

while g.running:
    g.new()

pg.quit()