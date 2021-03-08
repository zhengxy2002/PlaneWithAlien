'''
这里是游戏的主程序
创建于 2021年1月25日 12:43:11
'''
import sys
import pygame
from game_tree import Settings,game_control,screen_make_it_newer,bullets_moving,create_enemies,update_aliens
from ship     import Ship
from pygame.sprite import Group
from bullet import  Bullet
from alien import Alien
from game_stats import Gamestats
from button import Button
from scoreboard import Scoreboard

def run_game():

    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode(ai_settings.screen_pixel)

    pygame.display.set_caption(ai_settings.caption)

    play_button = Button(ai_settings,screen,'Play')

    stats = Gamestats(ai_settings)

    scoreboard = Scoreboard(ai_settings,screen,stats)

    ship = Ship(screen)

    aliens = Alien(screen,ai_settings)

    bullets = Group()
    aliens  = Group()

    create_enemies(screen,aliens,ship)

    while True:



        game_control(ship,screen,bullets,stats,play_button,aliens,scoreboard,ai_settings)

        if stats.game_active == True:

            ship.acting(bullets,screen,ship,stats)

            bullets_moving(bullets,aliens,screen,ship,ai_settings,stats,scoreboard)

            update_aliens(aliens,screen,ai_settings,ship,stats,bullets,scoreboard)



        screen_make_it_newer(ship,screen,bullets,aliens,play_button,stats,scoreboard)

run_game()