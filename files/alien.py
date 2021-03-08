import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,screen,ai_settings):
        super(Alien, self).__init__()
        self.screen = screen

        self.image = pygame.image.load('files/images/alien1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = self.screen_rect.centerx
        self.rect.y = self.screen_rect.top

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.alien_moving_speed_s = ai_settings.alien_moving_speed_s
        self.fleet_drop_speed = 10.0


    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self,settings):
        self.x += self.alien_moving_speed_s * settings.alien_direction
        self.rect.x = self.x

    def check_edges(self,screen):
        screen_rect = screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True

        elif self.rect.left <= 0:
            return True