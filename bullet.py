import pygame
from pygame.sprite import Sprite

class Bullet():
    #class for bullet control
    
    def __init__(self, ai_game):
        super.__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #create bullet rect
        self.rect = pygame.Rect(0, 0, self.setting.bullet_width,
                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #save cursor position
        self.y = float(self.rect.y)

    def update(self):
        #move bullet up
        #Update position
        self.y -= self.settings.bullet_speed
        #Update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

