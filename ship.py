import pygame

class Ship:
    
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Add ship 
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        #Save horisontal ship position
    
        self.x = float(self.rect.x)

        #Movement indicator
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """
        update player position based on movement indicator
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed

        #self.rect.x = self.x
            
    def blitme(self):
        self.screen.blit(self.image, self.rect)
