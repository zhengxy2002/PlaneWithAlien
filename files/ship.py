'''
这里用来存储有关游戏中飞船的相关数据
创建时间： 2021年1月25日 15:09:27
'''
import pygame
from game_tree import Settings
from bullet    import Bullet
from back_bullet import Back_bullet
setting = Settings()

class Ship():

    def __init__(self,screen):
        self.screen = screen


        #加载飞船图像并且获取外接矩形
        self.image = pygame.image.load('files/images/plane2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.locationx = float(self.rect.centerx)
        self.locationy = float(self.rect.bottom)          #支持浮点数的变动

        self.moving_right = False
        self.moving_left  = False
        self.moving_up    = False
        self.moving_down  = False
        self.fire_allowed = False
        self.fire_back_allowed = False
        self.ship_cold = False



    def blitme(self):               #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)

    def acting(self,bullets,screen,ship,stats):                       #控制飞船行为
        if self.moving_right and self.rect.right < setting.screen_width and stats.allowed:
            self.locationx += setting.plane_speed

        if self.moving_left  and self.rect.left  > 0 and stats.allowed:
            self.locationx -= setting.plane_speed

        if self.moving_up    and self.rect.top   > 0 and stats.allowed:
            self.locationy -= setting.plane_speed

        if self.moving_down  and self.rect.bottom < setting.screen_height and stats.allowed:
            self.locationy += setting.plane_speed

        if self.fire_allowed and len(bullets) < setting.bullet_magazine and stats.allowed:
            new_bullet = Bullet(screen, ship,setting)
            bullets.add(new_bullet)

        if self.fire_back_allowed and len(bullets) < setting.bullet_magazine and stats.allowed:
            new_bullet2 = Back_bullet(screen, ship, setting)
            bullets.add(new_bullet2)

        if self.ship_cold == True:
            stats.over_heated = 0

        self.rect.centerx = self.locationx
        self.rect.bottom  = self.locationy


    def center_ship(self):
        self.locationx = self.screen_rect.centerx
        self.locationy = self.screen_rect.bottom
