import pygame
from pygame.sprite import Sprite


class Back_bullet(Sprite):

    def __init__(self,screen,ship,ai_settings):

        super(Back_bullet,self).__init__()
        self.screen = screen

        self.bullet_speed = ai_settings.bullet_speed_factor
        self.bullet_width = 3.5
        self.bullet_height = 14
        self.bullet_color = 60, 60, 60

        self.rect = pygame.Rect(0,0,self.bullet_width,self.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.bottom =  ship.rect.bottom

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)



        self.color = self.bullet_color
        self.speed = self.bullet_speed



    def update(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)